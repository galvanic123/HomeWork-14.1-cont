def test_smartphone_init(smartphone):             # type: ignore[no-untyped-def]
    assert smartphone.name == "Samsung Galaxy C23 Ultra"
    assert smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5
    assert smartphone.efficiency == "3.4 Ггц"
    assert smartphone.model == "Galaxy C23 Ultra"
    assert smartphone.memory == "256Gb"
    assert smartphone.color == "Серый"
