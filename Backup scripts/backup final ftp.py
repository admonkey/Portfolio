from subprocess import call
import os, datetime, time, sys, shutil

# Setup ####################################
Username = os.environ["Username"] # Username for the ftp server
Password = os.environ["Password"] # Password for the ftp server
Archive = os.environ["Archive"]
Site = os.environ["Site"] # FTP site url
Source = os.environ["Source"] # Path on the FTP server
Destination = os.environ["Destination"] # Location on the your computer to download files
#############################################

# Options ###################################
Name = "Test" # Adds a name to downloaded files
Passive = "on" # Turns on or off passive or non passive mode
#############################################

linux = sys.platform.startswith('linux')
darmin = sys.platform.startswith('darmin')
os2 = sys.platform.startswith('os2')

if linux == linux or darmin == darmin or os2 == os2: # Makes sure that this scropt is running on one of these OS's 

	if os.path.exists(Destination) == False: # if the destination does not exists then create the destination
		os.makedirs(Destination)
	else:
		print("Directory already exists", Destination)

	nowDatetime = datetime.datetime.now()
	Year = str(nowDatetime.month) + "-" + str(nowDatetime.day) + "-" + str(nowDatetime.year) # Sets current Year to month, day, and year
	Time = str(nowDatetime.hour) + ":" + str(nowDatetime.minute) + ":" + str(nowDatetime.second) # Sets current Time to hour, minute, and second
	directoryName = Name + "" + Year + " " + Time # Combines Name, Year, and Time

	Url = Site + Source

	if Username and Password == " ":
		Url = "ftp://" + Url
	else:
		Url = "ftp://" + Username + ":" + Password + "@" + Site + "/" + Source

	os.mkdir(Destination + "/" + directoryName + "/")
	os.chdir(Destination + "/" + directoryName)

	if Passive == "on":
		Passive = "--passive-ftp"
	else:
		Passive = "--no-passive-ftp"

	def backUp(Source):
		call(["wget", "-r", Passive, Source])

	backUp(Url)

	call(["7z", "a", "-t7z", directoryName + ".7z", Destination + "/" + directoryName, "-mx9", "-mmt", "-ms", "-p" + Archive])
	shutil.move(directoryName + ".7z", Destination, copy_function="copy")
	shutil.rmtree(Destination + "/" + directoryName)

	nowTime = time.time()
	for file in os.listdir(Destination):
		file = os.path.join(Destination, file)
		if os.stat(os.path.join(Destination, file)).st_mtime <= nowTime - 30 * 86400:
			if os.path.isfile(file):
				os.remove(os.path.join(Destination, file))
else:
	print("This script is not supported on", sys.platform) # Runs if you are not running one of the supported OS's