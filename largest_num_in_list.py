#Return an array consisting of the largest number from each provided sub-array. For simplicity, the provided array will contain exactly 4 sub-arrays.

#Remember, you can iterate through an array with a simple for loop, and access each member with array syntax arr[i].

largest_num = []

def largestOfFour(arr): 
    for i in arr:
        
        for j in arr:
            print(j)


largestOfFour([[4, 5, 1, 3], [13, 27, 18, 26], [32, 35, 37, 39], [1000, 1001, 857, 1]])


#loop through the main list
#loop through each smaller list
#create a new variable to hold the largest number list
#start with the first number in the list if the next num is larger keep the larger etc
#put the largest nums in an array