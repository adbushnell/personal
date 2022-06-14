# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:17:59 2020

@author: Albert Tran
"""


# %% -------------------------------------------------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------------------------------------------------
import sys
sys.path.append('..')

import toy_datasets
import pytest


# %% -------------------------------------------------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------------------------------------------------
@pytest.fixture()
def resource():
    '''
    General setup to create a dataset of 20 positive and 20 negative examples
    '''
    # Setup
    data = toy_datasets.ring.get_data(20)
    
    # Return the result for the test
    yield data
    
    # Teardown
    print('Teardown')
    
    
def test_data_format(resource):
    assert resource.shape == (40,3)
    assert 'x1' in resource.columns
    assert 'x2' in resource.columns
    assert 'y'  in resource.columns


def test_data_labels(resource):
    '''
    Tests that the dataset generated was balanced.
    '''
    assert resource['y'].sum() == 20










