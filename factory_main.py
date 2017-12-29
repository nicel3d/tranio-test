def factory_decor(num):
    def decorator(fn):
        def decorator2(*x):
            try:
                if int(num) == float(num):
                    numeric = float(fn(*x))
                else:
                    return None
            except BaseException:
                return None
            return num * numeric
        return decorator2
    return decorator

@factory_decor(2.2)
def test():
    return 12

#print(test.__name__)
print(test())