from pages.swag_labs import SwagLabs


def test_check_icon(browser):
    swag_labs_page= SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_element('div.login_logo')
    # assert swag_labs_page.exist_icon()

def test_check_login(browser):
    swag_labs_page= SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_element('#user-name')
    # assert swag_labs_page.exist_login()

def test_check_password(browser):
    swag_labs_page= SwagLabs(browser)
    swag_labs_page.visit()
    assert swag_labs_page.exist_element('#password')
    # assert swag_labs_page.exist_password()