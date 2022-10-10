
def test_pytest_installed():
    import pytest
    assert 1

## NODES
import miniflow as mf

import pytest

import typing


def test_node_creation():
    def add(x,y):
        return x + y
    node = mf.Node(id='hi', function=add)
    assert node


def test_node_add_children():
    node = mf.Node()
    node2 = mf.Node()
    node.add_child(node2)
    children = list(node.get_children())
    assert children[0] == node2

def test_node_dft():
    node1 = mf.Node(id='n1')
    node11 = mf.Node(id='n11')
    node12 = mf.Node(id='n12')
    node21 = mf.Node(id='n21')
    node1.add_child(node11)
    node1.add_child(node12)
    node11.add_child(node21)
    dft = node1.dft()
    assert isinstance(dft, typing.Generator)
    ordered = list(dft)
    assert ordered == [node1, node11, node21, node12]


def test_node_parents():
    node1 = mf.Node(id='n1')
    node11 = mf.Node(id='n11')
    node12 = mf.Node(id='n12')
    node21 = mf.Node(id='n21')
    node1.add_child(node11)
    node1.add_child(node12)
    node11.add_child(node21)
    ordered = list(node21.parents())
    assert ordered == [node21, node11, node1]

## Runner

def test_runner_basic():
    r = mf.Runner()
    def ten():
        return 10
    r.add(ten)
    res = r.run(ten)
    assert res == 10

def test_runner_basic2():
    r = mf.Runner()
    def ten():
        return 10
    def double(val):
        return val * 2
    r.add(double, ten) # double depends on ten
    res = r.run(double)
    assert res == 20

## Cache

def test_cache():
    @mf.cache
    def add(x,y):
        return x + y

    res = add(10, 20)
    assert res == 30
    res = add(40, 60)
    assert res == 30

## Depends

def test_depends_dec():
    r = mf.Runner()
    @mf.depends(runner=r)
    def ten():
        return 10

    @mf.depends(ten, runner=r)
    def double(result):
        return result * 2

    result = r.run(double)
    assert result == 20
