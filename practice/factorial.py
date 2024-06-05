# Write a Python program to calculate the factorial of a given non-negative integer.
# The program should calculate the number twice, using two different functions.
# The first function uses loops, while the second uses recursion.

def fact_loop(num: int) -> int:
    answer = 1
    for i in range(1, num + 1):
        answer *= i
    return answer

def fact_recursive(num: int) -> int:
    if num <= 1:
        return 1
    return num * fact_recursive(num-1)


#print(fact_loop(5))
#print(fact_recursive(5))