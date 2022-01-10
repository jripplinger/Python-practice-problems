#Python code to sort a list using insertion sort. Note that insertion sort cannot be used with large arrays.

class InsertionSort:
    def __init__(self, input_list):
        self.input_list = input_list

    def insertion_sort(self):
       for i in range(1, len(self.input_list)):
           for m in range(i):
               if self.input_list[i] < self.input_list[m]:
                   temp = self.input_list[i]
                   self.input_list[i]  = self.input_list[m]
                   self.input_list[m] = temp

    def get_sorted_list(self):
        return self.input_list

length_input_list = int(input("How many elements would you like in your list?"))
print("Please enter the elements you would like to sort: ")
input_list = []
for i in range(length_input_list):
    element = int(input())
    input_list.append(element)
instance_insertion_sort = InsertionSort(input_list)
instance_insertion_sort.insertion_sort()
sorted_list = instance_insertion_sort.get_sorted_list()
print(f"Your sorted list is {sorted_list}.")