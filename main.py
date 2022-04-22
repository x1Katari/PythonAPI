from firstclass import Converter


# path = ('soccer.csv')
path = ('example.json')

Points = Converter().convert(path)

print(Points)
