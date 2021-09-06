
""" => Ejercicio 2:
    Realiza una función que tome como parametro una frase y devuelva una 
    lista de palabras en mayuscula. 

      Ej: 
        mi_frase = "Este sabado tenemos el ultimo encuentro online"

        palabras = convertir(mi_frase)

        print(palabras)

        >>> ["ESTE", "SABADO", "TENEMOS", "EL", "ULTIMO", "ENCUENTRO", "ONLINE"]"""
        
        

frase = "mi hermano es puerco y le gusta la chuleta de puerco"

def mayusculas(frase_cualquiera: str) -> list[str]:
    """funcion que convierte las palabras de minusculas a mayusculas"""
    frase_convert = frase_cualquiera.split(" ")
    frase_loc = list(map(lambda palabra: palabra.upper(), frase_convert))
    return frase_loc

frase_loca = mayusculas(frase)

print(frase_loca)
    