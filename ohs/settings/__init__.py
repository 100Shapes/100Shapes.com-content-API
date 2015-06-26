import os

if (os.environ.get('PRODUCTION') == 'True'):
	print "PRODUCTION Environment found"
	from .production import *
else:
	print "PRODUCTION Environment NOT found"
	from .dev import *