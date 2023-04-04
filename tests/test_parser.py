from requests.exceptions import MissingSchema

from parser import *
from test_fixtures import *


class TestGetPageContent:
    # Test for getting page content and links to scrape.
    def test_get_page_content(self):
        # Test for valid homepage link
        link = 'https://www.google.ch'
        parsed_page = get_page_content(link)
        assert isinstance(parsed_page, BeautifulSoup)

        # Test for invalid homepage link
        invalid_link = 'example.com'
        with pytest.raises(MissingSchema):
            get_page_content(invalid_link)

    def test_get_links_from_category(self, get_test_main_page):
        # Test the function for category snacks
        expected_output = ['https://shortcutapp.io/n/YjNhNTQxOWNjNWRkNjY3NDI0NWExYjZiODllYzRiNWVk']
        assert get_links_from_category(get_test_main_page, ["snacks"]) == expected_output

        # Test the function for a false category
        expected_output = []
        assert get_links_from_category(get_test_main_page, ["no_category"]) == expected_output

    def test_get_links_to_scrape(self, get_test_main_page):
        # Test the function for one category
        assert get_links_to_scrape(get_test_main_page, ["snacks"]) == [
            'https://shortcutapp.io/n/YjNhNTQxOWNjNWRkNjY3NDI0NWExYjZiODllYzRiNWVk']

        # Test the function for a false category
        assert get_links_to_scrape(get_test_main_page, ["snacks", "no_category"]) is False

        # Test the function for all category's
        assert get_links_to_scrape(get_test_main_page) == [
            'https://shortcutapp.io/n/MjgzMzNlMzRkZWZmMGRiYzVjMzkxNDM2OWU0ZDA1MmQz',
            'https://shortcutapp.io/n/OGZmNTk5NTVhNDk3MWVhNDYyZTlhZGY3NTA4YjQ0YTIx',
            'https://shortcutapp.io/n/YjhjMWYxODBkZTQwNTFhYWE5NWQ0YWQ1MzRkNGFiNzg5',
            'https://shortcutapp.io/n/ZmZjOWQ4YTczNTkwODY4MTI1ZTBiNmQ2ODNlMjYxNjEz',
            'https://shortcutapp.io/n/YjNhNTQxOWNjNWRkNjY3NDI0NWExYjZiODllYzRiNWVk',
            'https://shortcutapp.io/n/ZDc4MGIyOGJkMzJlY2RkY2Y1MTFjNGJjZjhkYTViZDM1',
            'https://shortcutapp.io/n/NDczZmVmMWVmYzBhNWRjNWJkYmFiNjNiMDM2OGQ5Njg0']


