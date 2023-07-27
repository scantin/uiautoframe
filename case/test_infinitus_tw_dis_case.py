import time
import unittest
import paramunittest
from BeautifulReport import BeautifulReport
from ui_test.base.assembler import Assembler
from ui_test.page.Infinitus_main_page import InfinitusMainPage
from ui_test.util.config_reader import ConfigReader
from ui_test.util.log_tool import start_info, end_info, log
from ui_test.util.screenshot_tool import ScreenshotTool
from ui_test.locator.infintus_main_locator import InfinitusLocator
from ui_test.common.page_common import PageCommon
from ui_test.data.Infinitus_tw_main_data_backup import InfinitusTwMainData
from selenium.webdriver.common.action_chains import ActionChains
import os

# # 参数化构建参数
# @paramunittest.parametrized(
#     # 参数{语言，环境}
#     {"lan": ConfigReader().read("project")["lan"], "env": ConfigReader().read("project")["env"]}
# )
# 测试用例
class Test_Main_Case_TW_DIS(unittest.TestCase, PageCommon):
    # 出错需要截图时此方法自动被调用
    def save_img(self, img_name):
        #self.driver.get_screenshot_as_file('../suite/img/Test_Main_Case_TW_DIS_{}.png'.format(img_name))
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(r"D:\work\Inifitus\ui_test\suite\img"), img_name))

    # # 参数化构建方法
    # def setParameters(self, lan, env):
    #     self.lan = lan
    #     self.env = env

    @classmethod
    def setUpClass(self):
        # 开始的 log 信息
        start_info()
        # 装配器初始化
        self.assembler = Assembler()

        # 提取驱动
        self.driver = self.assembler.get_driver()
        # 初始化页面
        self.main_page = InfinitusMainPage(self.driver)
        # 开启首页
        self.main_page.jump_to(InfinitusTwMainData.url)

    @classmethod
    def tearDownClass(self):
        # 结束的 log 信息
        end_info()
        # 装配器卸载
        self.assembler.disassemble_all()

    # dis用户登录
    @BeautifulReport.add_test_img("test_1_dis_login_tw")
    def test_1_dis_login_tw(self):
        # log 信息
        log().info(f"测试dis用户登录")
        # dis用户登录
        self.main_page.login_dis()
        time.sleep(5)
        result = self.iselementexisted(*InfinitusLocator.rebate_xpath)
        self.save_img("test_1_dis_login_tw")
        print(result)
        self.assertEqual(result, True, "登录成功后显示优惠券按钮")

    @unittest.skip("暂时跳过")
    # 通过商品搜索并添加购物车
    @BeautifulReport.add_test_img("test_2_searchandadd_tw")
    def test_2_searchandadd_tw(self):
        # log 信息
        log().info(f"测试dis搜索商品并加入购物车")
        self.main_page.search("陈皮", *InfinitusLocator.search_input)
        time.sleep(5)
        self.main_page.click_element(*InfinitusLocator.search_btn)
        time.sleep(5)
        self.main_page.click_element(*InfinitusLocator.addtocart_btn)
        time.sleep(5)
        self.main_page.click_element(*InfinitusLocator.cart_btn)
        time.sleep(5)
        result = self.iselementexisted(*InfinitusLocator.cart_product)
        #self.save_img("test_2_searchandadd_tw")
        print(result)
        self.assertEqual(result, True, "加入购物车后，购物车展示已添加的商品")
        time.sleep(5)
        #清空购物车
        self.main_page.clearcart()
        result = self.iselementexisted(*InfinitusLocator.cart_product)
        #self.save_img("test_2_searchandadd_tw")
        self.assertEqual(result, True, "购物车已清空")

    #@unittest.skip("暂时跳过")
    #通过分类筛选并添加购物车
    @BeautifulReport.add_test_img("test_3_cateandadd_tw")
    def test_3_cateandadd_tw(self):
        # log 信息
        log().info(f"测试dis通过分类筛选并加入购物车")
        # 通过筛选搜索产品
        self.main_page.filter_tw()
        #获取产品价格
        price = self.main_page.find_element_attribute('innerHTML', *InfinitusLocator.price)
        price = self.main_page.getprice(price)
        print(price)
        self.assertGreaterEqual(self.main_page.upper_price, price, "筛选出的商品价格不小于筛选条件最低价格")
        self.assertLessEqual(self.main_page.lower_price, price, "筛选出的商品价格不大于筛选条件最高价格")
        time.sleep(5)
        self.main_page.click_element(*InfinitusLocator.addtocart_btn)
        time.sleep(5)
        self.main_page.click_element(*InfinitusLocator.cart_btn)
        time.sleep(5)
        result = self.iselementexisted(*InfinitusLocator.cart_product)
        #self.save_img("test_3_cateandadd_tw")
        print(result)
        self.assertEqual(result, True, "加入购物车后，购物车展示已添加的商品")
        time.sleep(5)
        #清空购物车
        self.main_page.clearcart()
        result = self.iselementexisted(*InfinitusLocator.cart_product)
        #self.save_img("test_3_cateandadd_tw")
        self.assertEqual(result, True, "购物车已清空")

    @unittest.skip("暂时跳过")
    @BeautifulReport.add_test_img("test_4_checkout_tw")
    def test_4_checkout_tw(self):
        # log 信息
        log().info(f"测试dis结账")
        #搜索商品加入购物车
        self.main_page.search("陈皮", *InfinitusLocator.search_input)
        time.sleep(5)
        self.main_page.click_element(*InfinitusLocator.search_btn)
        time.sleep(5)
        self.main_page.click_element(*InfinitusLocator.addtocart_btn)
        time.sleep(5)
        #Infinitus购物车点击结账
        self.main_page.infinitus_checkout_tw()
        time.sleep(5)
        #Ctbc页面付款
        self.main_page.ctbc_checkout()
        order_number1, order_number2, order_payment_status = self.main_page.getorderdetail()
        #self.save_img("test_4_checkout_tw")
        order_payment_status = order_payment_status.strip().replace("\n", "")
        self.assertNotEqual(len(order_number1), 0, "订单编号位数不为0")
        self.assertNotEqual(len(order_number2), 0, "订单编号位数不为0")
        self.assertEqual(order_payment_status, "已支付", "订单状态为已支付")








# 当前用例程序入口
if __name__ == "__main__":
    # 使用 unittest 依次执行当前模块中 test 打头的方法
    # verbosity=0 静默模式，仅仅获取总的测试用例数以及总的结果
    # verbosity=1 默认模式，在每个成功的用例前面有个’.’,每个失败的用例前面有个’F’
    # verbosity=2 详细模式，测试结果会显示每个测试用例的所有相关信息
    unittest.main(verbosity=2)
