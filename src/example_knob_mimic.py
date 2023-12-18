#
#	Author:			Geraldine Barreto (gbarreto@robotshop.com)
#	Version:		1.0.0
#	Licence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#	
#	Desscription:	Moves one PRO using the position of a second PRO.
#

# Import required liraries
import time

# Import PRO library
import pro

# Constants
#CST_PRO_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
CST_PRO_Port = "COM3"				# For windows platforms

# Create and open a serial port
pro.initBus(CST_PRO_Port, 115200)

# Create two PRO object; one for output (ID=0), one for input (ID=1)
myPRO_Output = pro.PRO(6)
myPRO_Input = pro.PRO(1)

# Initialize PRO output to position 0.0
myPRO_Output.move(0)

# Wait for it to get there
time.sleep(2)

# Set maximum speed
myPRO_Output.setMaxSpeedRPM(15)

# Make input servo limp (no active resistance)
myPRO_Input.limp()

# Reproduces position of myPRO_Input on myPRO_Output
pos = 0
while 1:
	# Wait ~20 ms before sending another command (update at most 50 times per second)
	time.sleep(0.02)
	
	# Get position & check if it is valid (ex: servo missing)
	lastPos = pos
	posRead = myPRO_Input.getPosition()
	if(posRead is not None):
		pos = int(posRead,10)
		
		# Check if pos changed enough to warrant sending/showing (hysterisis of ±2)
		if ((pos < (lastPos - 2)) or (pos > (lastPos + 2))):
			# Send position to output servo and terminal
			print("Input @ " + str(pos))
			myPRO_Output.move(pos)

### EOF #######################################################################
