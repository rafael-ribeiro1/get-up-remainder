from win10toast import ToastNotifier
from config import get_configs


def notify(notifier, title, msg, duration):
    # icon_path needs to be defined (even if invalid) so the executable will work fine
    notifier.show_toast(title=title, msg=msg, duration=duration, icon_path="")


def min2sec(mins):
    return mins * 60


if __name__ == "__main__":
    toaster = ToastNotifier()
    while True:
        configs = get_configs()
        notify(toaster, configs[1], configs[2], min2sec(configs[0]))
