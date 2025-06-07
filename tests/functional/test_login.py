import pytest
from playwright.sync_api import expect

@pytest.mark.smoke
def test_login_positive(home_page, env_config)-> None:
    login_modal = home_page.open_login_modal()
    login_modal.enter_credentials(env_config.demoblaze_user, env_config.demoblaze_password)
    login_modal.submit_login()
    assert home_page.header.is_logged_in_as(env_config.demoblaze_user)


def test_login_cancel(home_page, env_config) -> None:
    login_modal = home_page.open_login_modal()
    login_modal.enter_credentials(env_config.demoblaze_user, env_config.demoblaze_password)
    login_modal.cancel_login()
    expect(home_page.header.login).to_be_visible()
    expect(home_page.header.signup).to_be_visible()
    expect(home_page.header.username).not_to_be_visible()


@pytest.mark.parametrize("user_name, password, alert_msg",
                         [("","", "Please fill out Username and Password."),
                          ("$demoblazer_user", "", "Please fill out Username and Password."),
                          ("wrong", "credentials", "Wrong password."),
                          ("$demoblazer_user", "credentials", "Wrong password."),
                          ("' OR '1'='1'","' OR '1'='1'", "Wrong password.")
                          ])
def test_login_credentials(home_page,env_config, user_name, password, alert_msg) -> None:
    if user_name == "$demoblazer_user":
        user_name = env_config.demoblaze_user

    login_modal = home_page.open_login_modal()
    login_modal.enter_credentials(user_name, password)
    home_page.handle_dialog()
    login_modal.submit_login()
    assert alert_msg in home_page.get_dialog_message()

