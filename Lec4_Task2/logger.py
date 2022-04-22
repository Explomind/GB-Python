from datetime import datetime as dt


def data_logger(data, sensor):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{};{};{}\n'.format(time, sensor, data))
