#Python code to find the three elements in an array that are closest to a user designated target
#and to return the sum of the three elements.

from itertools import combinations 

class FindSum:
    def __init__(self, input_list, target):
        self.input_list = input_list
        self.target = target
        self.sum = None

    def calculate_sum(self):
        if len(self.input_list) == 3:
            self.sum += self.input_list[0] + self.input_list[1] + self.input_list[2]
        else:
            list_combinations = list(combinations(self.input_list, 3))
            for i in range(len(list_combinations)):
                a_combination = list_combinations[i]
                a_sum = sum(a_combination)
                if self.sum == None:
                   self.sum = a_sum
                else:
                    if abs(self.target - a_sum) < abs(self.target - self.sum):
                        self.sum = a_sum

    def get_sum(self):
        return self.sum


print("If you give me a list of 3 or more integers and a target sum, I will find the sum of 3 elements that is closest to the target and return that sum.")
length_list = int(input("How many elements would you like in your list? Remember you must enter at least 3 elements. "))
input_list = []
print("Please enter your elements: ")
for i in range(length_list):
    element = int(input())
    input_list.append(element)
target = int(input("What is your target sum?"))
instance_find_sum = FindSum(input_list, target)
instance_find_sum.calculate_sum()
closest_sum = instance_find_sum.get_sum()
print(closest_sum)
print(f"The closest sum of 3 elements in your list to {target} is {closest_sum}.")

