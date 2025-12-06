import datetime

agora = datetime.datetime.now()

data_formatada = f"Data: {agora.day:02d}/{agora.month:02d}/{agora.year}"
hora_formatada = f"Hora: {agora.hour:02d}:{agora.minute:02d}"

print(data_formatada)
print(hora_formatada)
