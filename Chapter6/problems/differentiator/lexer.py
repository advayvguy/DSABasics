class Token:
    def __init__(self, value, type):
        self.type = type 
        self.value = value
    
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return self.value
    
def check_braces(inputStr):
    count = 0
    for i in inputStr:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
            if count < 0:
                raise ValueError("Invalid expression: illegal brackets")
    if count > 0:
        raise ValueError("Invalid expression: illegal brackets")

def Lexer(inputStr):
    check_braces(inputStr)
    tokenStream = []
    i = 0
    while i < len(inputStr):

        if inputStr[i] in [' ', '\t']:
            pass

        elif inputStr[i] in ['+','-','*','/','^']:
            if inputStr[i] == '-' and (i == 0 or inputStr[i-1] == '(' or inputStr[i-1] in ['+','-','*','/','^']):
                tokenStream.append(Token('-1', 'CONSTANT'))
                tokenStream.append(Token('*', 'OPERATOR'))
            else:
                tokenStream.append(Token(inputStr[i], 'OPERATOR'))
        
        elif inputStr[i] == 'e':
            tokenStream.append(Token('e', 'CONSTANT'))

        elif inputStr[i] == 's':
            if (i+1 < len(inputStr) and inputStr[i+1] == 'i') and (i+2 < len(inputStr) and inputStr[i+2] == 'n'):
                tokenStream.append(Token('sin', 'FUNCTION'))
                i += 2
            
        elif inputStr[i] == 'c' and (i+1 < len(inputStr) and inputStr[i+1] == 'o') and (i+2 < len(inputStr) and inputStr[i+2] == 's'):
                tokenStream.append(Token('cos', 'FUNCTION'))
                i += 2

        elif inputStr[i] == 'c' and (i+1 < len(inputStr) and inputStr[i+1] == 's') and (i+2 < len(inputStr) and inputStr[i+2] == 'c'):
                tokenStream.append(Token('csc', 'FUNCTION'))
                i += 2

        elif inputStr[i] == 'c' and (i+1 < len(inputStr) and inputStr[i+1] == 'o') and (i+2 < len(inputStr) and inputStr[i+2] == 't'):
                tokenStream.append(Token('cot', 'FUNCTION'))
                i += 2

        elif inputStr[i] == 't':
            if (i+1 < len(inputStr) and inputStr[i+1] == 'a') and (i+2 < len(inputStr) and inputStr[i+2] == 'n'):
                tokenStream.append(Token('tan', 'FUNCTION'))
                i += 2

        elif inputStr[i] == 's':
            if (i+1 < len(inputStr) and inputStr[i+1] == 'e') and (i+2 < len(inputStr) and inputStr[i+2] == 'c'):
                tokenStream.append(Token('sec', 'FUNCTION'))
                i += 2

        elif inputStr[i] == 'l':
            if (i+1 < len(inputStr) and inputStr[i+1] == 'n'):
                tokenStream.append(Token('ln', 'FUNCTION'))
                i += 1

        elif inputStr[i].isdigit():
            num = ""
            while i < len(inputStr) and inputStr[i].isdigit():
                num += inputStr[i]
                i += 1
            tokenStream.append(Token(num, 'CONSTANT'))
            if i < len(inputStr) and (inputStr[i].isalpha() or inputStr[i] == '('):
                tokenStream.append(Token('*', 'OPERATOR'))
            i -= 1 #pushback

        elif inputStr[i] == '(':
            tokenStream.append(Token('(', 'OPENBRACES'))

        elif inputStr[i] == ')':
            tokenStream.append(Token(')', 'CLOSEBRACES'))
            if i+1 < len(inputStr) and (inputStr[i+1] == '(' or inputStr[i+1].isdigit() or inputStr[i+1].isalpha()):
                tokenStream.append(Token('*', 'OPERATOR'))

        elif inputStr[i].isalpha():
            tokenStream.append(Token(inputStr[i], 'VARIABLE'))
            if i+1 < len(inputStr) and (inputStr[i+1] == '('):
                tokenStream.append(Token('*', 'OPERATOR'))

        else:
            raise ValueError("Invalid experssion: expression not supported")
        i += 1
    
    return tokenStream