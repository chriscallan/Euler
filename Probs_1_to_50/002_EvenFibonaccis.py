

runningtotal = 0
lowerlimit = 1
upperfibvalue = 4000000


def fibonacci(n, _cache={}):
    if n in _cache:
        return _cache[n]
    elif n > 1:
        # if n % 2 == 0:
        return _cache.setdefault(n, fibonacci(n - 1) + fibonacci(n - 2))
        # else:
        #     return n
    return n



for i in range(lowerlimit, 40):
    # if i % 1 == 0:
    tempreturn = 0
    tempreturn += fibonacci(i)
    print("term number: {0}, has value: {1}".format(i, tempreturn))
    if tempreturn % 2 == 0 and tempreturn < upperfibvalue:
        runningtotal += tempreturn
    elif tempreturn > upperfibvalue:
        break

# result = fibonacci(8)
print("The result is: {0}".format(runningtotal))