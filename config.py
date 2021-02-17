from configparser import ConfigParser


DEFAULT_INTERVAL = 10
DEFAULT_TITLE = "Hora de levantar da cadeira"
DEFAULT_MSG = "Aproveita para fazer também algum exercício físico"


def get_configs():
    config = ConfigParser()
    config.read('config.ini', encoding='utf-8')
    try:
        interval = int(config['DEFAULT'].get('Interval', DEFAULT_INTERVAL))
    except ValueError:
        interval = DEFAULT_INTERVAL
    title = config['DEFAULT'].get('ToastTitle', DEFAULT_TITLE)
    description = config['DEFAULT'].get('ToastDescription', DEFAULT_MSG)
    return interval, title, description
