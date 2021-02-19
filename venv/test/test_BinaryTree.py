import os
import pytest
import json

import sys
sys.path.insert(1, '../src')

import binaryTree

testCounter=0
VALUE_LIST = "VALUE_LIST"
values = '{"values":[9,4,8,1,3,6,7,2,5,10,0]}'

"""
Fixtures: a prime example of dependency injection
Fixtures allow test functions to easily receive and work against
specific pre-initialized application objects without having to 
care about import/setup/cleanup details. It’s a prime example 
dependency injection where fixture functions take the role of 
the injector and test functions are the consumers of fixture 
objects.
"""

@pytest.fixture(scope="module")
def bintree():
    if testCounter == 0:
        os.putenv(VALUE_LIST, '{"values":[9,4,8,1,3,6,7,2,5,10,0]}')
    elif testCounter == 1:
        os.putenv(VALUE_LIST, '{"values":[{}, {}, {}, {}, {} 3 '
                              ''
                              '    ]}')

def test_binaryTree(monkeypatch):
    monkeypatch.setenv(VALUE_LIST, values)
    valueList = os.getenv(VALUE_LIST)

    bt = binaryTree.BinaryTree()
    bt.buildTree()
    valueList = json.loads(valueList)["values"]
    bt.printTree(bt.getRoot())
    valueList.sort()
    assert(bt.sorted == valueList)

def test_noneListException(monkeypatch):
    with pytest.raises(Exception):
        bt = binaryTree.BinaryTree()

def test_treeHeight(monkeypatch):
    monkeypatch.setenv(VALUE_LIST, values)
    valueList = os.getenv(VALUE_LIST)

    bt = binaryTree.BinaryTree()
    bt.buildTree()
    treeHeight = bt.treeHeight(bt.getRoot())
    assert treeHeight == 5


"""   
                        9
                4           10
           1        8             
        0      3   6
           2     5       7
                

"""