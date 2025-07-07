from superhero_api import get_superheroes

heroes = get_superheroes()
if heroes:
    for hero in heroes:
        if hero.get('appearance', {}).get('gender') == 'Female' and ('work' not in hero or not bool(hero.get('work'))):
            print(f"Герой женского пола без работы: {hero}")

    for hero in heroes:
        if hero.get('appearance', {}).get('gender') == "Unknown Gender":
             print(f"Герой с полом 'Unknown Gender': {hero}")
else:
    print("get_superheroes() вернул None или пустой список")


