def test_category_str(first_category):             # type: ignore[no-untyped-def]
   assert str(first_category) == "Category1, количество продуктов: 44 шт."


def test_middle_price(category1):           # type: ignore[no-untyped-def]
   assert category1.middle_price() == 140333.33
