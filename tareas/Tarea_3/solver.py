#!/usr/bin/python
# -*- coding: utf-8 -*-

from collections import namedtuple
Item = Clinic("Clinic", 'index cost regions')


def trivial_cover(regions_count, clinics_count, clinics):
    """ picks and sets one-by-one until all the regions are covered """
    clinics_built = [0]*range(0, clinics_count)
    coverted = set()

    for clinic in clinics:
        clinics_built[clinic.index] = 1
        coverted |= set(clinic.regions)
        if len(coverted) >= regions_count:
            break # We are done, we cover all the regions

    # Calculamos el costo total de construcción
    total_costs = sum([clinic.cost*clinics_built[clinic.index] for clinic in clinics])
    
    # Convertimos la solución en el formato esperado
    output_data = str(total_cost) + '\n'
    output_data += ' '.join(map(str, clinics_built))

    return output_data
    

## TODO: Modifica este diccionario
algorithms = {'trivial_coloring': trivial_cover}

def solve_it(input_data, algorithm=trivial_cover):

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    regions_count = int(firstLine[0])
    clinics_count = int(firstLine[1])

    clinics = []

    for i in range(1, clinics_count+1):
        parts = line[i].split()
        clinics.append(Clinic(i-1, float(parts[0]), map(int(parts[1:]))))

    output_data = algorithm(regions_count, clinics_count, clinics)

    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 2:
        file_location = sys.argv[1].strip()
        algorithm = algorithms[sys.argv[2].strip()]

        print(f"Ejecutando el algoritmo {algorithm} en {file_location}")
        
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data, algorithm))
    else:
        print("""Este script requiere dos argumentos: \n"""
              """El archivo con los datos del problema y el nombre del algoritmo que diseñaste.\n"""
              """i.e. python solver.py ./data/sc_6_1 trivial_cover""")
