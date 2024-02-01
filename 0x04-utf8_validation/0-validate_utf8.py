#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines given data set represents valid UTF-8 encoding

    Args:
        data (list): list of integers representing 1 byte of data each

    Returns:
        bool: True if data is valid UTF-8 encoding, else False
    """
    # Variable to track number of remaining bytes in multi-byte character
    remaining_bytes = 0

    for byte in data:
        # Extract the 8 least significant bits
        byte &= 0xFF

        # If it's the start of a new character
        if remaining_bytes == 0:
            if byte >> 7 == 0:
                continue  # Single-byte character, move to the next byte

            # Determine the number of bytes in the character
            if byte >> 5 == 0b110:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            else:
                return False  # Invalid start of a multi-byte character

        else:
            # If it's a continuation byte (10xxxxxx)
            if byte >> 6 == 0b10:
                remaining_bytes -= 1
            else:
                return False  # Invalid continuation byte

    # If there are remaining bytes at the end, it's an incomplete sequence
    return remaining_bytes == 0


if __name__ == "__main__":
    # Test cases
    data1 = [65]
    print(validUTF8(data1))  # True

    data2 = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
    print(validUTF8(data2))  # True

    data3 = [229, 65, 127, 256]
    print(validUTF8(data3))  # False
