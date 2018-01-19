def count_words(s, n):
    words = s.split(' ')

    data = {}
    for word in words:
        if word in data.keys():
            data[word] += 1
        else:
            data[word] = 1

    return_result = sorted(data, key=lambda x: (-data[x], x))[:n]
    print(return_result)


def test_run():
    print(count_words("cat bat mat cat bat cat", 3))
    print(count_words("betty bought a bit of butter but the butter was bitter", 3))
    print(count_words("a b c c a d z", 4))  # a c b d


if __name__ == '__main__':
    test_run()
