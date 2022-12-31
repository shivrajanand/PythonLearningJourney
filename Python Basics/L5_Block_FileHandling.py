with open("file1.txt") as f:
    #No need to close the file. File is automatically closed after exiting the block
    a = f.read()
    print(a)