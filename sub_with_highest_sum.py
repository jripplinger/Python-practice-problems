#Python code to find the circular subarray (can wrap around) with the highest sum.

class SubarraySums:
    def __init__(self, input_list):
        self.input_list = input_list
        self.sum = None

    def calc_subarrays(self):
        if len(self.input_list) == 1:                                 
            self.sum = self.input_list[0]
        else:                                                         
            for i in range(len(self.input_list)):                    
                complete = False                                      
                running_sum = self.input_list[i]                      
                for m in range(i+1, len(self.input_list)):             
                    if running_sum + self.input_list[m] < running_sum:  
                        complete = True
                        if self.sum == None:
                            self.sum = running_sum
                        else:
                            if self.sum < running_sum:
                                self.sum = running_sum 
                        break
                    else:
                        running_sum += self.input_list[m]             
                if complete == False:
                    for n in range(0, i):
                        if running_sum + self.input_list[n] < running_sum:  
                            complete = True
                            break
                        else:
                            running_sum += self.input_list[n]
                    if self.sum == None:
                            self.sum = running_sum
                    else:
                        if self.sum < running_sum:
                            self.sum = running_sum 
               
    def get_sum(self):
        return self.sum


print("If you give me a list, I will calculate the sublist with the highest sum.")
list_length = int(input("How many elements will your list contain?"))
input_list = []
print("Please enter your list elements: ")
for i in range(list_length):
    element = int(input())
    input_list.append(element)
instance_subarray_sums = SubarraySums(input_list)
instance_subarray_sums.calc_subarrays()
subarray_sum = instance_subarray_sums.get_sum()
print(f"The max sum of any sublist in your list is {subarray_sum}.")
