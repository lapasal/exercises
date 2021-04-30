cuenta=0
Primerplato=["Sopa", "Ensalada", "Una servilleta mojada"]
Segundoplato=[ "Lentejas ricas", "Estofado de verduras", "Un puchero de agua caliente"]
Postre=["Natilla de chocolate", "Arroz con leche", "Helados caducados"]

print("Estos son los primeros platos: ", Primerplato, "\nEstos son los segundos platos: ", Segundoplato, "\nY por ultimo, si te has quedado con un poco de ganas de fiesta, estos son los postres: ", Postre)
hola1=input("¿Que vas a querer de primer plato? "),input("¿Que vas a querer de segundo plato? "),input("¿Que vas a querer de postre, papá? ")
#hola1=input("¿Sabes ya que vas a querer comer? ")
#for i in hola1:
#	if(i=="Sopa" or i=="Lentejas" or i=="Natilla de chocotofu"):
#		cuenta1=cuenta+4
#	if(i=="Ensalada" or i=="Estofado de verduras" or i=="Arroz con leche"):
#		cuenta2=cuenta+5
#	if(i=="Una servilleta mojada" or i=="Un puchero de agua caliente" or i=="Helados caducados"):
#		cuenta3=cuenta+6

for i in hola1:
	if(i=="Sopa" or i=="Ensalada" or i=="Una servilleta mojada"):
		if i=="Sopa":
			cuenta1=cuenta+4
		elif i=="Ensalada":
			cuenta1=cuenta+5
		else:
			cuenta1=cuenta+6
	if(i=="Lentejas ricas" or i=="Estofado de verduras" or i=="Un puchero de agua caliente"):
		if i=="Lentejas ricas":
			cuenta2=cuenta+4
		elif i=="Estofado de verduras":
			cuenta2=cuenta+5
		else:
			cuenta2=cuenta+6
	if(i=="Natilla de chocolate" or i=="Arroz con leche" or i=="Helados caducados"):
		if i=="Natilla de chocolate":
			cuenta3=cuenta+4
		elif i=="Arroz con leche":
			cuenta3=cuenta+5
		else:
			cuenta3=cuenta+6
#LOS ESTA EJECUTANDO UNO POR LINEA ES DECIR PRIMER PLATO CUENTA1 SEGUNDO PLATO
cuentafinal=cuenta1+cuenta2+cuenta3

print("Lo que debe pagar es: ",cuentafinal,"$")

iva=cuentafinal*0.21
print("El IVA de su cuenta es: ", iva,"$")
propina=cuentafinal*0.10
print("La propina que debería dejarme es: ", propina,"$")