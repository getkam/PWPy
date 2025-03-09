import pytest

@pytest.mark.smoke
def test_login_positive(home_page, env_config)-> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials(env_config.demoblaze_user, env_config.demoblaze_password)
    home_page.submit_login()
    assert home_page.is_logged_in()


def test_login_cancel(home_page) -> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials("unimportant", "unimportant")
    home_page.cancel_login()
    assert home_page.is_logged_in() == False


def test_login_empty_credentials(home_page) -> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials("", "")
    home_page.handle_dialog()
    home_page.submit_login()
    assert "Please fill out Username and Password." in home_page.get_dialog_message()


def test_login_empty_password(home_page, env_config) -> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials(env_config.demoblaze_user, "")
    home_page.handle_dialog()
    home_page.submit_login()
    assert "Please fill out Username and Password." in home_page.get_dialog_message()


def test_login_wrong_credentials(home_page) -> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials("wrong", "credentials")
    home_page.handle_dialog()

    home_page.submit_login()
    assert "Wrong password." in home_page.get_dialog_message()


def test_login_wrong_password(home_page, env_config) -> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials(env_config.demoblaze_user, "wrong_password")
    home_page.handle_dialog()

    home_page.submit_login()
    assert "Wrong password." in home_page.get_dialog_message()


def test_login_sql_injection(home_page) -> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials("' OR '1'='1'", "' OR '1'='1'")
    home_page.handle_dialog()

    home_page.submit_login()
    assert "Wrong password." in home_page.get_dialog_message()


def test_login_xss_injection(home_page) -> None:
    home_page.goto()
    home_page.open_login_modal()
    home_page.enter_credentials("<img src=x onerror=alert('XSS')>", "<img src=x onerror=alert('XSS')>")
    home_page.handle_dialog()

    home_page.submit_login()
    assert "User does not exist." in home_page.get_dialog_message()