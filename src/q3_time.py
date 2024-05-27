from typing import List, Tuple
from collections import Counter
import orjson

def q3_time(file_path: str) -> List[Tuple[str, int]]:

    print("Inicio del proceso")

    mentions_users = Counter()

    # Leemos el archivo en bloques
    with open(file_path, 'r', encoding='utf-8') as f:
        buffer = []
        # Leemos 10000 líneas a la vez, variable que se puede ajustar según memoria
        buffer_size = 10000
        for line in f:
            buffer.append(line.strip())
            if len(buffer) >= buffer_size:
                process_buffer(buffer, mentions_users)
                buffer = []
        if buffer:  # Procesar cualquier resto de líneas
            process_buffer(buffer, mentions_users)

    frecuencia_menciones = mentions_users.most_common(10)
    
    return frecuencia_menciones


# Función para procesamiento en bloques
def process_buffer(buffer, mentions_users):

    # Esta función para procesar los bloques permite que se reduzca la cantidad de comprobaciones dentro del bucle principal de lectura del json.
    for line in buffer:
    
        try:
            tweet = orjson.loads(line)
            mentioned_users = tweet.get('mentionedUsers')
            if mentioned_users:
                for user in mentioned_users:
                    username = user.get('username')
                    if username:
                        mentions_users[username] += 1
        except orjson.JSONDecodeError:
            continue





