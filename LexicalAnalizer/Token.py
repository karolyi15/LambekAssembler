class Token:

    # Class Fields
    _type = 0           # Token type
    _spell = ""         # The spelling of the token
    _position = (0,0)   # Number of line (line, charPos)

    # Class Constructor
    def __init__(self, type, spell, position):
        self._type = type
        self._spell = spell
        self._position = position

    # Class Setters & Getters
    def getType(self):
        return self._type

    def getSpell(self):
        return self._spell

    def getPosition(self):
        return self._position


# Token's Types
Tokens = {
    "INT": 0,           # Integer
    "CHAR": 1,          # Char
    "OPERATOR": 2,      # Operator
    "COMMA": 3,         # Comma
    "TWODOTS": 4,       # Two Dots
    "SEPARATOR": 5,     # Separator
    "COMMENT": 6,       # Comment
    "EOF": 7,           # End of File
    "ERROR": 8,         # Error
}