def get_even_squares(numbers):
    even_squares = [ ]
    for num in numbers:
        if num % 2 == 0:
            even_squares.append(num ** 2)
    return even_squares

input_string = input("숫자들을 공백으로 구분하여 입력하세요: ")

num_list = [int(num) for num in input_string.split()]

result= get_even_squares(num_list)

print("짝수의 제곱 리스트: ", result)
        
    
