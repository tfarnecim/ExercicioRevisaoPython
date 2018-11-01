cont = 0

resp = input("Telefonou para a vítima?")

if(resp == "S"):
	cont += 1

resp = input("Esteve no local do crime?")

if(resp == "S"):
	cont += 1

resp = input("Mora perto da vítima?")

if(resp == "S"):
	cont += 1

resp = input("Devia para a vítima?")

if(resp == "S"):
	cont += 1

resp = input("Já trabalhou com a vítima?")

if(resp == "S"):
	cont += 1

if(cont==5):
	print("Assassino")
elif(cont==4 or cont==3):
	print("Cumplice")
elif(cont==2):
	print("Suspeita")
else:
	print("Inocente")

