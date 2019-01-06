#
# USAGE - ./get_unidentifieds.py <FASTA_FILE> <KRAKEN_RESULTS_TXT_FILE> <OUTPUT_DIRECTORY_NAME>
# Not doing it in this format will just crash. Could not be bothered with data validation
#

import sys
import os

list_of_scaffolds = []

with open(sys.argv[2]) as inputfile:
	for line in inputfile:
		list_of_words = line.split("\t") #Split by tabs
		try:
			second_list_of_words = list_of_words[2].split()
			if second_list_of_words[0] == "unclassified":
				list_of_scaffolds.append(">" + list_of_words[1] + "\n")
		except:
			pass

print ("\nUNCLASSIFIED SCAFFOLDS: \n")
for line in list_of_scaffolds:
	print (line)

if not os.path.exists(sys.argv[3]):
	os.makedirs(sys.argv[3])

cur_path = os.path.dirname(__file__)
with open(sys.argv[1]) as fastaFile:
	isOpen = False
	for line in fastaFile:
		if line in list_of_scaffolds:
			newLine = line.rstrip()
			path = '.\\' + newLine + '.txt'
			new_path = os.path.join(os.getcwd(), sys.argv[3] + "/" + newLine[1:] + ".txt") 
			print ("UNCLASSIFIED! " + newLine)
			print ("PATH: " + new_path)
			f = open(new_path, "w+")
			isOpen = True
		elif line[0] == '>':
			print (line)
			isOpen = False

		if isOpen:	
			f.write(line)
			

