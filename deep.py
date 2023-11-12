def main():
    while True:
        try:
            a = int(input('What is the answer to the Great Question of Life, the Universe and Everything?\n'))
            if a == 42:
                print("Yes")
                break
                
        except ValueError:
            print("not correct")
main()