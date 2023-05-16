
try:
    r = int(input('Enter rate '))
    h = int(input('Enter hours '))
    if h > 40:
        pay = float(1.5 * r * h)
    else:
        pay = float(h * r)
    print(pay)
except:
    print('Error, please, enter numeric input')
