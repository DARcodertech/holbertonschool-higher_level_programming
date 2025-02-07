#!/usr/bin/env python3

class CountedIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        try:
            value = next(self.iterator)
            self.count += 1
            return value
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count