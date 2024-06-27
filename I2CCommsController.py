#from smbus import SMBus

class I2CCommsController:

	def __init__(self, I2CAddress):

		self.I2CAddress = I2CAddress
		self.I2CWrite = 0x01
		self.I2CRead = 0x02

		#self.bus = SMBus(1)

	def convertStringToByte(self, src):
		
		converted = []
		for i in src:
			converted.append(ord(i))
		return converted

	def sendHeading(self, heading):

		#Higher Level Command used to set secondary PID

		sendString = 'H '+ str(heading) + ' '

		#self.bus.write_i2c_block_data(self.I2CAddress, self.I2CWrite, self.convertStringToByte(sendString))

		print(sendString)

	def sendAltitude(self, altitude):

		#Higher Level command used to set secondary PID

		sendString = 'A '+ str(altitude) + ' '

		#self.bus.write_i2c_block_data(self.I2CAddress, self.I2CWrite, self.convertStringToByte(sendString))

		print(sendString)

	def sendPIDInputs(self, roll, pitch, throttle):

		#Lower level command used to set primary PIDS

		sendString = 'R '+ roll +' P '+ pitch +' T '+ throttle + '  '

		#self.bus.write_i2c_block_data(self.I2CAddress, self.I2CWrite, self.convertStringToByte(sendString))

		print(sendString)


	def getHeading(self):

		pass

	def getAltitude(self):

		pass


