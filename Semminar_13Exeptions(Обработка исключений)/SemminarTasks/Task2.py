# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и значение по умолчанию.
# При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.

def new_get(dict_, key, value):
    try:
        result = dict_[key]
    except KeyError:
        result = value
    finally:
        return result

if __name__ == '__main__':
    dict_ = {'1': 1, '2': 2}
    print(new_get(dict_, '1', 3))
    print(new_get(dict_, '3', 3))