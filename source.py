def fizz_buzz(s_value, e_value):
    """""
    This fizz_buzz function prints sequence between a given start and end value. It has two parameters as following:

    Parameters
        s_value (int): The start value of the sequence (inclusive).
        e_value (int): The end value of the sequence (inclusive) and

    Returns:
        None

     here I used try except for precise exception handling and clearer error messages, improving the robustness and
     usability of the code.

    """
    try:
        if s_value < 0 or e_value < 0:
            raise ValueError("Either of the input values are negative")
        elif not isinstance(s_value, int) or not isinstance(e_value, int):
            raise TypeError("Only integers are allowed")

        for num in range(s_value, e_value + 1):
            if num % 3 == 0 and num % 5 == 0:
                print('FizzBuzz')
            elif num % 3 == 0:
                print('Fizz')
            elif num % 5 == 0:
                print('Buzz')
            else:
                print(num)
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except TypeError as te:
        print(f"TypeError: {te}")
