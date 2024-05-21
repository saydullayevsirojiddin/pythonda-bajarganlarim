yosh = int(input("yoshingizni kiriting: "))
if yosh <= 4:
	narh=4
elif yosh <= 12:
	narh=8000
elif yosh <= 20:
	narh=12000
else:
	narh=20000
print(f"Sizga kirish {narh} so'm")