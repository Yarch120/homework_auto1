from smartphone import Smartphone

smartphone1 = Smartphone("Samsung", "Galaxy S22", "+79123456789")
smartphone2 = Smartphone("Apple", "iPhone 14", "+79234567890")
smartphone3 = Smartphone("Xiaomi", " Redmi Note 10", "+79325678901")
smartphone4 = Smartphone("Huawei", "P40 Pro", "+79426789012")
smartphone5 = Smartphone("OnePlus", "OnePlus 10 Pro", "+79527890123")

catalog = [smartphone1, smartphone2, smartphone3, smartphone4, smartphone5]


for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}.")