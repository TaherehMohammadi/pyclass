# Tahereh Mohammadi - Thursday 14-18
# making Class, Example 4

class Book:
    def __init__(self, name, btype, price, author, date):
        self.book_name = name
        self.book_type = btype
        self.book_price = price
        self.book_author = author
        self.pubdate = date
        self.inventory_qty = 1000
    def __str__(self):
        return f'"{self.book_name}" is a {self.book_type} book.'
    def sale_order(self):
                sale_qty = int(input('How many books would you like to order? '))
                if self.inventory_qty < sale_qty:
                    print('Sorry, the book is finished.')
                else:
                    self.inventory_qty = self.inventory_qty - sale_qty
                    return f'inventory of {self.book_name}= {self.inventory_qty}'

the_dancing_univerce = Book('The dancing univerce', 'scientific', 32000, 'Gleiser Marcelo', 1997)
rock_spring = Book('Rock Spring', 'novel', 28000, 'Richard Ford', 2018)

print(the_dancing_univerce)
print(the_dancing_univerce.book_type, the_dancing_univerce.book_price, sep=', ')
print(the_dancing_univerce.book_price)
the_dancing_univerce.sale_order()
print(the_dancing_univerce.inventory_qty)
the_dancing_univerce.sale_order()
print(the_dancing_univerce.inventory_qty)
print('------------------------')
print(rock_spring)
print(rock_spring.book_author)
rock_spring.sale_order()
print(rock_spring.inventory_qty)
print('------------------------')