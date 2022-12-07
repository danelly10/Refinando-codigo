"""Nombre: Danelly Urena
Matricula: 22-0559
Nombre del Problema: Refinando codigo
Descripcion: En este ejercicio, se refinara un codigo y se publicara en un repositorio de Github"""

def list_costs():
    """Recibe la ruta del archivo de costos como entrada y devuelve
    una lista con los costos en formato numerico"""
    with open('gift_costs.txt', encoding='UTF-8') as file:
        gift_costs = file.read().split('\n')
    list_gift_costs = [int(c) for c in gift_costs]
    return list_gift_costs

def t_price(list_gift_costs):
    """Recibe la lista de los costos como entrada y devuelve el precio total
    Decide cuales son los regalos que necesitan pagar impuestos al superar RD$1000"""
    list_gift_costs = list_costs()
    total_price = 0
    for cost in list_gift_costs:
        if cost > 1000:
            #Agrega el costo con los impuestos incluidos
            total_price += cost * 1.16
        else:
            total_price += cost
    return total_price

def main():
    """Funcion principal que llama a las funciones list_gift_costs y total_price.
    Luego imprime el precio total de los regalos en pantalla"""
    print(t_price(list_costs))

if __name__ == '__main__':
    main()
