'''N sweets are kept before Alice. Sweets are numbered from 0 to N-1 , and the time Alice takes
to eat the ith sweet is time[il minutes. Given the array time containing the time each sweet 
needs to be eaten, write a program to find the minimum sum, of the time required to eat each
sweet, if only one sweet can be eaten by Alice at a moment.

Means : Time taken in eating a sweet is sum of current + prev times 
Ex - Example:
Suppose Alice eats the sweets in the given order:
First sweet (4 minutes) is eaten first: She spends 4 minutes.
Then, the second sweet (2 minutes): She has already spent 4 minutes, so now the total is 4 + 2 = 6 minutes.
Then, the third sweet (1 minute): Total is 6 + 1 = 7 minutes.
Finally, the last sweet (3 minutes): Total is 7 + 3 = 10 minutes.
Total Time = 4 + 6 + 7 + 10 = 27 minutes.

If Alice eats in the order [1, 2, 3, 4]:
If Alice starts with the smallest time first:

First sweet (1 minute): She spends 1 minute.
Then, the second sweet (2 minutes): Total is 1 + 2 = 3 minutes.
Then, the third sweet (3 minutes): Total is 3 + 3 = 6 minutes.
Then, the fourth sweet (4 minutes): Total is 6 + 4 = 10 minutes.
Total Time = 1 + 3 + 6 + 10 = 20 minutes.
'''


def alice_eates_sweets(time):
    sorted_time= sorted(time)
    total_time = 0
    n = len(time)

    for i in range(n):
        total_time+=sorted_time[i] * (n-i)
    return total_time

