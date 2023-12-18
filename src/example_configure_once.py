#
#	Author:			Geraldine Barreto (gbarreto@robotshop.com)
#	Version:		1.0.0
#	Licence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#	
#	Desscription:	Example of all the possible configurations for a PRO motor.
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

# Create an PRO object
myPRO = pro.PRO(1)

# Uncomment any configurations that you wish to activate
# You can see above each configuration a link to its description in the Lynxmotion wiki
# Note: If you change a configuration to the same value that is already set,
#       the PRO will ignore the operation since the value is not changed.

# *** Basic configurations ***
# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#H6.OriginOffsetAction28O29
###myPRO.setOriginOffset(0)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#H7.AngularRange28AR29
###myPRO.setAngularRange(1800, lssc.LSS_SetConfig)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#H12.MaxSpeedinDegrees28SD29
# Set maximum speed in (1/10 deg)/s
###myPRO.setMaxSpeed(600, lssc.LSS_SetConfig)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#H13.MaxSpeedinRPM28SR29
###myPRO.setMaxSpeedRPM(100, lssc.LSS_SetConfig)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#H14.LEDColor28LED29
# Options are:
# LSS_LED_Black = 0
# LSS_LED_Red = 1
# LSS_LED_Green = 2
# LSS_LED_Blue = 3
# LSS_LED_Yellow = 4
# LSS_LED_Cyan = 5
# LSS_LED_Magenta = 6
# LSS_LED_White = 7
###myPRO.setColorLED(lssc.LSS_LED_Black, lssc.LSS_SetConfig)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#H15.GyreRotationDirection28G29
# Options are:
# LSS_GyreClockwise = 1
# LSS_GyreCounterClockwise = -1
###myPRO.setGyre(lssc.LSS_GyreClockwise, lssc.LSS_SetConfig)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#H19.FirstA0Position28Degrees29
###myPRO.setFirstPosition(0)
###myPRO.clearFirstPosition()

# *** Advaned configurations ***
# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#HA3:AngularAcceleration28AA29
###myPRO.setAngularAcceleration(100, lssc.LSS_SetConfig)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#HA4:AngularDeceleration28AD29
###myPRO.setAngularDeceleration(100, lssc.LSS_SetConfig)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#HA5:MotionControl28EM29
###myPRO.setMotionControlEnabled(True)

# https://www.robotshop.com/info/wiki/lynxmotion/view/lynxmotion-smart-servo/lss-communication-protocol/#HA6.ConfigureLEDBlinking28CLB29
# Options are an arithmetic addition of the following values:
# Limp	1
# Holding	2
# Accelerating	4
# Decelerating	8
# Free	16
# Travelling	32
# Therefore, 0 = no blinking and 63 = always blinking
###myPRO.setBlinkingLED(0)

# Reset motor to complete change of configurations
myPRO.reset()

# Wait for reboot
time.sleep(10)

# Create and open a serial port
pro.initBus(CST_PRO_Port, 115200)

# Create a PRO object
myPRO = pro.PRO(1)

color_names = ["Black","Red","Green","Blue","Yellow","Cyan","Magenta","White"]

while 1:
	# Loop through each of the 8 LED color (black = 0, red = 1, ..., white = 7)
	for i in range (0,7):
		print("Changing LED color to " + str(color_names[i]))
		# Set the color (session) of the PRO
		myPRO.setColorLED(i)
		# Wait 2 seconds per color change
		time.sleep(2)

### EOF #######################################################################
