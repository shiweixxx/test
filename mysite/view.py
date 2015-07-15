from django.http import *
from django.conf import settings
import MySQLdb

def testconf(request):
	return HttpResponse(settings.ROOT_URLCONF)
def tshell():
	print "hello,world"