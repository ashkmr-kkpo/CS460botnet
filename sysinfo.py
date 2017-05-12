#get system information
def info(self):
	return '%s: %s, %s, %s, %s' % (
	        __file__,
	        platform.platform(),
	        platform.architecture()[0],
	        platform.node(),
	        platform.python_version(),
	    )

info(self)