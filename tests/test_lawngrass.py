def test_lawngrass_init(lawngrass):
    assert lawngrass.name == "Lawngrass"
    assert lawngrass.description == "Lawngrass small size"
    assert lawngrass.price == 1500.0
    assert lawngrass.quantity == 5
    assert lawngrass.country == "Russia"
    assert lawngrass.germination_period == "2 month"
    assert lawngrass.color == "Зелёный"