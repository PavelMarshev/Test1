import datetime
def decorate(funct):
    def wrapper():
        print("Текущая дата: ")
        funct()
    return wrapper

@decorate
def f():
    print(datetime.datetime.now().date())

f()

