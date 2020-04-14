# The Fibonacci numbers are the numbers in the following integer sequence (Fn):

#     0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
# such as
#     F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
# Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying
#     F(n) * F(n+1) = prod.
# Your function productFib takes an integer (prod) and returns an array:
# [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)
# depending on the language if F(n) * F(n+1) = prod.
# If you don't find two consecutive F(m) verifying F(m) * F(m+1) = prodyou will return
# [F(m), F(m+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
# F(m) being the smallest one such as F(m) * F(m+1) > prod.
# Some Examples of Return:
# (depend on the language)
# productFib(714) # should return (21, 34, true), 
#                 # since F(8) = 21, F(9) = 34 and 714 = 21 * 34
# productFib(800) # should return (34, 55, false), 
#                 # since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
# -----
# productFib(714) # should return [21, 34, true], 
# productFib(800) # should return [34, 55, false], 
# -----
# productFib(714) # should return {21, 34, 1}, 
# productFib(800) # should return {34, 55, 0},        
# -----
# productFib(714) # should return {21, 34, true}, 
# productFib(800) # should return {34, 55, false}, 

def fibonacci(k):
    if k == 0:
        return 0
    elif k == 1:
        return 1
    n = 3
    prev = 1
    prev_prev = 0
    actual = prev + prev_prev
    while n <= k:
      prev_prev = prev
      prev = actual
      actual = prev + prev_prev
      n += 1
    return actual



def productFib(prod):
    # your code
    result = []
    if prod == 0:
        result.append(0)
        result.append(1)
        result.append(True)
        return result

    previous = fibonacci(0)
    actual = fibonacci(1)
    n=1
    while (previous * actual) < prod :
        previous = actual
        n+=1
        actual = fibonacci(n)
    result.append(previous)
    result.append(actual)
    if (previous*actual) == prod:
        result.append(True)
    else:
        result.append(False)
    return result




def print_fibo(n):
    for j in range(0, n):
      print('Fibonacci de n: ' + str(j) + '  es: ' + str(fibonacci(j)) )


def print_product(n):
    for i in range(0, n):
        print('ProducFibo de: ' + str(i) + '  es: ' + str(productFib(i)))



# print(productFib(3))
# print_fibo(10)
print_product(10)
