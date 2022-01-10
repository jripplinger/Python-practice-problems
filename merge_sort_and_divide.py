#Python code to merge two unsorted arrays in sorted order and then modify the
#first array to hold the lower value and the second array to hold the higher values.

class MergeSortDivide:
    def __init__(self, input_listA, input_listB):
        self.input_listA = input_listA
        self.input_listA_length = ""
        self.input_listB = input_listB
        self.input_listB_length = ""
        self.merged = []

    def merge_and_sort(self):
        self.merged = self.input_listA + self.input_listB
        for i in range(len(self.merged)):
            sublist_of_list = self.merged[i::]
            min_of_list = min(sublist_of_list)
            for m in range(i, len(self.merged)):
                if self.merged[m] == min_of_list:
                    del self.merged[m]
                    self.merged.insert(i, min_of_list)

    def divide(self):
        self.input_listA_length = len(self.input_listA)
        self.input_listB_length = len(self.input_listB)
        self.input_listA.clear()
        self.input_listB.clear()
        self.input_listA = self.merged[:self.input_listA_length]
        self.input_listB = self.merged[self.input_listA_length:]

    def get_input_listA(self):
        return self.input_listA

    def get_input_listB(self):
        return self.input_listB
        

print("If you give me 2 lists, I will sort their contents and place the smallest values in the first list and the largest in the second.")
listA_length = int(input("How long is your first list going to be?"))
input_listA = []
print("Please enter the elements for your first list: ")
for i in range(listA_length):
    element = int(input())
    input_listA.append(element)
listB_length = int(input("How long is your second list going to be?"))
input_listB = []
print("Please enter the elements for your second list: ")
for i in range(listB_length):
    element = int(input())
    input_listB.append(element)
instance_merge_sort_divide = MergeSortDivide(input_listA, input_listB)
instance_merge_sort_divide.merge_and_sort()
instance_merge_sort_divide.divide()
print(instance_merge_sort_divide.get_input_listA())
print(instance_merge_sort_divide.get_input_listB())

    
