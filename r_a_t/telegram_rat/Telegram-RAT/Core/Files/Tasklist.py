# Import modules

import subprocess


# Gets a list of active processes

def ProcessList():
	Calling = subprocess.Popen('tasklist',
		shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE).stdout.readlines()
	Process = [Calling[i].decode('cp866', 'ignore').split()[0].split('.exe')[0] for i in range(3,len(Calling))]
	Processes = '\n'.join(Process)
	return Processes