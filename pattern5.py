# piramid
row = int(input("Enter number of rows : "))

for i in range(row):
    for j in range((2*row-2)-(i+i)):
        print(" ",end='')
    for k in range(1+i+i):
        print("* ",end="")
    print()

#        *
#      * * *
#    * * * * *
#   * * * * * * *
# * * * * * * * * *