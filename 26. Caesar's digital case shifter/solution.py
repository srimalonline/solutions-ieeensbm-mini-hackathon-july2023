ct = input().strip() # Cipher text
ot = [] # Original text
shift = 14
uppercase_start, uppercase_end = 65, 90
lowercase_start, lowercase_end = 97, 122

i = 0
while i < len(ct):
    ascii_val = ord(ct[i])
    is_uppercase = ascii_val >= uppercase_start and ascii_val <= uppercase_end
    is_letter = (ascii_val >= lowercase_start and ascii_val <= lowercase_end) or is_uppercase

    if is_letter:
        if is_uppercase:
            if ascii_val > uppercase_end - shift:
                ascii_val -= shift - 2
            else:
                ascii_val += shift
        else:
            if ascii_val > lowercase_end - shift:
                ascii_val -= shift - 2
            else:
                ascii_val += shift

    ot.append(chr(ascii_val))
    i += 1
print(''.join(ot))