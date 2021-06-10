# Import modules

import os


# Antiviruses Directories

Antiviruses = {
	'C:\\Program Files\\Windows Defender': 'Windows Defender',
	'C:\\Program Files\\AVAST Software\\Avast': 'Avast',
	'C:\\Program Files\\AVG\\Antivirus': 'AVG',
	'C:\\Program Files (x86)\\Avira\\Launcher': 'Avira',
	'C:\\Program Files (x86)\\IObit\\Advanced SystemCare': 'Advanced SystemCare',
	'C:\\Program Files\\Bitdefender Antivirus Free': 'Bitdefender',
	'C:\\Program Files\\DrWeb': 'Dr.Web',
	'C:\\Program Files\\ESET\\ESET Security': 'ESET',
	'C:\\Program Files (x86)\\Kaspersky Lab': 'Kaspersky Lab',
	'C:\\Program Files (x86)\\360\\Total Security': '360 Total Security'
	}


Antivirus = [Antiviruses[d] for d in filter(os.path.exists, Antiviruses)]