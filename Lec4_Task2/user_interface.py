import data_provider as prov
import logger as log


def temperature_view(sensor):
    data = prov.get_temperature(sensor)
    log.data_logger(data, 'temperature')
    return data


def pressure_view(sensor):
    data = prov.get_pressure(sensor)
    log.data_logger(data, 'pressure')
    return data


def wind_speed_view(sensor):
    data = prov.get_wind_speed(sensor)
    log.data_logger(data, 'wind speed')
    return data
