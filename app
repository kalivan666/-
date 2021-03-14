import requests
import sys

class Main():
    def __init__(self):
        page = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        if page.status_code // 100 != 2:
            print(f'failed to execute request, status_code: {page.status_code}')
            sys.exit(-1)
        self.data = page.json()
        self.valute = self.data['Valute']

    def treatment(self, values):
        self.to_monitor = {}
        for value in values:
            if value in self.valute:
                valute = self.valute[value]
                self.to_monitor[value] = valute['Value']
        self.to_monitor['RUB'] = int(1)

    def second_treatment(self):
        pass


