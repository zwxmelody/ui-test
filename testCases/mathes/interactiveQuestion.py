#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time


class testInteractiveQuestion(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1: 单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])
        configPath = parentPATH('config/interactiveQuestion')

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])
        configPath = superPATH('config/interactiveQuestion')

    screenPath = getScreenShotDir('mathes','interactiveQuestion')
    screenName = 'interactive'

    @classmethod
    def setUpClass(cls):
        cls.UIA.initDriver()

        #先初始化下学生数据，因为调清除数据接口有时候会失败
        try:
            common.CommonLib.initStudent('ceb602cf9d44eec765349c81d783a6a2', '010', '9b267df220be47bbacc83695c7f0ec64')
        except:
            print('初始化学生数据失败！')
            pass
        #传入stuId,cityCode,courseLevelId清除学生该关卡的答题数据
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeed608c1')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_interactive_0(self):
        self.UIA.beforeAnswer()

    def test_interactive_1(self):
        print('\n' + '数学互动题第一题开始作答 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 进入lesson1,选择数学互动题
        self.UIA.waitForElement('lesson1', 5)
        self.UIA.clickElement('lesson1')
        self.UIA.clickElement('数学互动题')

        # 点击开始闯关
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('开始闯关', 5)
        self.UIA.clickElement('开始闯关')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 拖动2个方块到正确位置,坐标写在配置文件中
        list1 = getOptionList(self.configPath, 'test_interactive_1')
        time.sleep(3) # 第1题首次加载可能慢
        for l1 in list1:
            print(l1[0],l1[1],l1[2],l1[3])
            self.UIA.touchAction(l1[0], l1[1], l1[2], l1[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)
            time.sleep(1)

        # 点击确定按钮
        self.UIA.waitForElement('确定', 5)
        self.UIA.clickElement('确定')
        self.UIA.saveScreen(self.screenPath, self.screenName)

    # 数阵图坐标写在配置文件中
    def test_interactive_2(self):
        print('\n' + '数学互动题第二题数阵图开始作答 ' )
        list2 = getOptionList(self.configPath, 'test_interactive_2')
        self.UIA.waitForElement('1', 5) #第2题首次加载可能比较慢

        for l2 in list2:
            print(l2)
            self.UIA.touchAction(l2[0], l2[1], l2[2], l2[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)
            time.sleep(1)

        self.UIA.waitForElement('确定', 5)
        self.UIA.clickElement('确定')

    def test_interactive_3(self):
        self.UIA.endAnswer(self.screenPath)

        # 回到全部任务页
        self.UIA.waitForElement('切换班级', 5)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.assertEqual(text, '切换班级')
