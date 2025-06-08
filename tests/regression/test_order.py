from playwright.sync_api import expect

from src.pom.pages.cart_page import CartPage
from src.pom.pages.product_page import ProductPage
from tests.conftest import product_page


def test_order1(login_set_up):

    login_set_up.click_on_product("Samsung galaxy s6")
    product_page = ProductPage(login_set_up.page)

    expect(product_page.product_name).to_have_text("Samsung galaxy s6")
    expect(product_page.product_price).to_contain_text("360")

    product_page.handle_dialog()
    product_page.click_add_to_cart()
    assert "Product added" in product_page.get_dialog_message()
    product_page.header.click_cart()
    cart_page = CartPage(product_page.page())
    expect(cart_page.product_title(1)).to_have_text("Samsung galaxy s6")
    assert cart_page.total_price.text_content() == "360"


def test_order2(login_set_up):
    #login_set_up.wait_for_timeout(1000)
    assert login_set_up.header.is_logged_in_as("pwpy")