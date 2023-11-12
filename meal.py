"""
7-8 breakfast
12-13 lunch
18-19 dinner   
"""
   

def main():
    time = int(input("what time is it?\n"))

    if time >= 7:00 and time <= 8:00:
        print("breakfast time")
    elif time >= 12:00 and time <= 13:00:
        print("lunch time")
    elif time >= 18:00 and time <= 19:00:
        print("dinner time")


if __name__ == "__main__":
    main()
