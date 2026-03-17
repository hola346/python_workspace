with open("file.txt", "r", encoding="utf-8") as reader:
    content = reader.readlines()  # copy all lines in list
    print(content)
    rev_content = list(reversed(content))  # created new list with reversed content
    print(rev_content)

with open("file2.txt", "w", encoding="utf-8") as writer:
    for line in rev_content:
        writer.write(line)  # write rev line by line in text file

# only strings can be added - writen to files, not LISTS,
# That's why you should go - write line by line.


# Another way, not creating 2nd list:

with open("file.txt", "r", encoding="utf-8") as reader:
    content = reader.readlines()  # copy all lines in list
    with open("file.txt", "w", encoding="utf-8") as writer:
        for line in reversed(content):
            writer.write(line)
