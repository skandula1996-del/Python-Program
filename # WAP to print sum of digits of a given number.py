# WAP to print sum of digits given number
def hello(x):
    if x == 0:
        return 0
    else:
        return x%10 + hello(x//10)
res = hello(1235)
print(res)