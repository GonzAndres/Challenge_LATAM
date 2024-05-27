import emoji
from collections import Counter
from typing import List, Tuple
import orjson

# Función para extraer y contar emojis en un texto usando la librería emoji
def count_emojis(text: str, emoji_counts: Counter):
    for char in text:
        if char in emoji.EMOJI_DATA:
            emoji_counts[char] += 1


# Función principal que lee el archivo JSON y cuenta los emojis en los tweets
def q2_memory(file_path: str) -> List[Tuple[str, int]]:

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
                count_emojis(text, emoji_counts)

    # Obtener los 10 emojis más comunes
    most_common_emojis = emoji_counts.most_common(10)
    return most_common_emojis