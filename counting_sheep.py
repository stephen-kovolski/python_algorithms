
#Consider an array/list of sheep where some sheep may be missing from their place. 
#We need a function that counts the number of sheep present in the array (true means present).


#For example:

sheep_pen = ['true',  'true',  'true', 'true' ,'true',  'false', 'true', 'false', 'true', 'false', 'false', 'true', 'true',  'true',  'true',  'true', 'false', 'false', 'true',  'true']
frequency = {}


def sheep_function():
    for sheep in sheep_pen:
        if sheep in frequency:
            frequency[sheep] +=1
        else:
            frequency[sheep] = 1


    print("The amount of sheep in the pen equals", frequency['true'])


sheep_function()
