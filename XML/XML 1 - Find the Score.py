def get_attr_number(node):
    return sum(len(i.attrib) for i in node.iter())