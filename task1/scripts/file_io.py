

class fileIO():
    
    def __init__(self, fName):
        """
            Class constructor.

            Args:
                fName: Full path to the file to write to and read from.

            Returns:

            Raises:
                Exception: Fancy exception handling hasn't been implemented.
        """
        try:
            self.fName = fName

        except Exception as e:
            raise Exception(\
                "An exception occured during class initialization: " + str(e))

    def write_ints_to_file(self, startVal, endVal):
        """
            Write integers within a specific range to a file.

            Args:
                startVal: Start value of range (inclusive).
                endVal: End value of range (inclusive).

            Returns:

            Raises:
                Exception: Fancy exception handling hasn't been implemented.
        """
        try:
            with open(self.fName, mode='w') as wFile:            
                for val in range(startVal, endVal + 1):
                    wFile.write('%s\n' % str(val))
            pass
        
        except Exception as e:
            raise Exception("An exception occured: " + str(e))

    def read_half_ints_in_file(self):
        """
            Read integers from the start of up to half the length of the
            file (in number of lines).

            Args:

            Returns:

            Raises:
                Exception: Fancy exception handling hasn't been implemented.
        """
        try:
            with open(self.fName, mode='r') as rFile:
                readInts = []
                for line in rFile.readlines():
                    readInts.append(int(line))
                readInts = readInts[:int(len(readInts)/2)]
                print(readInts)

        except Exception as e:
            raise Exception("An exception occured: " + str(e))

    def write_ints_then_read_half(self):
        """
            Write integers from 1 to 100 (inclusive) to a file, then read
            half the numbers on the file.
        
            Args:

            Returns:

            Raises:
        """
        self.write_ints_to_file(1, 100)
        self.read_half_ints_in_file()
