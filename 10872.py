# 제목
# 팩토리얼
# https://www.acmicpc.net/problem/10872

# 문제
# 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.

# 출력
# 첫째 줄에 N!을 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 3628800
# 예제 입력 2 
# 0
# 예제 출력 2 
# 1

# 내 코드
n = int(input())
factorial = 1
while n > 1:
    factorial *= n
    n -= 1

print(factorial)

# 1등 코드
# d=1
# for i in range(1,int(input())):
#     d*=i+1
# print(d)

# 숏코딩 1등 코드
# r=i=1;exec('r*=i;i+=1;'*int(input()));print(r)