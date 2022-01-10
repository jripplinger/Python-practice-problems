#Python code to count the number of element pairs that add up to a third
#element where all elements occur in a user defined list.

class CountTriplets:
    def __init__(self, input_list):
        self.input_list = input_list
        self.numb_triplets = 0

    def calculate_the_triplets(self):
        for i in range(len(self.input_list)):
            for m in range(i+1, len(self.input_list)):
                comparison_list = self.input_list.copy()
                sum = self.input_list[i] + self.input_list[m]
                for n in range(len(comparison_list)):
                    if sum == comparison_list[n]:
                        self.numb_triplets += 1

    def get_input_list(self):
        return self.numb_triplets

print("If you give me a list, I will tell you how many pairs of elements add up to another element in the list.")
list_length = int(input("How long is your list going to be?"))
input_list = []
print(f"Please enter your {list_length} elements: ")
for i in range(list_length):
    element = int(input())
    input_list.append(element)
instance_count_triplets = CountTriplets(input_list)
instance_count_triplets.calculate_the_triplets()
numb_triplets = instance_count_triplets.get_input_list()
print(f"There are {numb_triplets} element pairs that add to a third element in your array.")






