# put your code here.
def count_words(filename):

    test_file = open(filename)
    word_count = {}
    for line in test_file:
        line = line.rstrip().lower()
        file_words = line.split(' ')
        for word in file_words:
            word_count[word] = word_count.get(word, 0) + 1
    for word in word_count:
        print("{}: {}".format(word, word_count[word]))


count_words('test.txt')
