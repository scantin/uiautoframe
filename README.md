[toc]

python + selenium + unittest + PageObject(PO 思想) + BeautifulReport + ParamUnittest(外部传参) + img 截图 + log 日志 + 多浏览器支持 + RemoteWebDriver + ini 文件读取 + 全参数化构建  

# 1.框架注意点
- 项目完全依靠参数化构建，见文件`ui-test/resource/config/config.ini`
- `ui-test/case` 中存放测试用例，测试用例需要以 test 打头，并且通过下划线加数字形式进行执行排序
- `ui-test/resource/driver`中的谷歌驱动对应浏览器103.0.5060.66版本的，请根据自己浏览器版本自行更新驱动（下载地址：http://chromedriver.storage.googleapis.com/index.html）
- `ui-test`包中`/resource/config/config.ini`中的键名参数不能大写，因为读取`.ini`的键名必以小写读出！
- 项目名一定要是`ui-test`，其下目录名或文件名不要使用同名
- 其他项目可复用该框架


# 2.所需依赖
本人使用的是 python 3.9.6
```
BeautifulReport 0.1.3
ParamUnittest   0.2
futures         3.1.1
pip             10.0.1	
selenium        4.3.0
setuptools      39.1.0	
tomorrow        0.2.4	
urllib3         1.26.6	
```

# 3.项目结构
```
Inifitus
    - ui-test（ui 测试包）
        - base（与项目初始化配置相关）
        - case（测试用例脚本）
        - common（共用方法）
        - data（数据驱动，存储账号密码等数据）
        - locator（页面对应的元素定位，当前项目均为xpath定位）
        - page（页面类，可封装页面公共方法）
        - report（输出报告）
            - html（html 类型报告）
            - log（log 日志报告）
        - resource（资源文件夹）
            - config（配置文件）
            - driver（驱动）
        - util（工具类）
        - README.md（项目介绍 md）
        - requirements.txt（项目依赖清单）
        - suite
            - run_all.py（测试套执行）
            - img(测试截图，最终在报告中体现截图)
```
# 4.执行方法
```
- 单用例执行
    以case下test_infinitus_global_dis_case为例，执行该py文件，即可执行global站点dis账户相关case，包括登录，搜索，筛选，添加购物车，结账流程，单用例执行不会生成html测试报告
- 测试套执行
    run_all.py中，将case下的测试用例加入到测试套中，可批量执行并生成html测试报告
    suites.addTests(loader.loadTestsFromModule(test_infinitus_tw_vip_case))
```

# 5.代码举例
```
- test_infinitus_tw_vip_case.py登录case段
    class Test_Main_Case_TW_VIP(unittest.TestCase, PageCommon):
    # 出错需要截图时此方法自动被调用，截图会写入测试报告，如果执行正常也需要截图，可在用例中直接调用该方法
    def save_img(self, img_name):
        self.driver.get_screenshot_as_file(r'D:\work\Inifitus\ui_test\suite\img'.format(img_name))

    # 前置条件执行方法，测试类执行前自动执行，包含启动浏览器，跳转，获取驱动
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
        self.main_page.jump_to(InfinitusData.url_tw)

    # 后置条件执行方法，测试类执行结束后自动执行，退出驱动
    @classmethod
    def tearDownClass(self):
        # 结束的 log 信息
        end_info()
        # 装配器卸载
        self.assembler.disassemble_all()

    #@unittest.skip("暂时跳过")
    # tw vip电话号码用户登录
    # 测试报告装饰器，失败后截图并加入测试报告
    @BeautifulReport.add_test_img("test_1_vip_loginphone_tw")
        def test_1_vip_loginphone_tw(self):
        # log 信息
        log().info(f"测试vip用户电话登录")
        # vip用户登录
        self.main_page.login_vip()
        time.sleep(5)
        result = self.iselementexisted(*InfinitusLocator.rebate_xpath)
        # 测试正确需要截图时，这里调用save_img保存截图
        #self.save_img("test_1_vip_loginphone_tw")
        print(result)
        # 断言，判断是否登录成功
        self.assertEqual(result, True, "登录成功后显示回赠金按钮")
        self.main_page.logout()
```

