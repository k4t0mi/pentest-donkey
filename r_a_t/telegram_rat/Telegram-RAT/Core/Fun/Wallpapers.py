# Import modules

import ctypes


# Sets a photo on the desktop wallpaper

def SetWallpapers(Photo, Directory):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, Directory + Photo.file_path, 0)