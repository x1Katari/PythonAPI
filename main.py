from firstclass import Converter


path = ('examp.csv')
# path = ('example.json')


# Получает объект типа:
# {"coordinates": [широта: float, долгота: float], "type": "Point"}
Points = Converter().convert(path)

print(Points)
