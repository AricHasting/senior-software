from server import *


def testName():
	startserver("127.0.0.1", 8083)
	if SERVER.getsockname() != ("127.0.0.1", 8083):
		raise Exception('Failed test!')
	closeserver()


def testStart():
	try:
		startserver("127.0.0.1", 8082)
		closeserver()
	except:
		raise Exception('Failed test!')


if __name__ == '__main__':
	testName()
	testStart()