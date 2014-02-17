import math

class Slice:
    #A custom 2D array that looks like this:
    # b4 b3 b2 b1 b0 c a0 a1 a2 a3 a4 etc
    #Special built for CA usage
    def __init__(self, data = []):
        assert isinstance(data, list) or isinstance(data, Slice)
        if (isinstance(data, list)):
            if (len(data) > 0):
                center = math.ceil(len(data) // 2)
                self._before = data[:center]
                self._before.reverse()
                self._after = data[center + 1:]
                self._center = data[center]
            else:
                self._before = []
                self._after = []
                self._center = 0
        elif isinstance(data, Slice):
            self._before = data._before
            self._after = data._after
            self._center = data._center
        else:
            self._before = []
            self._after = []
            self._center = 0

    def __getitem__(self,index):
        assert isinstance(index, int)
        if (not(self.exists(index))):
            raise IndexError("Slice index does not exist")
        if (index > 0):
            return self._after[index - 1]
        elif (index < 0):
            return self._before[(-index) - 1]
        else:
            return self._center

    def append(self, item):
        assert isinstance(item, int)
        self._after.append(item)

    def prepend(self, item):
        assert isinstance(item, int)
        self._before.append(item)

    def setCenterIndex(self, item):
        assert isinstance(item, int)
        self._center = item

    def getNeighbors(self, index):
        assert isinstance(index, int)
        left = right = -1
        try:
                left = self[index - 1]
        except IndexError:
            left = 0
        try:
            right = self[index + 1]
        except IndexError:
            right = 0
        return left, right

    def range(self):
        return -len(self._before), len(self._after)
        
    def exists(self, index):
        assert isinstance(index, int)
        if (index > len(self._after) or index < -len(self._before)):
            return False
        return True
    def trimTo(self, halfTargetSize):
        self._before = self._before[:halfTargetSize]
        self._after = self._after[:halfTargetSize]
    def __str__(self):
        return str(self._before[::-1])[1:-1] + ", _" + str(self._center) + "_, " + str(self._after)[1:-1]
    def to_short_str(self):
        return str(self._before[::-1]).replace(", ", "")[1:-1] + str(self._center) + str(self._after).replace(", ", "")[1:-1];
    def __len__(self):
        return len(self._before) + 1 + len(self._after)