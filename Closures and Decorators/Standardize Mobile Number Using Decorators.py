def wrapper(f):
    def fun(l):
        decorated_list = []
        for i in l:
            decorated_list.append('+91 {} {}'.format(i[-10 : -5], i[-5 : ]))

        f(decorated_list)
    return fun