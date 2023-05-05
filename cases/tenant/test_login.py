from playwright.sync_api import Page
import pytest
from pages.tenant import login


def test_login_tenant(page: Page):
    page.goto('https://welink.huaweicloud.com/web/app/#/admintenant/Homepage')
    # ch = page.locator(login.ch)
    # if ch.count() == 1:
    #     page.click(login.ch)
    # page.click(login.switch_icon)
    # page.get_by_placeholder('手机号').fill('18576797850')
    # page.get_by_text('获取验证码').click()
    # # text = input("请输入验证码：")
    # # page.get_by_placeholder('验证码').fill(text)
    # page.get_by_text('下一步').click()
    # page.get_by_text('胡桃里办公有限公司').click()
    # page.get_by_placeholder('密码').fill('lkjLKJ+2023')
    print(page.title())
    page.pause()


if __name__ == '__main__':
    pytest.main()
# https://welink.huaweicloud.com/sso-proxy-front/#/logintenant/cloudsecondlogin
# https://login.welink.huaweicloud.com/sso-proxy-front/#/logintenant/cloudsecondlogin
