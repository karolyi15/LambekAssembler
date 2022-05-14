##################################################
# LAMBEK ASSEMBLER
# Instituto Tecnologico de Costa Rica
# Escuala Computacion
# 13/05/2022
##################################################
from LexicalAnalizer.Parser import *

###################################
# MAIN PROGRAM
###################################

# Declare Source File Path

#sourcePath = "Source/test"
#sourcePath = "Source/SumaNoDestructiva.txt"
#sourcePath = "Source/MultiplicacionNoDestructiva.txt"
sourcePath = "Source/RestaNoDestructiva.txt"
#sourcePath = "Source/DivisionNoDestructiva.txt"


# Create Parser
parser = Parser(sourcePath)

# Parse Source File Program
parser.parse()

# The output will be generated in the Source dir, under the name output.
# The file extension for the output program is lmk  in dedicatory to Lambek.



