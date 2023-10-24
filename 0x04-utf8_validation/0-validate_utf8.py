#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """Returns true if data is valid utf-8"""
    def is_continuation_byte(byte):
        """Check if a byte is a continuation byte)"""
        return (byte & 0xC0) == 0x80

    i = 0
    while i < len(data):
        num_of_bytes = 0
        byte_mask = 0x80
        while data[i] & byte_mask:
            num_of_bytes += 1
            byte_mask >>= 1

        if num_of_bytes == 1 or num_of_bytes > 4:
            return False

        for j in range(1, num_of_bytes):
            if i + j >= len(data) or not is_continuation_byte(data[i + j]):
                return False

        i += 1

    return True
