import requests

a = [0, 1, 2, 3, 4, 5]

b = [3, 4, 5, 8]

s = [k for k in a if k in b]
print(s)

print(set(a).intersection(b))

"""второе задание"""

aa = [0, 2, 1, 0, 1, 2]

print(list(set(aa)))

bb = []

for item in aa:
    if item not in bb:
        bb.append(item)

print(bb)

"""третье задание"""

a3 = [0, 1, 2, 3, 4, 5]

print([k for k in a3 if (k % 2 == 0)])

"""четвертое задание"""

b4 = {0: 0}

a4 = ['foo', 'bar', 'baz']

for k4, num in enumerate(a4):
    b4[k4] = num

print(b4)

dict_my = {i: j for (i, j) in enumerate(a4)}

print(dict_my)

"""пятое задание"""

my_str = [
    'John', 'Allison', 'Brian',
    'Claire', 'Andrew'
]

for name in my_str:
    print(f'Hi, {name}')

"""шестое задание"""

a = ['foo', 'bar', 'baz', 'egg']
b = ['bar', 'baz']
c = [k for k in a if k not in b]

print('отсутствуют: ' + ', '.join(c))

"""седьмое задание"""

a = [0, 1, 2, 6, 7, 8]
b = [3, 4, 5]
s = sorted((a + b))
print(s)

"""восьмое задание"""

a = {0: 'foo', 1: 'bar', 2: 'baz'}

b = {i: a[i] for i in reversed(a)}

print(b)

b = {i: a[i] for i in list(a.keys())[::-1]}

print(b)

"""восьмое задание"""

response = requests.get('https://www.7timer.info/bin/astro.php?lon=113.2&lat=23.1&ac=0&unit=metric&output=json&tzshift=0')

response_json = response.json()


data = response_json.get('dataseries')

for elem in data:
    print(f'направление: {elem["wind10m"]["direction"]}, '
          f'скорость: {elem["wind10m"]["speed"]}')
