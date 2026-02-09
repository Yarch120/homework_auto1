class Address:
   
    def __init__(self, index, town, street, house, apartment):
     self.index = index
     self.town = town
     self.street = street
     self.house = house
     self.apartment = apartment

    
    def Say_index(self):
       print('Индекс', self.index)
    
    def Say_town(self):
       print('Город', self.town)

    def Say_street(self):
       print('Улица', self.street)
    
    def Say_house(self):
       print('Дом', self.house)

    def Say_apartment(self):
       print('Кватира', self.apartment)   