# Problem: Calculate the Sum of Even Numbers

# Write a Python program that calculates and prints the sum of all even numbers from 1 to a given positive integer n. The program should prompt the user to enter the value of n.


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_num = []
totals = []

def main():
    for even in num_list:
        if even % 2 == 0:
            even_num.append(even)
    print(even_num)
    for num in even_num:
        totals += num 
    print(totals)
main()