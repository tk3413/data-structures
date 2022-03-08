# sorting implementations in python3

see the `sort.py` file to see different sort implementations in python

see the `test_tree.py` file to see that the implementation matches the output produced by the builtin sort function

## dependency management
```
python3 -m virtualenv venv
source venv/bin/activate
```

## unit testing
```
pip3 install -r requirements.txt
make test
```

```
pytest --cov-report term-missing --cov=sort test_sort.py -v
================================= test session starts =================================
platform darwin -- Python 3.8.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0 -- /Users/taimorekhan/code/data-structures/stack/python/venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/taimorekhan/code/data-structures/sort/python
plugins: cov-3.0.0
collected 4 items

test_sort.py::test_merge_sort PASSED                                            [ 25%]
test_sort.py::test_builtin_sort PASSED                                          [ 50%]
test_sort.py::test_divide_list PASSED                                           [ 75%]
test_sort.py::test_get_mid PASSED                                               [100%]

---------- coverage: platform darwin, python 3.8.9-final-0 -----------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
sort.py      34      0   100%
---------------------------------------
TOTAL        34      0   100%


================================== 4 passed in 0.04s ==================================
```
