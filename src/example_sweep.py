#
#	Author:			Geraldine Barreto (gbarreto@robotshop.com)
#	Version:		1.0.0
#	Licence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#	
#	Desscription:	Basic example of the PRO moving back and forth.
#

# Import required liraries
import time

# Import PRO library
import pro

# Constants
#CST_PRO_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
CST_PRO_Port = "COM3"				# For Windows platforms

# Create and open a serial port
pro.initBus(CST_PRO_Port, 115200)

# Create a PRO object
myPRO = pro.PRO(1)

# Initialize PRO to position 0.0 deg
myPRO.move(0)

# Wait for it to get there
time.sleep(3)

# Loops between -180.0 deg and 180 deg, taking 1 second pause between each half-circle move.
while 1:
	# Send PRO to half a turn counter-clockwise from zero 1/100 deg (assumes gyre = 1)
	print("Moving to 180deg counter-clockwise")
	myPRO.move(-18000)
	
	# Wait for two seconds
	time.sleep(3)
	
	print("Moving to 180deg clockwise")
	# Send PRO to half a turn clockwise from zero 1/100 deg (assumes gyre = 1)
	myPRO.move(18000)
	
	# Wait for two seconds
	time.sleep(3)

### EOF #######################################################################
