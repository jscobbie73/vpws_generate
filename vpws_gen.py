#Script for creation of VPWS Configs for Extreme

#Get the VLAN Range needed for the Pseudo-wire config
#Get Starting VLAN
lowVLAN = int(raw_input("Please enter starting (low) VLAN: "))
#Get Ending VLAN 
highVLAN = int(raw_input("Please enter ending (high) VLAN: "))

#Bounds checking to ensure VLAN range is low to high
if lowVLAN > highVLAN:
	print 'Invalid VLAN Range: Low VLAN was higher than your High'
	exit	
vlan = (lowVLAN)
VLAN = str(vlan)
#DEBUGprint VLAN
#DEBUGprint highVLAN
# Openfile config write mode
fout = open('config.txt', 'w')
#Create Config Snippet
while vlan <= highVLAN:
#	Print code snippet, replace $VLAN with range
#DEBUG
	fout.write('create vlan "v2364-Customer"\n')
	fout.write('configure vlan v2364-Customer tag 2364\n')
	fout.write('disable igmp snooping vlan "v2364-Customer"\n')
	fout.write('configure vlan v2364-Customer add ports 48 tagged ')
	fout.write(VLAN)
	fout.write('\ncreate l2vpn vpws w2364-Customer fec-id-type pseudo-wire 2364\n')
	fout.write('configure l2vpn vpws w2364-Customer add service vlan v2364-Customer\n')
	fout.write('configure l2vpn vpws w2364-Customer mtu 9190\n')
	fout.write('configure l2vpn vpws w2364-Customer add peer 172.18.10.77\n')
	fout.write('\ncreate vlan "v2364-Customer"\n')
	fout.write('configure vlan v2364-Customer tag 2364\n')
	fout.write('disable igmp snooping vlan "v2364-Customer"\n')
	fout.write('configure vlan v2364-Customer add ports 11 tagged ')
	fout.write(VLAN)
	fout.write('\ncreate l2vpn vpws w2364-Customer fec-id-type pseudo-wire 2364\n')
	fout.write('configure l2vpn vpws w2364-Customer add service vlan v2364-Customer\n')
	fout.write('configure l2vpn vpws w2364-Customer mtu 9190\n')
	fout.write('configure l2vpn vpws w2364-Customer add peer 172.18.10.58\n')
	fout.write('\n')
# Increment VLAN and continue loop
	vlan = vlan + 1
#DEBUG	print vlan
	VLAN = str(vlan)
#DEBUGprint VLAN
fout.close()

