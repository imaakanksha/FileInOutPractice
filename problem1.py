#Write a program to read the text from a given file 'poem.txt' and find out whether it contains the word "layers" or not?
f=open("poem.txt")
content = f.read()
if("layers" in content):
    print("The word layers is present in the content.")
else:
    print("The word layers is not present in the content.")
f.close()

