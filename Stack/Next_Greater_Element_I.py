nums = [1,3,4,1]
nums = [1, 3, 4, 1]

def nextGreaterElement(arr):
    n = len(arr)  # Length of the array
    ans = [-1] * n  # Initialize the answer array with -1s (no greater element by default)
    stack = []  # Stack to keep track of elements

    # Iterate from the last element to the first element
    for i in range(n - 1, -1, -1):  # Corrected loop range
        # Pop elements from the stack that are smaller or equal to arr[i]
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is not empty, the top element is the next greater element
        if stack:
            ans[i] = stack[-1]

        # Push the current element onto the stack for future comparisons
        stack.append(arr[i])

    return ans

print(nextGreaterElement(nums))


print(nextGreaterElement(nums))