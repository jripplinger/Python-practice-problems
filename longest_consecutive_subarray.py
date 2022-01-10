#Python code to find the longest consecutive subsequence of a given array.

import copy

class ConsecutiveSubsequence:
    def __init__(self, input_list):
        self.input_list = input_list
        self.consecutive_list = []

    def calculate_consecutive(self):
        for i in range(len(self.input_list)):
            sublist = []
            sublist.append(self.input_list[i])
            pos = i
            while pos < len(self.input_list) - 1:
                if self.input_list[pos + 1] == self.input_list[pos] + 1:
                    sublist.append(self.input_list[pos+1])
                    pos += 1
                else:
                    break
            if len(sublist) > len(self.consecutive_list):
                self.consecutive_list = sublist
        
    def get_consecutive(self):
        return self.consecutive_list

print("If you give me an array, I will calculate its longest consecutive subarray.")
length_list = int(input("How long would you like your array to be?"))
print("Please enter the values of your elements: ")
input_list = []
for i in range(length_list):
    element = int(input())
    input_list.append(element)
instance_calculate_consecutive = ConsecutiveSubsequence(input_list)
instance_calculate_consecutive.calculate_consecutive()
longest_consecutive_sequence = instance_calculate_consecutive.get_consecutive()
print(f"The longest consecutive subarray is {longest_consecutive_sequence}.")

