

n = int(input())
for i in range(1, n+1):
	for j in range(i, n):
		print (" ", end = "")
	for p in range(1, i+1):
		print (p, end="")	
	for k in range(i-1, 0, -1):
		print(k, end = "")
	print()		

# for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     for j in range(i):
#         print((j+1), end="")
#     print("\n")


# def pyramid(rows=5):
#     for i in range(rows):
#         print ' '*(rows-i-1) + '*'*(2*i+1)

# pyramid(5)