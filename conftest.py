import pytest
from playwright.sync_api import sync_playwright
from pages.jsb_saas_zt.home import home_page as home
from pages.jsb_saas_zt.md import md_page

# 假设你有一个配置文件或环境变量来获取用户名和密码
# 这里我们仍然硬编码，但在实际项目中应避免这样做
USER = '18676770574'
PWD = '666666'


# 使用 pytest fixture 启动浏览器（module级别）
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        yield p.chromium.launch(channel="chrome", headless=False, slow_mo=1000)

    # 使用 pytest fixture 打开新页面并登录（function级别）


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    page.goto('https://midoffice.yhbtest.com/login')
    page.fill(home.user_input, USER)
    page.fill(home.pwd_input, PWD)
    page.click(home.login_btn)
    yield page
