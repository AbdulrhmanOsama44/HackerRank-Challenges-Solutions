from collections import OrderedDict

num_of_items = int(input())
item_dict_ordered = OrderedDict()

for i in range(num_of_items):
    
    item, price = input().strip().rsplit(' ', 1)
    price = int(price)
    
    if item in item_dict_ordered:
        item_dict_ordered[item] += price
    else:
        item_dict_ordered[item] = price

for item, price in item_dict_ordered.items():
    print(item, price)