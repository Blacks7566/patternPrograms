row = int(input("Enter number of row : "))


for i in range(row):
    for j in range(i+1):
        print("*",end="")
    print()

# second face 

for i in range(row):
    for j in range(row-i-1):
        print("*",end="")
    print()


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *