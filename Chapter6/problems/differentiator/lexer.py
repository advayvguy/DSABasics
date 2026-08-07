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
            tokenStream.append(Token(inputStr[i], 'OPERATOR'))
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