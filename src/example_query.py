#
#	Author:			Geraldine Barreto (gbarreto@robotshop.com)
#	Version:		1.0.0
#	Licence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#	
#	Desscription:	Basic example of reading values from the PRO and placing
#					them on the terminal.
#

# Import required liraries
import time

# Import PRO library
import pro

# Constants
#CST_PRO_Port = "/dev/ttyUSB0"		# For Linux/Unix platforms
CST_PRO_Port = "COM3"				# For 	Windows platforms

# Create and open a serial port
pro.initBus(CST_PRO_Port, 115200)

# Create a PRO object
myPRO = pro.PRO(1)

while 1:
	# Get the values from PRO
	print("\r\nQuerying PRO motor")
	pos = myPRO.getPosition()
	rpm= myPRO.getSpeedRPM()
	curr = myPRO.getCurrent()
	temp = myPRO.getPcbTemperature()
	imuX = myPRO.getIMULinearX()
	
	# Display the values in terminal
	print("\r\n---- Telemetry ----")
	print("Position  (1/100 deg) = " + str(pos))
	print("Speed          (rpm) = " + str(rpm))
	print("Current          (mA) = " + str(curr))
	print("PCB Temperature (1/10 C) = " + str(temp))
	print("IMU Linear Accel X (1/10 mm/s^2) = " + str(imuX))

	# Wait 1 second
	time.sleep(1)

### EOF #######################################################################
