from data_structures.hashtable import Hashtable


def left_join(table_a, table_b):
    '''
    Arguments: Two hashmaps
    Return: a List with the keys of table a and the values from both table a and table b (if available)
    '''
    joined_list = []

    for key, value in table_a.items():
        if table_b.get(key):
            joined_list.append([key, value, table_b.get(key)])

        else:
            joined_list.append([key, value, 'NONE'])

    print(joined_list)
    return joined_list
