row=int(input("Enter number of row : "))

for i in range(row):
    for j in range(2*row-2 - (i+i)):
        print(" ",end="")
    for k in range(i+1+i):
        print("* ",end="")
    print()

# second face     
for i in range(row):
    for j in range(i+i):
        print(" ",end="")
    for k in range(2*row-1-(i+i)):
        print("* ",end="")
    print()


#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *