
def job_li(li):
    job = '//*[@class="positionlist"]/div[' + str(li + 1) + ']'
    return job


def job_sc(i):
    sc = job_li(i) + '//*[contains(text(), "收藏")]'
    return sc


def job_sq(i):
    sc = job_li(i) + '//*[contains(text(), "申请职位")]'
    return sc


# 下一页
icon = '//*[@class="ui-icon-arrow-right"]'

# job名字
job_title = '//*[@class="summary-plane__title"]'
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
