###############################################################################
#	Author:			Geraldine Barreto (gbarreto@robotshop.com)
#	Version:		1.0.0
#	Licence:		LGPL-3.0 (GNU Lesser General Public License version 3)
#	
#	Desscription:	A library that makes using the PRO simple.
#					Offers support for most Python platforms.
#					Uses the Python serial library (pySerial).
###############################################################################

### List of constants

# PRO models
PRO_ModelLite = 0
PRO_ModelStandard = 1
PRO_ModelMega = 2
PRO_ModelUnknown = 3

PRO_MODEL_L1 = "LSS-P-L1"
PRO_MODEL_S1 = "LSS-P-S1"
PRO_MODEL_M1 = "LSS-P-M1"

# Commands - actions (settings)
GRIP_ActionJawOpeningOffset = "JO"
GRIP_ActionJawOpening	 = "J"
GRIP_ActionJawOpeningDeg = "JD"

# Commands - queries
PRO_QueryMotorTemperature = "QTP"
PRO_QueryMCUTemperature = "QTM"
PRO_QueryDriverTemperature = "QTCW"
PRO_QueryTerminalResistor = "QET"
PRO_QueryUSBConnection = "QUC"

# Commands - queries advanced
PRO_QueryIMULinearAccelX = "QIX"
PRO_QueryIMULinearAccelY = "QIY"
PRO_QueryIMULinearAccelZ = "QIZ"
PRO_QueryIMUAngularAccelA = "QIA"
PRO_QueryIMUAngularAccelB = "QIB"
PRO_QueryIMUAngularAccelG = "QIG"		# Potentially add C since many might assume A,B,C

# # Commands - Gripper queries
# GRIP_QueryCombinedJawForce = "QJF"
# GRIP_QueryJawForceLeft	 = "QJF1"
# GRIP_QueryJawForceRight	 = "QJF2"
# GRIP_QueryLoadCellForceX = "QFX"
# GRIP_QueryLoadCellForceY = "QFY"
# GRIP_QueryLoadCellForceZ = "QFZ"
# GRIP_QueryJawOpeningOffset = "QJO"
# GRIP_QueryJawOpening	 = "QJ"
# GRIP_QueryJawOpeningDeg	 = "QJD"

# Commands - configurations
PRO_ConfigTerminalResistor = "CET"
# GRIP_ConfigJawOpeningOffset = "CJO"

### EOF #######################################################################
