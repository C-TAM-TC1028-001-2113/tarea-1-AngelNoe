import math
def main():
    # escribe tu código abajo de esta línea
    palabras=int(input('Dame el número de palabras:'))
    paginas=math.ceil(palabras/475)
    descuento=(paginas*60)*.1
    total=(paginas*60)-descuento
    print('El costo de la publicacion es:',total)
if __name__ == '__main__':
    main()
