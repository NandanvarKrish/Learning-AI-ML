print('''
OE: Check even/odd
3L: Largest among 3 numbers
12N: print 1 to N
SNN: Sum of N numbers
RS:  Reverse String
SD: Sum of digits
MT: Multiplication Table
CDN: Count digits in number
CP: Check if a number is prime
FS: Fibonacci Sequence
FN: Factorial of a number
CVS: Count Vowels in a string
FB: FizzBuzz
PN: Power of a number
GCD: Greatest common divisor
PC: Palindrome Check
FDA: Find all duplicates in array
BIS: Binary Search
BUS: Bubble sort
ANC: Armstrong Number check
sqrt: square root
''')

# FUNCTIONS DEFINITION

def even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

def largest_among_3(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is greater"
    elif num2 > num1 and num2 > num3:
        return f"{num2} is greater"
    else:
        return f"{num3} is greater"
    
def one_to_n(num):
    for i in range(num+1):
        print(i)

def sum_of_n_numbers(n):
    total = 0

    for i in range(n):
        num = int(input("Enter number: "))
        total = total + num

    print("Sum:", total)

def reverse_string(text):
    return text[::-1]

def sum_of_digits(n):
    total = 0

    while n > 0:
        total += n % 10
        n = n // 10

    return f"Sum of digits: {total}"

def multiplication_table(n):
    for i in range(1, 11, 1):
        print(f"{n} x {i} = {n * i}")

def count_digit_in_number(n):
    count = 0

    while n > 0:
        n = n // 10
        count += 1
    
    return f"Number of digits: {count}"

def check_prime(n):
    if n <= 1:
        return f"{n} is not prime"
    
    for i in range(2,n):
        if n % i == 0:
            return f"{n} is not prime"
    
    return f"{n} is prime"

def fibonacci_sequence(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

def factorial_calculator(n):
    result = 1

    for i in range (1, n + 1):
        result = result * i
    
    return f"{n}! = {result}"

def count_vowel_in_string(sentence):
    count = 0

    for char in sentence:
        if char.lower() in "aeiou":
            count += 1

    return f"Vowel count: {count}"

def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

def power_of_number(n, p):
    return f"{n}^{p} = {n ** p}"

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b 

    return f"GCD: {a}"

def palindrome_check(text, cleaned):
    left = 0
    right = len(cleaned) - 1
    result = True

    while left < right:
        if cleaned[left] != cleaned[right]:
            result = False
            break

        left += 1
        right -= 1

    print("Palindrome!" if result else "Not a Palindrome")

def find_duplicate_array():
    numbers = [1, 2, 3, 2, 4, 3, 5, 1]
    count = {}

    for num in numbers:
        count[num] = count.get(num, 0) + 1

    print("Duplicates:")
    for num, freq in count.items():
        if freq > 1:
            print(num)

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1

    nums = [2, 5, 8, 12, 16, 23, 38, 45]
    result = binary_search(nums, 23)
    print("Found at index:", result) if result != -1 else print("Not found")
def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

    print("Sorted:", arr)

def Armstrong_Number_Check(num):
    digits = len(str(num))  
    total = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        total += digit ** digits  
        temp //= 10
    
    if total == num:
        return f"{num} is an Armstrong number"
    else:
        return f"{num} is not an Armstrong number"

def square_root(n):
    for i in range(1, n):
        if i ** 2 == n:
            return f"Square root of {n} is {i}"
        

# CHOICE SELECTION

choice = input("Enter your choice: ").lower().strip()

# FUNCTION CALLING

match(choice):
    case "oe":
        num = float(input("Enter the number: "))
        output = even_odd(num)
        print(output)

    case "3l":
        num1 = int(input("Enter your first number:"))
        num2 = int(input("Enter your second number:"))
        num3 = int(input("Enter your third number:"))
        output = largest_among_3(num1, num2, num3)
        print(output)

    case "12n":
        num = int(input("Enter thr range: "))
        output = one_to_n(num)
        print(output)

    case "snn":
        n = int(input("Enter the range: "))
        output = sum_of_n_numbers(n)
        print(output)

    case "rs":
        text = input("Enter the text: ")
        reverse_string(text)

    case "sd":
        num = int(input("Enter the number: "))
        output = sum_of_digits(num)
        print(output)

    case "mt":
        n = int(input("Enter the number: "))
        output = multiplication_table(n)
        print(output)

    case "cdn":
        n = int(input("Enter the number: "))
        output = count_digit_in_number(n)
        print(output)

    case "cp":
        n = int(input("Enter the number: "))
        output = check_prime(n)
        print(output)

    case "fs":
        n = int(input("Enter the number of terms: "))
        output = fibonacci_sequence(n)
        print(output)

    case "fn":
        n = int(input("Enter the number: "))
        output = factorial_calculator(n)
        print(output)

    case "cvs":
        sentence = input("Enter a sentence: ")
        output = count_vowel_in_string(sentence)
        print(output)

    case "fb":
        n = int(input("Enter N: "))
        output = fizzbuzz(n)
        print(output)
    
    case "pn":
        n = int(input("Enter the number: "))
        p = int(input("Enter the power: "))
        output = power_of_number(n, p)
        print(output)

    case "gcd":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        output = greatest_common_divisor(a, b)
        print(output)
    
    case "pc":
        text = input("Enter a string: ")
        cleaned = text.replace(" ", "").lower()

        output = palindrome_check(text, cleaned)
        print(output)
    
    case "fda":
        output = find_duplicate_array()
        print(output)
    
    case "bis":
        arr = [1,2,3,4,5]
        target = 5
        output = binary_search(arr, target)
        print(output)

    case "bus":
        arr = [64, 34, 25, 12, 22, 11, 90]
        output = bubble_sort(arr)
        print(output)
    
    case "anc":
        num = int(input("Enter a number: "))
        output = Armstrong_Number_Check(num)
        print(output)

    case "sqrt":
        n = int(input("Enter the squared value: "))
        output = square_root(n)
        print(output)

    case _:
        print("Invalid code!")
