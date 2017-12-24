from server.garage import Garage
import pytest

@pytest.mark.parametrize('garage_id, owner, admins, vehicles', [
    ('1', '1', '1', '1')
])
def test_garage_init(garage_id, owner, admins, vehicles):
    obj = Garage(garage_id, owner, admins, vehicles)
    assert isinstance(obj, Garage)
