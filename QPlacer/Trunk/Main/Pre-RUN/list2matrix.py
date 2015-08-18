#!usr/bin/env python
#
# Dev : Praveen Kumar K K 
# Email Id - praveen1460@iiitd.ac.in
#-------------------------------------------------------------------
# Functionality		 	: 	To form the C,A & b matrix
#
# Format Supported		: 	VLSI Logic to Layout format
#							UCLA Format
#							LEF & DEF
#
# INput		  			: 	List of Gates/Pads
# Output				:	Connectivity matrix
#-------------------------------------------------------------------

import 	time
import 	mode 				as Mode
import 	class4tool 			as cell
import	numpy
from 	scipy.sparse 		import coo_matrix
import	file_processor		as fp

#Note the Starting time
start_time = time.time()


def list2matrix(gate_list,pad_list,Number_of_Gates,Number_of_Pads,Number_of_Nets):
	# Purpose is to form the matrix using the list data
	# No list modification
	# Hence Shallow Copy.
	if(Mode.Mode.debug):
		print "Cell ID\tCell Type\tNet Connected\tX\tY"
		for each_gate in gate_list:
			print each_gate.Gate_ID,"\t",each_gate.cell_type,"\t",each_gate.Col_vector,"\t",each_gate.x,"\t",each_gate.y
		for each_pad in pad_list:
			print each_pad.Gate_ID,"\t",each_pad.cell_type,"\t",each_pad.Col_vector,"\t",each_pad.x,"\t",each_pad.y	

	#Prepare Connectivity Matrix & B matrix
	final_R_vector = []
	final_C_Vector = []
	final_Net_Weight = []
	final_BR_vector = []
	final_BC_vector = []
	final_BDX_vector = []
	final_BDY_vector = []


	for number in xrange(0,int(Number_of_Gates)):

		temp_col = set(gate_list[number].Col_vector)

		for other_number in xrange(0,int(Number_of_Gates)):
			#To establish Connectivity between gates
			if(number != other_number):
				temp_other_col = set(gate_list[other_number].Col_vector)
				temp_size = temp_col & temp_other_col
				
				if(len(temp_size)!=0):
					final_R_vector.append(int(number))
					final_C_Vector.append(int(other_number))
					final_Net_Weight.append(int(-1*len(temp_size)))
			else:
				#To establish Connectivity between gates and pads
				pad_count = 0
				temp_x = 0
				temp_y = 0
				temp_count = 0
				for someother_number in xrange(0,int(len(pad_list))):
					temp_pad_col = set(pad_list[someother_number].Col_vector)
					temp_pad_size= temp_col & temp_pad_col
					if(len(temp_pad_size)!=0):
						# Here Net_Weight can be added.
						pad_count = pad_count + 1
						#final_R_vector.append(int(number))
						#final_C_Vector.append(int(other_number))
						#Appending at the same location will add the
						#Netweigth
						#final_Net_Weight.append(int(-1))
						#
						# Bulding B matrix for X & Y
						temp_x = float(temp_x) + float(pad_list[someother_number].x)
						temp_y = float(temp_y) + float(pad_list[someother_number].y)
						temp_count = int(temp_count) + 1



				final_R_vector.append(int(number))
				final_C_Vector.append(int(other_number))
				final_Net_Weight.append(int(-1*pad_count))

				if(temp_count!=0):
					final_BR_vector.append(number)
					final_BC_vector.append(0)
					final_BDX_vector.append(float(temp_x)/temp_count)
					final_BDY_vector.append(float(temp_y)/temp_count)

			#Lets form B Matrix


		#if(Mode.Mode.debug):
		#	print "Row Vector\t", final_R_vector
		#	print "Column Vector\t",final_C_Vector
		#	print "Net Weight\t",final_Net_Weight
			#input('Stop')

		#Alter this list to get the final A MAtrix
		#for opp_num in xrange((number+1),len(final_Net_Weight)):
		#	print final_Net_Weight[number]
		#	print final_Net_Weight[opp_num]
		#	final_Net_Weight[number] = int(final_Net_Weight[opp_num]) + int(final_Net_Weight[number])  

		#if(Mode.Mode.debug):
		#	print "Row Vector\t", final_R_vector
		#	print "Column Vector\t",final_C_Vector
		#	print "Net Weight\t",final_Net_Weight
			#input('Stop')

	if(Mode.Mode.debug):
		print "R Vector :", final_R_vector
		print "C Vector :", final_C_Vector
		print "Net Vector:",final_Net_Weight
		print len(final_C_Vector)
		print len(final_R_vector)
		print len(final_Net_Weight)
		

	#Convert to Array
	R_VECTOR = numpy.array(final_R_vector)
	C_VECTOR = numpy.array(final_C_Vector)
	D_VECTOR = numpy.array(final_Net_Weight)
	BR_VECTOR = numpy.array(final_BR_vector)
	BC_VECTOR = numpy.array(final_BC_vector)
	BX_VECTOR = numpy.array(final_BDX_vector)
	BY_VECTOR = numpy.array(final_BDY_vector)

	if(Mode.Mode.debug):
		print "\nARRAY"
		print "R Vector :", R_VECTOR
		print "C Vector :", C_VECTOR
		print "Net Vector:",D_VECTOR
		print "BR Vector :",BR_VECTOR
		print "BC Vector :", BC_VECTOR
		print "BX Vector :", BX_VECTOR
		print "BY Vector :", BY_VECTOR
#
	#Convert to sparse matrix
	Connectivity_Matrix = coo_matrix((D_VECTOR, (R_VECTOR, C_VECTOR))).toarray()
	Bx_Matrix = coo_matrix((BX_VECTOR,(BR_VECTOR,BC_VECTOR))).toarray()
	By_Matrix = coo_matrix((BY_VECTOR,(BR_VECTOR,BC_VECTOR))).toarray()

	if(Mode.Mode.debug):
		print Connectivity_Matrix
		print Connectivity_Matrix.shape

	#Adding the elements of the rows and store on the diagonal element
	matrix_shape = list(Connectivity_Matrix.shape)
	matrix_rows	 = matrix_shape[0]
	matrix_coloumn = matrix_shape[1]

	if(Mode.Mode.debug):
		print matrix_rows
		print matrix_coloumn

	for number in xrange(0,int(matrix_rows)):
		#First add all the elements of a row
		temp_sum = 0
		for other_number in xrange(0,int(matrix_coloumn)):
				temp_sum = int(temp_sum) + Connectivity_Matrix[number][other_number]
		Connectivity_Matrix[number][number] = int(-1*temp_sum)

	if(Mode.Mode.debug):
		print "CONNECTIVITY ---->"
		print Connectivity_Matrix
		print Connectivity_Matrix.shape
		print "------------X--------------"
		print "BX MATRIX-------->"
		print Bx_Matrix.shape
		print "BY MAtrix ------->"
		print By_Matrix.shape
#
	##Auxillary Matrix Completed with Net and Pad Information

gate_list,pad_list,Number_of_Gates,Number_of_Pads,Number_of_Nets = fp.input_parse()
list2matrix(gate_list,pad_list,Number_of_Gates,Number_of_Pads,Number_of_Nets)




print time.time() - start_time