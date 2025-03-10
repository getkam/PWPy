import pytest

@pytest.mark.smoke
def test_login_positive(home_page, env_config)-> None:
    home_page.open_login_modal()
    home_page.enter_credentials(env_config.demoblaze_user, env_config.demoblaze_password)
    home_page.submit_login()
    assert home_page.is_logged_in()


def test_login_cancel(home_page) -> None:
    home_page.open_login_modal()
    home_page.enter_credentials("unimportant", "unimportant")
    home_page.cancel_login()
    assert home_page.is_logged_in() == False


@pytest.mark.parametrize("user_name, password, alert_msg",
                         [("","", "Please fill out Username and Password."),
                          ("$demoblazer_user", "", "Please fill out Username and Password."),
                          ("wrong", "credentials", "Wrong password."),
                          ("$demoblazer_user", "credentials", "Wrong password."),
                          ("' OR '1'='1'","' OR '1'='1'", "Wrong password."),
                          ("<img src=x onerror=alert('XSS')>", "<img src=x onerror=alert('XSS')>","User does not exist.")
                          ])
def test_login_credentials(home_page,env_config, user_name, password, alert_msg) -> None:
    if user_name == "$demoblazer_user":
        user_name = env_config.demoblaze_user

    home_page.open_login_modal()
    home_page.enter_credentials(user_name, password)
    home_page.handle_dialog()
    home_page.submit_login()
    assert alert_msg in home_page.get_dialog_message()

