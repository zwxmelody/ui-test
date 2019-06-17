#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time

class testFillInBlank2(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1: 单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])

    screenPath = getScreenShotDir('mathes','fillInBlank2')
    screenName = 'blank2'

    @classmethod
    def setUpClass(cls):
        cls.UIA.initDriver()
        #传入stuId,cityCode,courseLevelId清除学生该关卡的答题数据
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeef108c7')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_fillInBlank2_0(self):
        self.UIA.beforeAnswer()

    def test_fillInBlank2_1(self):

        print('\n' + '数学填空题2 '+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 进入lesson2：
        self.UIA.waitForElement('lesson2',5)
        self.UIA.clickElement('数学填空题Part2')

        # 点击开始闯关,进入答题页面
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('开始闯关',5)
        self.UIA.clickElement('开始闯关')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('交卷', 5)

        #开始做第1道题
        print('开始做第1道竖式题')
        print('点击第1个空弹出键盘，输入9')
        self.UIA.tapByCoordinate(269, 263)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(261, 379)

        print('点击第2个空的位置，输入9')
        self.UIA.tapByCoordinate(320, 265)
        self.UIA.tapByCoordinate(261, 379)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        print('点击第3个空的位置，输入1')
        self.UIA.tapByCoordinate(220, 300)
        self.UIA.tapByCoordinate(113, 485)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        print('点击第4个空的位置，输入0')
        self.UIA.tapByCoordinate(269, 261)
        self.UIA.tapByCoordinate(187, 540)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #第1题完成后点击确定按钮
        print('第1题完成后点击确定按钮')
        self.UIA.waitForElement('确定', 5)
        self.UIA.clickElement('确定')
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_fillInBlank2_2(self):
        #点击空格位置，弹出键盘
        time.sleep(3)
        print('点击空格位置，弹出键盘')
        self.UIA.tapByCoordinate(160, 360)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.waitForElement('公式', 5)
        self.UIA.clickElement('公式')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(50, 470) #点击有分子分母的公式
        self.UIA.tapByCoordinate(270, 290) #点空白位置退键盘
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(161, 406) #然后点分母的位置弹出键盘
        self.UIA.waitForElement('常用', 5) #弹出键盘在公式的位置，点击常用
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('常用')
        self.UIA.waitForElement('2', 5)
        self.UIA.clickElement('2') #点击2
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(163, 243) #选中分子
        self.UIA.clickElement('公式')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(109, 474) #选择根号的公式
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('常用')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('5')
        self.UIA.clickElement('-')
        self.UIA.clickElement('1')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.waitForElement('确定', 5)
        self.UIA.clickElement('确定')
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_fillInBlank2_3(self):
        self.UIA.endAnswer(self.screenPath)

        # 回到全部任务页
        self.UIA.waitForElement('切换班级', 5)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text, '切换班级')
