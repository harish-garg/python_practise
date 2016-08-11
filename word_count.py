word_dict = {}
string = "Harish Kumar Garg Aaavni Harinee Garg Neetha Naik Anitha Naik"
print string
word_list = string.split()
for word in word_list:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
print word_dict
