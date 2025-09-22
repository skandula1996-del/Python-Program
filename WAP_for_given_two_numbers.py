# WAP for given two numbers to result their product with out using * operator
def hello(a,b):
    if b == 0:
        return 0
    else:
        return a + hello(a, b-1)
print(hello(3,4))