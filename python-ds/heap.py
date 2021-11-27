import random
import unittest


class Heap:

    def __init__(self, **kwargs):
        self.list = []
        self.sortkey = kwargs.get("sortkey", lambda x: x)

    def insert(self, new_item):
        self.list.append(new_item)
        self.__float_up(self.__last_index())

    def peek(self):
        return self.list[0]

    def pop(self):
        self.__swap(0, self.__last_index())
        popped = self.list.pop()
        self.__bubble_down(0)
        return popped

    def remove(self, item):
        idx_to_remove = self.__find_index(item)
        if idx_to_remove is None:
            return False
        self.__swap(idx_to_remove, self.__last_index())
        self.list.pop()
        self.__float_up(idx_to_remove)
        return True

    def __len__(self):
        return len(self.list)

    def __find_index(self, item):
        return self.__find_index_recursive(item, self.sortkey(item), 0)

    def __find_index_recursive(self, item, itemkey, idx):
        while idx < len(self.list):
            crt = self.list[idx]
            if crt == item:
                return idx
            if self.sortkey(crt) > itemkey:
                return None

            lidx = self.__left_child(idx)
            ridx = self.__right_child(idx)
            return self.__find_index_recursive(item, itemkey, lidx) or self.__find_index_recursive(item, itemkey, ridx)

        return None

    def __float_up(self, idx):
        if idx > self.__last_index():
            # This can happen after removing the last item
            return
        if idx == 0:
            self.__bubble_down(idx)
            return

        parent_idx = self.__parent(idx)
        parent = self.list[parent_idx]
        crt = self.list[idx]
        if self.sortkey(parent) <= self.sortkey(crt):
            self.__bubble_down(idx)
            return

        self.__swap(idx, parent_idx)
        self.__float_up(parent_idx)

    def __bubble_down(self, idx):
        lidx = self.__left_child(idx)
        ridx = self.__right_child(idx)

        if lidx > self.__last_index():
            return
        l = self.list[lidx]
        crt = self.list[idx]

        if ridx > self.__last_index():
            if self.sortkey(crt) <= self.sortkey(l):
                return
            else:
                self.__swap(idx, lidx)
        else:
            r = self.list[ridx]
            scrt, sl, sr = [self.sortkey(x) for x in [crt, l, r]]

            if scrt <= sl and scrt <= sr:
                return

            if scrt <= sl and scrt > sr:
                self.__swap(idx, ridx)
                self.__bubble_down(ridx)
                return

            if scrt > sl and scrt <= sr:
                self.__swap(idx, lidx)
                self.__bubble_down(lidx)
                return

            if scrt > sl and scrt > sr:
                if sl < sr:
                    self.__swap(idx, lidx)
                    self.__bubble_down(lidx)
                    return
                else:
                    self.__swap(idx, ridx)
                    self.__bubble_down(ridx)
                    return

    def __swap(self, idx1, idx2):
        self.list[idx1], self.list[idx2] = self.list[idx2], self.list[idx1]

    def __last_index(self):
        return len(self.list) - 1

    def __left_child(self, idx):
        return idx * 2 + 1

    def __right_child(self, idx):
        return idx * 2 + 2

    def __parent(self, idx):
        if idx % 2 == 0:
            return (idx - 2) // 2
        else:
            return (idx - 1) // 2


class Tests(unittest.TestCase):

    def test_min_heap_by_default(self):
        h = Heap()

        h.insert(5)
        h.insert(3)

        self.assertEqual(h.peek(), 3)
        self.assertEqual(h.pop(), 3)
        self.assertEqual(h.peek(), 5)

    def test_random_stuff(self):
        rnums = [random.randint(1, 1000000) for _ in range(100)]
        snums = sorted(rnums)

        h = Heap()
        for r in rnums:
            h.insert(r)

        for n in snums:
            self.assertEqual(h.pop(), n)

    def test_random_stuff_maxheap(self):
        rnums = [random.randint(1, 1000000) for _ in range(100)]
        snums = sorted(rnums, key = lambda x: -x)

        h = Heap(sortkey = lambda x: -x)
        for r in rnums:
            h.insert(r)

        for n in snums:
            self.assertEqual(h.pop(), n)

    def test_remove_specific_item(self):
        h = Heap(sortkey = lambda x: x[0])
        h.insert((5, "item1"))
        h.insert((4, "item2"))
        h.insert((4, "item3"))

        self.assertEqual(3, len(h))
        self.assertFalse(h.remove((5, "item0")))
        self.assertTrue(h.remove((5, "item1")))
        self.assertFalse(h.remove((6, "item1")))
        self.assertEqual(2, len(h))

        self.assertEqual(h.peek(), (4, "item2"))
        result = h.remove((4, "item2"))
        self.assertTrue(result)
        self.assertEqual(h.peek(), (4, "item3"))

    def test_remove_last_item(self):
        h = Heap()
        h.insert(1)
        h.insert(2)
        h.remove(2)


unittest.main()
