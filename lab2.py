import datetime as dt

class Record:
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is not None:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()
        else:
            self.date = dt.date.today()

class Calculator(Record):
    def __init__(self, limit):
        self.lim = limit
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        stats_today = 0
        for Record in self.records:
            if Record.date == dt.date.today():
                stats_today += Record.amount
        return stats_today

    def get_week_stats(self):
        today = dt.date.today()
        day7 = today - dt.timedelta(days=7)
        stats_week = 0
        for Record in self.records:
            if Record.date >= today and Record.date <= day7:
                stats_week += Record.amount
        return stats_week

class CashCalculator(Calculator):
    def get_today_cash_remained(self, currency):
        USD_RATE = 57.73
        EURO_RATE = 55.10
        remained = self.lim - self.get_today_stats()
        if currency == "usd":
            remained = remained / USD_RATE
        elif currency == "eur":
            remained = remained / EURO_RATE
        if remained > 0:
            text = "Свободных средств:" + str(remained) + currency
        elif remained < 0:
            text = "Свободных средств нет. Долг:" + str(-1*remained) + currency
        elif remained == 0:
            text = "Ты на мели, бро" + str(remained) + currency
        return text

class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        remained = self.lim - Calculator.get_today_stats(self)
        if remained > 0:
            text = "Свободных средств:" + str(remained)
        elif remained < 0:
            text = "Свободных средств нет. Долг:" + str(-1*remained)
        elif remained == 0:
            text = "Ты на мели, бро" + str(remained)
        return text

cash_calculator = CaloriesCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
print(cash_calculator.get_calories_remained())

cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе'))
cash_calculator.add_record(Record(amount=3000, comment='Серёге за обед'))
cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др', date='08.11.2019'))
print(cash_calculator.get_today_cash_remained(" rub"))
# print(cash_calculator.__dict__)









