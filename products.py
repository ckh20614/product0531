import os  #operating system

# 找不找得到檔案 & 讀取檔案
def read_file(filename):
	products= []
	if os.path.isfile(filename):
		print('找到檔案了')
		with open(filename, 'r') as f:
			for line in f:
				if '商品,價格' in line:
					continue  #接續下一行
				product, price = line.strip().split(',')  #strip:除掉換行符號 split:使用(',')做分割
				products.append([product, price])
		print(products) 
	else:
		print('找不到檔案')
	return products


#使用者輸入
def user_input(products):
	while True:
		product = input('商品名稱: ')
		if product == 'q':
			break
		price = input('商品價格: ')
		products.append([product, price])
	print(products)	
	return products


#印出所有購買證明
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])


# 寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')


products = read_file('product.csv')
products = user_input(products)
print_products(products)
write_file('product.csv', products)