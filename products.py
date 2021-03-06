import os #operating system

if os.path.isfile('products.csv'):
	print('yeah! found the file!')
else:
	print('cannot find the file......')

#讀取檔案
products = []
with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格'in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#讓使用者輸入
while True:
	name = input('請輸入商品名稱')
	if name == "q":
		break
	price = input("請輸入商品價格")
	products.append([name, price])
print(products)

products[0][0]

#印出所有購買紀錄
for d in products:
	print('買了' + d[0] +',花了' + d[1] + '元')
#寫入檔案
with open('products.csv', "w", encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')