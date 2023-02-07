import pytest
def test_demo1():
    a=10
    b=20
    assert a!=b
def test_demo2():
    name="hcl"
    text="hcl is located all over India"
    assert name in text
test_demo1()
test_demo2()