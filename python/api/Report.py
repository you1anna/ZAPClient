import os
from python.api.config import Settings
from bs4 import BeautifulSoup


# noinspection PyPep8Naming
class report:
    def __init__(self, zapreport):
        self.zapreport = os.path.join(Settings['zapReportDir'], zapreport)
        self.html = BeautifulSoup(open(self.zapreport), "html.parser")
        print('\n', self.zapreport, '\n')

    def ParseAlerts(self):
        self.alerts = []
        self.results = self.html.find('table', attrs={"border": "0", "width": "45%"})
        self.rows = self.results.find_all('tr')[1:]
        for row in self.rows:
            cols = row.find_all('td')
            cols = [element.text.strip() for element in cols]
            self.alerts.append([element for element in cols if element])
        for alert in self.alerts:
            print(alert)
        return self.alerts

    def CompareReports(self, alerts1, alerts2):
        self.alerts1 = alerts1
        self.alerts2 = alerts2


rep1 = report('ZAPMontlyScan02-Mar-2016.html')
parsedAlerts1 = rep1.ParseAlerts()

rep2 = report('ZAP Montly Scan 04-Feb-2016.html')
parsedAlerts2 = rep2.ParseAlerts()

