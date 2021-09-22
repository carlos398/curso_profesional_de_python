def remove(some_list):
    without_duplicate = []
    for element in some_list:
        if element not in without_duplicate:
            without_duplicate.append(element)
    return without_duplicate


#con sets
def remove_sets(some_list):
    return set(some_list)


if __name__ == '__main__':
    random_list = [1,1,2,5,4,4,5,8,7,6]
    print(remove_sets(random_list))