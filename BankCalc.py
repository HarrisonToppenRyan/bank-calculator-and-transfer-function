h = input('Enter number of hours: ')
r = input('Enter rate earned per hour: ')
p = float(h)*float(r)
Pay = p - (0.14 * p)

print(float(Pay))