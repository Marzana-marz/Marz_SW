def calculate (num1,num2, operator):
    if operator =="+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator =="*":
        return num1 * num2
    elif operator =="/":
        if num2 ==0:
            return "0으로 나놀 수 없어"
        return num1/ num2
    else:
            return"잘못된 연산자입니다"

num1 = float(input("첫 번째 숫자:"))
num2 = float(input("두 번째 숫자:"))
operator = input("연산자를 이력하세요(+,-,*,/):")
result = calculate (num1,num2,operator)
print("결과:",result)            
