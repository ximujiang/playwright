from playwright.sync_api import sync_playwright

from pages.boss_page import boss_page as bs
import logging

# 上海悠悠 wx:283340479
# blog:https://www.cnblogs.com/yoyoketang/


with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp('http://localhost:12345/', slow_mo=10000)
    # 获取page对象
    page = browser.contexts[0].pages[0]
    # context = browser.new_context()
    # page = context.new_page()
    page.goto('https://www.zhipin.com/web/geek/job?query=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95&city=101280600')
    # page.click(bs.close)
    gt = []
    for k in range(30):
        for i in range(30):
            with browser.contexts[0].expect_page() as new_page_info:
                page.click(bs.job_li(i))
            new_page = new_page_info.value
            # 获取job的名字
            text = new_page.inner_text(bs.job_title)
            # 获取是否已经沟通过
            text2 = new_page.inner_text(bs.communication_btn)
            job_sec_text = new_page.inner_text(bs.job_sec_text)
            job_boss_info = new_page.inner_text(bs.job_boss_info)
            if '测试' not in text:
                logging.info('非测试岗')
            else:
                if '继续沟通' in text2:
                    logging.info('已经沟通过了')
                else:
                    job_title = [m for m in bs.job_title_list if m in text]
                    job_len = len(job_title)
                    if job_len > 0:
                        logging.info(f'岗位不太匹配:{job_title}')
                    else:
                        sec_text = [n for n in bs.job_sec_list if n in job_sec_text]
                        # print(sec_text)
                        if len(sec_text) > 0:
                            text3 = sec_text[0]
                            logging.info(f"太多要求了:{text3}")
                        else:
                            logging.info(f"-------------------沟通中--------------------------------")
                            # print(f"{job_sec_text}")
                            new_page.click(bs.communication_btn)
                            gt.append("立即沟通")
                            gt_ci_shu = str(len(gt))
                            logging.info(f'这是第{gt_ci_shu}次沟通')
            # new_page.pause()
            new_page.close()
        # 下一页
        page.click(bs.icon)
