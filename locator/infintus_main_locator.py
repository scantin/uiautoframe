from selenium.webdriver.common.by import By


# 百度首页的元素定位
class InfinitusLocator:
    # 右上账户按钮xpath
    account_xpath = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[2]/div/div')
    # 右上登录按钮xpath
    login_btn = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[2]/div/div/div[2]/ul/li[1]/div')
    # 手机号码输入框xpath
    phone_input = (By.XPATH, '//*[@id="signIn-phone"]')

    # 密码输入框xpath
    password_input = (By.XPATH, '//*[@id="signIn-password"]')
    # 验证码输入框xpath
    code_input = (By.XPATH, '//*[@id="signIn-code"]')
    #动态验证码xpath
    code_xpath = (By.XPATH, '//*[@id="signIn"]/span/form/div[3]/span[3]/div/div[1]/div/span/img[1]')
    #登录按钮xpath
    login = (By.XPATH, '//*[@id="signIn"]/span/form/button/div')
    #回赠金按钮xpath
    rebate_xpath = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[2]/div/button[1]')
    #主页搜索框xpath
    search_input = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[1]/div[2]/input')
    #搜索按钮
    search_btn = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[1]/div[2]/button')
    #搜索结果加入购物车按钮xpath
    addtocart_btn = (By.XPATH, '//*[@id="product_price"]/button')
    #右上角购物车按钮xpath
    cart_btn = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[2]/div/button[2]/span')

    #购物车图片xpath，用于判断购物车是否有商品
    cart_product = (By.XPATH, '//*[@id="cart"]/div[2]/div/div[1]/table/tr/td[1]/div/span/img[1]')
    #清空购物车按钮
    clear_cart = (By.XPATH, '//*[@id="cart"]/div[2]/div/div[1]/table/tr/td[5]/span')
    #确定清空购物车按钮
    confirm_clear_cart = (By.XPATH, '//*[@id="cart"]/section[2]/div[2]/div/div[2]/button[1]')
    #分类列表按钮
    category_btn = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[1]/div[1]/div/p/span')
    #分类列表第一个分类
    category_filter = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[1]/div[1]/div/div/ul/li')
    #tw价格筛选第一个价格区间
    price_filter_tw = (By.XPATH, '//*[@id="category"]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/div')
    #global价格筛选
    price_filter_global = (By.XPATH, '//*[@id="category"]/div[1]/div[1]/div/div/div[3]/div[1]/div[2]/div')
    #tw品牌筛选第一个品牌
    brand_filter_tw = (By.XPATH, '//*[@id="category"]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/div')
    #global品牌筛选
    brand_filter_global = (By.XPATH, '//*[@id="category"]/div[1]/div[1]/div/div/div[3]/div[2]/div[2]/div')
    #tw筛选后完成按钮
    filter_confirm_btn_tw = (By.XPATH, '//*[@id="category"]/div[1]/div[1]/div/div/div[3]/button[1]')
    #global筛选后完成按钮
    filter_confirm_btn_global = (By.XPATH, '//*[@id="category"]/div[1]/div[1]/div/div/div[4]/button[1]')
    #筛选后商品价格(优惠价)
    price = (By.XPATH, '//*[@id="product_price"]/div[2]/div[2]/span[2]')
    #tw结账按钮
    checkout_btn_tw = (By.XPATH, '//*[@id="cart"]/div[2]/div/div[2]/div[4]/button[1]')
    #global结账按钮
    checkout_btn_global = (By.XPATH, '//*[@id="cart"]/div[2]/div/div[2]/div[5]/button[1]')
    #结账弹窗确认按钮
    checkout_btn_global_popup = (By.XPATH, '//*[@id="cart"]/section[1]/div[2]/div/button[1]')
    #销售条款勾选
    terms_of_sale_tw = (By.XPATH, '//*[@id="checkout"]/div[2]/div[1]/div[8]/label/div')
    terms_of_sale_global = (By.XPATH, '//*[@id="checkout"]/div[2]/div[1]/div[7]/label/div')
    #提交订单按钮
    submit_btn_tw = (By.XPATH, '//*[@id="checkout"]/div[2]/div[1]/div[9]/button[2]')
    submit_btn_global = (By.XPATH, '//*[@id="checkout"]/div[2]/div[1]/div[8]/button[2]')
    #ctbc信用卡号输入框
    ctbc_cardnum = (By.XPATH, '//*[@id="pan_num"]')
    #ctbc检查码输入框
    ctbc_cvv = (By.XPATH, '//*[@id="cvc2"]')
    #ctbc安全验证码输入框
    ctbc_security_code = (By.XPATH, '//*[@id="sslForm"]/div[7]/div[2]/div/input')
    #ctbc确认付款按钮
    ctbc_confirm_checkout = (By.XPATH, '//*[@id="sslForm"]/div[8]/div[1]/button/span')
    #ctbc信用卡过期月份选择框
    ctbc_month_selector = (By.XPATH, '//*[@id="expire_month"]')
    #ctbc信用卡过期月份3月
    ctbc_month = (By.XPATH, '//*[@id="expire_month"]/option[3]')
    #ctbc信用卡过期年份选择框
    ctbc_year_selector = (By.XPATH, '//*[@id="expire_year"]')
    #ctbc信用卡过期年份2023年
    ctbc_year = (By.XPATH, '//*[@id="expire_year"]/option[2]')
    #stripe卡号输入框
    stripe_cardnum = (By.ID, 'cardNumber')
    #stripe过期年月
    stripe_date = (By.ID, 'cardExpiry')
    #stripe cvv
    stripe_cvv = (By.ID, 'cardCvc')
    #stripe姓名
    stripe_name = (By.ID, 'billingName')
    #stripe支付按钮
    stripe_confirm_checkout = (By.XPATH, '//*[@id="root"]/div/div/div[2]/div/div[2]/form/div[2]/div[2]/button/div[3]')
    #我的订单按钮
    my_order = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[2]/div/div/div[2]/ul/li[2]')
    #第一条订单编号
    order_num1 = (By.XPATH, '//*[@id="my-account"]/div/section/div[2]/div/div[3]/div/div/div/div/div/div/div[1]/table/tbody[2]/tr/td[2]/div/span[1]')
    #第二条订单编号
    order_num2 = (By.XPATH, '//*[@id="my-account"]/div/section/div[2]/div/div[3]/div/div/div/div/div/div/div[1]/table/tbody[2]/tr/td[2]/div/span[2]')
    #订单支付状态
    order_payment_status = (By.XPATH, '//*[@id="my-account"]/div/section/div[2]/div/div[3]/div/div/div/div/div/div/div[1]/table/tbody[2]/tr/td[4]')
    #登录方式
    login_type = (By.XPATH, '//*[@id="signIn"]/span/form/div[2]/div[1]/div[1]')
    #下拉列表会员卡号登录
    login_membership_card = (By.XPATH, '//*[@id="會員卡號"]/div')
    #会员卡号输入框
    membership_card = (By.XPATH, '//*[@id="signIn-agencyId"]')
    #退出登录按钮
    logout_btn = (By.XPATH, '//*[@id="__layout"]/div/div[4]/div[1]/div[1]/div[2]/div/div/div[2]/ul/li[4]/div')
    #下拉列表邮箱登录
    login_email = (By.XPATH, '//*[@id="電子郵件"]/div')
    #邮箱输入框
    email_input = (By.XPATH, '//*[@id="signIn-email"]')
    #global按地区筛选
    area_filter = (By.XPATH, '//*[@id="category"]/div[1]/div[1]/div/div/div[1]/div')







