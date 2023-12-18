###############################################################################
#	Author:			Geraldine Barreto (gbarreto@robotshop.com)
#	Version:		1.0.0
#	Licence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#	
#	Desscription:	A library that makes using the PRO simple.
#					Offers support for most Python platforms.
#					Uses the Python serial library (pySerial).
###############################################################################

### Import constants
import lss_const as lssc
import pro_const as proc
from lss import *

class PRO:
	### Constructor
	def __init__(self, id = 0):
		self.lss = LSS(id)
		self.servoID = id
	
	### Functions
	#> Actions
	def reset(self):
		return (self.lss.reset())
	
	def limp(self):
		return (self.lss.limp())
	
	def hold(self):
		return (self.lss.hold())
	
	# 0.01°
	def move(self, pos):
		return (self.lss.move(pos))
	
	# 0.01°/s
	def moveRelative(self, delta):
		return (self.lss.moveRelative(delta))
	
	# 0.01°/s
	def wheel(self, speed):
		return (self.lss.wheel(speed))
	
	def wheelRPM(self, rpm):
		return (self.lss.wheelRPM(rpm))
	
	#> Queries
	#def getID(self):
	#def getBaud(self):
	
	def getStatus(self):
		return (self.lss.getStatus())
	
	def getOriginOffset(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getOriginOffset(queryType))
	
	def getAngularRange(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getAngularRange(queryType))

	# 0.01°
	def getPosition(self):
		return (self.lss.getPosition())
	
	def getSpeed(self):
		return (self.lss.getSpeed())
	
	def getSpeedRPM(self):
		return (self.lss.getSpeedRPM())
	
	def getMaxSpeed(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getMaxSpeed(queryType))
	
	def getMaxSpeedRPM(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getMaxSpeedRPM(queryType))
	
	def getColorLED(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getColorLED(queryType))
	
	def getGyre(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getGyre(queryType))
	
	# returns 0 if "DIS"
	# 0.01°
	def getFirstPosition(self):
		return (self.lss.getFirstPosition())
	
	# returns true/false based on if QFD returns "DIS" (= False)
	def getIsFirstPositionEnabled(self):
		return (self.lss.getIsFirstPositionEnabled())
	
	def getModel(self):
		return (self.lss.getModel())
	
	def getSerialNumber(self):
		return (self.lss.getSerialNumber())
	
	def getFirmwareVersion(self):
		return (self.lss.getFirmwareVersion())
	
	def getPcbTemperature(self):
		return (self.lss.getTemperature())
	
	def getMotorTemperature(self):
		genericWrite(self.servoID, proc.PRO_QueryMotorTemperature)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryMotorTemperature))
	
	def getMcuTemperature(self):
		genericWrite(self.servoID, proc.PRO_QueryMCUTemperature)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryMCUTemperature))
	
	def getDriverTemperature(self):
		genericWrite(self.servoID, proc.PRO_QueryDriverTemperature)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryDriverTemperature))
	
	def getTerminalResistor(self):
		genericWrite(self.servoID, proc.PRO_QueryTerminalResistor)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryTerminalResistor))
	
	def getUSBConnection(self):
		genericWrite(self.servoID, proc.PRO_QueryUSBConnection)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryUSBConnection))
	
	def getCurrent(self):
		return (self.lss.getCurrent())
	
	# 1/10 mm/s^2
	def getIMULinearX(self):
		genericWrite(self.servoID, proc.PRO_QueryIMULinearAccelX)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryIMULinearAccelX))
	
	# 1/10 mm/s^2
	def getIMULinearY(self):
		genericWrite(self.servoID, proc.PRO_QueryIMULinearAccelY)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryIMULinearAccelY))
	
	# 1/10 mm/s^2
	def getIMULinearZ(self):
		genericWrite(self.servoID, proc.PRO_QueryIMULinearAccelZ)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryIMULinearAccelZ))
	
	# 1/10 mm/s^2
	def getIMUAngularA(self):
		genericWrite(self.servoID, proc.PRO_QueryIMUAngularAccelA)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryIMUAngularAccelA))
	
	# 1/10 mm/s^2
	def getIMUAngularB(self):
		genericWrite(self.servoID, proc.PRO_QueryIMUAngularAccelB)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryIMUAngularAccelB))
	
	# 1/10 mm/s^2
	def getIMUAngularG(self):
		genericWrite(self.servoID, proc.PRO_QueryIMUAngularAccelG)
		return (genericRead_Blocking_int(self.servoID, proc.PRO_QueryIMUAngularAccelG))
	
	#> Queries (advanced)
	def getAngularAcceleration(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getAngularAcceleration(queryType))
	
	def getAngularDeceleration(self, queryType = lssc.LSS_QuerySession):
		return (self.lss.getAngularDeceleration(queryType))
	
	def getIsMotionControlEnabled(self):
		return (self.lss.getIsMotionControlEnabled())
	
	def getBlinkingLED(self):
		return (self.lss.getBlinkingLED())
	
	#> Configs
	def setOriginOffset(self, pos, setType = lssc.LSS_SetSession):
		return (self.lss.setOriginOffset(pos, setType))
	
	# 0.01°
	def setAngularRange(self, delta, setType = lssc.LSS_SetSession):
		return (self.lss.setAngularRange(delta, setType))
	
	# 0.01°/s
	def setMaxSpeed(self, speed, setType = lssc.LSS_SetSession):
		return (self.lss.setMaxSpeed(speed, setType))
	
	def setMaxSpeedRPM(self, rpm, setType = lssc.LSS_SetSession):
		return (self.lss.setMaxSpeedRPM(rpm, setType))
	
	def setColorLED(self, color, setType = lssc.LSS_SetSession):
		return (self.lss.setColorLED(color, setType))
	
	def setGyre(self, gyre, setType = lssc.LSS_SetSession):
		return (self.lss.setGyre(gyre, setType))
	
	def setFirstPosition(self, pos):
		return (self.lss.setFirstPosition(pos))
	
	def clearFirstPosition(self):
		return (self.lss.clearFirstPosition())
	
	#> Configs (advanced)
	# 0.01°/s
	def setAngularAcceleration(self, value, setType = lssc.LSS_SetSession):
		return (self.lss.setAngularAcceleration(value, setType))
	
	# 0.01°/s
	def setAngularDeceleration(self, value, setType = lssc.LSS_SetSession):
		return (self.lss.setAngularDeceleration(value, setType))
	
	def setMotionControlEnabled(self, value):
		return (self.lss.setMotionControlEnabled(value))
	
	def setBlinkingLED(self, state):
		return (self.lss.setBlinkingLED(state))
	
### EOF #######################################################################
