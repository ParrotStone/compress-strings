#!/usr/bin/env python3

def compress_str(repeated_char):
    '''Function that compress the repeated characters in a string and add the number of repeated characters before compressing'''
    for i in range(0, len(repeated_char) - 1, 2):
        counter = 1
        for j in range(i + 1, len(repeated_char)):
            if repeated_char[i] == repeated_char[j]:
                counter += 1
            else:
                repeated_char = repeated_char.replace(
                    repeated_char[i:j], f'{repeated_char[j - 1]}{counter}')
                break

    repeated_char += str(counter)
    return repeated_char


print(compress_str('AAAAaaBCCCDDe'))  # Result should be >> A4a2B1C3D2e1
