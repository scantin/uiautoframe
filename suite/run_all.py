import os
import unittest
from ui_test.case import test_infinitus_global_vip_case
from ui_test.case import test_infinitus_global_dis_case
from ui_test.case import test_infinitus_tw_dis_case
from ui_test.case import test_infinitus_tw_vip_case
from ui_test.util.config_reader import ConfigReader
from ui_test.util.report_tool import ReportTool

# 报告存放路径
report_path = os.path.abspath(os.path.dirname(__file__))[
              :os.path.abspath(os.path.dirname(__file__)).find("ui_test") + len(
                  "ui_test")] + ConfigReader().read("html")["htmlfile_path"]
# 报告名字
report_name = ConfigReader().read("html")["htmlfile_name"]

# 运行所有用例（单线程）
if __name__ == "__main__":
    # 创建测试套
    suites = unittest.TestSuite()
    loader = unittest.TestLoader()

    # 测试流程添加到测试套
    suites.addTests(loader.loadTestsFromModule(test_infinitus_global_vip_case))
    suites.addTests(loader.loadTestsFromModule(test_infinitus_global_dis_case))

    # 报告生成器，运行用例并生成报告，对 BeautifulReport 套了一层外壳
    ReportTool(suites).run(filename=report_name, description='Infinitus', report_dir=report_path, theme="theme_cyan")
