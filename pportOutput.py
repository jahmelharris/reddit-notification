import pluginBase
import thread
import serial
import time
class pportPlugin(pluginBase.Plugin):
#	def __init__(self):
#		self.ser = serial.Serial(port='/dev/ttyS0')
#		self.ser.open()
#		self.Flash = False
#		self.ser.setDTR(False)
	def update(self):
		print("Message To read")
		self.flash = True
		thread.start_new_thread(self.flashLED, ())
		
	
	def stop(self):
		print("No more messages")
		self.flash = False

	def flashLED(self):
		self.ser = serial.Serial(port='/dev/ttyS0')
		self.ser.open()
		self.Flash = False
		self.ser.setDTR(False)

		while self.flash:
			self.ser.setDTR(True)
			time.sleep(2)
			self.ser.setDTR(False)
			time.sleep(2)
		
