# Import modules

import win32api
import win32con


# Variables

Rotations = {
	'0': win32con.DMDO_DEFAULT,
	'90': win32con.DMDO_90,
	'180': win32con.DMDO_180,
	'270': win32con.DMDO_270
}


# Monitor position control

def DisplayRotate(Degrees='0'):
	try:
		RotationValue = Rotations[Degrees]
	except KeyError:
		RotationValue = win32con.DMDO_DEFAULT
	Device = win32api.EnumDisplayDevices(None, 0)
	dm = win32api.EnumDisplaySettings(Device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
	if (dm.DisplayOrientation + RotationValue) % 2 == 1:
		dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
	dm.DisplayOrientation = RotationValue
	win32api.ChangeDisplaySettingsEx(Device.DeviceName, dm)
