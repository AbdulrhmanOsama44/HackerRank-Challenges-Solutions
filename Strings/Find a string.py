def count_substring(string, sub_string):
    
    counter = 0
    start = 0
    end = len(sub_string)
    while end <= len(string):
        if sub_string == string[start : end]:
            counter += 1
        start += 1
        end += 1
    
    return counter