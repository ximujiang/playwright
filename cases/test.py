from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # 启动一个chromium浏览器
    # context = browser.new_context()
    # page = browser.new_page()  # 打开一个新标签
    # page.goto('https://login.welink.huaweicloud.com/sso-proxy-front/#/logintenant')
    # page.wait_for_timeout(5000)
    # page.click('//*[@id="login"]/section/div[1]/section/section/div[1]/div[1]/div[1]/div')
    # page.fill('//*[@id="login"]/section/div[1]/section/section/div[1]/div/div[4]/div[1]/input', '18576797850')
    # page.click('text=获取验证码')
    # mima = input("请输入手机验证码：")
    # page.fill('//*[@id="login"]/section/div[1]/section/section/div[1]/div/div[4]/div[3]/div[1]/input', mima)
    # page.click('text=下一步')
    # print(page.title())
    # page.click('text=胡桃里')
    # page.fill('//*[@type="password"]', 'lkjLKJ+2023')
    # page.click('text=登录')
    # storage = context.storage_state(path="auth/state.json")

    context = browser.new_context(storage_state="auth/state.json")
    # 打开页面继续操作
    page = context.new_page()
    page.goto('https://login.welink.huaweicloud.com/sso-proxy-front/#/logintenant')

    page.pause()

    context.close()
    browser.close()
