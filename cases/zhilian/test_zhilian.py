from playwright.sync_api import sync_playwright

from pages.zhilian_page import zhilian_page as zp
import logging

with sync_playwright() as p:
    cdp = {
        "endpoint_url": 'http://localhost:12345/',
        "slow_mo": 600000
    }
    browser = p.chromium.connect_over_cdp(**cdp)
    # 获取page对象
    context = browser.contexts[0]
    page = context.pages[0]
    page.goto('https://sou.zhaopin.com/?jl=765&kw=%E6%B5%8B%E8%AF%95&kt=3&srccode=')
    page.get_by_text('最新发布').click()
    page.
    for i in range(29):
        # page.hover(zp.job_li(i))
        page.click(zp.job_li(i))
        page.pause()


    # page.click(boss_page.close)
    # # 查询软件测试岗位
    # page.fill(boss_page.search_input, "软件测试")
    # # 点击查询按钮
    # page.click(boss_page.search_btn)
    # page.click(boss_page.city_label)
    # # sz=深圳 fs=佛山 dg=东莞
    # c = boss_page.city('dg')
    # page.click(c[0])
    # page.click(c[1])
    # # 鼠标悬停学历要求
    # page.hover(boss_page.xl_btn)
    # # 点击大专
    # page.click(boss_page.dz_btn)
    # # 鼠标悬停薪资设置
    # page.hover(boss_page.xz_btn)
    # # 点击10-20K
    # page.click(boss_page.xz)
    # gt = []
    # for k in range(30):
    #     for i in range(30):
    #         with browser.contexts[0].expect_page() as new_page_info:
    #             page.click(boss_page.job_li(i))
    #         new_page = new_page_info.value
    #         # 获取job的名字
    #         text = new_page.inner_text(boss_page.job_title)
    #         # 获取是否已经沟通过
    #         text2 = new_page.inner_text(boss_page.communication_btn)
    #         job_sec_text = new_page.inner_text(boss_page.job_sec_text)
    #         job_boss_info = new_page.inner_text(boss_page.job_boss_info)
    #         if '测试' not in text:
    #             print('非测试岗')
    #         else:
    #             if '继续沟通' in text2:
    #                 print('已经沟通过了')
    #             else:
    #                 job_title_list = ['调试', '实习', '开发', '经理', '空调', '质量', '制冷', '硬件', '工艺', '销售',
    #                                   '客服', '认证', '储能', '评估', '灯具', '设备', '电源',
    #                                   '电控', '打包', '产品', '笔记本', '游戏', '整机', 'TE', '电子', '生产', '嵌入',
    #                                   '机器', '区块', '银行', 'c++', 'java', '顾问', 'sensor', '器械', '金融', 'QA',
    #                                   '英文',
    #                                   '客户端', '助理', '伺服', '医疗', '大数据', '充电', 'ERP', 'Linux', 'pcb', '粤语',
    #                                   '制', 'sdk', '管理']
    #                 job_title = [m for m in job_title_list if m in text]
    #                 job_len = len(job_title)
    #                 if job_len > 0:
    #                     print(f'岗位不太匹配:{job_title}')
    #                 else:
    #                     # print(job_sec_text)
    #                     job_sec_list = ['证券金融行业经验', '金融项目', '英语阅读能力', '银行系统', '银行项目',
    #                                     '英文可以读写', '硬件测试', '电路', '英文材料', '电源产品', '安规',
    #                                     '精通英语', '产品的检测', '熟悉家电', '大家电', '4级', '英语要求']
    #                     sec_text = [n for n in job_sec_list if n in job_sec_text]
    #                     # print(sec_text)
    #                     if len(sec_text) > 0:
    #                         text3 = sec_text[0]
    #                         print(f"太多要求了:{text3}")
    #                     else:
    #                         print(f"-------------------沟通中--------------------------------")
    #                         # print(f"{job_sec_text}")
    #                         new_page.click(boss_page.communication_btn)
    #                         gt.append("立即沟通")
    #                         gt_ci_shu = str(len(gt))
    #                         print(f'这是第{gt_ci_shu}次沟通')
    #         # new_page.pause()
    #         new_page.close()
    #     # 下一页
    #     page.click(boss_page.icon)
