class SegmentTree:
    def __init__(self, arr, fn, identity_element):
        self.n = len(arr)
        self.arr = [identity_element for _ in arr] + arr
        self.fn = fn
        self.identity_element = identity_element
        for i in range(self.n - 1, 0, -1):
            left = self.arr[i * 2]
            right = self.arr[i * 2 + 1]
            self.arr[i] = fn([left, right])

    def interval_query(self, left, right):
        left += self.n
        right += self.n

        acc = self.identity_element

        while left < right:
            if left % 2 == 1:
                acc = self.fn([acc, self.arr[left]])
                left += 1
            if right % 2 == 1:
                right -= 1
                acc = self.fn([acc, self.arr[right]])
            left //= 2
            right //= 2

        return acc

    def update(self, ix, newval):
        """
        Update one element from the initial array (a segment tree leaf),
        and have all the segment counts updated.
        """
        i = ix + self.n
        if self.arr[i] == newval:
            return
        delta = newval - self.arr[i]
        self.arr[i] = newval
        while i > 0:
            i //= 2
            self.arr[i] += delta

class SlowOp:
    def __init__(self, arr, fn, identity_element):
        self.arr = arr
        self.fn = fn
        self.identity_element = identity_element

    def interval_query(self, left, right):
        acc = self.identity_element
        for i in range(left, right):
            acc = self.fn([acc, self.arr[i]])
        return acc


# from random import randint
#
# rnd = [randint(1, 1000000) for _ in range(100000)]
#
# def test():
#     fn = min
#     idel = float('inf')
#
#     slow = SlowOp(rnd, fn, idel)
#     st = SegmentTree(rnd, fn, idel)
#
#     print(st.interval_query(1, 100))
#
#     for _ in range(1000):
#         left = randint(0, 100000 - 1)
#         right = randint(0, 100000 - 1)
#         if left > right:
#             left, right = right, left
#         if left == right:
#             continue
#         if slow.interval_query(left, right) != st.interval_query(left, right):
#             raise Exception("incorrect")
