#! usr/bin/env python
# Dev : Praveen Kumar K K 
# Email Id - praveen1460@iiitd.ac.in
#
#-------------------------------------------------------------------
# Functionality 	: Provides base classes
# Format Supported	: N/A
#
# Input 		  	: N/A
# Output		  	: N/A
#
#-------------------------------------------------------------------
# Primary Classes

#Defines mode of operations
import mode as Mode

#CELL
class Cell():
	#co-ordinates - bottom left
	def __init__(self):
		self.x = 0
		self.y = 0
	#Physical dimensions of cells
		self.height = 0
		self.width  = 0

# CORE CELL
class stdCell(Cell):
	#reset id and numnets
	def __init__(self):
		Cell.__init__(self)
		self.Gate_ID = 0
		self.Num_nets= 0
		self.cell_type = 'CORE'
		self.Row_vector = []
		self.Col_vector = []
		self.Net_Weight = []

	# Set the ID and number of net information for this cell
	def get_id_numnets(self,id_cell,numnets,name):
		self.Gate_ID = id_cell
		self.name_cell = name
		self.Num_nets= numnets

	def construct_R_C_D(self,Net_data,Net_Val):
		self.Row_vector.append(int(self.Gate_ID))
		self.Col_vector.append(int(Net_data))
		self.Net_Weight.append(int(Net_Val))





#To test and debug
if(Mode.Mode.debug):
	a = stdCell()
	a.get_id_numnets(1,34,'ANDx4112')
	print "Cell Name     : %s" % a.name_cell
	print "Bottom Left X : %d" % a.x
	print "Bottom Left Y : %d" % a.y
	print "Cell Heigth   : %d" % a.height
	print "Cell Width    : %d" % a.width
	print "Cell Type     : %s" % a.cell_type
	print "Cell ID       : %d" % a.Gate_ID
	print "Cell Nut Conn.: %d" % a.Num_nets