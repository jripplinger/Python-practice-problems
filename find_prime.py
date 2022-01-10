#Python code to calculate and display the nth prime number where n is chosen by the user.

class CalculatePrime:
    def __init__(self, prime_position):
        self.prime_position = prime_position
        self.prime_dict = {1:2}
        self.key = 2
        self.test_value = 3
        self.divisor = 2
        self.prime = True

    def calculate_primes(self):
        while self.key <= self.prime_position:  
            while self.divisor < self.test_value:            
                if self.test_value % self.divisor == 0:
                    self.prime = False
                self.divisor += 1
            if self.prime == True:                        
                self.prime_dict[self.key] = self.test_value
                self.key += 1
            self.test_value += 1                      
            self.divisor = 2                           
            self.prime = True                  

    def get_last_prime(self):
        return self.prime_dict[self.key-1]


print("A prime number is only divisible by itself and 1.")
print("The first prime number is 2.")
prime_position = int(input("Which prime number would you like me to find?"))
instance_calculate_prime = CalculatePrime(prime_position)
instance_calculate_prime.calculate_primes()
value = instance_calculate_prime.get_last_prime()
prime_position = str(prime_position)
if prime_position[-1] == "1" and prime_position != "11":
    suffix = "st"
elif prime_position[-1] == "2" and prime_position != "12":
    suffix = "nd"
elif prime_position[-1] == "3" and prime_position != "13":
    suffix = "rd"
else:
    suffix = "th"
print(f"The {prime_position}{suffix} prime is {value}.")

