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

import 	mode 				as Mode
import 	class4tool 			as cell
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
# ...Note - Col_list --> populate with the net_id
#      	  - Set-ify each list
# ...Note - net_Weight --> Initially 1 for all nets
# Check for sanity :P
# After that, pad info.
# CORRCTION:
# No Need to populate the Row and Data Vector initially.
# Form Gate List
# Take one gate at a time, find the intersection of the net info
# ... by comparing each gate net info
# ALgo :
# 

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

	# Form the Gate List
	for number in xrange(int(Number_of_Gates)):
		in_data = input_file.readline().split()
		temp_gate_id = in_data[0]
		temp_gate_numnets = in_data[1]
		temp_name = 'gate#'+in_data[0]
		temp_gate = cell.stdCell()
		temp_type = 'CORE'
		temp_gate.get_id_numnets(int(temp_gate_id),int(temp_gate_numnets),temp_name,temp_type)
		for number in xrange(int(temp_gate_numnets)):
			temp_Net_data = in_data[2+number]
			#Net Weigth currently 1
			temp_Net_Weight = 1
			temp_gate.construct_R_C_D(int(temp_Net_data),int(temp_Net_Weight))
		Design_Gate_List.append(temp_gate)	
		
	
	# Form the Pad List
	# The next line to read consist of Number pads.
	# Pad has these info:
	#	X,Y Cordinates
	#	Net_Id
	#   Pad ID
	
	#Get Number of pads for this design.
	in_data = input_file.readline().split()
	Number_of_Pads = in_data[0]


	#Form the Pad List
	for number in xrange(int(Number_of_Pads)):
		in_data = input_file.readline().split()
		temp_pad_id = in_data[0]
		temp_name = 'Pad#'+in_data[0]
		temp_pad_numnets = 1
		temp_pad = cell.stdCell()
		temp_type = 'PAD'
		temp_pad.get_id_numnets(int(temp_pad_id),int(temp_pad_numnets),temp_name,temp_type)
		temp_Net_data = in_data[1]
		#Net Weigth currently 1
		temp_Net_Weight = 1
		temp_pad.construct_R_C_D(int(temp_Net_data),int(temp_Net_Weight))
		temp_pad_x = in_data[2]
		temp_pad_y = in_data[3]
		temp_pad.x = float(temp_pad_x)
		temp_pad.y = float(temp_pad_y)
		Design_Pad_List.append(temp_pad)

	#GATE AND PAD LIST HAVE BEEN FORMED
	
	print "|------------SUMMARY-------------|"
	print "\n"
	print "Number\tof\tCore\tCells\t %d" % len(Design_Gate_List)
	print "Number\tof\tPad\tCells\t %d" % len(Design_Pad_List)
	print "Number\tof\tNets\t\t %d"	% int(Number_of_Nets)
	
	#REMOVE --> 
	if(Mode.Mode.debug):
		print "Cell ID\tCell Type\tNet Connected\tX\tY"
		for each_gate in Design_Gate_List:
			print each_gate.Gate_ID,"\t",each_gate.cell_type,"\t",each_gate.Col_vector,"\t",each_gate.x,"\t",each_gate.y
		for each_pad in Design_Pad_List:
			print each_pad.Gate_ID,"\t",each_pad.cell_type,"\t",each_pad.Col_vector,"\t",each_pad.x,"\t",each_pad.y	
			
	return (Design_Gate_List,Design_Pad_List,Number_of_Gates,Number_of_Pads,Number_of_Nets)


# For Testing ; Remove Only.
#if(Mode.Mode.debug):
#	input_parse()