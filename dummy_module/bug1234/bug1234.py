import logging
from abc import ABC, ABCMeta, abstractmethod
from functools import cache, wraps
from pathlib import Path
from warnings import warn

RAWDATADIR = Path("~/.my_package/raw_data")
DATASETDIR = Path("~/.my_package/datasets")


class DatasetMetaClass(ABCMeta):
    """Meta Class for Datasets"""

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
        r"""Compute an expensive property (for example: dataset statistics)."""
        warn("Caching metaclass property...")
        return "result"

    # def __dir__(cls):
    #     return list(super().__dir__()) + ['metaclass_property']


class DatasetBaseClass(metaclass=DatasetMetaClass):
    """Base Class for datasets that all datasets must subclass"""

    @classmethod
    @property
    @cache
    def baseclass_property(cls):
        r"""Compute an expensive property (for example: dataset statistics)."""
        warn("Caching baseclass property...")
        return "result"

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
assert 'foo' in dir(a)  # fails


