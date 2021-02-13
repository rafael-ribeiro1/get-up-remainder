from win10toast import ToastNotifier


def notify(notifier, title, msg, duration):
    notifier.show_toast(title=title, msg=msg, duration=duration)


if __name__ == "__main__":
    toaster = ToastNotifier()
    DEFAULT_INTERVAL = 10
    DEFAULT_TITLE = "Hora de levantar da cadeira"
    DEFAULT_MSG = "Aproveita para fazer também algum exercício físico"
    while True:
        notify(toaster, DEFAULT_TITLE, DEFAULT_MSG, DEFAULT_INTERVAL)
