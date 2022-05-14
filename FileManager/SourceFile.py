from ErrorManager.Error import *


class SourceFile:

    # Class Fields
    _filePath = ""
    _fileInstructions = []

    # Class Constructor
    def __init__(self, path):
        self._filePath = path
        self._createFile()

    # Class Process
    # createFile - Method to create a file
    def _createFile(self):
        try:
            # Create and open file
            file = open(self._filePath, 'x')

        except:
            # Error - The file already exits
            # Read file content
            self._readFile()

        else:
            # File created successfully
            file.close()
            return Error(0, ErrSuccess)  # Error(line, err)

    # readFile - Method to read content from file
    def _readFile(self):
        try:
            # Open File
            file = open(self._filePath,'r')
            # Read Fife by Lines
            for line in file:
                self._fileInstructions.append(line)

        except:
            # Error - Reading file
            return Error(0, ErrReadingSourceFile)  # Error(line, err)

        else:
            # File successfully read
            file.close()
            return Error(0, ErrSuccess)  # Error(line, err)

    # writeFile - Method to write content to a file
    def writeFile(self, content):
        try:
            # Open file
            file = open(self._filePath, 'w')
            # Write to file
            file.write(content)
            # Update file lines
            self._fileLines.clear()
            for line in file:
                self._fileLines.append(line)

        except:
            return Error(0, ErrReadingSourceFile)  # Error(line, err)

        else:
            return Error(0, ErrSuccess)  # Error(line, err)

        finally:
            file.close()

    # Class Setters & Getters
    def getPath(self):
        return self._filePath

    def getInstructions(self):
        return self._fileInstructions
