# pip install chardet
# python.org
import chardet

# with open("test.log") as f:
#     lines = f.read()
# print(lines)

with open("test.log", "rb") as fh:
    raw_data = fh.read()
print(raw_data)
# b'Parametr 1\r\nParametr 2\r\nParametr 3\r\nParametr 4\r\nDodane1\r\nDodane2\r\nDodane3\r\nDo\xc5\x9bdane3\r\n'

result = chardet.detect(raw_data)
print(result)
# {'encoding': 'Windows-1254', 'confidence': 0.6563300878188562, 'language': 'Turkish'}
# pozwiekszeniu próbki danych (więcej polskich znaków)
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
encoding = result['encoding']
print("Kodowanie:", encoding) # Kodowanie: utf-8
print(raw_data.decode(encoding=encoding))
# Parametr 1
# Parametr 2
# Parametr 3
# Parametr 4
# Dodane1
# Dodane2
# Dodane3
# Dośąźćdane3