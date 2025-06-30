def fun(n):
    if n % 2==0:
        return "짝수"
    else:
        return "휼수"

x=int(input("1~100 시이의 숫지를 입력하세요:"))
result=fun(x)
print(result)
