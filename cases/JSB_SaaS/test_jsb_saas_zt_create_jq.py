import pytest
import allure
from pages.jsb_saas_zt.md import md_page
from common import common


@allure.story("添加店群")
def test_add_store_group(page):
    page.goto('https://midoffice.yhbtest.com/storesmanage')
    with allure.step("步骤1: 点击添加店群按钮"):
        page.click(md_page.add_store_group_btn)
    with allure.step("步骤2: 生成随机店群名称"):
        store_group_name = common.generate_random_chinese_title()
    with allure.step("步骤3: 输入店群名称"):
        page.fill(md_page.store_group_name_input, store_group_name)
    with allure.step("步骤4: 点击确定按钮  "):
        page.click(md_page.confirm_btn)


@allure.story("新建工坊")
def test_add_workshop(page):
    page.goto('https://midoffice.yhbtest.com/addworkshop?breadNum=2')
    with allure.step("步骤1: 生成随机工坊名称"):
        gf_name = common.generate_random_chinese_title()
    with allure.step("步骤2: 输入工坊名称"):
        page.fill(md_page.gf_input, gf_name)
    with allure.step("步骤3: 点击保存并编辑工坊商品按钮"):
        page.click(md_page.bcgf_btn)
    with allure.step("步骤4: 点击添加商品按钮"):
        page.click(md_page.add_sp_btn)
    with allure.step("步骤5: 全选商品"):
        page.click(md_page.qx_btn)
    with allure.step("步骤6: 选择商品后确定"):
        page.click(md_page.add_sp_qr_btn)
    with allure.step("步骤7: 点击保存按钮"):
        page.click(md_page.bc_btn)


@allure.story("新建区域")
def test_add_area(page):
    page.goto('https://midoffice.yhbtest.com/storearea')
    with allure.step("步骤1: 点击新建区域按钮"):
        page.click(md_page.add_qy_btn)
    with allure.step("步骤2: 生成区域名称"):
        qy_name = common.generate_random_chinese_title()
    with allure.step("步骤3: 输入区域名称"):
        page.fill(md_page.qy_name_input, qy_name)
    with allure.step("步骤4: 点击确定按钮"):
        page.click(md_page.qd_btn)


@allure.story("新建运费模板")
def test_add_freight_template(page):
    page.goto('https://midoffice.yhbtest.com/freightmanage')
    with allure.step("步骤1: 点击新增运费模板"):
        page.click(md_page.add_yfmb_btn)
    with allure.step("步骤2: 生成运费模板名称"):
        yfmb_name = common.generate_random_string(5)
    with allure.step("步骤3: 输入模板名称"):
        page.fill(md_page.yfmb_input, yfmb_name)
    with allure.step("步骤4: 输入统一运费"):
        page.fill(md_page.tyyf_input, "10")
    with allure.step("步骤5: 点击保存按钮"):
        page.click(md_page.bc_btn)
