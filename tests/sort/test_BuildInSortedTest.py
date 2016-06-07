from tests.sort.base_sort import BaseSortTestCase


class QuickBaseSortTestCase(BaseSortTestCase):
    def test_build_in_sorted(self):
        self.loop(sorted, self.data)

    def test_build_in_sorted_worst(self):
        self.loop(sorted, self.reverse_data)
