"""
image/.gif
image/.jpg
image/.jpeg
image/.png
application/.pdf
text/.txt
application/.zip
application/octet-stream
"""


def main():
    file = input("enter file name\n")
    x = file.split(".")
    if x[1] in ["gif", "jpg", "jpeg", "png"]:
        print("image/." + x[1])
    elif x[1] == "txt":
        print("text/.txt")
    elif x[1] in ["zip", "pdf"]:
        print("application/." + x[1])
    else:
        print("application/octet-stream")
    


main()