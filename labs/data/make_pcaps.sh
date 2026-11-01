#!/bin/bash
# 编者录制抓包文件用的脚本（Linux，需 root；学生不需要运行）
# 用网络命名空间搭一个小网络：  PC ── R1 ── R2 ── 服务器
#   PC   192.168.1.10/24  （网关 192.168.1.1）
#   R1   192.168.1.1  /  10.0.12.1/30
#   R2   10.0.12.2    /  203.0.113.1/24
#   服务器 203.0.113.10 （DNS：www.xiaohe.com；网站 80 端口；HTTPS 443 端口）
# 依赖：iproute2 tcpdump dnsmasq-base isc-dhcp-client iputils-ping traceroute python3 openssl curl
set -e
OUT=$(cd "$(dirname "$0")" && pwd)/pcap
HERE=$(cd "$(dirname "$0")" && pwd)
WORK=$(mktemp -d)
mkdir -p "$OUT"

cleanup() { for n in pc r1 r2 srv; do ip netns del $n 2>/dev/null || true; done; }
cleanup
for n in pc r1 r2 srv; do ip netns add $n; ip -n $n link set lo up; done

link() {  # link ns1 if1 mac1 ns2 if2 mac2
  ip link add tmpa type veth peer name tmpb
  ip link set tmpa netns $1; ip -n $1 link set tmpa name $2; ip -n $1 link set $2 address $3
  ip link set tmpb netns $4; ip -n $4 link set tmpb name $5; ip -n $4 link set $5 address $6
  ip -n $1 link set $2 up; ip -n $4 link set $5 up
}
link pc  eth0 00:e0:4c:68:01:0a  r1  eth0 00:e0:fc:12:34:01   # 网卡厂商：Realtek / Huawei
link r1  eth1 00:e0:fc:12:34:02  r2  eth0 00:e0:fc:56:78:01
link r2  eth1 00:e0:fc:56:78:02  srv eth0 00:1b:21:9a:00:10   # 服务器网卡：Intel
for n in pc r1 r2 srv; do ip netns exec $n sysctl -qw net.ipv6.conf.all.disable_ipv6=1 2>/dev/null || true; done

ip -n r1 addr add 192.168.1.1/24 dev eth0; ip -n r1 addr add 10.0.12.1/30 dev eth1
ip -n r2 addr add 10.0.12.2/30 dev eth0;   ip -n r2 addr add 203.0.113.1/24 dev eth1
ip -n srv addr add 203.0.113.10/24 dev eth0; ip -n srv route add default via 203.0.113.1
ip -n r1 route add default via 10.0.12.2;  ip -n r2 route add 192.168.1.0/24 via 10.0.12.1
for n in r1 r2; do ip netns exec $n sysctl -qw net.ipv4.ip_forward=1; done

# ---- 服务器：DNS、网站、HTTPS ----
cat > $WORK/hosts <<H
203.0.113.10 www.xiaohe.com
203.0.113.10 mail.xiaohe.com
H
ip netns exec srv dnsmasq --no-daemon --no-resolv --no-hosts --addn-hosts=$WORK/hosts --listen-address=203.0.113.10 \
   --bind-interfaces --local=/xiaohe.com/ --pid-file=$WORK/dns.pid >/dev/null 2>&1 &
mkdir -p $WORK/www
cp "$HERE/site/index.html" "$HERE/site/login.html" $WORK/www/
ip netns exec srv python3 "$HERE/tiny_server.py" $WORK/www 80 >/dev/null 2>&1 &
openssl req -x509 -newkey rsa:2048 -nodes -keyout $WORK/key.pem -out $WORK/cert.pem -days 3650 \
   -subj "/C=CN/O=Xiaohe Design Studio/CN=www.xiaohe.com" -addext "subjectAltName=DNS:www.xiaohe.com" 2>/dev/null
ip netns exec srv python3 "$HERE/tiny_server.py" $WORK/www 443 $WORK/cert.pem $WORK/key.pem >/dev/null 2>&1 &
sleep 1.5

