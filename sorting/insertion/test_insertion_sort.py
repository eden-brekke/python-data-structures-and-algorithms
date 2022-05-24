from insertion_sort import insertion_sort

list_a = [3, 7, 1]
list_b = [72, 63, 15]
list_c = [4, 8, 52, 23, 68, 24, 9, 100, 78, 42, 392, 19928, 576, 90]
list_d = [2, 2, 2, 10, 1, 3]
list_e = [-2, -3, 24, 38]


def test_insertion_sort_exists():
  assert insertion_sort


def test_sort_random_assortment():
  actual = insertion_sort(list_a)
  expected = [1, 3, 7]
  assert actual == expected


def test_sort_descending():
  actual = insertion_sort(list_b)
  expected = [15, 63, 72]
  assert actual == expected


def test_sort_of_large_list():
  actual = insertion_sort(list_c)
  expected = [4, 8, 9, 23, 24, 42, 52, 68, 78, 90, 100, 392, 576, 19928]
  assert actual == expected


def test_duplicate_value():
  actual = insertion_sort(list_d)
  expected = [1, 2, 2, 2, 3, 10]
  assert actual == expected


def test_negative_values():
  actual = insertion_sort(list_e)
  expected = [-3, -2, 24, 38]
  assert actual == expected
