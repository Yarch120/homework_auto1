from Address import Address
from Mailing import Mailing

to_address = Address(
    index="123456",
    town="Москва",
    street="Ленина",
    house="10",
    apartment="15")


from_address = Address(
    index="654321",
    town="Санкт-Петербург",
    street="Пушкина",
    house="5",
    apartment="3")

NewMailing = Mailing(to_address=to_address, from_address=from_address, cost=1000, track='TRK125')

print(f"Отправление {NewMailing.track} из {NewMailing.from_address.index}, {NewMailing.from_address.town}, {NewMailing.from_address.street}, {NewMailing.from_address.house} - {NewMailing.from_address.apartment} в {NewMailing.to_address.index}, {NewMailing.to_address.town}, {NewMailing.to_address.street}, {NewMailing.to_address.house} - {NewMailing.to_address.apartment}. Стоимость {NewMailing.cost} рублей.")