cap() {  # cap 文件名 命令...
  local f=$1; shift
  ip netns exec pc tcpdump -i eth0 -U -s 0 -w "$OUT/$f" >/dev/null 2>&1 &
  local p=$!; sleep 0.8
  "$@"
  sleep 1; kill $p; wait $p 2>/dev/null || true
}
flush() { ip -n pc neigh flush all; ip -n r1 neigh flush all; }

# ---- 1. DHCP + ARP + ping 网关（第 8 章）----
ip netns exec r1 dnsmasq --no-daemon --port=0 --interface=eth0 --bind-interfaces \
   --dhcp-range=192.168.1.100,192.168.1.199,255.255.255.0,12h --no-ping --dhcp-option=3,192.168.1.1 \
   --dhcp-option=6,203.0.113.10 --dhcp-leasefile=$WORK/leases >/dev/null 2>&1 &
DHCPD=$!
sleep 1
cat > $WORK/noop.sh <<S
#!/bin/sh
case "\$reason" in BOUND|RENEW|REBIND|REBOOT) ip addr add \$new_ip_address/24 dev \$interface ;; esac
S
chmod +x $WORK/noop.sh
dhcp_then_ping() {
  ip netns exec pc dhclient -1 -sf $WORK/noop.sh -lf $WORK/dhc.lease -pf $WORK/dhc.pid eth0 2>/dev/null
  ip -n pc route add default via 192.168.1.1
  ip netns exec pc ping -c 3 -i 0.3 192.168.1.1 >/dev/null
}
cap dhcp_arp.pcap dhcp_then_ping
ip netns exec pc dhclient -x -pf $WORK/dhc.pid 2>/dev/null || true
kill $DHCPD 2>/dev/null || true
ip -n pc addr flush dev eth0
ip -n pc addr add 192.168.1.10/24 dev eth0; ip -n pc route add default via 192.168.1.1

# ---- 2. 打开一个网页：ARP → DNS → TCP 三次握手 → HTTP → 四次挥手（第 2、4、9、10 章）----
flush
cat > $WORK/resolv.conf <<R
nameserver 203.0.113.10
R
mkdir -p /etc/netns/pc; cp $WORK/resolv.conf /etc/netns/pc/resolv.conf
web() { ip netns exec pc python3 "$HERE/fetch.py" http://www.xiaohe.com/ >/dev/null; }
cap web_visit.pcap web

# ---- 3. ping 与 traceroute（第 1、7、8 章）----
pt() { ip netns exec pc ping -c 4 -i 0.3 203.0.113.10 >/dev/null; ip netns exec pc traceroute -I -n -q 1 -N 1 -m 5 -w 1 203.0.113.10 >/dev/null; }
cap ping_trace.pcap pt

# ---- 4. 登录：HTTP 明文 与 HTTPS 密文（第 11 章）----
login() {
  ip netns exec pc python3 "$HERE/fetch.py" http://www.xiaohe.com/login "user=xiaolin&password=Xh2026!" >/dev/null
  ip netns exec pc python3 "$HERE/fetch.py" https://www.xiaohe.com/login "user=xiaolin&password=Xh2026!" $WORK/cert.pem >/dev/null
}
cap http_vs_https.pcap login

# ---- 5. TCP 聊天与 UDP 聊天（第 9 章）----
chat() {
  ip netns exec srv python3 "$HERE/chat_demo.py" server tcp &  sleep 0.5
  ip netns exec pc  python3 "$HERE/chat_demo.py" client tcp 203.0.113.10; sleep 0.5
  ip netns exec srv python3 "$HERE/chat_demo.py" server udp &  sleep 0.5
  ip netns exec pc  python3 "$HERE/chat_demo.py" client udp 203.0.113.10; sleep 0.5
}
cap tcp_udp_chat.pcap chat

# ---- 6. 802.1Q 标签（第 5 章）：本机内核不支持 VLAN 接口，改用 scapy 生成，见 make_vlan_pcap.py ----
python3 "$HERE/make_vlan_pcap.py" "$OUT/vlan_trunk.pcap"

kill $(jobs -p) 2>/dev/null || true
rm -rf /etc/netns/pc
cleanup
echo "抓包文件已生成到 $OUT"; ls -l "$OUT"
