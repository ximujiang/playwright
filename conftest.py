# import pytest
# import getpass
# from playwright.sync_api import BrowserType
# from typing import Dict
#
# USER_DIR_PATH = f'C:\\Users\\{getpass.getuser()}\\AppData\Local\Google\Chrome\\User Data'
#
#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         # "viewport": {
#         #     "width": 1920,
#         #     "height": 1080,
#         # },
#         "headless": False,
#         "slow_mo": 9000,  # 慢动作运行
#         # "no_viewport": True,  # 禁用窗口大小
#         "channel": "chrome",
#         "bypass_csp": True,
#         "user_data_dir": str(USER_DIR_PATH),
#         "ignore_https_errors": True  # 忽略https 错误
#     }
#
#
# @pytest.fixture(scope="session")
# def context(
#         browser_type: BrowserType,
#         browser_type_launch_args: Dict,
#         browser_context_args: Dict
# ):
#     print(browser_context_args)
#     context = browser_type.launch_persistent_context(
#         "./foobar",
#         **{**browser_type_launch_args,
#            **browser_context_args,
#            "locale": "de-DE", })
#     yield context
#     context.close()
