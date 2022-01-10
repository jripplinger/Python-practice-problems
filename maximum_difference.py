#Python code to calculate the maximum difference between a pair
#of array element values, x and y, and their position in the array,
#denoted as Px and Py. The code therefore maximizes |x-y| + |Px - Py|.

class MaxDifference:
    def __init__(self, input_list):
        self.input_list = input_list
        self.max_difference = 0
        self.value_element_x = None
        self.element_x_position = None
        self.value_element_y = None
        self.element_y_position = None
        
    def calculate_max_difference(self):
        for i in range(len(self.input_list)):
            for m in range(i, len(self.input_list)):
                difference = abs(self.input_list[i] - self.input_list[m]) + abs(i - m)
                if difference > self.max_difference:
                    self.max_difference = difference
                    self.value_element_x = self.input_list[i]
                    self.element_x_position = i
                    self.value_element_y = self.input_list[m]
                    self.element_y_position = m

    def get_max_difference(self):
        return self.max_difference

    def get_element_x(self):
        return self.value_element_x

    def get_element_x_position(self):
        return self.element_x_position
    
    def get_element_y(self):
        return self.value_element_y

    def get_element_y_position(self):
        return self.element_y_position

print("If you give me a list, I will find the maximum difference between a pair of the list elements and their positions.")
input_length = int(input("How many elements will your list include?"))
input_list = []
print("Please enter your list elements: ")
for i in range(input_length):
    element = int(input())
    input_list.append(element)
instance_max_difference = MaxDifference(input_list)
instance_max_difference.calculate_max_difference()
difference = instance_max_difference.get_max_difference()
value_x = instance_max_difference.get_element_x()
position_x = instance_max_difference.get_element_x_position()
value_y = instance_max_difference.get_element_y()
position_y = instance_max_difference.get_element_y_position()
print(f"The maximum difference is {difference}, based on value {value_x} at position {position_x} and {value_y} at position {position_y}.")



    

    