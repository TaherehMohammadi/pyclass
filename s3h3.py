#Tahereh Mohammadi - Thursday 14-18
#calculate area or primeter of a shape
def shape(name,what,var1,var2):
    if name=='rectangle' and what=='primeter':
        print(f'rectangle primeter={2*(var1+var2)}')
    elif name=='rectangle' and what=='area':
        print(f'rectangle area={var1*var2}')
    elif name=='triangle' and what=='primeter':
        print(f'triangle primeter={(var1+var2+(var1+var2)/2)}')
    elif name=='triangle' and what=='area':
        print(f'triangle areaa={(var1*var2)/2}')
    elif name=='circle' and what=='primeter':
        print(f'circle primeter={2*var1*var2}')
    elif name=='circle' and what=='area':
        print(f'circle areaa={var2*var1**2}')

shape('rectangle','primeter',12,10)
shape('rectangle','area',12,10)
shape('triangle','primeter',12,10)
shape('triangle','area',12,10)
shape('circle','primeter',12,3.14)
shape('circle','area',12,3.14)
