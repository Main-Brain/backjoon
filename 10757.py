# 제목
# 큰 수 A+B
# https://www.acmicpc.net/problem/10757

# 문제
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)

# 출력
# 첫째 줄에 A+B를 출력한다.

# 예제 입력 1 
# 9223372036854775807 9223372036854775808
# 예제 출력 1 
# 18446744073709551615

# 내 코드
A, B = input().split()

print(int(A) + int(B))

# 1등 코드
# print(sum(map(int,input().split())))

# 숏코딩 1등 코드
# print(sum(map(int,input().split())))