def BruteForce(first,second):
    match_List = []
    for i in range(len(first) - len(second) + 1):
        flag = True
        if first[i]==second[0]:
            for j in range(len(second)):
                if first[i+j]!=second[j]:
                    flag = False
            if flag == True:
                match_List.append(i)
    return match_List

print(BruteForce('abababbababbbbababab','abab'))