import collections

class LRUCache:

    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity

    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return False, None
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return True, price

    def insert(self, isbn, price):
        # we add the value for key only if the key is not present - we don't
        # update existing values.
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif self._capacity <= len(self._isbn_price_table):
            self._isbn_price_table.popitem(last=False)

        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        return self._isbn_price_table.pop(isbn, None) is not None
