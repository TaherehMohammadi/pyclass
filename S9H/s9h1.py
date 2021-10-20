# Tahereh Mohammadi - Thursday 14-18
# making Class, Example 1

class SparePart:
    def __init__(self, name, vendor, part, serial):
        self.unit_name = name
        self.vendor = vendor
        self.part_number = part
        self.serial_number = serial
        self.unit_status_i = -1
    def __str__(self):
        return f'The requested unit is {self.unit_name}:{self.part_number}'
    def unit_status(self):
        process = ['Received', 'Repaired', 'Delivered']
        self.unit_status_i = self.unit_status_i + 1
        return process[self.unit_status_i]

unit1 = SparePart('FlatPack','Nokia', 'CS7213300', '8M050271057')
unit2 = SparePart('RUS 01 B8', 'Ericsson','KRC11862/1', 'CC46854710')
unit3 = SparePart('UPBA0', 'Huawei', '03053404', '210305340410EB000410')

print(unit1.unit_name, unit2.unit_name, unit3.unit_name, sep='-')
print('---------------------------------')
print(unit2)
unit2.unit_status()
print(f'Its status is:{unit2.unit_status()}')
print('---------------------------------')
print(unit1)
unit1.unit_status()
unit1.unit_status()
print(f'Its status is:{unit1.unit_status()}')
print('---------------------------------')
print(unit3)
print(f'Its status is:{unit3.unit_status()}')
print('---------------------------------')

