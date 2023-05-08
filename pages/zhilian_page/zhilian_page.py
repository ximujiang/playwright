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
next_button = '//*[@class="pagination clearfix"]//*[contains(text(), "下一页")]'

# job名字
job_title = '//*[@class="summary-plane__title"]'
# job要求
job_detail = '//*[@class="describtion__detail-content"]'

job_title_list = ['调试', '实习', '开发', '经理', '空调', '质量', '制冷', '硬件', '工艺', '销售',
                  '客服', '认证', '储能', '评估', '灯具', '设备', '电源',
                  '电控', '打包', '产品', '笔记本', '游戏', '整机', 'TE', '电子', '生产', '嵌入',
                  '机器', '区块', '银行', 'c++', 'java', '顾问', 'sensor', '器械', '金融', 'QA',
                  '英文', '班主任', '讲师', '电商',
                  '客户端', '助理', '伺服', '医疗', '大数据', '充电', 'ERP', 'Linux', 'pcb', '粤语',
                  '制', 'sdk', '管理']

job_sec_list = ['证券金融行业经验', '金融项目', '英语阅读能力', '银行系统', '银行项目',
                '英文可以读写', '硬件测试', '电路', '英文材料', '电源产品', '安规',
                '精通英语', '产品的检测', '熟悉家电', '大家电', '4级', '英语要求']

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
