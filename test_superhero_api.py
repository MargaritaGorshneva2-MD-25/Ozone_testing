import unittest
from superhero_api import find_highest_hero, get_superheroes, get_height

class TestSuperheroAPI(unittest.TestCase):

    def test_get_superheroes_success(self):
        """Проверяет успешное получение данных о супергероях."""
        heroes = get_superheroes()
        self.assertIsNotNone(heroes, "Функция get_superheroes() вернула None")
        self.assertIsInstance(heroes, list, "get_superheroes() должен возвращать список")
        self.assertTrue(len(heroes) > 0, "Список героев пуст")

    def test_find_highest_hero_male_with_work(self):
        """Проверяет поиск самого высокого героя мужского пола с работой."""
        highest = find_highest_hero(gender="Male", has_work=True)
        self.assertIsNotNone(highest, "Не найден герой мужского пола с работой")
        self.assertEqual(highest.get('appearance', {}).get('gender'), "Male")
        self.assertTrue('work' in highest and highest.get('work'))


    def test_find_highest_hero_female_no_work(self):
        """Проверяет, что функция возвращает None, если нет героев женского пола без работы."""
        highest = find_highest_hero(gender="Female", has_work=False)
        self.assertIsNone(highest, "Должен вернуться None, если нет подходящих героев")


    def test_find_highest_hero_no_heroes(self):
        """Проверяет случай, когда нет героев с не указанным полом, но с работой."""
        highest = find_highest_hero(gender="-", has_work=True)
        self.assertIsNone(highest, "Должен вернуться None, если нет подходящих героев")


if __name__ == '__main__':
    unittest.main()
