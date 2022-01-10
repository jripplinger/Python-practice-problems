#Python code to bubble sort a list provided by the user. Note you cannot use bubble sort on large lists. 

class BubbleSort:
    def __init__(self, user_list):
        self.user_list = user_list
        self.number_loops = len(self.user_list)
        self.comparisons = len(self.user_list) -1

    def bubble_sort(self):
        for num in range(self.number_loops):
            for i in range(self.comparisons):
                if self.user_list[i] > self.user_list[i+1]:
                    tempA = self.user_list[i]
                    tempB = self.user_list[i+1]
                    self.user_list[i] = tempB
                    self.user_list[i+1] = tempA
            self.comparisons -= 1
                    
    def get_list(self):
        return self.user_list


user_list = []
length_list = int(input("How many integers would you like to enter in your list?"))
print("Please enter the integers you would like to sort: ")
for i in range(length_list):
    element = int(input())
    user_list.append(element)
instance_bubble_sort = BubbleSort(user_list)
instance_bubble_sort.bubble_sort()
sorted_list = instance_bubble_sort.get_list()
print(f"Here is your list in ascending order: {sorted_list}.")