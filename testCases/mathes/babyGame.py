#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time


class testBabyGame(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1：单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])
        configPath = parentPATH('config/babyGame')

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])
        configPath = superPATH('config/babyGame')

    screenPath = getScreenShotDir('mathes','babyGame')
    screenName = 'babyGame'
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
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeed608c3')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_babyGame_0(self):
        self.UIA.beforeAnswer()

    def test_babyGame_1(self):
        print('\n' + '幼儿游戏题 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 进入第一课：lesson1
        self.UIA.waitForElement('lesson1', 5)
        self.UIA.clickElement('lesson1')
        self.UIA.swipeUp()
        self.UIA.waitForElement('数学幼儿游戏', 5)
        self.UIA.clickElement('数学幼儿游戏')

        # 点击开始，第一次关卡答题
        try:
            self.UIA.saveScreen(self.screenPath, self.screenName)
            self.UIA.waitForElement('开始', 5)
            self.UIA.clickElement('开始')
            self.UIA.saveScreen(self.screenPath, self.screenName)
        except:

            #非第一次答题，选择序号可以重新作答
            #选择序号为1的游戏
            print('选择序号为1的游戏：')
            self.UIA.saveScreen(self.screenPath, self.screenName)
            self.UIA.waitForElement('数学幼儿游戏', 5)
            self.UIA.clickElement('1')
            self.UIA.saveScreen(self.screenPath, self.screenName)

        #1：四幅图的拼图游戏

        time.sleep(8)
        optionList1 = getOptionList(self.configPath, 'test_babyGame_1_fourPics')
        for ol in optionList1:
            self.UIA.touchAction(ol[0], ol[1], ol[2], ol[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)
            time.sleep(1)
        print('四幅图的拼图游戏完成')

        #2：六幅图的拼图游戏
        time.sleep(3)
        optionList2 = getOptionList(self.configPath, 'test_babyGame_1_sixPics')
        for ol2 in optionList2:
            self.UIA.touchAction(ol2[0], ol2[1], ol2[2], ol2[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)
            time.sleep(1)
        print('六幅图的拼图游戏完成')

        #3：九幅图的拼图游戏
        time.sleep(3)
        optionList3 = getOptionList(self.configPath, 'test_babyGame_1_ninePics')
        for ol3 in optionList3:
            self.UIA.touchAction(ol3[0], ol3[1], ol3[2], ol3[3])
            self.UIA.saveScreen(self.screenPath, self.screenName)
            time.sleep(1)
        print('九幅图的拼图游戏完成')
        time.sleep(3)

        # 第1题结束后，出现you win的动画和弹窗（弹窗上只有一个完成按钮）
        time.sleep(3)
        self.UIA.singleTap(333, 245) #返回到全部任务页
        print('点击游戏结束的完成按钮')

    def test_babyGame_2(self):
        # 点击全部任务页的数学幼儿园
        print('再次点击数学幼儿游戏的任务入口，进入游戏')
        self.UIA.swipeUp()
        self.UIA.waitForElement('数学幼儿游戏', 5)
        self.UIA.clickElement('数学幼儿游戏')

        self.UIA.waitForElement('数学幼儿游戏', 5)
        print('选择序号为2的游戏：')
        self.UIA.clickElement('2')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #1 选择15个香蕉
        time.sleep(6)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.singleTap(180, 342) #第1个场景出现15个水果，点击15
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #2 选择12个
        time.sleep(5)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.singleTap(384, 342) #第2个场景出现12个水果
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #3 选择16个
        time.sleep(6)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.singleTap(486, 344) #第3个场景出现16个水果
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(3)

        # 点击完成按钮
        time.sleep(3)
        self.UIA.singleTap(333, 245)  # 返回到全部任务页
        print('点击游戏结束的完成按钮')

    def test_babyGame_3(self):
        # 点击全部任务页的数学幼儿园
        print('再次点击数学幼儿游戏的任务入口，进入游戏')
        self.UIA.swipeUp()
        self.UIA.waitForElement('数学幼儿游戏', 5)
        self.UIA.clickElement('数学幼儿游戏')

        self.UIA.waitForElement('数学幼儿游戏', 5)
        print('选择序号为3的游戏：')
        self.UIA.clickElement('3')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #1 选择数字5
        time.sleep(4)
        print('第1题选择数字5')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.touchAction(371, 281, 337, 166)
        self.UIA.singleTap(531, 341)
        time.sleep(4)

        #2 选择数字9
        print('第2题选择数字9')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.touchAction(500, 203, 333, 161)
        self.UIA.singleTap(531, 341)
        time.sleep(4)

        #3 选择数字9
        print('第3题选择数字9')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.touchAction(500, 209, 333, 161)
        self.UIA.singleTap(531, 341)
        time.sleep(4)

        # 选择数字19
        print('第4题选择数字19')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.touchAction(161, 291, 306, 164)
        self.UIA.touchAction(500, 206, 353, 164)
        self.UIA.singleTap(531, 341)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(4)

        # 选择数字3
        print('第5题选择数字3')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.touchAction(272, 286, 333, 167)
        self.UIA.singleTap(531, 341)
        time.sleep(10) #动画比较长，需要停留会
        self.UIA.saveScreen(self.screenPath, self.screenName)
        print('点击完成按钮')
        self.UIA.singleTap(330, 245)

        # 回到全部任务页
        self.UIA.waitForElement('切换班级', 8)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text, '切换班级')
