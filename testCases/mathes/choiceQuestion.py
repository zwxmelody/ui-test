#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time

class testChoice(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1: 单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])

    screenPath = getScreenShotDir('mathes','choiceQuestion')
    screenName = 'choice'

    @classmethod
    def setUpClass(cls):
        cls.UIA.initDriver()
        # 传入stuId,cityCode,courseLevelId清除学生该关卡的答题数据
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeed608bf')

        if rsps:
            print('清除学生该关卡的答题数据成功！')
        else:
            print('清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_choice_0(self):
        #处理弹窗，进入全部任务页面
        self.UIA.beforeAnswer()

    def test_choice_1(self):
        print('\n' + '数学选择题 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

        # 进入第一课：lesson1
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('lesson1', 5)
        self.UIA.clickElement('lesson1')
        self.UIA.clickElement('数学选择题')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 点击开始闯关
        self.UIA.waitForElement('开始闯关', 5)
        self.UIA.clickElement('开始闯关')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 上滑找到正确的答案A
        print('\n' + '开始作答第一道题，答案A... ')
        time.sleep(2)
        #swipeToFindElement方法还是有问题
        #element = self.UIA.swipeToFindElement(10,'//XCUIElementTypeStaticText[@name="A"]')
        self.UIA.swipeUp(n=1)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('A')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_choice_2(self):
        # 第二道题答案 A
        print('\n' + '开始作答第二道题，答案A... ')
        time.sleep(1)
        self.UIA.clickElement('A')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_choice_3(self):
        # 第三道题答案 A
        print('\n' + '开始作答第三道题，答案A... ')
        time.sleep(2)
        self.UIA.swipeUp(n=2)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('A')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_choice_4(self):
        # 第四道题答案 ABA
        print('\n' + '开始作答第四道题，答案ABA... ')
        self.UIA.dragFromDownToUp(187,467,187,243) #拖拽前后两个坐标的位置(x1,y1)(x2,y2)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #第一个空选择A
        self.UIA.clickElement('//XCUIElementTypeButton[@name="1"]')
        self.UIA.clickElement('A')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #第二个空选择B
        self.UIA.clickElement('//XCUIElementTypeButton[@name="2"]')
        self.UIA.clickElement('B')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #第三个空选择A
        self.UIA.clickElement('//XCUIElementTypeButton[@name="3"]')
        self.UIA.tapByCoordinate(47, 374)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_choice_5(self):
        # 第五道题答案 AB
        print('\n' + '开始作答第五道题，答案AB... ')
        self.UIA.clickElement('A')
        self.UIA.clickElement('B')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_choice_6(self):
        self.UIA.endAnswer(self.screenPath)

        #回到全部任务页
        self.UIA.waitForElement('切换班级',5)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text,'切换班级')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testChoice)
    unittest.TextTestRunner(verbosity=2).run(suite)




