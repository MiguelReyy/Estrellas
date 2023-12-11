import turtle #Se importa la biblioteca turtle para realizar gráficos simples.

"""Se utiliza un bloque try-except para manejar posibles errores al ingresar la longitud
 y el número de puntas, asegurándose de que ambos sean valores enteros."""
try:
    longitud = int(input("Introduce una longitud para las puntas: "))
except ValueError:
    longitud = int(input("Introduce una longitud válida: "))


try:
    puntas = int(input("cuantas puntas quieres (teniendo en cuenta que las estrellas tienen puntas impares > 5): "))
except ValueError:
    puntas = int(input("Por favor introduzca un numero: "))
    
"""Se define una función main que configura la ventana de dibujo, establece el color de
 fondo y la velocidad de dibujo, y luego utiliza un bucle for para dibujar la estrella."""
def main(puntas):
    
    turtle.setup(600, 600)
    turtle.bgcolor("white")
    turtle.speed(2)  # Configura la velocidad de dibujo
     # Dibuja la estrella

    for _ in range(puntas, longitud):
        turtle.forward(longitud)
        angle = 180 - (180 / puntas)
        turtle.right(angle)

    turtle.mainloop()
    """La condición if puntas % 2 == 0 or puntas < 5 verifica si el número de puntas
 es par o menor que 5. En caso afirmativo, solicita al usuario que ingrese un número
 impar mayor que 5 y luego llama a la función main con el nuevo valor. En caso
    contrario, simplemente llama a la función main con el número de puntas ingresado
 inicialmente."""
if puntas % 2 == 0 or puntas < 5 :
    puntas = int(input("Por favor, ingresa un número impar mayor que 5: "))
    main(puntas)
else:
    main(puntas)