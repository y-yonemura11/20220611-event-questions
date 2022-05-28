for num in range(1, 101):
    string = ''

    # ここから記述
    string = 'FizzBuzz'[(4 if num % 3 else 0):(4 if num % 5 else 8)] or num

    # ここまで記述

    print(string)