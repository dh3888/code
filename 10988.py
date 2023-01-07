# 팰린드롬
A = input()
B = len(A)
check = True
for i in range(B//2) :
    if A[i] != A[-i-1] :
        check = False
if check == True :
    print(1)
else :
    print(0)