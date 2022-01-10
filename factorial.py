#Python code to calculate the number of trailing 0's in a factorial.

class TrailingZeros:
    def __init__(self, numb):
        self.numb = numb
        self.factorial = 1
        self.trailing_zeros = 0

    def calculate_factorial(self):
        while self.numb > 1:
            self.factorial *= self.numb
            self.numb -= 1

    def calculate_trailing_zeros(self):
        self.factorial = str(self.factorial)
        self.factorial = self.factorial[::-1]
        position = 0
        for digit in self.factorial:
            if digit == "0":
                self.trailing_zeros += 1
                position += 1
            else:
                break
    
    def get_trailing_zeros(self):
        return self.trailing_zeros


print("If you give me an integer, I will tell you the number of trailing zero's in its factorial.")
numb = int(input("Please enter an integer: "))
instance_trailing_zeros = TrailingZeros(numb)
instance_trailing_zeros .calculate_factorial()
instance_trailing_zeros .calculate_trailing_zeros()
trailing_zeros = instance_trailing_zeros .get_trailing_zeros()
print(f"There are {trailing_zeros} trailing zeros in {numb}!.")