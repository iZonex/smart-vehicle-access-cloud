from server.tokens import VehicleToken
import datetime
import pytest


@pytest.mark.parametrize('user_id', 'vehicle_id', 'expired', [
    ('1', '1', datetime.datetime.now())
])
def test_vehicle_token_init(user_id, vehicle_id, expired):
    obj = VehicleToken(user_id, vehicle_id, expired)
    assert isinstance(obj, VehicleToken)
