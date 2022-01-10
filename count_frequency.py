#Python code to count the frequency of values in an array. Possible values will be
#limited to [-50, 50].

import random

class CountFrequency:
    def __init__(self, input_list):
        self.input_list = input_list
        self.frequencies = {}

    def calculate_frequencies(self):
        for i in range(-50,50):
            self.frequencies[i] = 0
        for i in range(len(self.input_list)):
            self.frequencies[self.input_list[i]] += 1
        
    def get_frequencies(self):
        return self.frequencies


print("I can calculate the frequency of values in an array.")
length_list = int(input("How long would you like the array to be?"))
input_list = []
for i in range(length_list):
    element = random.randint(-50,50)
    input_list.append(element)
instance_count_frequency = CountFrequency(input_list)
instance_count_frequency.calculate_frequencies()
frequencies = instance_count_frequency.get_frequencies()
for key in frequencies:
    value = frequencies.get(key)
    print(f"{key} occurs {value} times.")

