import time, os
from colorama import Fore, Style, init

# Initialize colorama
init()

def slow_print(text, color=Fore.WHITE, delay=0.1):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print(Style.RESET_ALL)

def pause():
    input("\nPress Enter to continue...")

def clear():
    os.system("clear")

def introduction():
    slow_print("Welcome to the Python Beginners Tutorial!", Fore.CYAN)
#    pause()
    slow_print("You will learn about variables, data types, operations, conditionals, loops, functions, and OOP.", Fore.CYAN)
#    pause()
    slow_print("Let's get started!\n", Fore.CYAN)
    pause()
    clear()

def section_variables():
    slow_print("1. Variables and Data Types", Fore.YELLOW)
    pause()
    slow_print("Variables are used to store information to be referenced and manipulated in a program.", Fore.YELLOW)
    pause()
    slow_print("Example:", Fore.YELLOW)
    pause()
    slow_print("age = 25  # Integer", Fore.GREEN)
    pause()
    slow_print("height = 5.9  # Float", Fore.GREEN)
    pause()
    slow_print("name = 'John'  # String", Fore.GREEN)
    pause()
    slow_print("is_student = True  # Boolean", Fore.GREEN)
    pause()
    slow_print("fruits = ['apple', 'banana', 'cherry']  # List", Fore.GREEN)
    pause()
    slow_print("coordinates = (10.0, 20.0)  # Tuple", Fore.GREEN)
    pause()
    slow_print("person = {'name': 'Alice', 'age': 30}  # Dictionary", Fore.GREEN)
    pause()
    slow_print("\n")

def section_operations():
    slow_print("2. Basic Operations", Fore.YELLOW)
    pause()
    slow_print("Example of arithmetic operations:", Fore.YELLOW)
    pause()
    slow_print("a = 10", Fore.GREEN)
    pause()
    slow_print("b = 5", Fore.GREEN)
    pause()
    slow_print("print('Addition:', a + b)", Fore.GREEN)
    pause()
    slow_print("print('Subtraction:', a - b)", Fore.GREEN)
    pause()
    slow_print("print('Multiplication:', a * b)", Fore.GREEN)
    pause()
    slow_print("print('Division:', a / b)", Fore.GREEN)
    pause()
    slow_print("print('Modulus:', a % b)", Fore.GREEN)
    pause()
    slow_print("\n")

def section_conditionals():
    slow_print("3. Conditional Statements", Fore.YELLOW)
    pause()
    slow_print("Example:", Fore.YELLOW)
    pause()
    slow_print("age = 25", Fore.GREEN)
    pause()
    slow_print("if age > 18:", Fore.GREEN)
    pause()
    slow_print("    print('You are an adult.')", Fore.GREEN)
    pause()
    slow_print("else:", Fore.GREEN)
    pause()
    slow_print("    print('You are not an adult.')", Fore.GREEN)
    pause()
    slow_print("\n")

def section_loops():
    slow_print("4. Loops", Fore.YELLOW)
    pause()
    slow_print("Example of a for loop:", Fore.YELLOW)
    pause()
    slow_print("fruits = ['apple', 'banana', 'cherry']", Fore.GREEN)
    pause()
    slow_print("for fruit in fruits:", Fore.GREEN)
    pause()
    slow_print("    print('I like', fruit)", Fore.GREEN)
    pause()
    slow_print("\n")
    slow_print("Example of a while loop:", Fore.YELLOW)
    pause()
    slow_print("count = 0", Fore.GREEN)
    pause()
    slow_print("while count < 3:", Fore.GREEN)
    pause()
    slow_print("    print('Count is:', count)", Fore.GREEN)
    pause()
    slow_print("    count += 1", Fore.GREEN)
    pause()
    slow_print("\n")

def section_functions():
    slow_print("5. Functions", Fore.YELLOW)
    pause()
    slow_print("Example:", Fore.YELLOW)
    pause()
    slow_print("def greet(name):", Fore.GREEN)
    pause()
    slow_print("    return f'Hello, {name}!'", Fore.GREEN)
    pause()
    slow_print("print(greet('Alice'))", Fore.GREEN)
    pause()
    slow_print("\n")

def section_oop():
    slow_print("6. Object-Oriented Programming (OOP)", Fore.YELLOW)
    pause()
    slow_print("Example:", Fore.YELLOW)
    pause()
    slow_print("class Dog:", Fore.GREEN)
    pause()
    slow_print("    def __init__(self, name, age):", Fore.GREEN)
    pause()
    slow_print("        self.name = name", Fore.GREEN)
    pause()
    slow_print("        self.age = age", Fore.GREEN)
    pause()
    slow_print("    def description(self):", Fore.GREEN)
    pause()
    slow_print("        return f'{self.name} is {self.age} years old'", Fore.GREEN)
    pause()
    slow_print("my_dog = Dog('Buddy', 3)", Fore.GREEN)
    pause()
    slow_print("print(my_dog.description())", Fore.GREEN)
    pause()
    slow_print("\n")

def quiz():
    score = 0
    total_questions = 5

    slow_print("Quiz Time! Answer the following questions:", Fore.CYAN)
    pause()

    # Question 1
    answer = input(Fore.WHITE + "1. What data type is this: [1, 2, 3, 4]? ")
    if answer.lower() == "list":
        score += 1
        slow_print("Correct!", Fore.GREEN)
    else:
        slow_print("Incorrect. The correct answer is 'list'.", Fore.RED)

    # Question 2
    answer = input(Fore.WHITE + "2. What is the output of 10 % 3? ")
    if answer == "1":
        score += 1
        slow_print("Correct!", Fore.GREEN)
    else:
        slow_print("Incorrect. The correct answer is '1'.", Fore.RED)

    # Question 3
    answer = input(Fore.WHITE + "3. How do you define a function in Python? (use 'def' keyword) ")
    if "def" in answer:
        score += 1
        slow_print("Correct!", Fore.GREEN)
    else:
        slow_print("Incorrect. You define a function using the 'def' keyword.", Fore.RED)

    # Question 4
    answer = input(Fore.WHITE + "4. What keyword is used for conditional statements in Python? ")
    if answer.lower() == "if":
        score += 1
        slow_print("Correct!", Fore.GREEN)
    else:
        slow_print("Incorrect. The correct answer is 'if'.", Fore.RED)

    # Question 5
    answer = input(Fore.WHITE + "5. What method is used to initialize an object's attributes in a class? ")
    if answer.lower() == "__init__":
        score += 1
        slow_print("Correct!", Fore.GREEN)
    else:
        slow_print("Incorrect. The correct answer is '__init__'.", Fore.RED)

    slow_print(f"\nYour score is {score}/{total_questions}", Fore.CYAN)
    if score == total_questions:
        slow_print("Excellent! You got all questions right!", Fore.GREEN)
    elif score >= total_questions / 2:
        slow_print("Good job! You passed the quiz!", Fore.YELLOW)
    else:
        slow_print("You need more practice. Review the tutorial and try again.", Fore.RED)

def main():
    introduction()
    section_variables()
    section_operations()
    section_conditionals()
    section_loops()
    section_functions()
    section_oop()
    quiz()

if __name__ == "__main__":
    main()
