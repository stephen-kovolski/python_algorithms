
greeting = input("would you like to convert to celsius or fahrenheit?\n")

if greeting == "fahrenheit":
    question = input("what temperature would you like converted to fahrenheit?\n")
    fahrenheit_formula = (int(question) * 1.8) + 32

    print(fahrenheit_formula)
else:
    other_question = input("what temperature would you like to convert to celsius?\n")
    celisus_formula = (int(other_question) - 32) * 5/9


    print(celisus_formula)


  