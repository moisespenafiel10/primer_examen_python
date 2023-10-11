#1.la siguiente funcion debera retornar la suma de sus parametros
def suma(a,b):
  #reemplazar pass por la sintaxis correcta

  return a+b

#2. la funcion debera retornar 'es menor' o 'es mayor' segun la edad que pase por parametro
def is_greater_than(edad):
  #reemplazar pass por la sintaxis correcta
  valor = 18
  # Comparar la edad con el valor y retornar el resultado adecuado
  if edad >= valor:
    return 'es mayor'
  elif edad < valor:
    return 'es menor'
  else:
    return edad ('es igual')

#3. la funcion recibe como parametros dos datos el primero arr recibe una array(lista) el segundo num un numero entero positivo, la funcion debera retornar un nuevo array con el num insertado en la tercera posicion del array
def new_array(arr,num):
  
  new_arr = arr.copy()
  new_arr.insert(2,num)
  return new_arr
#4. la funcion recibe una array debera retornar la suma de los numero ejm: [4,2,8,10] retornara 24
def suma_array(arr):
  suma = 0
  for num in arr:
    suma += num
  return suma