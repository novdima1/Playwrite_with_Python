import pytest


@pytest.fixture
def input(a=3, b=4):
    return a, b


@pytest.fixture(scope="function")
def greeting(input):
    print(f"\n Hi, calculate this values: {input}")
    yield


@pytest.mark.usefixtures('greeting')
def test_plus(input):
    a = input[0]
    b = input[1]
    print(f"\n{a} + {b} =", a + b)
    return a + b


@pytest.mark.usefixtures('greeting')
def test_minus(input):
    a = input[0]
    b = input[1]
    print(f"\n{a} - {b} =", a - b)
    return a - b

@pytest.mark.usefixtures('greeting')
def test_mult(input):
    a = input[0]
    b = input[1]
    print(f"\n{a} * {b} =", a * b)
    return a * b

@pytest.mark.usefixtures('greeting')
def test_div(input):
    a = input[0]
    b = input[1]
    print(f"\n{a} / {b} =", a / b)
    return a / b