class TestParseRecipeContent:
    # Tests for parsing the recipe
    def test_get_timestamp(self, get_test_recipe):
        assert get_timestamp(get_test_recipe) == '2021-07-09 13:04:45'

    def test_get_recipe_title(self, get_test_recipe):
        assert get_recipe_title(get_test_recipe) == 'Chilli Con Simon'

    def test_get_prep_time(self, get_test_recipe):
        assert get_prep_time(get_test_recipe) == 'about 1 hour'

    def test_get_serves(self, get_test_recipe):
        assert get_serves(get_test_recipe) == '4 persons'

    def test_get_difficulty(self, get_test_recipe):
        assert get_difficulty(get_test_recipe) == 'medium'

    def test_get_ingredients(self, get_test_recipe):
        assert get_ingredients(get_test_recipe) == [{'name': 'Peperoni (gelb)', 'quantity': '1'},
                                                    {'name': 'Zwiebel', 'quantity': '1'},
                                                    {'name': 'Knoblauch', 'quantity': '1 Zehe'},
                                                    {'name': 'Öl', 'quantity': '4 EL'},
                                                    {'name': 'Gemüsebujong', 'quantity': '1 EL'},
                                                    {'name': 'Büchse Pelati (Tomaten)', 'quantity': '1'},
                                                    {'name': 'Büchse Kidneybohnen', 'quantity': '1'},
                                                    {'name': 'Büchse Mais', 'quantity': '1'},
                                                    {'name': 'Kartoffeln', 'quantity': '300 g'},
                                                    {'name': 'Tomatenmark', 'quantity': '6 EL'},
                                                    {'name': 'Rinderhackfleisch oder Quorn', 'quantity': '500 g'},
                                                    {'name': 'Rotwein', 'quantity': '100 ml'},
                                                    {'name': 'Bier', 'quantity': '50 ml'},
                                                    {'name': 'Chilli je nach Schärfe', 'quantity': ''},
                                                    {'name': 'Basilikum und Oregano', 'quantity': '1 TL'},
                                                    {'name': 'Kakaopulver', 'quantity': '2 TL'},
                                                    {'name': 'Paprikapulver', 'quantity': '3 TL'},
                                                    {'name': 'Zimt', 'quantity': '1 TL'},
                                                    {'name': 'Kreuzkrümel (Pulver)', 'quantity': '2 TL'},
                                                    {'name': 'Salz', 'quantity': '2 TL'},
                                                    {'name': 'Espresso', 'quantity': '1'},
                                                    {'name': 'Sauercreme', 'quantity': '200 g'},
                                                    {'name': 'Chiabatta Brot', 'quantity': '1'}]

    def test_get_instructions(self, get_test_recipe):
        assert get_instructions(get_test_recipe) == [
            {'instruction': 'Alles klein schneiden und die Zutaten bis auf die Pelati aus '
                            'der Dose, in einem Sieb abwaschen.',
             'step': 'Step 1'},
            {'instruction': 'Die Zwiebeln mit Öl in der Pfanne andünsten. Danach das '
                            'Fleisch oder Quorn beigeben und goldbraun anbraten. '
                            'Anschliessend mit Rotwein, Bier und Espresso ablöschen.',
             'step': 'Step 2'},
            {'instruction': 'Die restlichen Zutaten und Gewürze hinzu gebeben und für 20 '
                            'min mit geschlossenem Deckel köcheln lassen. Danach für 10 '
                            'min unter ständigem rühren kochen, bis die gewünschte '
                            'Konsistenz erreicht ist.',
             'step': 'Step 3'},
            {'instruction': 'Mit Chiabatta Brot und einem Klecks Sauercreme servieren.',
             'step': 'Step 4'}]

    def test_get_category_from_recipe(self, get_test_main_page, get_test_recipe_link):
        assert get_category_from_recipe(get_test_main_page, get_test_recipe_link) == "hauptgang"

    def test_get_recipe_img_path(self, get_test_main_page, get_test_recipe_link):
        assert get_recipe_img_path(get_test_main_page, get_test_recipe_link) == 'img/hauptgang/chilliconcarne.jpg'

    def test_get_parsed_recipe(self, get_test_recipe_link, get_test_recipe_link_corrupt):
        assert get_parsed_recipe(get_test_recipe_link_corrupt) is None
        assert get_parsed_recipe(get_test_recipe_link) == {'difficulty': 'medium',
                                                           'img_path': 'img/hauptgang/chilliconcarne.jpg',
                                                           'ingredients': [{'name': 'Peperoni (gelb)', 'quantity': '1'},
                                                                           {'name': 'Zwiebel', 'quantity': '1'},
                                                                           {'name': 'Knoblauch', 'quantity': '1 Zehe'},
                                                                           {'name': 'Öl', 'quantity': '4 EL'},
                                                                           {'name': 'Gemüsebujong', 'quantity': '1 EL'},
                                                                           {'name': 'Büchse Pelati (Tomaten)',
                                                                            'quantity': '1'},
                                                                           {'name': 'Büchse Kidneybohnen',
                                                                            'quantity': '1'},
                                                                           {'name': 'Büchse Mais', 'quantity': '1'},
                                                                           {'name': 'Kartoffeln', 'quantity': '300 g'},
                                                                           {'name': 'Tomatenmark', 'quantity': '6 EL'},
                                                                           {'name': 'Rinderhackfleisch oder Quorn',
                                                                            'quantity': '500 g'},
                                                                           {'name': 'Rotwein', 'quantity': '100 ml'},
                                                                           {'name': 'Bier', 'quantity': '50 ml'},
                                                                           {'name': 'Chilli je nach Schärfe',
                                                                            'quantity': ''},
                                                                           {'name': 'Basilikum und Oregano',
                                                                            'quantity': '1 TL'},
                                                                           {'name': 'Kakaopulver', 'quantity': '2 TL'},
                                                                           {'name': 'Paprikapulver',
                                                                            'quantity': '3 TL'},
                                                                           {'name': 'Zimt', 'quantity': '1 TL'},
                                                                           {'name': 'Kreuzkrümel (Pulver)',
                                                                            'quantity': '2 TL'},
                                                                           {'name': 'Salz', 'quantity': '2 TL'},
                                                                           {'name': 'Espresso', 'quantity': '1'},
                                                                           {'name': 'Sauercreme', 'quantity': '200 g'},
                                                                           {'name': 'Chiabatta Brot', 'quantity': '1'}],
                                                           'instructions': [{
                                                                                'instruction': 'Alles klein schneiden und die Zutaten bis '
                                                                                               'auf die Pelati aus der Dose, in einem Sieb '
                                                                                               'abwaschen.',
                                                                                'step': 'Step 1'},
                                                                            {
                                                                                'instruction': 'Die Zwiebeln mit Öl in der Pfanne '
                                                                                               'andünsten. Danach das Fleisch oder Quorn '
                                                                                               'beigeben und goldbraun anbraten. '
                                                                                               'Anschliessend mit Rotwein, Bier und '
                                                                                               'Espresso ablöschen.',
                                                                                'step': 'Step 2'},
                                                                            {
                                                                                'instruction': 'Die restlichen Zutaten und Gewürze hinzu '
                                                                                               'gebeben und für 20 min mit geschlossenem '
                                                                                               'Deckel köcheln lassen. Danach für 10 min '
                                                                                               'unter ständigem rühren kochen, bis die '
                                                                                               'gewünschte Konsistenz erreicht ist.',
                                                                                'step': 'Step 3'},
                                                                            {
                                                                                'instruction': 'Mit Chiabatta Brot und einem Klecks '
                                                                                               'Sauercreme servieren.',
                                                                                'step': 'Step 4'}],
                                                           'prep_time': 'about 1 hour',
                                                           'recipe_class': 'hauptgang',
                                                           'serves': '4 persons',
                                                           'time': '2021-07-09 13:04:45',
                                                           'title': 'Chilli Con Simon'}

