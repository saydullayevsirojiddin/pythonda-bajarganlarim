table=8
for i in range(1,11):
	print(table, 'x', i, '=?')
	pup=input()
	if pup=='bilmayman':
		break
	if pup=='keyingisi':
		print("Kiyingi savol")0
		+
		continue
	res = table*i
	if int(pup)==res:
		print('Barakalla')
	else:
		print('Notugri, javob:', res)
print('tugadi')