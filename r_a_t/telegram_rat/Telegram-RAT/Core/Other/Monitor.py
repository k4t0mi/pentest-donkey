# Import modules

import ctypes


# Variables

SendMessageA = ctypes.windll.user32.SendMessageA
HWND = 0xFFFF
WM_SYSCOMMAND = 0x112
SC_MONITORPOWER = 0xF170


# Monitor power management

def Off():
	SendMessageA(HWND, WM_SYSCOMMAND, SC_MONITORPOWER, 2)

def On():
	SendMessageA(HWND, WM_SYSCOMMAND, SC_MONITORPOWER, -1)