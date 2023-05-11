# 1. TAREA: imprime "Hola, mundo"
print( "Hola,mundo" )
# 2. imprime "Hola, Noelle" con el nombre en una variable
nombre = "Vicente"
print("Hola,", nombre, "!")	# con una coma
print("Hola," +  nombre + "!")	# con un +
# 3. imprimir "Hola 42!" con el número en una variable
nombre = 42
print("Hola,", nombre, "!")	# con una coma
print("Hola," +  str(nombre) + "!")	# con una +	-- este debería arrojar un error!
# 4. imprimir "Amo comer sushi y pizza" con las comidas en variables
comida_uno = "sushi"
comida_dos = "pizza"
print("Amo comer {} y {}.".format(comida_uno, comida_dos)) # con .format()
print(f"Amo comer {comida_uno} y {comida_dos}.") # con una cadena f

