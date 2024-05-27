import re
from collections import Counter
from typing import List, Tuple
import orjson

# Expresión regular para encontrar emojis
emoji_pattern = re.compile(r'[\U0001F300-\U0001F64F\U0001F680-\U0001F6FF\u2600-\u26FF\u2700-\u27BF]')


# Función principal que lee el archivo JSON y cuenta los emojis en los tweets
def q2_time(file_path: str) -> List[Tuple[str, int]]:

    print("Inicio del proceso")

    # Asignamos contador de emojis
    emoji_counts = Counter() 

    # Abrimos el archivo en modo lectura (r).
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # Cargar cada línea como un objeto JSON
            tweet = orjson.loads(line.strip())  
            if "content" in tweet:
                text = tweet["content"]
                # Encontrar emojis en el texto según las expresiones
                emojis_in_tweet = emoji_pattern.findall(text)  
                emoji_counts.update(emojis_in_tweet) 

    # Obtener los 10 emojis más comunes
    most_common_emojis = emoji_counts.most_common(10)
    return most_common_emojis


