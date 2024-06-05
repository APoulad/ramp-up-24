#Write a program that takes a list of integers as input
# and prints the sum, minimum, maximum, and average of the numbers.

def print_stat(data):
    total = sum(data)
    ave = total / len(data)
    minimum = min(data)
    maximum = max(data)
    print(f"Sum: {total}\nAverage: {ave}\nMinimum:{minimum}\nMaximum:{maximum}")


#print_stat([1,2,3,4])