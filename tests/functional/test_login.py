import pytest
from src.pom.demoblazer_pom import Demoblazer

def test_login(demoblazer: Demoblazer)-> None:
    import sys
    print(sys.path)
    demoblazer.home_page.goto()
    demoblazer.home_page.login()
    assert demoblazer.home_page.is_logged_in()