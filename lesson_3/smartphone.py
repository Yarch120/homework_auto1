class Smartphone:
   
    def __init__(self, brand, model, number):
     self.brand = brand
     self.model = model
     self.number = number

    
    def Say_brand(self):
       print('Марка телефона', self.brand)
    
    def Say_model(self):
       print('Модель телефона', self.model)

    def Say_number(self):
       print('Номер телефона', self.number)