from typing import List, Tuple
from datetime import datetime
import pandas as pd
import json
import heapq
import os
from collections import defaultdict
from collections import Counter


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    print("Inicio del proceso")

    # Creamos un diccionario  para contabilizar la cantidad de tweets por usuario. En caso de que no exista una clave, defauldict lo considera vacio
    fecha_usuario_count = defaultdict(Counter)

    # Abrimos el archivo en modo lectura (r).
    with open(file_path, 'r', encoding='utf-8') as f:

        # Iteramos línea por línea del archivo y transformamos cada una en un diccionario de python.
        for line in f:
            tweet_data = json.loads(line)
            # Extraemos la fecha y la asignamos al dic
            fecha = tweet_data['date'].split('T')[0]
            # Extraemos el usuario y la asignamos al dic
            usuario = tweet_data['user']['username']
            # Generamos un incrementador para el usuario en dicha fecha
            fecha_usuario_count[fecha][usuario] += 1

    # Utilizamos función para extraer el top 10 fechas
    top10_fechas = heapq.nlargest(10, fecha_usuario_count.keys(), key=lambda fecha: sum(fecha_usuario_count[fecha].values()))

    # Buscamos los usuarios con más tweets para cada una de las 10 fechas
    usuarios_top_por_fecha = [(fecha, max(fecha_usuario_count[fecha], key=fecha_usuario_count[fecha].get)) for fecha in top10_fechas]

    return usuarios_top_por_fecha

