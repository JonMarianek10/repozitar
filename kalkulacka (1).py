import math

print('Pythagorova věta, kvadratická rovnice, prvočísla nebo obdélník?')
odpoved = input()

if odpoved == 'pythagorova věta':
    print('Délka delší strany?')
    num = int(input())
    print('Délka kratší strany?')
    num2 = int(input())
    def pythagorovaveta(num, num2):
        list = []
        print('Chcete zjistit délku přepony (zadejte p) nebo odvěsny (zadejte o)?')
        x = input()
        if x == 'o':
            r = round((math.sqrt((float(num)**2) - (float(num2)**2))), 5)
            list.append(r)
        elif x == 'p':
            r = round((math.sqrt((float(num)**2) + (float(num2)**2))), 5)
            list.append(r)
        print(list)
    pythagorovaveta(num, num2)

elif odpoved == 'kvadratická rovnice':
    print('ax² + bx + c = 0')
    print('Zadejte hodnotu konstanty a.')
    a = input()
    print('Zadejte hodnotu konstanty b.')
    b = input()
    print('Zadejte hodnotu konstanty c.')
    c = input()
    def rovnice(a, b, c):
        list = []
        if float(a) == 0:
            list.append('Rovnice není kvadratická.')
            if float(b) == 0:
                if float(c) == 0:
                    list.append('Evidentní pravda.')
                else:
                    list.append('Evidentní nepravda.')
            else:
                x = (0-float(c))/b
                list.append(x)

        else:
            D = (float(b)**2) - 4*float(a)*float(c)
            if D < 0:
                list.append('Rovnice nemá řešení.')

            elif D == 0:
                x = (0-float(b))/(2*float(a))
                list.append(x)

            elif D > 0:
                x1 = ((0-float(b))+(float(D)**(1/2)))/(2*float(a))
                x2 = ((0-float(b))-(float(D)**(1/2)))/(2*float(a))
                list.append(x1)
                list.append(x2)
        print(list)
    rovnice(a,b,c)

elif odpoved == 'prvočísla':
    print('Zadejte číslo.')
    hornihranice = int(input())

    def prvocisla(hornihranice):
        list = []
        for number in range (1, hornihranice + 1):  
            if number > 1:  
                for i in range (2, number):  
                    if (number % i) == 0:  
                        break  
                else:  
                    list.append(number)
        print(list)
    prvocisla(hornihranice)

elif odpoved == 'obdélník':
    print('Strana x:')
    x = int(input())
    print('Strana y:')
    y = int(input())
    def obdelnik(x,y):
        list = []
        row = []

        for i in range(x):
            for j in range(y):
                if (i == 0 or i == x - 1):
                    row += '*'
                elif (j == 0 or j == y - 1):
                    row += '*'
                else:
                    row += ' '
            list.append(row)
            row = []

        for i in list:
            print (i)
        obdelnik(x,y)

else:
    exit()