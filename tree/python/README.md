# stack implementation in python3

## implementation

### initialization

from stack import Stack

test_stack = Stack()

### api

peek, pop, push, get_size(), get_type()

### restrictions

raises a TypeError if mismatched types are pushed


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
collected 5 items                                                                               

test_stack.py .....                                                                       [100%]

---------- coverage: platform darwin, python 3.8.2-final-0 -----------
Name       Stmts   Miss  Cover   Missing
----------------------------------------
stack.py      29      0   100%
----------------------------------------
TOTAL         29      0   100%


======================================= 5 passed in 0.04s =======================================
```

## end to end testing
```
cd end-to-end/
pip3 install -r requirements.txt
cd ..
make etest
```

```
2 features passed, 0 failed, 0 skipped
4 scenarios passed, 0 failed, 0 skipped
17 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.002s
```
