#You are given two arrays and an index.
#Copy each element of the first array into the second array, in order.
#Begin inserting elements at index n of the second array.
#Return the resulting array. The input arrays should remain the same after the function runs.

def frankenSplice(arr1, arr2, n):
    arr1[n:n] = arr2
    print(arr1)



    #for i in arr1:
        #print(i)
    #for j in arr2:
     #   new_list = j
      #  print(new_list)
       # #print(arr2.insert(n, arr1))
frankenSplice([1, 2, 3], [4, 5, 6], 1)