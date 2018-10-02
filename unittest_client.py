from client import *
from server import *


def testConeectNoServer():
	try:
		connect("127.0.0.1", 8080)
		raise Exception("We connected even though the server is not up!")
	except:
		pass

def testConnectServer():
	try:
		startserver("127.0.0.1", 8081)
		connect("127.0.0.1", 8081)
		closeserver()
	except:
		raise Exception("Cannot connect!")

def testReceiveEmpty():
	if (has_message()):
		raise Exception("Has message even though we're not connected!")
	if(receive() != ''):
		raise Exception("Message received is not empty!")


if __name__ == '__main__':
	testConeectNoServer()
	testConnectServer()
	testReceiveEmpty()
	something()