class No1(list):
push = list.append

def modify_stack(symbolString):
    stack=No1()
    result = []
        for character in symbolString:
            if character != '*':
                stack.push(character)
            else:
                result.append(stack.pop())
        return ''.join(result)
print(modify_stack('E A S * Y * Q U E * * * S T * * * I O * N * * *'))