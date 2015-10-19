from subprocess import call 
import os, datetime

# Variables #################################
Destination = "/Users/alowe/Desktop/testdir/"
Source = "/debian/project/trace/"
Site = "ftp.debian.org"
Options = "r"

Username = " "
Password = " "
#############################################

if os.path.exists(Destination) == False:
	os.mkdir(Destination)

now = datetime.datetime.now()
Year = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
Time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
directoryName = Year + " " + Time

Url = Site + Source

if Username and Password == " ":
	Url = "ftp://" + Url
else:
	Url = "ftp://" + Username + ":" + Password + Url

os.mkdir(Destination + directoryName + "/")
os.chdir(Destination + "/" + directoryName + "/")

def backUp(Source):
	call(["wget", "-" + Options, Source])

backUp(Url)