#Python code to sort a list using selection sort. Note that you cannot use selection sort on large lists.

class SelectionSort:
    def __init__(self, input_list):
        self.input_list = input_list

    def selection_sort(self):
        for i in range(len(self.input_list)):
            sublist_of_list = self.input_list[i::]
            min_of_list = min(sublist_of_list)
            for m in range(i, len(self.input_list)):
                if self.input_list[m] == min_of_list:
                    del self.input_list[m]
                    self.input_list.insert(i, min_of_list)

    def get_sorted_list(self):
        return self.input_list


length_input_list = int(input("How many elements would you like in your list?"))
print("Please enter the elements you would like to sort: ")
input_list = []
for i in range(length_input_list):
    element = int(input())
    input_list.append(element)
instance_selection_sort = SelectionSort(input_list)
instance_selection_sort.selection_sort()
sorted_list = instance_selection_sort.get_sorted_list()
print(f"Your sorted list is {sorted_list}.")

