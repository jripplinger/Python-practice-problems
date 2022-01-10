#Python code to find the missing number in an array of contiguous integers.

class FindMissingInt:
    def __init__(self, input_list):
        self.input_list = input_list
        self.missing_int = None

    def sort_array(self):
        for i in range(len(self.input_list)):
            sublist_of_list = self.input_list[i::]
            min_of_list = min(sublist_of_list)
            for m in range(i, len(self.input_list)):
                if self.input_list[m] == min_of_list:
                    del self.input_list[m]
                    self.input_list.insert(i, min_of_list)
    
    def find_missing_int(self):
        for i in range(len(self.input_list)-1):
            if self.input_list[i] + 1 != self.input_list[i+1]:
                self.missing_int = self.input_list[i] + 1 
    
    def get_missing_int(self):
        return self.missing_int


print("I can detect a missing value in a contiguous list. The list does not need to be in order.")
length = int(input("How long would like the array to be?"))
print("Please enter your lists values in any order: ")
input_list = []
for i in range(length):
    element = int(input())
    input_list.append(element)
instance_find_missing_int = FindMissingInt(input_list)
instance_find_missing_int.sort_array()
instance_find_missing_int.find_missing_int()
missing_int = instance_find_missing_int.get_missing_int()
print(f"The array's missing value is {missing_int}.")


        

