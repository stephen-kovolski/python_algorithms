# Whats the total?
# How many people are splitting the bill?
# How much do you want to tip?


total_owed = input("What is the total owed on the bill?")
how_many_people = input("How many people are splitting the bill?")
tip = input('What percentage do you want to tip?')
tip_math = (((float(tip) / 100) + 1) * float(total_owed)) / float(how_many_people)
print(tip_math)
