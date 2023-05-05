# 登录按钮
login_btn = '//*[@id="header"]/div[1]/div[4]/div/a[4]'
# APP扫码登录
APP_btn = '//*[@id="wrap"]/div/div[2]/div[2]/div[1]'
# 首页
herder_home_btn = '//*[contains(text(), "首页")]'
# 输入框
search_input = '//*[@name="query"]'
# 搜索按钮
search_btn = '//*[@id="wrap"]/div[3]/div/div[1]/div[1]/form/button'
# 学历要求
xl_btn = '//*[@id="wrap"]/div[2]//span[contains(text(), "学历要求")]'
# 大专
dz_btn = '//*[@id="wrap"]/div[2]/div[1]//*[contains(text(), "大专")]'
# 薪资待遇
xz_btn = '//*[@id="wrap"]/div[2]//*[contains(text(), "薪资待遇")]'
# 薪资设置
xz = '//*[@id="wrap"]/div[2]/div[1]//*[contains(text(), "10-20K")]'


def job_li(li):
    job = '//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[1]/ul/li[' + str(li + 1) + ']/div[1]/a'
    return job


# 下一页
icon = '//*[@class="ui-icon-arrow-right"]'

# job名字
job_title = '//*[@id="main"]/div[1]/div/div/div[1]/div[2]/h1'
# 立即沟通按钮
communication_btn = '//*[@id="main"]/div[1]/div/div/div[1]/div[3]/div[1]/a[2]'
job_sec_text = '//*[@class="job-sec-text"]'

job_boss_info = '//*[@class="job-boss-info"]'
# 城市
city_label = '//*[@class="city-label"]'

#

# 广告X
close = '//*[@class="active-close"]'

# 城市
sz = 'text="深圳"'
# 城市
city_area = '//*[@class="city-area-dropdown"]//*[contains(text(), "东莞")]'

# abcde
abcde = '//*[contains(text(), "ABCDE")]'
# fghj
fghj = '//*[contains(text(), "FGHJ")]'


# KLMN
def city(c):
    if c == 'sz':
        klmn = f'//*[contains(text(), "PQRST")]'
        city = '//*[@class="city-select-wrapper"]//*[contains(text(), "深圳")]'
        return klmn, city
    elif c == 'fs':
        klmn = f'//*[contains(text(), "FGHJ")]'
        city = '//*[@class="city-select-wrapper"]//*[contains(text(), "佛山")]'
        return klmn, city
    elif c == 'dg':
        klmn = f'//*[contains(text(), "ABCDE")]'
        city = '//*[@class="city-select-wrapper"]//*[contains(text(), "东莞")]'
        return klmn, city