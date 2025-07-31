def fun(s):
    import re
    pattern = r'[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{,3}'
    
    return bool(re.fullmatch(pattern, s))