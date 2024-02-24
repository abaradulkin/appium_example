from allure import title
from pytest import *

from ui import first_page


class TestSmoke:
    @title("Verify is first quest can be loaded")
    def test_start_game(self):
        assert first_page.wait_game_loaded()
        first_page.click_skip_button()
        assert first_page.is_first_quest_dialog()
