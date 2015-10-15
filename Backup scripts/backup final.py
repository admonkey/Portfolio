from subprocess import call 
import os, datetime

# Variables #################################
Destination = "/Users/alowe/Desktop/testdir/"
Site = "ftp.debian.org/*"
Options = "r"

Username = " "
Password = " "
#############################################

now = datetime.datetime.now()
Year = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
Time = str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
directoryName = Year + " " + Time

if Username and Password == " ":
	Site = "ftp://" + Site
else:
	Site = "ftp://" + Username + ":" + Password + Site

os.mkdir(Destination + directoryName + "/")
os.chdir(Destination + "/" + directoryName + "/")

def backUp(Source):
	call(["wget", "-" + Options, Source])

backUp(Site)