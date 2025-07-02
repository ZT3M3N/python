value = "123456789"
value_to_digits = [int(digit) for digit in str(value)]
print(value_to_digits)

# ✅ Crear una lista de los números del 1 al 10.
numbers_list = [n for n in range(1, 11)]
print(numbers_list)

# ✅ Crear una lista de los cuadrados de los números del 1 al 10.
powing = [n**2 for n in range(1,11)]
print(powing)

# ✅ Obtener solo los números impares del 1 al 20.
odds = [n for n in range(1,21) if n%2==1]
print(odds)

# 🔠 Convertir esta lista de palabras a minúsculas:
palabras = ["Hola", "MUNDO", "Python"]
lower_words = [palabra.lower() for palabra in palabras]
print(lower_words)

# Obtener una lista con la longitud de cada palabra:
palabras2 = ["list", "comprehension", "is", "powerful"]
length  = [len(word) for word in palabras2]
print(length)

# ✅ Obtener los múltiplos de 3 entre 1 y 30.
mult_3rd = [m for m in range(1, 31) if m%3==0]
print(mult_3rd)

# Filtrar solo las palabras que empiezan con la letra 'p':
palabras = ["python", "es", "poderoso", "y", "práctico"]
filtered_words = [word for word in palabras if word.startswith("p")]
print(filtered_words)

# Obtener los números pares entre 1 y 50 que además sean múltiplos de 5.
even_and_5th = [n for n in range(1, 51) if n%2==0 and n%5==0]
print(even_and_5th)