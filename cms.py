import os
import sys
import fnmatch
import glob

#
# Usage, when specifying the directory, affirm that it includes the full path
#

root = "c:/users/benbe/desktop/c"

fList = []

def finalize(t):
	s = []
	
	for i in t:
		if i not in s:
			s.append(i)
		  
	return s

def listf(d):
	fList = []

	for path, dirs, files in os.walk('c:/users/benbe/desktop/c'):
		for f in glob.iglob(os.path.join(path, '', '*.c')):
			fList.append(f)
	
		for d in dirs:
			for f in glob.iglob(os.path.join(path, d, '*.c')):
				fList.append(f)
			for f in glob.iglob(os.path.join(path, d, '*.h')):
				fList.append(f)
				
	return finalize(fList)


if(len(sys.argv) == 2):
	fList = listf(sys.argv[1])
	string = "gcc "

	for f in fList:
		string = string + "\"" + f + "\"" + " "

	os.system(string)
	print("Executing command: " + string + "\n")
	print("Generated new executable (a.exe)")
else:
	print("Invalid argument count (specify the directory)")
	
