def conversion(hell):
    decimal, i = 0, 0
    while(hell != 0):
        dec = hell % 10
        decimal = decimal + dec * pow(2, i)
        hell = hell//10
        i += 1
    print(decimal)

if __name__ == '__main__':
    conversion(10111010)
