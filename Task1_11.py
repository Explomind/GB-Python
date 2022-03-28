# Сделайте так, чтобы число секунд отображалось в виде дни:часы:минуты:секунды

sec_input = int(input('Input amount of seconds: '))
days = sec_input // 86400
hours = (sec_input - days * 86400) // 3600
minutes = (sec_input - days * 86400 - hours * 3600) // 60
seconds = (sec_input - days * 86400 - hours * 3600 - minutes * 60)
print(f'days:hours:minutes:seconds\t{days}:{hours}:{minutes}:{seconds}')
