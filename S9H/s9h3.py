# Tahereh Mohammadi - Thursday 14-18
# making Class, Example 3

class MobilePhone:
    def __init__(self, brand, model, network, simcard, storage, ram):
        self.brand = brand
        self.model = model
        self.network_support = network
        self.qty_simcard = simcard
        self.storage = storage
        self.ram_size = ram
    def __str__(self):
        return f'This mobile is {self.brand}: {self.model}'

tahereh_mobile = MobilePhone('Huawei', 'VTR-L29', '2G/3G/4G', '2 SIM', '64GB', '4GB')
majid_mobile = MobilePhone('Samsung', 'Galaxy A12', '2G/3G/4G', '1 SIM', '64GB', '4GB')

print(tahereh_mobile,'and storage=',tahereh_mobile.storage)
print(majid_mobile,'and RAM=',majid_mobile.ram_size)
print(majid_mobile, ':',majid_mobile.network_support)
print(tahereh_mobile,tahereh_mobile.storage,tahereh_mobile.ram_size, sep=' : ')