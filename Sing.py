class Singleton(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)

