import json


class AdvertAtr:
    def __init__(self, data) -> None:
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, AdvertAtr(value))
            else:
                setattr(self, key, value)
        return None


class ColorizeMixin():
    repr_color_code = 33  # green

    def __repr__(self):
        return f"\033[1;31;40m {self.title} | {self.price} ₽\033[0;0;0m"


class Advert(ColorizeMixin, AdvertAtr):
    def __init__(self, data) -> None:
        super().__init__(data)
        if hasattr(self, 'price'):
            if self.price < 0:
                raise ValueError('Price must be >= 0')
        else:
            self.price = 0


if __name__ == "__main__":
    lesson_str = """{
    "title": "python",
    "price": 10,
    "location": {
    "address": "город Москва, Лесная, 7",
    "metro_stations": ["Белорусская"]
    }
    }"""
    lesson = json.loads(lesson_str)
    item = Advert(lesson)
    print(item.location.address)
    print(item.location.metro_stations)
    print(item.price)
    print(item)

    # no price

    lesson_str = """{
    "title": "python",
    "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
                }
    }"""
    lesson = json.loads(lesson_str)
    item = Advert(lesson)
    print(item.price)

    # price < 0

    lesson_str = """{
    "title": "python",
    "price": - 10,
    "location": {
                "address": "город Москва, Лесная, 7",
                "metro_stations": ["Белорусская"]
                }
    }"""
    # lesson = json.loads(lesson_str)
    # item = Advert(lesson)
    # print(item.price)

    iphone_str = """
    {
    "title": "iPhone X",
    "price": 100,
    "location": {
                "address": "город Самара, улица Мориса Тореза, 50",
                "metro_stations": ["Спортивная", "Гагаринская"]
                }
    }"""
    iphone = json.loads(iphone_str)
    item = Advert(iphone)
    print(item.location.metro_stations)
    print(item)
