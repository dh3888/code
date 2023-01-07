# 팩토리얼
N = int(input())
r = 1
for i in range(1, N+1, 1) : # 1부터 N+1 범위에 r이 존재하는한 계속 반복
    r *= i
print(r)
# 재귀함수 이용가능