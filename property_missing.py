from abc import ABC, ABCMeta


class MyMetaClass(ABCMeta):
    @property
    def metaclass_property(cls):
        return "result"

    # def __dir__(cls):
    #     return list(super().__dir__()) + ['metaclass_property']


class MyBaseClass(ABC, metaclass=MyMetaClass):

    def __new__(cls, *args, **kwargs):
        cls.baseclass_attribute = cls.__name__ + " is awesome"
        return super().__new__(cls, *args, **kwargs)

    @classmethod
    @property
    def baseclass_property(cls):
        return "result"


class MyClass(MyBaseClass, metaclass=MyMetaClass):
    pass


assert hasattr(MyClass, "baseclass_attribute")

assert MyClass.baseclass_property == "result"
assert hasattr(MyClass, 'baseclass_property')
assert 'baseclass_property' in dir(MyClass)

assert MyClass.metaclass_property == "result"
assert hasattr(MyClass, 'metaclass_property')
assert 'metaclass_property' in dir(MyClass)
