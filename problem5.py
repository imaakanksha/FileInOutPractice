#Repeat program 4 for a list of such words to be censored.
words=["Tiger","bad","worst"]
with open("anifile.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#"*len(word))

with open("anifile.txt", "w") as f:
    f.write(content)