from LexicalAnalizer.Scanner import *
from LexicalAnalizer.Token import *
from ErrorManager.Error import *


class Parser:

    # Class Fields
    _sourceFile = None
    _outputFile = None
    _assemblyListFile = None

    _scanner = None
    _currentToken = None

    _translation = ""
    _assemblyList = ""

    # Class Constructor
    def __init__(self, sourceFilePath):
        # Init source file
        self._sourceFile = SourceFile(sourceFilePath)
        # Init scanner
        self._scanner = Scanner(self._sourceFile)
        # Init output file
        self._outputFile = SourceFile("Source/output.lmk")
        # Init assembly list file
        self._assemblyListFile = SourceFile("Source/assemblylist.lst")
        # Init current token
        self._fetchToken()

    # Class Process
    # fetchToken - Method to fetch the next token
    def _fetchToken(self):
        self._currentToken = self._scanner.scan()

    # acceptToken - Method to accept an expected token
    def _acceptToken(self, expected):
        if self._currentToken.getType() == expected:
            self._fetchToken()
            return Error(0, ErrSuccess)
        return Error(self._currentToken.getPosition()[1], ErrNonExpectedToken)

    def parse(self):
        for x in range(8):
            self._parseInstruction()
            self._translation += "\n"
        self._outputFile.writeFile(self._translation)

    # parseInstruction - Method to parse an instruction
    def _parseInstruction(self):
        # Declare the grammar for instructions
        # Parse an integer token
        err = self._parseInteger()
        if err.getError() != ErrSuccess:
            return err

        # Parse a two dots token
        err = self._acceptToken(Tokens["TWODOTS"])
        if err.getError() != ErrSuccess:
            return err

        # Validate grammar rule
        if self._currentToken.getType() == Tokens["INT"]:
            # Complete instruction
            # Parse and integer token
            err = self._parseInteger()
            if err.getError() != ErrSuccess:
                return err

            # Parse a comma token
            err = self._acceptToken(Tokens["COMMA"])
            if err.getError() != ErrSuccess:
                return err

            # Parse an operator token
            err = self._parseOperator()
            if err.getError() != ErrSuccess:
                return err

            # Parse a comma token
            err = self._acceptToken(Tokens["COMMA"])
            if err.getError() != ErrSuccess:
                return err

            # Parse an integer token
            err = self._parseInteger()
            if err.getError() != ErrSuccess:
                return err

            # Parse a comma token
            err = self._acceptToken(Tokens["COMMA"])
            if err.getError() != ErrSuccess:
                return err

            # Parse an integer token
            err = self._parseInteger()
            if err.getError() != ErrSuccess:
                return err

        else:
            # Partial instruction - operator "h"
            # Parse an operator token
            err = self._parseOperator()
            if err.getError() != ErrSuccess:
                return err

        # End of instruction
        return Error(0, ErrSuccess)

    # parseInteger - Method to parse an integer token
    def _parseInteger(self):
        # Validate integer token type
        if self._currentToken.getType() == Tokens["INT"]:
            # Convert to hex
            hexVal = int(self._currentToken.getSpell())
            # Append to output file
            self._translation += " " + format(hexVal, "04x")
            # Get next token
            self._fetchToken()
            return Error(0, ErrSuccess)
        else:
            return Error(self._currentToken.getPosition()[1], ErrExpectedTokenInt)

    # parseOperator - Method to parse an operator token
    def _parseOperator(self):
        # Validate operator token type
        if self._currentToken.getType() == Tokens["OPERATOR"]:
            # Convert operator (+ = 0x01, - = 0x00, h = 0x11)
            hexVal = "" # Default value h
            if self._currentToken.getSpell() == "-":
                hexVal = "00"
            elif self._currentToken.getSpell() == "+":
                hexVal = "01"
            elif self._currentToken.getSpell() == "h":
                hexVal = "0000 11"  # Appending and empty by...
            # Append to output file
            self._translation += " " + hexVal
            # Get next token
            self._fetchToken()
            return Error(0, ErrSuccess)
        else:
            return Error(self._currentToken.getPosition()[1], ErrExpectedTokenOpt)








