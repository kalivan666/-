import requests

def Main(to_monitor):
    a = Valute(to_monitor)
    USD(to_monitor)
    EUR(to_monitor)
    print(to_monitor)
    print(transfer(to_monitor))

def Valute(to_monitor):
    page = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    data = page.json()
    valute = data['Valute']
    Value = ['USD', 'EUR', 'RUB']
    print(valute)
    for value in Value:
        if value in valute:
            to_monitor[value] = valute[value]
        else:
            to_monitor['RUB'] = Rub()
def USD(to_monitor):
    usd = {}
    Usd = to_monitor['USD']
    for key in to_monitor['USD']:
        if key == 'Value':
            usd['Value'] = Usd['Value']
    Usd.clear()
    Usd['Value'] = usd['Value']
def Rub():
    RUB = {}
    RUB['Value'] = 1
    return RUB
def EUR(to_monitor):
    eur = {}
    Eur = to_monitor['EUR']
    for key in to_monitor['EUR']:
        if key == 'Value':
            eur['Value'] = Eur['Value']
    Eur.clear()
    Eur['Value'] = eur['Value']
def transfer(to_monitor):
    print('В EUR или в USD?')
    a = input()
    usd = to_monitor['USD']
    eur = to_monitor['EUR']

    if a == 'EUR':
        output = eur['Value']
    elif a == 'USD':
            output = usd['Value']
    else:
            output = print('вы ввели неправильно, либо USD либо EUR')
    return output

if __name__ == '__main__':
    to_monitor = {}
    Main(to_monitor)
