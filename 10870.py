# 제목
# 피보나치 수 5
# https://www.acmicpc.net/problem/10870

# 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
# n=17일때 까지 피보나치 수를 써보면 다음과 같다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 55

# 내 코드
n = int(input())
fibonacci = [0, 1]
for i in range(1, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i])

print(fibonacci[n])

# 1등 코드
# def p(n):
#     x=0
#     y=1
#     for i in range(n):
#         x,y=y,x+y;
#     return x
# a=int(input())
# print(p(a))

# 숏코딩 1등 코드
# a=0;b=1;exec("a,b=b,a+b;"*int(input()));print(a)