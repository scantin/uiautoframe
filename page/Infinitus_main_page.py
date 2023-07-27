import time

from ui_test.common.page_common import PageCommon
from ui_test.data.Infinitus_data import InfinitusData
from ui_test.data.Infinitus_tw_main_data_backup import InfinitusTwMainData
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from ui_test.locator.infintus_main_locator import InfinitusLocator
import random
import re

# 百度首页页面类
class InfinitusMainPage(PageCommon):
    # 百度首页进入页面操作
    def jump_to(self, url):
        self.driver.get(url)

    # vip电话登录
    def login_vip(self):
        #通过xpath定位账户按钮
        account_icon = self.find_element(*InfinitusLocator.account_xpath)
        #鼠标悬停在账户按钮
        mouse = ActionChains(self.driver)
        mouse.move_to_element(account_icon).perform()
        #点击登录按钮
        self.click_element(*InfinitusLocator.login_btn)
        #输入电话号码
        self.input(InfinitusData.phone, *InfinitusLocator.phone_input)
        #输入密码
        self.input(InfinitusData.password, *InfinitusLocator.password_input)
        #获取动态验证码
        code = self.getcode(*InfinitusLocator.code_xpath)
        #输入验证码
        self.input(code, *InfinitusLocator.code_input)
        #点击登录
        self.click_element(*InfinitusLocator.login)


    # vip邮箱登录
    def login_vipemail(self):
        #通过xpath定位账户按钮
        account_icon = self.find_element(*InfinitusLocator.account_xpath)
        #鼠标悬停在账户按钮
        mouse = ActionChains(self.driver)
        mouse.move_to_element(account_icon).perform()
        #点击登录按钮
        self.click_element(*InfinitusLocator.login_btn)
        self.click_element(*InfinitusLocator.login_type)
        self.click_element(*InfinitusLocator.login_email)
        #输入邮箱
        self.input(InfinitusData.email, *InfinitusLocator.email_input)
        #输入密码
        self.input(InfinitusData.password, *InfinitusLocator.password_input)
        print("Password is " + InfinitusData.password)
        #获取动态验证码
        code = self.getcode(*InfinitusLocator.code_xpath)
        #输入验证码
        self.input(code, *InfinitusLocator.code_input)
        #点击登录
        self.click_element(*InfinitusLocator.login)

    # tw vip登录
    def login_dis(self):
        #通过xpath定位账户按钮
        account_icon = self.find_element(*InfinitusLocator.account_xpath)
        #鼠标悬停在账户按钮
        mouse = ActionChains(self.driver)
        mouse.move_to_element(account_icon).perform()
        #点击登录按钮
        self.click_element(*InfinitusLocator.login_btn)
        self.click_element(*InfinitusLocator.login_type)
        self.click_element(*InfinitusLocator.login_membership_card)
        #输入电话号码
        self.input(InfinitusData.membership_card, *InfinitusLocator.membership_card)
        #输入密码
        self.input(InfinitusData.password_card, *InfinitusLocator.password_input)
        #获取动态验证码
        code = self.getcode(*InfinitusLocator.code_xpath)
        #输入验证码
        self.input(code, *InfinitusLocator.code_input)
        #点击登录
        self.click_element(*InfinitusLocator.login)

    # 搜索产品
    def search(self, product, *args):
        #输入搜索的产品
        self.input(product, *args)


    #清空购物车
    def clearcart(self):
        # 通过xpath定位删除按钮
        delete_icon = self.find_element(*InfinitusLocator.cart_product)
        # 鼠标悬停在账户按钮
        mouse = ActionChains(self.driver)
        mouse.move_to_element(delete_icon).perform()
        self.click_element(*InfinitusLocator.clear_cart)
        self.click_element(*InfinitusLocator.confirm_clear_cart)

    #tw 随机category
    def random_category_filter(self):
        category_icon = self.find_element(*InfinitusLocator.category_btn)
        # 鼠标悬停在账户按钮
        mouse = ActionChains(self.driver)
        mouse.move_to_element(category_icon).perform()
        # 定位所有分类列表
        category_list = self.find_elements(*InfinitusLocator.category_filter)
        # 获取列表长度
        i = len(category_list)
        # 随机点击分类
        xpath = InfinitusLocator.category_filter[1] + "[" + str(random.randint(1, i)) + "]"
        #xpath = InfinitusLocator.category_filter[1] + "[4]"
        category_filter = (InfinitusLocator.category_filter[0], xpath)
        return category_filter

    def random_area_filter_global(self):
        # 定位所有区域
        area_list = self.find_elements(*InfinitusLocator.area_filter)
        # 获取列表长度
        i = len(area_list)
        # 随机点击价格区间
        xpath = InfinitusLocator.area_filter[1] + "[" + str(random.randint(2, 3)) + "]" + "/label/span[2]/span[1]"
        print("xpath is" + xpath)
        area_filter = (InfinitusLocator.area_filter[0], xpath)
        return area_filter

    #tw 随机价格区间
    def random_price_filter_tw(self):
        # 定位所有价格区间列表
        price_list = self.find_elements(*InfinitusLocator.price_filter_tw)
        # 获取列表长度
        i = len(price_list)
        # 随机点击价格区间
        xpath = InfinitusLocator.price_filter_tw[1] + "[" + str(random.randint(1, i)) + "]" + "/label/span[2]/span[1]"
        print("xpath is" + xpath)
        price_filter = (InfinitusLocator.price_filter_tw[0], xpath)
        #获取价格区间边界值
        price_filter_text = self.find_element_attribute('innerHTML', *price_filter)
        price_filter_text = price_filter_text.split("-")
        self.lower_price = float(price_filter_text[0])
        self.upper_price = float(price_filter_text[1])
        print(self.lower_price)
        print(self.upper_price)
        return price_filter

    #global 随机价格区间
    def random_price_filter_global(self):
        # 定位所有价格区间列表
        price_list = self.find_elements(*InfinitusLocator.price_filter_global)
        # 获取列表长度
        i = len(price_list)
        # 随机点击价格区间
        xpath = InfinitusLocator.price_filter_global[1] + "[" + str(random.randint(1, i)) + "]" + "/label/span[2]/span[1]"
        print("xpath is" + xpath)
        price_filter = (InfinitusLocator.price_filter_global[0], xpath)
        #获取价格区间边界值
        price_filter_text = self.find_element_attribute('innerHTML', *price_filter)
        price_filter_text = price_filter_text.split("-")
        self.lower_price = float(price_filter_text[0])
        self.upper_price = float(price_filter_text[1])
        return price_filter


    #tw 随机品牌
    def random_brand_filter_tw(self):
        # 定位所有品牌
        brand_list = self.find_elements(*InfinitusLocator.brand_filter_tw)
        # 获取列表长度
        i = len(brand_list)
        # 随机点击品牌
        xpath = InfinitusLocator.brand_filter_tw[1] + "[" + str(random.randint(1, i)) + "]" + "/div"
        print("xpath is" + xpath)
        brand_filter = (InfinitusLocator.brand_filter_tw[0], xpath)
        return brand_filter

    #global 随机品牌
    def random_brand_filter_global(self):
        # 定位所有品牌
        brand_list = self.find_elements(*InfinitusLocator.brand_filter_global)
        # 获取列表长度
        i = len(brand_list)
        # 随机点击品牌
        xpath = InfinitusLocator.brand_filter_global[1] + "[" + str(random.randint(1, i)) + "]" + "/div"
        print("xpath is" + xpath)
        brand_filter = (InfinitusLocator.brand_filter_global[0], xpath)
        return brand_filter

    #分类筛选
    def filter_tw(self):
        category_filter = self.random_category_filter()
        self.click_element(*category_filter)
        time.sleep(5)
        price_filter = self.random_price_filter_tw()
        self.click_element(*price_filter)
        time.sleep(5)
        brand_filter = self.random_brand_filter_tw()
        self.click_element(*brand_filter)
        time.sleep(5)
        self.click_element(*InfinitusLocator.filter_confirm_btn_tw)
        time.sleep(5)

    #分类筛选
    def filter_global(self):
        category_filter = self.random_category_filter()
        self.click_element(*category_filter)
        time.sleep(5)
        area_filter = self.random_area_filter_global()
        self.click_element(*area_filter)
        time.sleep(5)
        price_filter = self.random_price_filter_global()
        self.click_element(*price_filter)
        time.sleep(5)
        brand_filter = self.random_brand_filter_global()
        self.click_element(*brand_filter)
        time.sleep(5)
        self.click_element(*InfinitusLocator.filter_confirm_btn_global)
        time.sleep(5)


    #tw infinitus结账
    def infinitus_checkout_tw(self):
        self.click_element(*InfinitusLocator.cart_btn)
        self.click_element(*InfinitusLocator.checkout_btn_tw)
        time.sleep(5)
        self.click_element(*InfinitusLocator.terms_of_sale_tw)
        time.sleep(5)
        self.click_element(*InfinitusLocator.submit_btn_tw)

    #global infinitus结账
    def infinitus_checkout_global(self):
        self.click_element(*InfinitusLocator.cart_btn)
        self.click_element(*InfinitusLocator.checkout_btn_global)
        self.click_element(*InfinitusLocator.checkout_btn_global_popup)
        self.click_element(*InfinitusLocator.terms_of_sale_global)
        time.sleep(5)
        self.click_element(*InfinitusLocator.submit_btn_global)

    #ctbc付款
    def ctbc_checkout(self):
        self.input(InfinitusData.ctbc_cardnum, *InfinitusLocator.ctbc_cardnum)
        time.sleep(2)
        self.input(InfinitusData.ctbc_cvv, *InfinitusLocator.ctbc_cvv)
        #time.sleep(2)
        # self.click_element(*InfinitusLocator.ctbc_month_selector)
        # time.sleep(2)
        # self.click_element(*InfinitusLocator.ctbc_month)
        # time.sleep(2)
        # self.click_element(*InfinitusLocator.ctbc_year_selector)
        # time.sleep(2)
        # self.click_element(*InfinitusLocator.ctbc_year)
        time.sleep(2)
        self.input(InfinitusData.ctbc_security_code, *InfinitusLocator.ctbc_security_code)
        time.sleep(2)
        self.click_element(*InfinitusLocator.ctbc_confirm_checkout)

    #stripe付款
    def stripe_checkout(self):
        self.input(InfinitusData.stripe_cardnum, *InfinitusLocator.stripe_cardnum)
        time.sleep(2)
        self.input(InfinitusData.stripe_date, *InfinitusLocator.stripe_date)
        time.sleep(2)
        self.input(InfinitusData.stripe_cvv, *InfinitusLocator.stripe_cvv)
        time.sleep(2)
        self.input(InfinitusData.stripe_name, *InfinitusLocator.stripe_name)
        time.sleep(2)
        self.click_element(*InfinitusLocator.stripe_confirm_checkout)


    def order(self):
        #通过xpath定位账户按钮
        account_icon = self.find_element(*InfinitusLocator.account_xpath)
        #鼠标悬停在账户按钮
        mouse = ActionChains(self.driver)
        mouse.move_to_element(account_icon).perform()
        time.sleep(2)
        self.click_element(*InfinitusLocator.my_order)

    def getorderdetail(self):
        self.order()
        order_num1 = self.find_element_attribute('innerHTML', *InfinitusLocator.order_num1)
        order_num2 = self.find_element_attribute('innerHTML', *InfinitusLocator.order_num2)
        order_payment_status = self.find_element_attribute('innerHTML', *InfinitusLocator.order_payment_status)
        return order_num1, order_num2, order_payment_status

    def logout(self):
        # 通过xpath定位账户按钮
        account_icon = self.find_element(*InfinitusLocator.account_xpath)
        # 鼠标悬停在账户按钮
        mouse = ActionChains(self.driver)
        mouse.move_to_element(account_icon).perform()
        self.click_element(*InfinitusLocator.logout_btn)

    def getprice(self, price):
        price = price.strip()
        price = re.findall(r'(\d+,.+|\d+.+)', price)[0]
        price = price.replace(",", "")
        return float(price)
