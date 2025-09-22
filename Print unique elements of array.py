'''
Print unique elements of array
Print unique elements of the array in the same order as they appear in the input.
Note: Do not use any inbuilt functions/libraries for your main logic.

Input Format

First line of input contains a single integer N - the size of array and second line contains array elements.

Constraints

1 <= N <= 100
0 <= ar[i] <= 109

Output Format

Print unique elements of the array.
Input                Output
7                    5,9,21
5 4 10 9 21 4 10
'''

n = int(input())
x = list(map(int, input().split()))
r = []
for i in x:
    #print(i, "=>", x.count(i))
    if x.count(i) == 1:
        r.append(i)
print(*r, sep=" ")