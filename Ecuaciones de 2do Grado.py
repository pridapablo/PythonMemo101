import math
print ("ECUACIÓNES DE SEGUNDO GRADO")

print ("Dame las siguientes constantes:")



def ecuation (a,b,c):
	dis = math.pow (b,2)-4*a*c
	if dis==0:
		print ("Las raices son iguales")
		x1=(-b)/2*a
		x2=x1
		print ("y son: x1=", x1, "x2=", x2)

	elif dis>0:
		print ("Las raices son diferentes")
		x1=(-b+math.sqrt(dis))/2*a
		x2=(-b-math.sqrt(dis))/2*a
		print ("y son: x1=", x1, "x2=", x2)	

	else:
		print ("Las raices son imaginarias")

volver="s"

while volver not in ("n", "N", "no", "No", "NO"):
	a = int(input("Dame el valor de a: "))
	b = int(input("Dame el valor de b: "))
	c = int(input("Dame el valor de c: "))

	ecuation(a,b,c)
	
	volver=input("¿Quieres volver a empezar? ")

#math.sqrt es para sacar las raices cuadradas de algo
#math.pow es para elevar algo a alguna potencia
