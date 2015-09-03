import urllib
import optparse


parser = optparse.OptionParser("usage : %prog "+\
		"-u <Enter Taget URL Here>")
parser.add_option('-u', dest = 'uname', type = 'string',\
		help='Specify Target URL')
(options, arg) = parser.parse_args()
if (options.uname == None) :
	print parser.usage
	exit(0)
else :
	print '\t\t\t ######################################'
	print '\t\t\t ##                                  ##'
	print '\t\t\t ##   Author : Sandeep Saini         ##'
	print '\t\t\t ######################################'
	uname = options.uname
 	url = urllib.urlopen(uname)
for header , value in url.headers.items():
	print header + ':' + value 	
