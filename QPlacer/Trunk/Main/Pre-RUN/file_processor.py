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
import numpy
from scipy.sparse import coo_matrix


#Task List:
# Read the file in different directory							- D
# Output the entire input_file 									- D
# Once that is done,
# Create a function in this file, which parses the input file.
# Get Number of gates and nets for the netlist
# Create an ID Counter and numnets var
# Create an method in stdCell class, to...
# ...create 3 lists -> Row List, Coloumn List, NetWeigth list...
# ...Note - List size will be number of gates.
# ...Data below is to facilitate in creation of sparse matrix...
# ...using a co-ordinate matrix. (Row,Coloumn)-(data)
# ...Note - Row_List --> populate all the elements as id number.
# ...Note - Col_list --> populate with the net_id.
# ...Note - net_Weight --> Initially 1 for all nets
# Check for sanity :P
# After that, pad info.

def input_parse():
	#Gate_List
	Design_Gate_List = []
	Design_Pad_List  = []
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

	for number in xrange(int(Number_of_Gates)):
		in_data = input_file.readline().split()
		temp_gate_id = in_data[0]
		temp_gate_numnets = in_data[1]
		temp_name = 'gate#'+in_data[0]
		temp_gate = cell.stdCell()
		temp_gate.get_id_numnets(int(temp_gate_id),int(temp_gate_numnets),temp_name)
		for number in xrange(int(temp_gate_numnets)):
			temp_Net_data = in_data[2+number]
			#Net Weigth currently One.
			temp_Net_Weight = 1
			temp_gate.construct_R_C_D(int(temp_Net_data),int(temp_Net_Weight))
		Design_Gate_List.append(temp_gate)	
		if(Mode.Mode.debug):
			print "Cell ID       : %d" % temp_gate.Gate_ID,"\tCell Nut Conn.: %d" % temp_gate.Num_nets
			print "Cell's R Data :   ",temp_gate.Row_vector
			print "Cell's C Data :   ",temp_gate.Col_vector
			print "Cell's D Data :   ",temp_gate.Net_Weight

	#Prepare Connectivity Matrix
	final_R_vector = []
	final_C_Vector = []
	final_Net_Weight = []
	for each_gate in Design_Gate_List:
		final_R_vector = final_R_vector + each_gate.Row_vector
		final_C_Vector = final_C_Vector + each_gate.Col_vector
		final_Net_Weight = final_Net_Weight + each_gate.Net_Weight


	if(Mode.Mode.debug):
		print "R Vector :", final_R_vector
		print "C Vector :", final_C_Vector
		print "Net Vector:",final_Net_Weight

	#Convert to Array
	R_VECTOR = numpy.array(final_R_vector)
	C_VECTOR = numpy.array(final_C_Vector)
	D_VECTOR = numpy.array(final_Net_Weight)

	if(Mode.Mode.debug):
		print "\nARRAY"
		print "R Vector :", R_VECTOR
		print "C Vector :", C_VECTOR
		print "Net Vector:",D_VECTOR

	#Convert to sparse matrix
	Connectivity_Matrix = coo_matrix(D_VECTOR, (R_VECTOR, C_VECTOR)).toarray()

	if(Mode.Mode.debug):
		print Connectivity_Matrix
	







# For Testing ; Remove Only.
if(Mode.Mode.debug):
	input_parse()