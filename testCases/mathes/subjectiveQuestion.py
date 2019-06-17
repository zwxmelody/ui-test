#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time


class testSubjectiveQuestion(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1: 单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])

    screenPath = getScreenShotDir('mathes','subjectiveQuestion')
    screenName = 'subjective'

    @classmethod
    def setUpClass(cls):
        cls.UIA.initDriver()
        #传入stuId,cityCode,courseLevelId清除学生该关卡的答题数据
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeef108c5')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            rsps = common.CommonLib.initStudent('ceb602cf9d44eec765349c81d783a6a2', '010', '9b267df220be47bbacc83695c7f0ec64')
            if rsps:
                common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeef108c5')
            else:
                print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_subjective_0(self):
        self.UIA.beforeAnswer()

    def test_subjective_1(self):
        print('\n' + '数学主观题 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        #进入主观题
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('数学主观题', 5)
        self.UIA.clickElement('数学主观题')

        #点击开始闯关
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('开始闯关', 5)
        self.UIA.clickElement('开始闯关')

        #第一道题，点击拍照上传
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('拍照上传', 5)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('拍照上传')


        #从相册选择一张照片
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(2)
        self.UIA.tapByCoordinate(190, 558)
        time.sleep(2)
        self.UIA.tapByCoordinate(328, 116)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(2)
        self.UIA.tapByCoordinate(337, 641)

        #点击确认上传
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('确认上传', 5)
        self.UIA.clickElement('确认上传')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #TODO：校验toast提示 上传成功

    def test_subjective_2(self):

        #第二道题，点击拍照上传
        self.UIA.waitForElement('拍照上传', 5)
        self.UIA.clickElement('拍照上传')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 从相册选择一张照片
        time.sleep(2)
        self.UIA.tapByCoordinate(190, 558)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(2)
        self.UIA.tapByCoordinate(328, 116)
        time.sleep(2)
        self.UIA.tapByCoordinate(337, 641)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 点击确认上传
        self.UIA.waitForElement('确认上传', 5)
        self.UIA.clickElement('确认上传')
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_subjective_3(self):
        # 第三道题，点击拍照上传
        self.UIA.waitForElement('拍照上传', 5)
        self.UIA.clickElement('拍照上传')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 从相册选择一张照片
        time.sleep(2)
        self.UIA.tapByCoordinate(190, 558)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(2)
        self.UIA.tapByCoordinate(328, 116)
        time.sleep(2)
        self.UIA.tapByCoordinate(337, 641)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 点击重新上传
        self.UIA.waitForElement('重新上传', 5)
        self.UIA.clickElement('重新上传')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 从相册选择另一张照片
        time.sleep(2)
        self.UIA.tapByCoordinate(190, 558) #点去相册选择
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(2)
        self.UIA.tapByCoordinate(144, 113) #点照片
        time.sleep(2)
        self.UIA.tapByCoordinate(337, 641) #点 done
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 点击确认上传
        self.UIA.waitForElement('确认上传', 5)
        self.UIA.clickElement('确认上传')
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_subjective_4(self):

        self.UIA.endAnswer(self.screenPath)

        # 回到全部任务页
        self.UIA.waitForElement('切换班级', 5)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text, '切换班级')
