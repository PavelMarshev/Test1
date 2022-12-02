def decorate(funct):
    def wrapper():
        print("wrapper")
        funct()
    return wrapper


@decorate
def test():
    print("test")

test()