from app import Main
import aiohttp
import asyncio
import pprint

class wallet:
    def __init__(self):
        self.course = {}
        self.value = 0

def check(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

async def kaka():
    loop = asyncio.get_event_loop()
    my_wallet.value = await loop.run_in_executor(None, input, 'How much money to add? (RUB)\n')
    task = asyncio.create_task(main())
    await task
async def Loop(values, N):
    while True:
        Main.__init__(Main)
        Main.treatment(Main, values)
        print('курс обновлен')
        await asyncio.sleep(N)

async def main():
    print(my_wallet.value)
    print(my_wallet.value)
    print(my_wallet.value)

if __name__ == '__main__':
    Main.__init__(Main)
    print(Main.valute)
    i = 0
    values = []
    while i == 0:
        Bool = (input('Add currency? y/f\n')).upper()
        if Bool == 'Y':
            valute = ((input('Enter currency\nExample: usd\n')).upper())
            if valute in Main.valute:
                values.append(valute)
            else:
                print('Wrong currency')
        elif Bool == 'F':
            i = i + 1
            while i == 1:
                N = input('Updating currency data (period)\n')
                if check(N):
                    N = int(N)
                    i = i + 1
                else:
                    print('Wrond period')
        else:
            print('Wrong y/f')

loop = asyncio.new_event_loop()
main_task = asyncio.wait([Loop(values, N), kaka()])
try:
    loop.run_until_complete(main_task)
except asyncio.CancelledError:
    loop.run_until_complete(main_task)
loop.close()
my_wallet = wallet()
