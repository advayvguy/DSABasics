from stack import Stack

def bin_convert(n):
    s = Stack()
    while(n > 0):
        s.push(n%2)
        n = n//2

    bin_string = ""
    while (not s.is_empty()):
        bin_string = bin_string + str(s.pop())

    return bin_string

def octal_convert(n):
    s = Stack()
    while(n > 0):
        s.push(n%8)
        n = n//8

    octal_string = ""
    while (not s.is_empty()):
        octal_string = octal_string + str(s.pop())
    
    return octal_string

def hex_convert(n):
    s = Stack()
    while(n > 0):
        s.push(n%16)
        n = n//16

    hex_string = ""
    while (not s.is_empty()):
        a = s.pop()
        if (a >= 10):
            hex_string = hex_string + str(chr(65 + (a-10)))
        else:
            hex_string = hex_string + str(a)

    return "0x" + hex_string


def base_26(n):
    s = Stack()
    while(n > 0):
        s.push(n%26)
        n = n//26

    string = ""
    while (not s.is_empty()):
        a = s.pop()
        if (a >= 10):
            string = string + str(chr(65 + (a-10)))
        else:
            string = string + str(a)

    return string


print(bin_convert(19023))
print(octal_convert(25))
print(hex_convert(256))
print(base_26(26))
