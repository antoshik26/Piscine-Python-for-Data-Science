import re
import pytest
from financial import 

@pytest.fixture
def total_revenue():
    return get_row('MSFT', 'Total Revenue')

def test_invalid_row():
    with pytest.raises(ValueError, match='row does not exist'):
        get_row('MSFT', 'abcdef')


def test_return_type(total_revenue):
    assert isinstance(total_revenue, tuple)
	
def test_return_len(total_revenue):
    assert len(total_revenue) == 6