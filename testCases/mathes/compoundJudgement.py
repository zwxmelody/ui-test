#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time

class testCompoundJudgement(unittest.TestCase):
    # 通过testSuite.py执行时
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1：单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])

    screenPath = getScreenShotDir('mathes', 'compoundJudgement')
    screenName = 'compound'

    @classmethod
    def setUpClass(cls):
        cls.UIA.initDriver()
        # 传入stuId,cityCode,courseLevelId清除学生该关卡的答题数据
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeed608c2')

        if rsps:
            print('清除学生该关卡的答题数据成功！')
        else:
            print('清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_judgement_0(self):
        self.UIA.beforeAnswer()

    def test_judgement_1(self):
        # 进入课次：lesson2
        print('\n' + '数学判断题 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.UIA.waitForElement('lesson1', 5)
        self.UIA.clickElement('lesson1')
        self.UIA.clickElement('数学复合判断题')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 点击开始闯关
        self.UIA.waitForElement('开始闯关', 5)
        self.UIA.clickElement('开始闯关')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #第一道题，点击视频播放
        print('\n' + '第一道题先播放视频，之后选择 ✔️ ')
        #等待题目打开
        self.UIA.waitForElement('今天的教具你会玩了吗',5)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(187,256)
        self.UIA.tapByCoordinate(187,256)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #播放视频10秒钟，返回,并选择 对号
        time.sleep(10)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(125,125)
        self.UIA.waitForElement('xclvideoplayer backbtn icon',5)
        self.UIA.clickElement('xclvideoplayer backbtn icon')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.waitForElement('我会了',5)
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_judgement_2(self):
        # 第二道题，答案：错错对对错
        print('\n' + '第二道选择题，答案：错错对对错...️ ')
        self.UIA.waitForElement('判断．',5)
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[2]')
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[2]')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.swipeUp(n=2)
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[3]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[4]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.swipeUp()
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[2]/XCUIElementTypeOther[5]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[2]')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('确定')

    def test_judgement_3(self):
        #第三道题答案：2，28，A，AB
        print('\n' + '第三道复合题，答案：2，28，A，AB...')
        self.UIA.tapByCoordinate(285,288)

        self.UIA.waitForElement('常用',5)
        self.UIA.tapByCoordinate(188,485)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #点击空白处，退出键盘
        self.UIA.tapByCoordinate(50,150)
        self.UIA.tapByCoordinate(50, 150)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #点击第二个空弹出键盘
        self.UIA.tapByCoordinate(120,340)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        time.sleep(2)
        self.UIA.tapByCoordinate(187,487)
        self.UIA.waitForElement('8',5)
        self.UIA.clickElement('8')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #点击空白处退出键盘
        self.UIA.tapByCoordinate(50, 150)
        self.UIA.tapByCoordinate(50, 150)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.waitForElement('A',5)
        self.UIA.clickElement('A')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.swipeUp(n=2)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('(//XCUIElementTypeStaticText[@name="A"])[2]')
        self.UIA.clickElement('(//XCUIElementTypeStaticText[@name="B"])[2]')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_judgement_4(self):
        #第四道题答案：A，✔️，✔，✔
        print('\n' + '第四道复合题答案：A,对，对，对')
        self.UIA.clickElement('A')
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[7]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.swipeUp(n=2)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[10]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
        self.UIA.clickElement('//XCUIElementTypeOther[@name="IPS"]/XCUIElementTypeOther[13]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeButton[1]')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_judgement_5(self):
        self.UIA.endAnswer(self.screenPath)

        #回到全部任务页
        self.UIA.waitForElement('切换班级',5)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text,'切换班级')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testCompoundJudgement)
    unittest.TextTestRunner(verbosity=2).run(suite)