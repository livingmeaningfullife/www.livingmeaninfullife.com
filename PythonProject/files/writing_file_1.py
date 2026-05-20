"""To an existing file"""

with open("demofile.txt", "a") as f:
    f.write("\nNow the file has more content!")

# open and read the file after the appending:
with open("demofile.txt") as f:
    print(f.read())

"""Overwrite existing content"""
with open("demofile.txt", "w") as f:
    f.write("Oops, I have deleted the content")

with open("demofile.txt") as f:
    print(f.read())
