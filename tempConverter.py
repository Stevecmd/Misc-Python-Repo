def convert_to_fahrenheit(celsius):
    c = float(celsius)
    f = round(c * 9 / 5 + 32,2)
    print (f'\n{c} Celsius converted is: {f} Fahrenheit.')


def convert_to_celsius(fahrenheit):
    f = float(fahrenheit)
    c = round((f - 32) * 5 / 9,2)
    print (f'\n{f} Fahrenheit converted is: {c} Celsius.')



def convert():
    user_input = input('From what do you want to convert?: Celsius or Fahrenheit ')

    if user_input == 'Celsius' or 'C' or 'c' or 'celsius':
        print ('To convert a temperature from Celsius to Fahrenheit:')
        celsius = input('CELSIUS: ')
        convert_to_fahrenheit(celsius)

    elif user_input == 'Fahrenheit' or 'F' or 'f' or 'fahrenheit':
        print ('To convert a temperature from Fahrenheit to Celsius:')
        fahrenheit = input('FAHRENHEIT: ')
        convert_to_celsius(fahrenheit)
        
convert()