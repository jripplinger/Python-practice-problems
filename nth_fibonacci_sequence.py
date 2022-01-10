#Python code to iteratively calculate and then display the nth term of the Fibonacci sequence where n is chosen by the user.
#I have chosen to start the Fibonacci sequence at 0 and not 1 although some people start the sequence at 1.

class FibonacciTerm:
    def __init__(self, term):
        self.term = term
        self.term_one = 0
        self.term_two = 1
        self.current_term = 3
        self.current_placevalue = None

    def calc_fibonacci(self):
        if self.term == 1:
            self.current_placevalue = 0
        elif self.term == 2:
            self.current_placevalue = 1
        else:
            while self.current_term <= self.term:
                self.current_placevalue = self.term_one + self.term_two
                self.term_one = self.term_two
                self.term_two = self.current_placevalue
                self.current_term += 1
    
    def get_current_placevalue(self):
        return self.current_placevalue
        
while True: 
    term = int(input("Which Fibonacci term value would you like displayed?"))
    if term <= 0:
        print("I'm sorry, this is not a valid entry. Please enter a positive integer.")
    else:
        break
instance_fibonacci = FibonacciTerm(term)
instance_fibonacci.calc_fibonacci()
value_term = instance_fibonacci.get_current_placevalue()
print(f"The value for term {term} is {value_term}.")
