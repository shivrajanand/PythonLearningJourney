"""
"r" - Open file for reading
"rt" - default r-mode - read in text mode
"rb" read in binary mode
"w" - open a file for writing
"x" - Creates file if not exist
"a" - Add more content to a file
"t" - open file and deal with data in string format text mode
"b" - binary mode
"+" - read and write both
f.tell() - returns character index at which file pointer exists
f.seek(n) - resets file pointer at nth character index

"""

f = open("file1.txt", "rt") #f is a file pointer
# # content = f.read()
# words3 = f.read(3) #reads 3 words only
# print(words3, end="")

# words = f.read(344)
# print(words)

# content = f.read()
# for line in content:
#     print(line)
# print(f.tell())
print(f.readline())
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(16)
print(f.readline())

f.close()