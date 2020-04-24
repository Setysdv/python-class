def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return fib(num-1) + fib(num-2)




def fib1(num):
    if num == 1:
        return [1]
    if num == 2:
        return [1,1]
    else:
        y = fib1(num-1)
        y.append(y[-1] + y[-2])
        return y

    
