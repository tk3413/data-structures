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

## end to end testing
```
cd end-to-end/
pip3 install -r requirements.txt
cd ..
make etest
```
