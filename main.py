from firstclass import Converter
from geojson import Polygon, Point, MultiPoint, MultiPolygon, LineString, MultiLineString

path = ('examp.csv')


# Получает объект типа:
# {"coordinates": [широта: float, долгота: float], "type": "Point"}
points = Converter().convert(path)

multi = MultiPoint(points)
line = LineString(points)
lines = [LineString(points) for i in range(5)]


print('Список поинтов')
print(points)
print('Мультипоин')
print(multi)
print('Линия')
print(line)
print('Список линий')
print(lines)