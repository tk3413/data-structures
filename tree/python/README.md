# tree search implementations in python3

see the `tree.py` file to see binary search tree implementations in both recursive and iterative fashion.

see the `test_tree.py` file which covers preorder, inorder, and postorder results

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
pytest --cov-report term-missing --cov=tree test_tree.py
======================= test session starts =======================
platform darwin -- Python 3.8.9, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /Users/taimorekhan/code/data-structures/tree/python
plugins: cov-3.0.0
collected 5 items

test_tree.py .....                                          [100%]

---------- coverage: platform darwin, python 3.8.9-final-0 -----------
Name      Stmts   Miss  Cover   Missing
---------------------------------------
tree.py      33      0   100%
---------------------------------------
TOTAL        33      0   100%


======================== 5 passed in 0.05s ========================
```
