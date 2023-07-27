#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from ui_test.common.browser_common import BrowserCommon
from aip import AipOcr
from selenium.webdriver.common.action_chains import ActionChains
from ui_test.locator.infintus_main_locator import InfinitusLocator

# Page 项目无关页面类封装基本页面操作
class PageCommon(BrowserCommon):

    ############################## 基本方法再封装 ##############################
    # 查找指定元素
    def find_element(self, *args):
        """
        查找元素
        :param xpath: 元素定位
        :return: 原生通过 xpath 找元素方法
        """
        return self.driver.find_element(*args)
    #通过定位元素，返回对应属性值
    def find_element_attribute(self, attr, *args):
        return self.driver.find_element(*args).get_attribute(attr)

    # 查找指定的一批元素
    def find_elements(self, *args):
        """
        找多元素
        :param args: 定位与通过什么定位
        :return: 原生找多元素方法
        """
        return self.driver.find_elements(*args)

    ############################## 单个元素操作 ##############################
    # 点击元素
    def click_element(self, *args):
        """
        点击元素
        :param By.x: 元素定位
        :return: 返回原生点击事件
        """
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(args))
        # 点击元素
        ele = self.driver.find_element(*args)
        if args[1] in [InfinitusLocator.terms_of_sale_tw[1], InfinitusLocator.terms_of_sale_global[1], InfinitusLocator.ctbc_month[1], InfinitusLocator.ctbc_year[1]]:
            self.driver.execute_script("arguments[0].click();", ele)
        else:
            #偏移5像素点击
            ActionChains(self.driver).move_to_element(ele).move_by_offset(3, 3).click().perform()


    #点击销售条款
    def click_element_term(self, *args):
        """
        点击元素
        :param By.x: 元素定位
        :return: 返回原生点击事件
        """
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(args))
        # 点击元素
        ele = self.driver.find_element(*args)
        #偏移5像素点击
        self.driver.execute_script("arguments[0].click();", ele)

    # 输入框输入数据
    def input(self, value, *args):
        """
        输入值
        :param By.x: 元素定位
        :param value: 输入值
        :return: 返回 send_keys 原生方法
        """
        # 显示等待元素可点击
        WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(args))
        # 输入框输入数据
        self.driver.find_element(*args).send_keys(value)

    #动态验证码OCR
    def getcode(self, *args):
        #百度ocr app_id, key, secret
        APP_ID = '26673818'
        API_KEY = 'dRvOpcp9Z7ddzfkuXc83Kdbr'
        SECRET_KEY = '3Y4ce8WTKhzIlbDnwjb45BPXN1j403CF'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        i = 1
        #动态获取验证码，10s内获取不到重试，10s超时退出
        while(1):
            try:
                src_url = self.find_element_attribute('src', *args)
                res_url = client.basicGeneralUrl(src_url)
                code = res_url.get('words_result')[0].get('words')
                time.sleep(1)
                i += 1
                return code
            except:
                if i < 10:
                    continue
                else:
                    break


    #判断元素是否存在
    def iselementexisted(self, *args):
        try:
            # 显示等待元素可点击
            WebDriverWait(self.driver, 10, 0.1).until(expected_conditions.element_to_be_clickable(args))
            self.find_element(*args)
            return True
        except:
            return False

