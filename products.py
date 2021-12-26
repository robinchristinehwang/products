#兩個維度的清單
#清單中的清單
products = []
while True:
	name = input('請輸入商品名稱')
	if name == "q":
		break
	price = input("請輸入商品價格")
	products.append([name, price])
print(products)

products[0][0]