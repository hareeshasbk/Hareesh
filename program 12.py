#write python program to implement bracket matching using stack
def bracketsbalanced(expr):
    STACK=[]
    for char in expr:
        if char in['(','{','[']:
            STACK.append(char)
        else:
            if not STACK:
                return False
            current_char=STACK.pop()
            if current_char=='(':
                if char!=')':
                    return False

            if current_char=='{':
                if char!='}':
                    return False

            if current_char=='[':
                if char!=']':
                    return False
    if STACK:
        return False
    return True

if __name__=="__main__":
    expr=input("Enter expression = ")
    if bracketsbalanced(expr):
        print("balanced")
    else:
        print("not balanced")
