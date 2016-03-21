+ Setup

+ Misc eratta
* Network configuration on cloned VMs (the mac address is also cloned...) [*http://forums.virtualbox.org/viewtopic.php?f=7&t=36892 topic]

* Looks like you can also cycle the MAC address from the VirtualBox Settings/Network (Advanced section).

[[code]]

sudo mv /etc/udev/rules.d/70-persistent-net.rules /etc/udev/rules.d/70-persistent-net.rules.bak
sudo gedit /etc/network/interfaces

; In /etc/network/interfaces, define
eth0
iface eth0 inet dhcp

; back in shell:
sudo gedit /var/run/network/ifstate

; In /var/run/networ/ifstate, define:
eth0=eth0

[[/code]]