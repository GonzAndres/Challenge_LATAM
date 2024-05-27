from typing import List, Tuple
from collections import Counter
import orjson

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    
    print("Iniciando test")

    # Counter para contar las menciones de usuarios
    mentions_users = Counter()

    # Leer el archivo línea por línea
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Procesar cada línea como JSON
            tweet = orjson.loads(line.strip())
            mentioned_users = tweet.get('mentionedUsers')
            
            # Si hay usuarios mencionados, contar sus menciones
            if mentioned_users is not None:
                for user in mentioned_users:
                    if 'username' in user:
                        mentions_users[user['username']] += 1

    # Obtener los 10 usuarios más mencionados
    frecuencia_menciones = mentions_users.most_common(10)
    
    return frecuencia_menciones

    