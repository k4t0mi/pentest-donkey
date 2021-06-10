# Import modules

import os
import sys


# Organizations list (By Directories)

OrganizationsPaths = (
	'C:\\Users\\' + os.getlogin() + '\\Desktop\\Financial_Report.xls',
	'C:\\Users\\Peter Wilson\\Desktop\\Microsoft Word 2010.lnk',
	'C:\\Users\\Administrator\\Desktop\\Callaghan_1966.rtf',
	'C:\\Users\\admin\\Desktop\\my school calendar.xlsx',
	'C:\\Users\\raustin\\Desktop\\zaqrnsnoefaa.xlsx',
	'C:\\Users\\Administrator\\Desktop\\decoy.cpp',
	'C:\\Users\\John\\Desktop\\foobar.txt',
	'C:\\Bank-statement-08-2013.docx',
	'C:\\Users\\STRAZNICA.GRUBUTT',
	'C:\\Users\\Jason\\Desktop',
	'C:\\Users\\Lisa\\Desktop',
	'C:\\TEMP\\Sample.exe',
	'C:\\Users\\Joe Cage'
	)


# Detect Antivirus organization by Directories

def Organization():
	return any([os.path.exists(Organization) for Organization in OrganizationsPaths])


# Checks if the script is running  computer of the anti-virus organization

if Organization() is True:
	sys.exit()
