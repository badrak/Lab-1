class Decorator(object):
    def __init__(self, f):
        print("Код, который отработает до вызова функции")
        f()

    def __call__(self):
        print("Код, срабатывающий после")


@Decorator
def function():
    print("Неизменяемая функция")
function()
