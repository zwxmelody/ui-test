#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time
sys.path.append('../')

class testChildGame(unittest.TestCase):

    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1: 单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])
        configPath = parentPATH('config/childGame')

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])
        configPath = superPATH('config/childGame')

    screenPath = getScreenShotDir('mathes','childGame')
    screenName = 'childGame'
    @classmethod
    def setUpClass(cls):
        cls.UIA.initDriver()

        # 先初始化下学生数据，因为调清除数据接口有时候会失败
        try:
            common.CommonLib.initStudent('ceb602cf9d44eec765349c81d783a6a2', '010', '9b267df220be47bbacc83695c7f0ec64')
        except:
            print('初始化学生数据失败！')
            pass

        #传入stuId,cityCode,courseLevelId清除学生该关卡的答题数据
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeef108c4')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_childGame_0(self):
        self.UIA.beforeAnswer()

    def test_childGame_1(self):
        print('\n' + '小低游戏题 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('lesson2', 5)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('数学小低游戏')
        
        #弹出开始弹窗，选择第1个游戏（共2个）
        self.UIA.waitForElement('数学小低游戏', 5)
        self.UIA.clickElement('1')

        #等待加载第1个游戏
        time.sleep(6)
        #点击屏幕任意位置退出引导图
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.singleTap(201, 36)

        print('\n' + '开始1_1的俄罗斯方块游戏')
        #点击3次，处理方块位置
        self.UIA.singleTap(401, 95)
        self.UIA.singleTap(408, 104)
        self.UIA.singleTap(401, 114)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #拖动第一个方块
        self.UIA.touchAction(390, 105, 137, 197)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #点击1次第2个方块，处理方块位置
        self.UIA.singleTap(399, 190)
        #拖动第2个方块
        self.UIA.touchAction(399, 190, 155, 142)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #拖动第3个方块
        self.UIA.touchAction(488, 193, 172, 108)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #点击第4个方块，处理方块方向
        self.UIA.singleTap(491, 101)
        #拖动第4个方块
        self.UIA.touchAction(491, 101, 227, 160)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #点击提交答案
        self.UIA.singleTap(400, 350)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #等待you win动画消失
        time.sleep(4)

        print('\n' + '开始1_2的俄罗斯方块游戏')
        #点击第1个方块，处理方向
        self.UIA.singleTap(417, 191)
        #拖动第1个方块
        self.UIA.touchAction(418, 210, 210, 197)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #拖动第2个方块
        self.UIA.touchAction(480, 111, 119, 176)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #拖动第3个方块
        self.UIA.singleTap(391, 103)
        self.UIA.touchAction(399, 94, 192, 108)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #拖动第4个方块
        self.UIA.touchAction(490, 191, 195, 157)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 点击提交答案
        self.UIA.singleTap(400, 350)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 等待you win动画消失
        time.sleep(4)

        print('\n' + '开始1_3的俄罗斯方块游戏')
        #点击方块，处理方向
        self.UIA.singleTap(489, 116)
        self.UIA.singleTap(475, 103)
        self.UIA.singleTap(489, 91)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #拖动方块
        self.UIA.touchAction(502, 102, 248, 197)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #点击方块，处理方向
        self.UIA.singleTap(398, 111)
        #拖动方块
        self.UIA.touchAction(389, 102, 159, 181)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #拖动方块
        self.UIA.touchAction(400, 183, 158, 106)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 点击提交答案
        self.UIA.singleTap(400, 350)
        # 出现完成动画，点击完成按钮
        time.sleep(3)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.singleTap(333, 245)

        # 回到全部任务页
        self.UIA.waitForElement('切换班级', 5)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text, '切换班级')

    def test_childGame_2(self):
        # 再次点击小低数学游戏
        print('全部任务页，再次点击数学小低游戏')
        self.UIA.waitForElement('数学小低游戏', 5)
        self.UIA.clickElement('数学小低游戏')

        self.UIA.waitForElement('数学小低游戏', 5)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('2')

        # 等待游戏资源加载
        time.sleep(10)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 点击退出引导及说明页
        self.UIA.singleTap(154, 55)

        print('开始2_1连线游戏')
        optionList1 = getOptionList(self.configPath, 'test_childGame_2_1')
        for ol1 in optionList1:
            self.UIA.touchAction(ol1[0], ol1[1], ol1[2], ol1[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)

        # 连线完成后，点击确认
        self.UIA.singleTap(530, 350)
        time.sleep(3)

        print('开始2_2连线游戏')
        optionList2 = getOptionList(self.configPath, 'test_childGame_2_2')
        for ol2 in optionList2:
            self.UIA.touchAction(ol2[0], ol2[1], ol2[2], ol2[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)

        # 连线完成后，点击确认
        self.UIA.singleTap(530, 350)
        time.sleep(3)

        print('开始2_3连线游戏')
        optionList3 = getOptionList(self.configPath, 'test_childGame_2_3')
        for ol3 in optionList3:
            self.UIA.touchAction(ol3[0], ol3[1], ol3[2], ol3[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)

        # 连线完成后点击确认
        self.UIA.singleTap(530, 350)
        time.sleep(3)

        print('开始2_4连线游戏')
        optionList4 = getOptionList(self.configPath, 'test_childGame_2_4')
        for ol4 in optionList4:
            self.UIA.touchAction(ol4[0], ol4[1], ol4[2], ol4[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)

        #连线完成后点击确定
        self.UIA.singleTap(530, 350)
        time.sleep(7)

        self.UIA.singleTap(333, 245)

        # 回到全部任务页
        self.UIA.waitForElement('切换班级', 8)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text, '切换班级')
