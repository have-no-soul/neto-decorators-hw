from datetime import datetime
import requests


def log_decorator(path):
    """Декоратор-логер для записи в файл даты, времени вызова декорируемой функции, ее имени, агрументов и результата"""

    def _log_decorator(old_function):
        def foo(*args, **kwargs):
            date_time = datetime.now()
            str_time = date_time.strftime('%Y-%m-%d, %H-%M-%S')
            func_name = old_function.__name__
            result = old_function(*args, **kwargs)
            with open(f'{path}decorator_logs_2.txt', 'a', encoding='utf-8') as file:
                file.write(f'\nДата вызова функции: {str_time}\n'
                           f'Имя функции: {func_name}\n'
                           f'Аргументы функции: {args, kwargs}\n'
                           f'Возвращаемое значение функции: {result}\n'
                           f'{"*" * 50}\n')
            return result

        return foo

    return _log_decorator


@log_decorator('C:/Users/Виктор/Desktop/PythonCourse/neto-decorators-hw/logs/')
def get_status(*args):
    url = ','.join(args)
    response = requests.get(url=url)
    return response.status_code


if __name__ == '__main__':
    get_status('https://yandex.ru/')
