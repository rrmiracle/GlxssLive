from selenium import webdriver
from Case.User.update import Login, UsernameAndPassword, Update
import unittest
from .depmanagement import DepartmentManagement
from Case.BusinessManagement.businessmanangement import BusinessManagement
from Case.UserManagement.management import Management


class Test033_DeleteError(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        l = Login(self.driver)
        l.login()
        print("start")

    def tearDown(self):
        self.driver.quit()
        print("finish")

    def test_hasbranch(self):
        man = DepartmentManagement(self.driver)
        man.goto_depmanagement()
        man1 = BusinessManagement(self.driver)
        self.assertEqual(man1.tagname(), "部门管理")
        man.deptstatus(2)
        man.delete_dept()
        up = Update(self.driver)
        self.assertEqual(up.result(), "您确定要删除这条信息吗")
        man1 = Management(self.driver)
        man1.confirm()
        self.assertEqual(up.result(), "删除失败")
        uap = UsernameAndPassword(self.driver)
        self.assertEqual(uap.notification(), "请先删除子部门")


if __name__ == "__main__":
    unittest.main()


