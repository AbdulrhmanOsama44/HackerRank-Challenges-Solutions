def person_lister(f):
    def inner(people):
        sorted_list = sorted(people, key = lambda x: int(x[2]))
        return [f(i) for i in sorted_list]
    return inner