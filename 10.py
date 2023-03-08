# create the dictionary
sample_dict = {'C': 92, 'Java': 66, 'Python': 85}

# find the key with the lowest value
lowest_key = min(sample_dict, key=sample_dict.get)

# print the key with the lowest value
print(lowest_key)
