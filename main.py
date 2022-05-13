from LexicalAnalizer.Parser import *

###################################
# MAIN PROGRAM
###################################

# Declare Source File Path
sourcePath = "Source/test"

# Create Parser
parser = Parser(sourcePath)

# Parse Source File Program
parser.parse()

# The output will be generated in the Source dir, under the name output.
# The file extension for the output program is lmk  in dedicatory to Lambek.



