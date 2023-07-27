#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import threading
from selenium import webdriver
from ui_test.util.config_reader import ConfigReader
# from ui_test.util.mysql_tool import MysqlTool
# from ui_test.util.redis_pool import RedisPool
from ui_test.util.thread_local_storage import ThreadLocalStorage
#from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.ie.options import Options as IeOptions


# 初始装配工具（一个线程分配一个驱动，一个 redis 连接，一个 mysql 连接）
class Assembler:
    # 初始化所有工具
    def __init__(self):
        # 驱动装配
        self.assemble_driver()
        ThreadLocalStorage.set(threading.current_thread(), self)

    # 卸下所有
    def disassemble_all(self):
        # 卸下驱动
        self.disassemble_driver()
        ThreadLocalStorage.clear_current_thread()

    ############################## 驱动 ##############################
    # 装配驱动
    def assemble_driver(self):
        # 若是谷歌驱动
        if ConfigReader().read("project")["driver"].lower() == "chrome":
            # chrome option
            chrome_options = ChromeOptions()
            # 服务端 root 用户不能直接运行 chrome，添加此参数可以运行
            chrome_options.add_argument('--no-sandbox')
            # # 下面参数可自行选择
            # chrome_options.add_argument('--user-data-dir')
            # chrome_options.add_argument('--dns-prefetch-disable')
            # chrome_options.add_argument('--lang=en-US')
            # chrome_options.add_argument('--disable-setuid-sandbox')
            # chrome_options.add_argument('--disable-gpu')

            # 驱动路径
            executable_path = os.path.abspath(os.path.dirname(__file__))[
                              :os.path.abspath(os.path.dirname(__file__)).find("ui_test") + len(
                                  "ui_test")] + ConfigReader().read("driver")[
                                  "chrome_driver_path"]
            # 获取chrome驱动
            self.driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)

        # 若是火狐驱动
        elif ConfigReader().read("project")["driver"].lower() == "firefox":
            # firefox option
            firefox_options = FirefoxOptions()
            # 服务端 root 用户不能直接运行 chrome，添加此参数可以运行
            firefox_options.add_argument('--no-sandbox')
            # 驱动路径
            executable_path = os.path.abspath(os.path.dirname(__file__))[
                              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("driver")[
                                  "firefox_driver_path"]
            # 获取驱动自己产出日志路径
            log_path = os.path.abspath(os.path.dirname(__file__))[
                       :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                           "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("log")["logfile_path"]
            self.driver = webdriver.Firefox(executable_path=executable_path, log_path=log_path + "geckodriver.log",
                                            firefox_options=firefox_options)

        # 若是 IE 驱动
        elif ConfigReader().read("project")["driver"].lower() == "ie":
            # ie option
            ie_options = IeOptions()
            # 服务端 root 用户不能直接运行 chrome，添加此参数可以运行
            ie_options.add_argument('--no-sandbox')
            # 驱动路径
            executable_path = os.path.abspath(os.path.dirname(__file__))[
                              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("driver")["ie_driver_path"]
            self.driver = webdriver.Ie(executable_path=executable_path, ie_options=ie_options)

        # 若是 Edge 驱动
        elif ConfigReader().read("project")["driver"].lower() == "edge":
            executable_path = os.path.abspath(os.path.dirname(__file__))[
                              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("driver")[
                                  "edge_driver_path"]
            self.driver = webdriver.Edge(executable_path=executable_path)

        # 若是欧朋驱动
        elif ConfigReader().read("project")["driver"].lower() == "opera":
            executable_path = os.path.abspath(os.path.dirname(__file__))[
                              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("driver")[
                                  "opera_driver_path"]
            self.driver = webdriver.Opera(executable_path=executable_path)

        # 若是 Safari 驱动
        elif ConfigReader().read("project")["driver"].lower() == "safari":
            executable_path = os.path.abspath(os.path.dirname(__file__))[
                              :os.path.abspath(os.path.dirname(__file__)).find("python-ui-auto-test") + len(
                                  "python-ui-auto-test")] + "/ui-test" + ConfigReader().read("driver")[
                                  "safari_driver_path"]
            self.driver = webdriver.Safari(executable_path=executable_path)

        # 不支持的浏览器类型
        else:
            self.driver = None
            raise RuntimeError("配置文件中配置了不支持的浏览器类型！请修改浏览器类型！")

    # 卸下驱动
    def disassemble_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None

    # 获取驱动
    def get_driver(self):
        return self.driver

