import urllib2
import json
from daemon import runner
import time
import pluginBase
import pportOutput
import sys

class App():
	def __init__(self):
		self.stdin_path = '/dev/null'
		self.stdout_path = '/dev/tty'
		self.stderr_path = '/dev/tty'
		self.pidfile_path =  '/tmp/foo.pid'
		self.pidfile_timeout = 5
		self.numberOfMessages = 0
		self.pluginList = []
		self.sendUpdate = True
		#self.data = 
		for plugin in pluginBase.Plugin.__subclasses__():
			self.pluginList.append(plugin())
	def run(self):
		while True:
			try:
				address = 'http://www.reddit.com/message/unread/.json?feed=7f7c1e26998324cfcc8480d15ed68cad40781db1&user=supersecrettestaccou'
				data = urllib2.urlopen(address)
				messages = json.load(data)
				self.numberOfMessages = len(messages['data']['children'])
				if self.numberOfMessages != 0:
					if self.sendUpdate:
						self.update()
						self.sendUpdate = False
				else:
					if self.sendUpdate == False:
						self.stop()
						self.sendUpdate = True
			except urllib2.HTTPError as e:
				print(e)
			time.sleep(1)
	def update(self):
		for plugin in self.pluginList:
			plugin.update()
	
	def stop(self):
		for plugin in self.pluginList:
			plugin.stop()

if __name__=='__main__':
	app = App()
	daemon_runner = runner.DaemonRunner(app)
	daemon_runner.do_action()
