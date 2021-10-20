# Tahereh Mohammadi - Thursday 14-18
# making Class, Example 2

class Laptop:
    def __init__(self, brand, model, screen, processor, ram, hard):
        self.brand = brand
        self.model = model
        self.screen_size = screen
        self.processor = processor
        self.RAM_size = ram
        self.hard_size = hard
    def __str__(self):
        return f'My laptop is {self.brand}: {self.model}.'
    def upgrade_hard(self):
        upgraded_hard_size = input('enter the size of hard you want to added:')
        self.hard_size = f'{self.hard_size} + {upgraded_hard_size}'
        return self.hard_size


my_laptop = Laptop('ASUS', 'R545F', '15.6"', 'core i7', '12GB', '1TB')
print(my_laptop)
Laptop.upgrade_hard(my_laptop)
Laptop.upgrade_hard(my_laptop)
Laptop.upgrade_hard(my_laptop)
print(my_laptop.hard_size)