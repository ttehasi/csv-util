from pathlib import Path

from csv_project.utils import make_table, processing, unite


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_unite():
  file1 = get_test_data_path('products1.csv')
  file2 = get_test_data_path('products2.csv')
  expect = [['apple', '4.9'], ['samsung', '4.8'],
            ['xiaomi', '4.6'], ['apple', '4.7'],
            ['samsung', '4.2'], ['xiaomi', '4.4'],
            ['apple', '4.1'], ['samsung', '4.6'],
            ['xiaomi', '4.1'], ['apple', '4.5']
          ]
  assert unite([file1, file2]) == expect
  
  
def test_processing():
  file1 = get_test_data_path('products1.csv')
  file2 = get_test_data_path('products2.csv')
  unite_data = unite([file1, file2])
  expect = [['apple', 4.55], ['samsung', 4.533333333333333],
            ['xiaomi', 4.366666666666666]]
  assert processing(unite_data) == expect
  
  
def test_make_table():
  file1 = get_test_data_path('products1.csv')
  file2 = get_test_data_path('products2.csv')
  unite_data = unite([file1, file2])
  process_data = processing(unite_data)
  expect = '''+----+---------+----------+
|    | brand   |   rating |
+====+=========+==========+
|  1 | apple   |     4.55 |
+----+---------+----------+
|  2 | samsung |     4.53 |
+----+---------+----------+
|  3 | xiaomi  |     4.37 |
+----+---------+----------+'''
  assert make_table(process_data) == expect
