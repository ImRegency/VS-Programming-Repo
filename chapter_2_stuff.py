def add_two_numbers(number1,number2):
    #print(number1)
    #print(number2)
    answer = number1 + number2
    return answer

def subtract_two_numbers(number1,number2):
    #print(number1)
    #print(number2)
    answer = number1 - number2
    return answer

def multiply_two_numbers(number1,number2):
    #print(number1)
    #print(number2)
    answer = number1 * number2
    return answer

def divide_two_numbers(numerator,denominator):
    #print(numerator)
    #print(denominator)
    answer = numerator / denominator
    return answer

def calculate_exponent(number1,number2):
    #print(number1)
    #print(number2)
    answer = number1 ** number2
    return answer

def get_user_input():
    number1 = float(input("Number 1?: "))
    number2 = float(input("Number 2?: "))
    return number1, number2

def display_rounded_number(number1):
    rounded_number = round(number1,0)
    return rounded_number



def main():
    number1, number2 = get_user_input()
    #answer = add_two_numbers(number1,number2)
    answer = subtract_two_numbers(number1,number2)
    #answer = multiply_two_numbers(number1,number2)
    #answer = divide_two_numbers(number1,number2)
    #answer = calculate_exponent(number1,number2)
    #answer = display_rounded_number(number1)
    #formatted_answer = f'{answer:,.1f}'
    formatted_answer = '{:,.1f}'.format(answer)
    print(formatted_answer)

main()
