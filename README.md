# delphiBIC

# FizzBuzz Task

This program is in python and prints the FizzBuzz sequence between a given start and end value. It follows the FizzBuzz rules where:
- If a number is divisible by 3, it prints "Fizz"
- If a number is divisible by 5, it prints "Buzz"
- If a number is divisible by both 3 and 5, it prints "FizzBuzz"
- Otherwise, it just prints that number

## Usage

To use the FizzBuzz program, follow these steps:

1. Install Python (if not already installed) from the official Python website: [https://www.python.org](https://www.python.org)

2. Clone or download this repository to your local machine.

3. Open terminal or command prompt and navigate to the directory containing the FizzBuzz program files called `source.py`

4. Run the `main.py` file using the Python interpreter:

   `python main.py`
   
5. Enter the start and end values in this `fizz_buzz` function. The program will print the FizzBuzz sequence between the given values.

## Testing

How too run test cases

1. install `pytest` if you haven't already by running the following command in your terminal:
   `pip istall pytest`
   
2. Create a new Python file, for example `pytest.py`.
    `import pytest`
    `from source import fizz_buzz`
    
3. create a `test_fizz_buzz()` function, add the desired test cases using `assert` statements to check excpected outputs.

5. Open your terminal or command prompt, navigate to the directory containing `pytest.py`, and run command as following:
   `pytest`
Note:`pytest` will automatically discover and run the test cases defined in the file, and display the test results in the terminal.

I made three use cases as follows:


Test case 1:

Description: Testing a normal sequence
Expected Output: [Expected output here]


Test case 2:

Description: Testing negative input values
Expected Error: ValueError: Either of the input values are negative

Test case 3:

Description: Testing non-integer input values
Expected Error: TypeError: Only integers are allowed


## Example

Here's an example usage of the FizzBuzz program:


$ python main.py
import source
source.fizzbuzz(1,50)
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
Fizz
22
23
Fizz
Buzz
26
Fizz
28
29
FizzBuzz
31
32
Fizz
34
Buzz
Fizz
37
38
Fizz
Buzz
41
Fizz
43
44
FizzBuzz
46
47
Fizz
49
Buzz

In this example, the program prints the FizzBuzz sequence from 1 to 50 according to the FizzBuzz rules.
