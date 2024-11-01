def operation(num_1,num_2,op):
    if op == "*":
        return num_1 * num_2
    elif op == "/":
        return num_1 // num_2
    elif op == "+":
        return num_1 + num_2
    else:
        return num_1 - num_2

def rev_Polish(arr):
    stack = []
    for i in arr:
        if i.isnumeric():
            stack.append(int(i))
        else:
            if len(stack) < 2:
                return stack[0]
            second = stack.pop()
            first = stack.pop()
            stack.append(operation(first,second,i))
    return stack[-1]

print(rev_Polish(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
