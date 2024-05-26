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

    # Inicializamos un contador de fechas y usuarios
    fecha_usuario_count = defaultdict(Counter)

    # Leemos el archivo y procesamos línea por línea
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet_data = json.loads(line)
            fecha = tweet_data['date'].split('T')[0]
            usuario = tweet_data['user']['username']
            fecha_usuario_count[fecha][usuario] += 1

    # Extraemos las top 10 fechas
    top10_fechas = heapq.nlargest(10, fecha_usuario_count.keys(), key=lambda fecha: sum(fecha_usuario_count[fecha].values()))

    # Obtenemos los usuarios más activos para cada fecha top
    usuarios_top_por_fecha = [(fecha, max(fecha_usuario_count[fecha], key=fecha_usuario_count[fecha].get)) for fecha in top10_fechas]

    return usuarios_top_por_fecha

