#!usr/bin/env python
#
# Dev : Praveen Kumar K K 
# Email Id - praveen1460@iiitd.ac.in
#-------------------------------------------------------------------
# Functionality : To process the input file and provide necessary 
#				  format for further processsing.
# Format Supported: VLSI Logic to Layout format
#					UCLA Format
#					LEF & DEF
#
# Input 		  : Design Netlist (Gate,Nets,Pads)
# Output		  : List of Gates/Pads
#
#-------------------------------------------------------------------

#Remove Only --> Shoud be Integrated in the Main Caller
import mode as Mode
import class4tool as cell


#Task List:
# Read the file in different directory							- D
# Output the entire input_file 									- D
# Once that is done,
# Create a function in this file, which parses the input file.
# Get Number of gates and nets for the netlist
# Create an ID Counter and numnets var
# Create an method in stdCell class, to...
# ...create 2 lists -> Row List, Coloumn List, NetWeigth list...
# ...Note - List size will be number of gates.
# ...Data below is to facilitate in creation of sparse matrix...
# ...using a co-ordinate matrix. (Row,Coloumn)-(data)
# ...Note - Row_List --> populate all the elements as id number.
# ...Note - Col_list --> populate with the net_id.
# ...Note - net_Weight --> Initially 1 for all nets
# Check for sanity :P
# After that, pad info.

def input_parse():
	input_file = open('../../Input/Test_1','r')

	# this *.split() returns numbers from the file
	in_data = input_file.readline().split()

	if(Mode.Mode.debug):
		print in_data

	#Getting the number of Gates and netid
	Number_of_Gates = in_data[0]
	Number_of_Nets  = in_data[1]

	if(Mode.Mode.debug):
		print "Number of Gates : %s" % Number_of_Gates
		print "Number of Nets  : %s" % Number_of_Nets


# For Testing ; Remove Only.
if(Mode.Mode.debug):
	input_parse()