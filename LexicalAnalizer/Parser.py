from LexicalAnalizer.Scanner import *
from LexicalAnalizer.Token import *


class Parser:

    # Class Fields
    _sourceFile = None
    _outputFile = None

    _scanner = None
    _currentToken = None

    _translation = ""

    # Class Constructor
    def __init__(self, sourceFilePath):
        # Init source file
        self._sourceFile = SourceFile(sourceFilePath)
        # Init scanner
        self._scanner = Scanner(self._sourceFile)
        # Init output file
        self._outputFile = SourceFile("Source/output.lmk")
        # Init current token
        self._fetchToken()

    # Class Process
    # fetchToken - Method to fetch the next token
    def _fetchToken(self):
        self._currentToken = self._scanner.scan()

    def _acceptToken(self, expected):
        if self._currentToken.getType() == expected:
            self._fetchToken()
            return True
        return False

    def parse(self):
        self._parseInstruction()
        self._parseInstruction()
        self._outputFile.writeFile(self._translation)

    # parseInstruction - Method to parse an instruction
    def _parseInstruction(self):
        # Declare the grammar for instructions
        self._parseInteger()
        self._acceptToken(Tokens["TWODOTS"])

        if self._currentToken.getType() == Tokens["INT"]:
            self._parseInteger()
            self._acceptToken(Tokens["COMMA"])
            self._parseOperator()
            self._acceptToken(Tokens["COMMA"])
            self._parseInteger()
            self._acceptToken(Tokens["COMMA"])
            self._parseInteger()

        else:
            self._parseOperator()
            #End of instruction

    # parseInteger - Method to parse an integer token
    def _parseInteger(self):
        # Validate integer token type
        if self._currentToken.getType() == Tokens["INT"]:
            # Convert to hex
            hexVal = int(self._currentToken.getSpell())
            # Append to output file
            self._translation += " " +  format(hexVal, "04x")
            # Get next token
            self._fetchToken()
        else:
            print("Error, integer expected")

    # parseOperator - Method to parse an operator token
    def _parseOperator(self):
        # Validate operator token type
        if self._currentToken.getType() == Tokens["OPERATOR"]:
            # Convert operator (+ = 0x01, - = 0x00, h = 0x11)
            hexVal = "11" # Default value h
            if self._currentToken.getSpell() == "-":
                hexVal = "00"
            elif self._currentToken.getSpell() == "+":
                hexVal = "01"
            # Append to output file
            self._translation += " " + hexVal
            # Get next token
            self._fetchToken()
        else:
            print("Error, operator expected")








