import pytest
import random
from base import Library


@pytest.fixture
def library():
    address = 'Sadova, 14'
    helmet = random.choice(['Musienko', 'Kox'])
    return Library(address, helmet=helmet)









