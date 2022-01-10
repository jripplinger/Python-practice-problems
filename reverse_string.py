#Python code to reverse a user-defined string in 3 ways: 1) reverse the entire string character by character, 
#2) reverse each word in the string but do not reverse the order the of the words compared to each other, and 
#3) reverse the order of the words compared to each other but do not reverse the actual words.

class ReverseList:
    def __init__(self, string_words):
        self.string_words = string_words
        self.whole_string_reversed = ""
        self.string_with_words_reversed = ""
        self.string_reversed_but_not_words = ""

    def reverse_whole_string(self):
        self.whole_string_reversed = self.string_words[::-1]

    def reverse_words_not_string(self):
        string_to_split = self.string_words
        string_ending = ""
        if string_to_split[-1] == "." or string_to_split[-1] == "!" or string_to_split[-1] == "?":
            string_ending = string_to_split[-1]
            string_to_split = string_to_split[:-1]
        split_string = string_to_split.split(" ")
        for word in split_string:
            word = word[::-1]
            self.string_with_words_reversed = self.string_with_words_reversed + " " + word
        self.string_with_words_reversed = self.string_with_words_reversed + string_ending

    def reverse_string_not_words(self):
        string_to_split = self.string_words
        string_ending = ""
        if string_to_split[-1] == "." or string_to_split[-1] == "!" or string_to_split[-1] == "?":
            string_ending = string_to_split[-1]
            string_to_split = string_to_split[:-1]
        split_string = string_to_split.split(" ")
        for word in split_string:
            self.string_reversed_but_not_words = word + " " + self.string_reversed_but_not_words
        self.string_reversed_but_not_words = self.string_reversed_but_not_words[:-1]
        self.string_reversed_but_not_words = self.string_reversed_but_not_words + string_ending
        
    def get_whole_string_reversed(self):
        return self.whole_string_reversed

    def get_string_with_reversed_words(self):
        return self.string_with_words_reversed

    def get_string_reversed_but_not_words(self):
        return self.string_reversed_but_not_words


string_words = input("Please enter a string you would like to reverse: ")
instance_reverse_list = ReverseList(string_words)
instance_reverse_list.reverse_whole_string()
reversed_whole_string = instance_reverse_list.get_whole_string_reversed()
print(f"Your string reversed character by character is: {reversed_whole_string}")
instance_reverse_list.reverse_words_not_string()
reversed_words_only = instance_reverse_list.get_string_with_reversed_words()
print(f"Your string with only the words reversed, not their order, is: {reversed_words_only}")
instance_reverse_list.reverse_string_not_words()
reversed_word_order = instance_reverse_list.get_string_reversed_but_not_words()
print(f"Your string with the order of the words reversed is: {reversed_word_order}")




