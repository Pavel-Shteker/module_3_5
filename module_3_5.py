def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        return first * get_multiplied_digits(int(str_number[1:])) # выглядит вырвиглазно, но видно надо привыкать
    else:
        return int(str_number[0])

result = get_multiplied_digits(40203)
print(result)

another_result = get_multiplied_digits(11509)
print(another_result)

# компилятор ругается на попытку задать чисто с нулями впереди типа 007, обойдемся без них
