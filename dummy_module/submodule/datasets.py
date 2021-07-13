import logging
import os
from abc import ABC, ABCMeta, abstractmethod
from functools import cache, wraps
from time import sleep
from pathlib import Path
from warnings import warn

RAWDATADIR = Path("~/.my_package/raw_data")
DATASETDIR = Path("~/.my_package/datasets")


class DatasetMetaClass(ABCMeta):
    """Meta Class for Datasets"""  # Some metaclass attribute.

    metaclass_attribute: str = "result"

    def __init__(cls, *args, **kwargs):
        r"""Initialize the paths such that every dataset class has them available BEFORE instantiation!."""
        super().__init__(*args, **kwargs)
        cls.url = None
        cls.rawdata_path = RAWDATADIR.joinpath(cls.__name__)
        # cls.rawdata_path.mkdir(parents=True, exist_ok=True)
        cls.dataset_path = DATASETDIR.joinpath(cls.__name__)
        # cls.dataset_path.mkdir(parents=True, exist_ok=True)
        cls.dataset_file = DATASETDIR.joinpath(cls.__name__ + ".h5")

    @property
    @cache
    def metaclass_property(cls):
        r"""Some metaclass property."""
        warn("Caching metaclass property...")
        return "result"

    def metaclass_function(cls):
        r"""Some metaclass function."""

    # def __dir__(cls):
    #     return list(super().__dir__()) + ['metaclass_property']


class DatasetBaseClass(metaclass=DatasetMetaClass):
    """Base Class for datasets that all datasets must subclass"""

    baseclass_attribute: str = "result"  # Some baseclass attribute.

    @classmethod
    @property
    @cache
    def baseclass_property(cls):
        r"""Some baseclass property."""
        if os.environ.get("GENERATING_DOCS", False):
            warn("cancelling execution due to 'GENERATING_DOCS' environment variable.")
            return
        warn("Caching baseclass property...")
        sleep(3)
        return "result"

    def baseclass_function(cls):
        r"""Some baseclass function."""

    @classmethod
    @abstractmethod
    def load(cls):
        r"""Load the dataset from disk into memory."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def download(cls):
        r"""Download the dataset from ``cls.url``."""
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def clean(cls):
        r"""Pre-process the raw dataset."""
        raise NotImplementedError


class DatasetExampleClass(DatasetBaseClass, metaclass=DatasetMetaClass):
    """One dataset. Since Datasets are"""

    url = "https://dataset_origin"

    @classmethod
    def load(cls):
        """Custom load function of the DatasetExampleClass."""
        pass

    @classmethod
    def download(cls):
        """Custom load function of the DatasetExampleClass."""
        pass

    @classmethod
    def clean(cls):
        """Custom clean function of the DatasetExampleClass."""
        pass


class A:
    @property
    def foo():
        pass


a = A()
assert "foo" in dir(a)  # fails
