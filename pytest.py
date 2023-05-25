def test_fizz_buzz():
    # Test case 1: Testing a normal sequence
    expected_output = [
        'FizzBuzz', 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz',
        13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz',
        26, 'Fizz', 28, 29, 'FizzBuzz'
    ]
    captured_output = capture_output(fizz_buzz, 1, 30)
    assert captured_output == expected_output

    # Test case 2: Testing negative input values
    with pytest.raises(ValueError) as ve:
        fizz_buzz(-5, 10)
    assert str(ve.value) == "Either of the input values are negative"

    # Test case 3: Testing non-integer input values
    with pytest.raises(TypeError) as te:
        fizz_buzz(1.5, 20)
    assert str(te.value) == "Only integers are allowed"
