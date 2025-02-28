import os
import subprocess

def install_software():
    os.system('sudo apt-get update')
    os.system('sudo apt-get install -y hostapd dnsmasq')

def configure_network_interfaces():
    dhcpcd_conf = """
    interface wlan0
    static ip_address=192.168.4.1/24
    nohook wpa_supplicant
    """
    with open('/etc/dhcpcd.conf', 'a') as file:
        file.write(dhcpcd_conf)
    os.system('sudo service dhcpcd restart')
    os.system('sudo ip addr add 192.168.4.1/24 dev wlan0')

def configure_hostapd():
    hostapd_conf = """
interface=wlan0
driver=nl80211
ssid=Pi_AP
hw_mode=g
channel=7
wmm_enabled=0
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_passphrase=YourPassword
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
"""
    with open('/etc/hostapd/hostapd.conf', 'w') as file:
        file.write(hostapd_conf)
    
    hostapd_default = 'DAEMON_CONF="/etc/hostapd/hostapd.conf"'
    with open('/etc/default/hostapd', 'w') as file:
        file.write(hostapd_default)

def configure_dnsmasq():
    dnsmasq_conf = """
interface=wlan0
dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h
"""
    with open('/etc/dnsmasq.conf', 'w') as file:
        file.write(dnsmasq_conf)

def enable_and_start_services():
    os.system('sudo systemctl stop hostapd')
    os.system('sudo systemctl stop dnsmasq')
    os.system('sudo systemctl start hostapd')
    os.system('sudo systemctl start dnsmasq')
    os.system('sudo systemctl enable hostapd')
    os.system('sudo systemctl enable dnsmasq')

def main():
    install_software()
    configure_network_interfaces()
    configure_hostapd()
    configure_dnsmasq()
    enable_and_start_services()
    print("Access point created successfully.")

if __name__ == "__main__":
    main()
