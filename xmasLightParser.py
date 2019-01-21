#Christmas Light Parser
#
#Author: Dimitri Charitou
#December 2017
#Python 2

#UPDATE: July 23, 2018

#Parser which outputs code for inputted light sequence
#Use: python3 xmasLightParser.py data file


#UPDATE: December 21, 2018

#Instead of printing out python code to be copied and pasted into a file, 
#program simply generates a python sequence file, named "outputfile.py"
#This output file can be renamed and then executed on a raspberry pi. 
#Redesigned code to remove global lists



import sys

def createTimes(timeList):
	timeIntervalsList = [0.0]
	x = 0
	y = 1

	while y < len(timeList):
		realTime = timeList[y] - timeList[x]
		realTime = round(realTime, 4)
		timeIntervalsList.append(realTime)
		x += 1
		y += 1
		
	return timeIntervalsList

def OnOff():

	try:
		foo = open(sys.argv[1])
	except IndexError:
		print ("Could not open " + sys.argv[1])
		sys.exit()	

	#creates outletList
	OnOffList = []
	outletList = []

	#interprets whether which outlet is on or off
	for line in foo:
		line = line.strip()

		if line[7] == '1':
			outletList.append('7')
		elif line[7] == '2':
			outletList.append('11')
		elif line[7] == '3':
			outletList.append('13')
		elif line[7] == '4':
			outletList.append('15')
		elif line[7] == '5':
			outletList.append('16')
		elif line[7] == '6':
			outletList.append('18')
		elif line[7] == '7':
			outletList.append('22')
		else:
			outletList.append('29')

		#creates OnOffList
		if line[9] == '1':
			OnOffList.append('False')
		else:
			OnOffList.append('True')

	foo.close()

	return OnOffList, outletList


def generateOutputFile(timeIntervalsList, onOffList, outletList):
	#creates output python file

	#opens file for writing.  
	outFile = open("outputFile.py", "w")

	outFile.write('#' + sys.argv[1].upper() + "\n")
	
	outFile.write('\nimport time\n')
	outFile.write('import RPi.GPIO as GPIO\n')
	outFile.write('\nGPIO.setmode(GPIO.BOARD)\n')
	outFile.write('GPIO.setup(7, GPIO.OUT)\n')
	outFile.write('GPIO.setup(11, GPIO.OUT)\n')
	outFile.write('GPIO.setup(13, GPIO.OUT)\n')
	outFile.write('GPIO.setup(15, GPIO.OUT)\n')
	outFile.write('GPIO.setup(16, GPIO.OUT)\n')
	outFile.write('GPIO.setup(18, GPIO.OUT)\n')
	outFile.write('GPIO.setup(22, GPIO.OUT)\n')
	outFile.write('GPIO.setup(29, GPIO.OUT)\n')
	
	#Sets countdown to song and light sequence
	outFile.write("\nprint 'Sequence starting in 5'\n")
	outFile.write("time.sleep(1)\n")
	outFile.write("print '4'\n")
	outFile.write("time.sleep(1)\n")
	outFile.write("print '3'\n")
	outFile.write("time.sleep(1)\n")
	outFile.write("print '2'\n")
	outFile.write("time.sleep(1)\n")
	outFile.write("print '1'\n")
	outFile.write("time.sleep(1)\n")

	#analyzes each line of the data file and writes appropriate code to output file
	for num in range(0, len(timeIntervalsList)):
		outFile.write("GPIO.output(" + outletList[num] + ", " + onOffList[num] + ")\n")
		if timeIntervalsList[num] != 0.0:
			outFile.write("time.sleep(" + str(timeIntervalsList[num]) + ")\n")

	#cleanly exits GPIO sequence
	outFile.write("GPIO.cleanup()\n")

	outFile.close()


def interpretTimes():
	#creates tempTimeList

	try:
		foo = open(sys.argv[1])
	except IndexError:
		print ("Could not open " + sys.argv[1])
		sys.exit()	
	
	tempTimeList = []

	for line in foo:
		line = line.strip()
		
		#creates temp
		tempTimeList.append(float(line[:6]) / 1000)

	tempTimeList.pop()
	foo.close()

	return tempTimeList


def main():
	#initialize lists to hold times, on and off sequence, and outlets


	tempTimeList = interpretTimes()
	timeIntervalsList = createTimes(tempTimeList)
	channels = OnOff()
	generateOutputFile(timeIntervalsList, channels[0], channels[1])

	

if __name__ == "__main__":
	main()





