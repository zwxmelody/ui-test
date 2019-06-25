#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time


class testYuxiObjective(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('chinese')

    # rynType[0]=0 模拟器/真机 1：单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])

    screenPath = getScreenShotDir('chinese','YuxiObjective')
    screenName = 'YuxiObjective'
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
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816b643865016b898fe3530b7f')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_yuxiObjective_0(self):
        self.UIA.beforeAnswer()

    def test_yuxiObjective_1(self):
        # 进入语文页，打开lesson1，并点击预习客观题
        print('进入全部任务的语文页，打开lesson1，并点击预习客观题')
        self.UIA.gotoChineseLesson1()
        self.UIA.waitForElement('预习客观题', 5)
        self.UIA.clickElement('预习客观题')

        # 点击开始闯关
        print('点击开始闯关')
        self.UIA.waitForElement('开始闯关', 5)
        self.UIA.clickElement('开始闯关')

