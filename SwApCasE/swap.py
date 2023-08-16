def swap_case(s):
    s1=""
    for letter in s:
        if letter.isupper():
            s1 += letter.lower()
        elif letter.islower():
            s1 += letter.upper()
        else:
            s1+=letter
    return s1
