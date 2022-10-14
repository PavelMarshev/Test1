from lab2 import *

def test_get_calories_remained():

    calories_calculator = CaloriesCalculator(1000) # init calc

    records = [Record(amount=145, comment='кофе'),
               Record(amount=300, comment='Серёге за обед'),
               Record(amount=3000, comment='бар в Танин др', date='08.11.2019')] # create records

    for record in records:
        calories_calculator.add_record(record) # insert records

    amounts = records[0].amount + records[1].amount  # sum valid records

    assert calories_calculator.get_calories_remained() == "Свободных средств:" + str(1000 - amounts)


def test_get_today_cash_remained():

    cash_calculator = CashCalculator(1000) # init calc

    records = [Record(amount=145, comment='кофе'),
               Record(amount=3000, comment='Серёге за обед'),
               Record(amount=3000, comment='бар в Танин др', date='08.11.2019')] # create records

    for record in records:
        cash_calculator.add_record(record) # insert records

    amounts = records[0].amount + records[1].amount  # sum valid records

    assert cash_calculator.get_today_cash_remained(" rub") == "Свободных средств нет. Долг:" + str(-1*(1000 - amounts)) + " rub"

















