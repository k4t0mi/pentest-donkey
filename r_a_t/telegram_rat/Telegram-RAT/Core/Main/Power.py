# Import modules

import ctypes
import subprocess
import ctypes.wintypes


# Puts the computer to sleep 

def Hibernate():
	subprocess.call('shutdown -h /f', shell=True)

# Turns off the computer

def Shutdown():
	subprocess.call('shutdown -s /t 0 /f', shell=True)


# Restarts computer

def Restart():
	subprocess.call('shutdown -r /t 0 /f', shell=True)

# Ends user session

def Logoff():
	subprocess.call('shutdown -l /f', shell=True)


# Blue screen of death

def BSoD():
	ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
	ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))