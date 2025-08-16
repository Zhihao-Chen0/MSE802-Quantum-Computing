# write python script to calculate complex numbers and plot the result:
# prompt to input the numbers
# prompt to choose calculation methods: add, substract, multiply, divide
# print the result in text 
# show the result visually

import matplotlib.pyplot as plt

class ComplexNumber:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num1 - self.num2
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num1 / self.num2
    
def main():
    complexnum1 = complex(input("Enter the first complex number (e.g., 1+3j, no space): "))
    complexnum2 = complex(input("Enter the second complex number (e.g., 1+3j, no space): "))
    operation = input("Choose an operation (add, subtract, multiply, divide)just input '+, -, *, /': ")

    calc = ComplexNumber(complexnum1, complexnum2)

    if operation == "+":
        result = calc.add()
    elif operation == "-":
        result = calc.subtract()
    elif operation == "*":
        result = calc.multiply()
    elif operation == "/":
        result = calc.divide()
    else:
        print("Invalid operation")
        return

    print("Result:", result)

    # Plotting the result
    plt.plot([0, result.real], [0, result.imag], marker='o')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.grid(True)
    plt.axhline(0, color='black')
    plt.axvline(0, color='black')
    plt.title("Complex Number Result")
    plt.show()

if __name__ == "__main__":
    main()