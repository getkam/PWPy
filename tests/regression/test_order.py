def test_order1(login_set_up):
    login_set_up.wait_for_timeout(1000)
    assert login_set_up.is_logged_in()


def test_order2(login_set_up):
    login_set_up.wait_for_timeout(1000)
    assert login_set_up.is_logged_in()

def test_order3(login_set_up):
    login_set_up.wait_for_timeout(1000)
    assert login_set_up.is_logged_in()