with open("Write.txt", "w") as file:
    file.write("first line.\n")
    file.write("I'm write something here!\n")

print("succesfully writed in Write.txt\n")

with open("Write.txt", "r") as file:
    print("result:")
    r = file.read()
    print(r)

with open("Write.txt", "a") as file:
    file.write("\nnew line.\n")
    file.write("Great!")

print("\nNew line has been succesfully added")

with open("Write.txt", "r") as file:
    print("result:")
    print(file.read())
   