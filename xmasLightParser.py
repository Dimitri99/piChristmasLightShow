#Christmas Light Parser
#
#Author: Dimitri Charitou
#December 2017

#Update: July 23, 2018

#Parser which outputs code for inputted light sequence
#python3 xmasLightParser.py data file

import sys

#initialize lists to hold times, on and off sequence, and outlets
tempTimeList = []
timeIntervalsList = [0.0]
OnOffList = []
outletList = []


def createTimes():
	x = 0
	y = 1
	while y < len(tempTimeList):
		realTime = tempTimeList[y] - tempTimeList[x]
		realTime = round(realTime, 4)
		timeIntervalsList.append(realTime)
		x += 1
		y += 1
	

def OnOff():
	#creates outletList
	try:
		file = open(sys.argv[1])
	
	except IndexError:
		print ("Could not open " + sys.argv[1])
		sys.exit()

	#interprets whether which outlet is on or off
	for line in file:
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


	file.close()


def generate():
	#prints code for light sequence

	#sets up GPIO settings
	print ('#' + sys.argv[1].upper())
	print ('#\n')
	print ('import time\n')
	print ('import RPi.GPIO as GPIO')
	print ('GPIO.setmode(GPIO.BOARD)')
	print ('GPIO.setup(7, GPIO.OUT)')
	print ('GPIO.setup(11, GPIO.OUT)')
	print ('GPIO.setup(13, GPIO.OUT)')
	print ('GPIO.setup(15, GPIO.OUT)')
	print ('GPIO.setup(16, GPIO.OUT)')
	print ('GPIO.setup(18, GPIO.OUT)')
	print ('GPIO.setup(22, GPIO.OUT)')
	print ('GPIO.setup(29, GPIO.OUT)\n')
	#Sets countdown to song and light sequence
	print ("print 'Sequence starting in 5'")
	print ("time.sleep(1)")
	print ("print '4'")
	print ("time.sleep(1)")
	print ("print '3'")
	print ("time.sleep(1)")
	print ("print '2'")
	print ("time.sleep(1)")
	print ("print '1'")
	print ("time.sleep(1)")

	#analyzes each line of the data file and generates the appropriate code
	for a in range(0, len(timeIntervalsList)):
		print ('GPIO.output(' + outletList[a] + ', ' + OnOffList[a] + ')')
		if timeIntervalsList[a] != 0.0:
			print ('time.sleep(' + str(timeIntervalsList[a]) + ")")

	#cleanly exits GPIO sequence
	print ("GPIO.cleanup()\n")


def interpretTimes():
	#creates tempTimeList
	try:
		file = open(sys.argv[1])
	except IndexError:
		print ("Could not open " + sys.argv[1])
		sys.exit()

	for line in file:
		#creates temp
		tempTimeList.append(float(line[:6]) / 1000)

	tempTimeList.pop()

	file.close()


def main():
	interpretTimes()
	createTimes()
	OnOff()
	generate()

if __name__ == '__main__':
	main()





