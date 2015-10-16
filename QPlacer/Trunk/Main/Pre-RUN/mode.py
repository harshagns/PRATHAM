#! usr/bin/env python
# Dev : Praveen Kumar K K 
# Email Id - praveen1460@iiitd.ac.in
#
#-------------------------------------------------------------------
# Functionality   	: To run application in application mode 
#					  and debug mode.
# Format Supported 	: N/A
#
# Input 		 	: N/A
# Output		  	: N/A
# 
#-------------------------------------------------------------------

class Mode():
	def __init__(self):
		self.debug = 0

#Default mode will be application, unless specified
print "Do you want to operate in Debug mode? Y/N"
mode_input = raw_input()

if mode_input == 'y' or mode_input == 'Y':
	Mode.debug = 1
else:
	Mode.debug = 0

if(Mode.debug):
	print "Debug Mode %d" % Mode.debug