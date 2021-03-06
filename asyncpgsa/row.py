

class Row:
    __slots__ = ('row',)

    def __init__(self, row):
        self.row = row

    def __getattr__(self, item):
        try:
            return self.row[item]
        except KeyError:
            raise AttributeError("'Row' object has no attribute '{}'"
                                 .format(item))


class RowGenerator:
    __slots__ = ('data', 'iter')

    def __init__(self, data):
        self.data = data
        self.iter = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        return Row(next(self.iter))