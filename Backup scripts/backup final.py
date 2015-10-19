from subprocess import call
import os, datetime, time, sys

# Options #################################
Username = " "
Password = " "
Site = "ftp.debian.org"
Source = "/path/to/source"
Destination = "/path/to/destination"
#############################################

linux = sys.platform.startswith('linux')
darmin = sys.platform.startswith('darmin')
osx2 = sys.platform.startswith('os2')
os2emax = sys.platform.startswith('os2emax')

if linux == linux or darmin == darmin or osx2 == osx2 or os2emax == os2emax:

	if os.path.exists(Destination) == False:
		os.mkdir(Destination)

	nowDatetime = datetime.datetime.now()
	Year = str(nowDatetime.month) + "-" + str(nowDatetime.day) + "-" + str(nowDatetime.year)
	Time = str(nowDatetime.hour) + ":" + str(nowDatetime.minute) + ":" + str(nowDatetime.second)
	directoryName = Year + " " + Time

	Url = Site + Source

	if Username and Password == " ":
		Url = "ftp://" + Url
	else:
		Url = "ftp://" + Username + ":" + Password + Url

	os.mkdir(Destination + "/" + directoryName + "/")
	os.chdir(Destination + "/" + directoryName)

	def backUp(Source):
		call(["wget", "-r", Source])

	backUp(Url)

	os.chdir(Destination)
	call(["tar", "-jcvf", directoryName + ".tar.bz2", "-P", Destination + "/" + directoryName])
	call(["rm", "-rf", directoryName])

	nowTime = time.time()

	for file in os.listdir(Destination):
		file = os.path.join(Destination, file)
		if os.stat(os.path.join(Destination, file)).st_mtime <= nowTime - 30 * 86400:
			if os.path.isfile(file):
				os.remove(os.path.join(Destination, file))
else:
	print "This script is not supported on", sys.platform