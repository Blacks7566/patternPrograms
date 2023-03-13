row=int(input("Enter number of rows : "))

for i in range(row):
    for j in range(row-i-1):
        print(' ',end='')
    for k in range(i+1):
        print('*',end='')
    print()        

# second face


for i in range(row):
    for k in range(i+1):
        print(' ',end='')
    for j in range(row-i-1):
        print('*',end='')
    print()        

#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *