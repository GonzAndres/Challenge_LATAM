from typing import List, Tuple
from datetime import datetime
import json
import heapq
import os
from typing import List, Tuple
from datetime import datetime
import json
import heapq
from collections import defaultdict

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    print("Inicio del proceso")

    # Inicializamos un contador de fechas y usuarios
    fecha_usuario_count = defaultdict(int)

    # Leemos el archivo y procesamos línea por línea
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet_data = json.loads(line)
            fecha = tweet_data['date'].split('T')[0]
            usuario = tweet_data['user']['username']
            fecha_usuario_count[fecha + ' ' + usuario] += 1

    # Extraemos las top 10 fechas
    top10_fechas = heapq.nlargest(10, fecha_usuario_count.keys(), key=lambda key: fecha_usuario_count[key])

    # Obtenemos los usuarios más activos para cada fecha top
    usuarios_top_por_fecha = []
    for fecha_usuario in top10_fechas:
        parts = fecha_usuario.split(' ')
        if len(parts) == 2:
            fecha, usuario = parts
            usuarios_top_por_fecha.append((fecha[:10], usuario[10:]))
        else:
            print("Error: formato no válido en:", fecha_usuario)

    print("Fin del proceso")

    return usuarios_top_por_fecha
