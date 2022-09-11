import unittest

def kmp_compute_prefixes(needle):
    prefs = [-1 for s in needle]
    j = 0
    i = 1
    while i < len(needle):
        if needle[i] == needle[j]:
            prefs[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = prefs[j-1] + 1
        else:
            i += 1
    return prefs

def kmp_contains(haystack, needle):
    prefs = kmp_compute_prefixes(needle)
    i = 0
    j = 0
    while i < len(haystack):
        if haystack[i] == needle[j]:
            if j == len(needle) - 1:
                return True
            i += 1
            j += 1
        elif j > 0:
            j = prefs[j - 1] + 1
        else:
            i += 1
    return False

class Tests(unittest.TestCase):

    def test_min_heap_by_default(self):
        self.assertEqual(kmp_compute_prefixes("ab"), [-1, -1])
        self.assertEqual(kmp_compute_prefixes("abababca"), [-1, -1, 0, 1, 2, 3, -1, 0])
        self.assertEqual(kmp_compute_prefixes("aaaa"), [-1, 0, 1, 2])
        self.assertEqual(kmp_compute_prefixes("ababababa"), [-1, -1, 0, 1, 2, 3, 4, 5, 6])

    def test_kmp_contains(self):
        self.assertTrue(kmp_contains("ababaca", "baca"))
        self.assertFalse(kmp_contains("ababaca", "baxa"))

    def test_kmp_contains_performance(self):
        haystack = "ab" * 1_000_000 + "x"
        needle = "ab" * 500_000 + "x"
        self.assertTrue(kmp_contains(haystack, needle))

        haystack = "ab" * 1_000_000 + "x"
        needle = "ab" * 500_000 + "y"
        self.assertFalse(kmp_contains(haystack, needle))
unittest.main()
