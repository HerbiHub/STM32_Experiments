#!/usr/bin/env python3

import unittest

# Handle importing things above this dir
import sys
sys.path.append("..")

from comm_protocol import Status, Baud, Parser

class TestCommsMethods(unittest.TestCase):


    def test_parsing_baud(self):
        Parser("1,SLAV,HOST,BAUD,GET,0xbd05806e\n").iparse()
        Parser("1,SLAV,HOST,BAUD,SET,9600,0xf2434f96\n").iparse()
        Parser("1,SLAV,HOST,BAUD,SAY,9600,0xba92785b\n").iparse()
        Parser("1,SLAV,HOST,BAUD,CLEAR,0xae740462\n").iparse()

    def test_parsing_baud_validated(self):
        x = Parser("1,SLAV,HOST,BAUD,GET,0xbd05806e\n").iparse()
        x.validate()
        x = Parser("1,SLAV,HOST,BAUD,SET,9600,0xf2434f96\n").iparse()
        x.validate()
        x = Parser("1,SLAV,HOST,BAUD,SAY,9600,0xba92785b\n").iparse()
        x.validate()
        x = Parser("1,SLAV,HOST,BAUD,CLEAR,0xae740462\n").iparse()
        x.validate()

    def test_parsing_baud_errors(self):

        # Manual CRC is wrong, should be 0xae740462
        x = Parser("1,SLAV,HOST,BAUD,CLEAR,0xae740463\n").iparse()
        with self.assertRaises(ValueError) as cm:
            x.validate()

        # Shouldn't have a baud rate on a get
        x = Parser("1,SLAV,HOST,BAUD,GET,9600,0xf2434f96\n").iparse()
        with self.assertRaises(ValueError) as cm:
            x.validate()

        # Set needs a baud rate
        x = Parser("1,SLAV,HOST,BAUD,SET,0x58ff172d\n").iparse()
        with self.assertRaisesRegex(ValueError,"missing argument") as cm:
            x.validate()

        # Say needs a baud rate
        x = Parser("1,SLAV,HOST,BAUD,SAY,0x102e20e0\n").iparse()
        with self.assertRaisesRegex(ValueError,"missing argument") as cm:
            x.validate()

        # Clear shouldn't have a baud rate
        x = Parser("1,SLAV,HOST,BAUD,CLEAR,12345,0xae740462\n").iparse()
        with self.assertRaisesRegex(ValueError,"Invalid argument") as cm:
            x.validate()


    def test_parsing_status(self):
        Parser("1,SLAV,HOST,STATUS,200,0x12345678,0x6ed95d53\n").iparse()

    def test_parsing_status_allcodes(self):
        Parser("1,SLAV,HOST,STATUS,100,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,200,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,400,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,401,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,402,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,404,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,405,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,418,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,429,0x12345678\n").iparse().validate()
        Parser("1,SLAV,HOST,STATUS,500,0x12345678\n").iparse().validate()

    def test_parsing_status_invalidcodes(self):
        valid_codes = [100,
                       200,
                       400,
                       401,
                       402,
                       404,
                       405,
                       418,
                       429,
                       500,]
        # Test complete valid range
        for i in range(100,600):
            if i in valid_codes: continue
            with self.assertRaisesRegex(ValueError, "Invalid status code") as cm:
                Parser(f"1,SLAV,HOST,STATUS,{i},0x12345678\n").iparse().validate()
        # Test < valid range
        for i in range(0,100):
            with self.assertRaisesRegex(ValueError, "Invalid range of status code") as cm:
                Parser(f"1,SLAV,HOST,STATUS,{i},0x12345678\n").iparse().validate()
        # Test > valid range
        for i in range(600,1000):
            with self.assertRaisesRegex(ValueError, "Invalid range of status code") as cm:
                Parser(f"1,SLAV,HOST,STATUS,{i},0x12345678\n").iparse().validate()

    def test_parsing_status_validated(self):
        x = Parser("1,SLAV,HOST,STATUS,200,0x12345678,0x6ed95d53\n").iparse()
        x.validate()

    def test_parsing_status_errors(self):
        # Manual CRC is wrong
        x = Parser("1,SLAV,HOST,STATUS,200,0x12345678,0x6ed95d52\n").iparse()
        with self.assertRaises(ValueError) as cm:
            x.validate()



if __name__ == '__main__':
    unittest.main()