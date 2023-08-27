def stringmatch(first,second):
    poslist = []
    for i in range(len(first)-len(second)+1):
        matched = True
        j = 0
        while j<len(second) and matched:
            if first[j+i]!=second[j]:
                matched = False

            j = j+1
        if matched == True:
            poslist.append(i)
    return poslist

print(stringmatch('abababbababbbbababab','abab'))
