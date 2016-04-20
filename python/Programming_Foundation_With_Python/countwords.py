"""Count words."""
def word_cmp(a, b):
    if a[1] < b[1]:
        return -1
    elif a[1] == b[1] and a[0] < b[0]:
        return -1
    else:
        return 1
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    
    # TODO: Count the number of occurences of each word in s
    s= s.split()
    temp_dict = {}
    for w in s:
        if not w in temp_dict:
            temp_dict[w] = 0 
        temp_dict[w] = temp_dict[w] + 1
        
    sorted_items = temp_dict.items() 
    sorted_items.sort(cmp = word_cmp, reverse = True)
    
    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    
    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    top_n = sorted_items[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()