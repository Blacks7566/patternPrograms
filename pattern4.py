row = int(input("Enter number of row : "))

for i in range(row):
    for j in range(i+1):
        print("*",end='')
    for k in range(row-i):
        print(" ",end="")    
    for l in range(row-1-i):
        print(' ',end='')
    for t in range(i+1):
        print('*',end='')
    print()

# second face 
    
for i in range(row):
    for j in range(row-i):
        print("*",end='')
    for k in range(i+1):
        print(" ",end="")    
    for l in range(i):
        print(' ',end='')
    for t in range(row-i):
        print('*',end='')
    print()








# *         *
# **       **
# ***     ***
# ****   ****
# ***** *****
# ****   ****
# ***     ***
# **       **
# *         *