#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    validates UTF-8 Data
    """
    bytes_left = 0
    
    for byte in data:
        if bytes_left == 0:
            if byte >> 5 == 0b110:
                bytes_left = 1
            elif byte >> 4 == 0b1110:
                bytes_left = 2
            elif byte >> 3 == 0b11110:
                bytes_left = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes_left -= 1
                
    return bytes_left == 0
