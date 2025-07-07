import requests

BASE_URL = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api"

def get_superheroes():
    """Получает данные о всех супергероях."""
    try:
        response = requests.get(f"{BASE_URL}/all.json")
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None

def get_height(hero):
    """Извлекает рост героя в сантиметрах."""
    height_str = hero.get('appearance', {}).get('height', [])
    if height_str and height_str[1]: # Проверяем наличие значения в метрах
        try:
            return float(height_str[1].split()[0]) * 100 # Берем значение в метрах и переводим в см
        except (ValueError, IndexError):
            return 0
    return 0


def find_highest_hero(gender="", has_work=None):
    """Находит самого высокого героя по заданным критериям."""
    heroes_data = get_superheroes()
    if heroes_data is None:
        return None

    filtered_heroes = [
        hero for hero in heroes_data
        if (not gender or hero.get('appearance', {}).get('gender') == gender) and
           (has_work is None or (has_work == any(value and value != "-" and value != "" for value in hero.get('work', {}).values()))) # Основное исправление здесь
    ]

    if not filtered_heroes:
        return None

    highest_hero = max(filtered_heroes, key=get_height, default=None)
    return highest_hero
