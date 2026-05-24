import pytest
from iotest import harness

@pytest.mark.parametrize("case", harness.find_cases())
def test_contacts_app(case):
    harness.execute(case)