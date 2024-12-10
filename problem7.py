#Write a program to find out the line number where Python is present from ques 6.



with open("log.html") as f:
    lines = f.readlines()

lineno=1
for line in lines:
    if ("Python" in line):
        print(f"Yes, Python is present in the line. Line no:{lineno}")
        break
    lineno += 1
else:
    print("No, Python is not present in the content.")