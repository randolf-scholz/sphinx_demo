class A:
    @property
    def foo():
        return None


assert 'foo' in dir(A)  # fails
assert 'foo' in dir(A())  # fails
assert 'goo' in dir(A())  # fails
