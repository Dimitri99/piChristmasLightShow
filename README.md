# piChristmasLightShow
A Christmas light display using a raspberry pi 3

This light controller currently possesses 8 channels using the General Input and Output (G.P.I.O.) pins on the raspberry pi.  I am currently working towards making a 16 channel controller.

--THE PARSER--
The parser, written in Python 3, takes one command line argument, a .txt file, and outputs the appropriate Python code to the terminal or console.  To run the parser, type

   python3 xmasLightParser.py inputFile.txt

into the terminal.  The parser will then output the code for the .py file.  Then, one can copy and paste the python code into a .py file to create a new light sequence for the pi.  

--THE .TXT INPUT FILE/DATA FILE--
The .txt files I included in the project are not my own. They come from a google drive in the comments section of https://www.instructables.com/id/Raspberry-Pi-Christmas-Tree-Light-Show/
These data files can be created using the Light-O-Rama software application.  When analyzing the data file, each line contains 1) a channel number, 2) whether it is on or off, and 3) at what time in the song to turn the light on, measured in 1 one-thousandths of a second.  

--THE GPIO PINS--
The GPIO pins I used to control the 8-channel relay are 
channel 1) pin 7 (GPIO 4) 
channel 2) pin 11 (GPIO 17)
channel 3) pin 13 (GPIO 27)
channel 4) pin 15 (GPIO 22)
channel 5) pin 16 (GPIO 23)
channel 6) pin 18 (GPIO 24)
channel 7) pin 22 (GPIO 25)
channel 8) pin 29 (GPIO 5)

--NOTE--
My parser generates code so that 'False' or '1' means "turn the light on" and 'True' or '0' means "Turn the light off. Some relays may represent 'True' as on and 'False' as off.  I am used a Sans-Smart 8-channel relay board, which represents 'False' as on, and visa versa.  
