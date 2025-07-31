def average(array):
    
    distinct_heights = set(array)
    average = sum(distinct_heights) / len(distinct_heights)
    
    return round(average, 3)