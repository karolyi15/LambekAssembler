class Error:

    # Class Fields
    _line = 0
    _error = 0
    _errMsg = ""

    # Class Constructor
    def __init__(self, line, err):
        self._line = line
        self._error = err
        self._errMsg = ErrMsg[self._error]

    # Class Setters & Getters
    def setLine(self, line):
        self._line = line

    def getLine(self):
        return self._line

    def setError(self, error):
        self._error = error

    def getError(self):
        return self._error

    def setErrMsg(self, errMsg):
        self._errMsg = errMsg

    def getErrMsg(self):
        return self._errMsg

    def toString(self):
        return "Error" + self._error + "in line " + self._line + ": " + self._errMsg


# Errors List
# O - Success Error
ErrSuccess = 0
# 10XX - Source Files Errors
ErrReadingSourceFile = -1001
ErrWritingSourceFile = -1002
# 20XX - Parser Errors
ErrNonExpectedToken = -2001
ErrExpectedTokenInt = -2002
ErrExpectedTokenOpt = -2003


# Errors Msg
ErrMsg = {
    # O - Success Error
    ErrSuccess: "Success",
    # 10XX - Source Files Errors
    ErrReadingSourceFile: "Error while reading source file",
    ErrWritingSourceFile: "Error while writing source file",
    # 20XX - Parser Errors
    ErrNonExpectedToken: "Error non expected token",
    ErrExpectedTokenInt: "Error expected integer token",
    ErrExpectedTokenOpt: "Error expected operator token"
}


