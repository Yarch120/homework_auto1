class User:
   
    def __init__(self, first_name, last_name):
     self.f_name = first_name
     self.l_name = last_name
    
    def Say_name(self):
       print('Ваше имя', self.f_name)
    
    def Say_surname(self):
       print('Ваша фамилия', self.l_name)

    def Say_fullname(self):
       print('Вас зовут', self.f_name, self.l_name)

