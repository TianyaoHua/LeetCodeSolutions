class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.c = capacity
        self.cc = 0
        self.h = {}
        self.m = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.h:
            self.m.remove(key)
            self.m.append(key)
            return self.h[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cc < self.c:
            self.cc += 1
            self.h.update({key: value})
            self.m.append(key)
        else:
            self.h.update({key: value})
            d = self.m.pop(0)
            self.m.append(key)
            self.h.pop(d)