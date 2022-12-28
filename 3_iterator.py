
class FlatIterator:

    def __init__(self, list_of_list):

        def normalize(item):
            return flatten(item) if isinstance(item, list) else [item]

        def flatten(tree):
            return sum(map(normalize, tree), [])

        self.list_of_list = normalize(list_of_list)

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        if not self.list_of_list:
            raise StopIteration
        return self.list_of_list.pop(0)


def test_3():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()


