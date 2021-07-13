r"""Testing of Base Dataset."""

import logging
from copy import copy
from warnings import warn

from dummy_module import DatasetBaseClass, DatasetMetaClass, DatasetExampleClass

logger = logging.getLogger(__name__)


def test_datasetbaseclass():
    pass


def test_datasetmetaclass():
    pass


def test_DatasetExampleClass():
    r"""Test if all attributes are present."""

    attrs = {
        '__dir__',
        'url',
        'metaclass_property',
        'baseclass_property',
        'rawdata_path',
        'dataset_path',
        'dataset_file',
        'load',
        'download',
        'clean',
    }

    base_attrs = set(dir(DatasetExampleClass))

    if not attrs <= base_attrs:
        warn(f"{attrs - base_attrs} missing from DatasetExampleClass!")

    assert hasattr(DatasetExampleClass, 'url')
    assert hasattr(DatasetBaseClass, 'metaclass_property')
    assert hasattr(DatasetBaseClass, 'baseclass_property')
    assert hasattr(DatasetExampleClass, 'rawdata_path')
    assert hasattr(DatasetExampleClass, 'dataset_path')
    assert hasattr(DatasetExampleClass, 'dataset_file')
    assert hasattr(DatasetExampleClass, 'load')
    assert hasattr(DatasetExampleClass, 'download')
    assert hasattr(DatasetExampleClass, 'clean')
    assert DatasetExampleClass.metaclass_property == "result"
    assert DatasetExampleClass.baseclass_property == "result"


def test_DatasetBaseClass():
    r"""Test if all attributes are present."""

    attrs = {
        '__dir__',
        'url',
        'metaclass_property',
        'baseclass_property',
        'rawdata_path',
        'dataset_path',
        'dataset_file',
        'load',
        'download',
        'clean',
    }

    base_attrs = set(dir(DatasetBaseClass))
    if not attrs <= base_attrs:
        warn(f"{attrs - base_attrs} missing from DatasetBaseClass!")

    assert hasattr(DatasetBaseClass, 'url')
    assert hasattr(DatasetBaseClass, 'metaclass_property')
    assert hasattr(DatasetBaseClass, 'baseclass_property')
    assert hasattr(DatasetBaseClass, 'rawdata_path')
    assert hasattr(DatasetBaseClass, 'dataset_path')
    assert hasattr(DatasetBaseClass, 'dataset_file')
    assert hasattr(DatasetBaseClass, 'load')
    assert hasattr(DatasetBaseClass, 'download')
    assert hasattr(DatasetBaseClass, 'clean')
    assert DatasetBaseClass.metaclass_property == "result"
    assert DatasetBaseClass.baseclass_property == "result"


if __name__ == "__main__":
    test_DatasetBaseClass()
    test_DatasetExampleClass()
