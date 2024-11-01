def rec(n,stack,answer,count_start,count_end):
    #Recursion Base Case
    if count_start == n == count_end:
        answer.append("".join(stack))
    
    if count_start < n:
        stack.append("(")
        rec(n,stack,answer,count_start+1,count_end)
        stack.pop()
    if count_end < count_start:
        stack.append(")")
        rec(n,stack,answer,count_start,count_end+1)
        stack.pop()


def generate_parenthesis(n):
    stack = []
    answer = []
    rec(n,stack,answer, 0,0)
    return(answer)

print(generate_parenthesis(3))