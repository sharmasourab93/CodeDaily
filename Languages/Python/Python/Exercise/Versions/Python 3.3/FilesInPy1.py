def print_line_lengths():
    a=open("sourab.txt","r")
    text=a.readlines()
    for line in text:
        print(len(line))
