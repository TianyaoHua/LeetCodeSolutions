class LFUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dict = {}
        self.heap = [[float('inf'), 0] for i in range(capacity)]
        self.time = 0
        self.n = 0
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dict:
            self.time += 1

            return self.dict[key]
        else:
            return -1
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """