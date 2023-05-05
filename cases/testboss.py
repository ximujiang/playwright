from playwright.sync_api import Playwright, sync_playwright
import boss_page


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.zhipin.com/shenzhen/")
    page.click(boss_page.login_btn)
    page.click(boss_page.APP_btn)
    sm = input("请扫码:")
    print(sm)
    page.click(boss_page.herder_home_btn)
    page.goto("https://www.zhipin.com/shenzhen/?ka=header-home")
    page.fill(boss_page.search_input, "软件测试")
    page.click(boss_page.search_btn)
    page.locator("div:nth-child(7) > .filter-select-dropdown > ul > li:nth-child(5)").click()
    page.get_by_text("10-20K").click()
    page.pause()
    with page.expect_popup() as page1_info:
        page.get_by_role("link",
                         name="测试（双休！待遇好！节假日不补班！） [ 深圳·福田区·会展中心 ] 11-12K 3-5年 大专 继续沟通 在线").click()
    page1 = page1_info.value
    page1.close()
    page.get_by_role("link", name="立即沟通", exact=True).click()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
