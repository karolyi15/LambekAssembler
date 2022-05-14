from FileManager.SourceFile import *
from LexicalAnalizer.Token import *


class Scanner:

    # Class Fields
    _sourceFile = None              # Source file
    _sourceInstructions = []        # Source file instructions

    _currentInstruction = ""        # Current instruction
    _currentInstructionPos = -1     # Current instruction position (End of Lines = -1)

    _currentChar = ""               # Current char
    _currentCharPos = -1            # Current char position (End of Line = -1)

    _currentToken = ""              # Current token
    _fetching = False               # fetching instruction flag
    _scanning = False               # Scanning flag

    # Class Constructor
    def __init__(self, sourceFile):
        # Assign source file
        self._sourceFile = sourceFile
        self._sourceInstructions = self._sourceFile.getInstructions()
        # Fetch an instruction
        self._fetchInstruction()
        # Update fetching flag
        self._fetching = False

    # Class Process
    # isDigit - Method to validate if char is a digit
    def _isDigit(self, char):
        if "0" <= char <= "9":
            return True
        return False

    # isOperator - Method to validate if char is an operator
    def _isOperator(self, char):
        if char == "+" or char == "-" or char == "h":
            return True
        return False

    # isSeparator - Method to validate if char is a separator
    def _isSeparator(self, char):
        if char == "\r" or char == "\n" or char == "\t" or char.isspace():
            return True
        return False

    # getChar - Method to consume a char
    def _fetchChar(self):
        # Validate if scanning
        if self._scanning:
            # Append char to token spelling
            self._currentToken += self._currentChar

            # Update char position
            self._currentCharPos += 1

            # Validate char position
            if self._currentCharPos >= len(self._currentInstruction):
                # Skip instruction
                self._fetchInstruction()
            else:
                # Update current char
                self._currentChar = self._currentInstruction[self._currentCharPos]

    # skipInstruction - Method to fetch the next instruction
    def _fetchInstruction(self):
        # Update fetching flag
        self._fetching = True

        # Update current instruction position
        self._currentInstructionPos += 1

        # Validate current instruction position
        if self._currentInstructionPos >= len(self._sourceInstructions):
            # Update current instruction
            self._currentInstructionPos = -1
            self._currentInstruction = ""
            # Update current char
            self._currentCharPos = -1
            self._currentChar = ""
            # Update scanning flag
            self._scanning = False
        else:
            # Update current instruction
            self._currentInstruction = self._sourceInstructions[self._currentInstructionPos]
            # Update current char
            self._currentCharPos = 0
            self._currentChar = self._currentInstruction[self._currentCharPos]

    # scanToken - Method to scan a token
    def _scanToken(self):
        # Validate if Digit
        if self._isDigit(self._currentChar):
            self._fetchChar()
            while self._isDigit(self._currentChar) and not self._fetching:
                self._fetchChar()
            return Tokens["INT"]

        # Validate if Operator
        elif self._isOperator(self._currentChar):
            self._fetchChar()
            return Tokens["OPERATOR"]

        # Validate if Comma
        elif self._currentChar == ",":
            self._fetchChar()
            return Tokens["COMMA"]

        # Validate if Two Dots
        elif self._currentChar == ":":
            self._fetchChar()
            return Tokens["TWODOTS"]

        # Validate if Separator
        elif self._isSeparator(self._currentChar):
            self._fetchChar()
            while self._isSeparator(self._currentChar) and not self._fetching:
                self._fetchChar()
            return Tokens["SEPARATOR"]

        # Validate if Comment
        elif self._currentChar == ";":
            self._fetchChar()
            while not self._fetching:
                self._fetchChar()
            return Tokens["COMMENT"]

        # Default Case Error
        else:
            return Tokens["ERROR"]

    # flushScanner - Method to flush
    def _flushScanner(self):
        self._fetching = False
        self._currentToken = ""

    # parse - Method to scan a token
    def scan(self):
        # Update Parsing Flag
        self._scanning = True

        # Init current token type (Default)
        tokenType = Tokens["EOF"]

        # Validate number of instructions
        if self._currentInstructionPos != -1:
            # Scan token
            tokenType = self._scanToken()
            # Skip comment token and separator token
            while tokenType in [Tokens["COMMENT"],Tokens["SEPARATOR"]]:
                self._flushScanner()
                tokenType = self._scanToken()

        # Create a new token to retrieve data
        token = Token(tokenType, self._currentToken, (self._currentInstructionPos, self._currentCharPos))

        # Update Parsing Flag
        self._scanning = False
        self._flushScanner()

        return token
