#Tahereh Mohammadi - Thursday 14-18
#calculate area and volume of a shape

def sphere_area(pi,radius):
    area=round(4*pi*(radius**2),2)
    return area

def sphere_volume(pi,radius):
    volume=round((4/3)*pi*(radius**3),2)
    return volume

def cube_area(length,width,height):
    area=round(2*(length*width+length*height+width*height),2)
    return area

def cube_volume(length,width,height):
    volume=round(length*width*height,2)
    return volume

def cone_area(pi,radius,height):
    area=round((pi*radius**2)+(pi*radius*(radius**2+height**2)**(1/2)),2)
    return area

def cone_volume(pi,radius,height):
    volume=round((1/3)*pi*(radius**2)*height,2)
    return volume

shape=input('enter the name of shape (sphere,cube,cone) :\n')
selection=input('volume or area?\n')
pi=3.14
if shape=='sphere':
    radius=float(input('enter the radius in cm:\n'))
    if selection=='area':
        print(f'\narea={sphere_area(pi,radius)}')
    elif selection=='volume':
        print(f'\narea={sphere_volume(pi,radius)}')
elif shape=='cube':
    length=float(input('enter the length in cm?\n'))
    width=float(input('enter the width in cm?\n'))
    height=float(input('enter the height in cm?\n'))
    if selection=='area':
        print(f'\narea={cube_area(length,width,height)}')
    elif selection=='volume':
        print(f'\narea={cube_volume(length,width,height)}')
elif shape=='cone':
    radius=float(input('enter the radius in cm:\n'))
    height=float(input('enter the height in cm:\n'))
    if selection=='area':
        print(f'\narea={cone_area(pi,radius,height)}')
    elif selection=='volume':
        print(f'\nvolume={cone_volume(pi,radius,height)}')
