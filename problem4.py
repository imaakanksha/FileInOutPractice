#A File contains a word "Donkey" multiple times. You need to write a program which replace this word with ###### by updating the same file.

word="Tiger"
with open("anifile.txt", "r") as f:
    content = f.read()
contentNew = content.replace(word, "######")

with open("anifile.txt", "w") as f:
    content=f.write(contentNew)