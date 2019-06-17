#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time


class testVideoPaper(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1: 单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])
        configPath = parentPATH('config/videoPaper')

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])
        configPath = superPATH('config/videoPaper')

    screenPath = getScreenShotDir('mathes','videoPaper')
    screenName = 'videoPaper'
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
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeef108c6')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_videoPaper_0(self):
        self.UIA.beforeAnswer()

    def test_videoPaper_1(self):
        # 点击数学口述题和视频题
        print('\n' + '数学口述题和视频题 ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.UIA.waitForElement('lesson2', 5)
        self.UIA.clickElement('数学口述题和视频题')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.waitForElement('开始闯关', 5)
        self.UIA.clickElement('开始闯关')

        print('\n' + '开始录制第1个题的视频')
        self.UIA.waitForElement('录制作品', 5)
        self.UIA.clickElement('录制作品')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        time.sleep(1)

        # 录制页面，点击按钮开始录制视频
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 等待视频录制5秒，再次点击录制按钮停止录制
        time.sleep(2)
        time.sleep(2)
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 点击对勾，确认
        time.sleep(1)
        self.UIA.singleTap(432, 297)
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_videoPaper_2(self):
        print('\n' + '开始录制第2个题的视频')
        self.UIA.waitForElement('录制作品', 5)
        self.UIA.clickElement('录制作品')

        # 录制页面，点击按钮开始录制视频
        time.sleep(1)
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 等待视频录制5秒，再次点击录制按钮停止录制
        time.sleep(2)
        time.sleep(2)
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 点击对勾，确认
        self.UIA.singleTap(432, 297)
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_videoPaper_3(self):
        print('\n' + '开始录制第3个题的视频')
        self.UIA.waitForElement('录制作品', 5)
        self.UIA.clickElement('录制作品')

        # 录制页面，点击按钮开始录制视频
        time.sleep(1)
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 等待视频录制5秒，再次点击录制按钮停止录制
        time.sleep(2)
        time.sleep(2)
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 点击对勾，确认
        self.UIA.singleTap(432, 297)
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_videoPaper_4(self):
        print('\n' + '开始录制第4个题的视频')
        self.UIA.waitForElement('录制作品', 5)
        self.UIA.clickElement('录制作品')

        # 录制页面，点击按钮开始录制视频
        time.sleep(1)
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath,self.screenName)
        # 等待视频录制5秒，再次点击录制按钮停止录制
        time.sleep(2)
        time.sleep(2)
        self.UIA.singleTap(334, 324)
        # 点击对勾，确认
        self.UIA.singleTap(432, 297)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        print('\n' + '点击重新录制按钮，重新录制第4个题的视频')
        self.UIA.waitForElement('重新录制', 5)
        self.UIA.clickElement('重新录制')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.waitForElement('确定', 5)
        self.UIA.clickElement('确定')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 录制页面，点击按钮开始录制视频
        time.sleep(1)
        self.UIA.singleTap(334, 324)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 等待视频录制5秒，再次点击录制按钮停止录制
        time.sleep(2)
        time.sleep(2)
        self.UIA.singleTap(334, 324)
        # 点击对勾，确认
        self.UIA.singleTap(432, 297)
        self.UIA.saveScreen(self.screenPath, self.screenName)

    def test_videoPaper_5(self):
        self.UIA.endAnswer(self.screenPath)

        # 回到全部任务页
        self.UIA.waitForElement('切换班级', 8)
        self.UIA.saveScreen(self.screenPath, self.screenName)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text, '切换班级')