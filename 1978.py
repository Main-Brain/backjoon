# 제목
# 소수 찾기
# https://www.acmicpc.net/problem/1978

# 문제
# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 입력
# 첫 줄에 수의 개수 N이 주어진다. N은 100이하이다. 다음으로 N개의 수가 주어지는데 수는 1,000 이하의 자연수이다.

# 출력
# 주어진 수들 중 소수의 개수를 출력한다.

# 예제 입력 1 
# 4
# 1 3 5 7
# 예제 출력 1 
# 3

# 내 코드
import math

input()
numbers = list(map(int,input().split()))
is_prime = True      # 소수 확인
prime_count = 0       # 소수 개수

for n in numbers:
    is_prime = True
    if n < 2:
        continue
    for i in range(2, math.ceil(n / 2) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_count += 1

print(prime_count)


# 1등 코드
# n=int(input())
# li=list(map(int,input().split()))
# cnt=0
# for i in li:
#     f=True
#     if i<=1:continue
#     for j in range(2,i):
#         if i%j==0:
#             f=False
#             break
#     if f:
#         cnt+=1
# print(cnt)

# 숏코딩 1등 코드
# input();print(sum(all(n%j for j in range(2,n))*n>1for n in map(int,input().split())))