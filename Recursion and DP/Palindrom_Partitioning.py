def isPalindrome(s):
    return s == s[::-1]

def partition(word, n, index, ans, curr):
    if index == n:
        ans.append(curr[:])  
        return
    
    for i in range(index, n):
        substring = word[index:i+1]  
        if isPalindrome(substring):
            curr.append(substring)  
            partition(word, n, i+1, ans, curr)  
            curr.pop()  

word = "aab"
ans = []
partition(word,len(word),0,ans,[])
print(ans)