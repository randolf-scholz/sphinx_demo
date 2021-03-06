from abc import ABCMeta, abstractmethod
from pathlib import Path
from time import sleep
from warnings import warn

RAWDATADIR = Path("~/.my_package/raw_data")
DATASETDIR = Path("~/.my_package/datasets")


class MetaClass(ABCMeta):
    """Meta Class."""

    metaclass_attribute: str = "result"  #: Some metaclass attribute.

    def __init__(cls, *args, **kwargs):
        r"""Initialize the paths such that every dataset class has them available BEFORE instantiation!."""
        super().__init__(*args, **kwargs)
        cls.dynamic_class_attribute: str = "dynamic_class_attribute"  # Some dynamic_class_attribute.

    # def __dir__(cls):
    #     return list(super().__dir__()) + ['metaclass_property']

    @classmethod
    @property
    def metaclass_class_property(mcs):
        r"""Some metaclass metaclass_class_property."""
        warn("Caching metaclass_class_property")
        return "metaclass_class_property"

    @classmethod
    def metaclass_classmethod(mcs):
        r"""Some classmethod."""
        return "metaclass_classmethod"

    @property
    def metaclass_property(cls):
        r"""Some metaclass_property."""
        warn("Caching metaclass_property")
        return "metaclass_property"

    def metaclass_method(cls):
        r"""Some method."""
        return "metaclass_method"

    @staticmethod
    def metaclass_static_method():
        r"""Some static metaclass method."""
        return "metaclass_static_method"


class BaseClass(metaclass=MetaClass):
    """Base Class all classes should subclass."""

    baseclass_attribute: str = "result"  #: Some baseclass attribute.
    dynamic_class_attribute: str
    """Docstring for dynamic_class_attribute"""

    @classmethod
    @property
    def baseclass_class_property(cls):
        r"""Some baseclass_class_property."""
        warn("Caching baseclass_class_property")
        return "baseclass_class_property"

    @classmethod
    def baseclass_classmethod(cls):
        r"""Some classmethod."""
        return "baseclass_classmethod"

    @property
    def baseclass_property(self):
        r"""Some baseclass_property."""
        warn("Caching baseclass_property")
        sleep(3)
        return "baseclass_property"

    def baseclass_method(self):
        r"""Some method."""
        return "baseclass_method"

    @staticmethod
    def baseclass_static_method():
        r"""Some static baseclass method."""
        return "baseclass_static_method"


class SubClass(BaseClass, metaclass=MetaClass):
    """One dataset. Since Datasets are"""

    subclass_attribute: str = "result"  #: Some subclass attribute.
    dynamic_class_attribute: str
    """Docstring for dynamic_class_attribute"""

    @classmethod
    @property
    def subclass_class_property(cls):
        r"""Some subclass_class_property."""
        warn("Caching subclass_class_property")
        return "subclass_class_property"

    @classmethod
    def subclass_classmethod(cls):
        r"""Some classmethod."""
        return "subclass_classmethod"

    @property
    def subclass_property(self):
        r"""Some subclass_property."""
        warn("Caching subclass_property")
        sleep(3)
        return "subclass_property"

    def subclass_method(self):
        r"""Some method."""
        return "subclass_method"

    @staticmethod
    def subclass_static_method():
        r"""Some static subclass method."""
        return "subclass_static_method"

