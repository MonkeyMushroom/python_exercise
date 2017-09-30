items = {'Apple': 3.99, 'Banana': 2.68, 'Pear': 2.99}

width = input('Please input width: ')

price_width = item_width = width / 2

header_format = '%-*s%*s'
item_format = '%-*s%*.2f'

print '=' * width
print header_format % (item_width, 'Item', price_width, 'price')
print '-' * width
for k, v in items.items():
    print item_format % (item_width, k, price_width, v)
