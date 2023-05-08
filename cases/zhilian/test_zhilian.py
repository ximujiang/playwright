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
    page.goto('https://sou.zhaopin.com/?jl=765&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&p=1')
    page.get_by_text('最新发布').click()
    gt = []
    for k in range(30):
        for i in range(29):
            with context.expect_page() as new_page_info:
                page.click(zp.job_li(i))
            new_page = new_page_info.value
            # 获取job的名字
            job_title = new_page.inner_text(zp.job_title)
            job_detail = new_page.inner_text(zp.job_detail)
            if '测试' not in job_title:
                logging.info('非测试岗')
            else:
                zw = new_page.get_by_role('button', name='申请职位')
                if zw:
                    # 判断job标题是否有不符的关键字
                    job_list = [m for m in zp.job_title_list if m in job_title]
                    if len(job_list) > 0:
                        logging.info(f'岗位不太匹配:{job_list}')
                    else:
                        # 判断job内容是否有不符的关键字
                        job_text_list = [n for n in zp.job_sec_list if n in job_detail]
                        if len(job_text_list) > 0:
                            logging.info(f'太多要求了吧:{job_text_list}')
                        else:
                            logging.info(f"-------------------沟通中--------------------------------")
                            gt.append("申请")
                            gt_ci_shu = str(len(gt))
                            with context.expect_page() as td_page_info:
                                zw.click()
                            td_page = td_page_info.value
                            logging.info(f'这是第{gt_ci_shu}次沟通')
                            # page.pause()
                            logging.info(f'本次沟通的职位是:{job_title}')
                            logging.info(f'本次沟通的职位信息是:{job_detail}')
                            td_page.close()
                else:
                    logging.info("已经申请过了，无法申请！")
            new_page.close()
        # 下一页
        page.click(zp.next_button)
