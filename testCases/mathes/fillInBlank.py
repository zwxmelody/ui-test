#!/usr/local/bin/python3
#coding:utf-8

import sys
sys.path.append('../../')
from common.uiAutoIos import *
import common.CommonLib
import unittest
import time

class testFillInBlank(unittest.TestCase):
    # 下面的方法返回一个list，runType[0]代表运行环境，runType[1]为所选机型
    runType = getRuntimeConfig('mathes')

    # rynType[0]=0 模拟器/真机 1: 单文件调试
    if runType[0] == 0:
        UIA = UiAuto(parentPATH('config/device'), runType[1])

    else:
        UIA = UiAuto(superPATH('config/device'), runType[1])

    screenPath = getScreenShotDir('mathes','fillInBlank')
    screenName = 'blank'

    @classmethod
    def setUpClass(cls):
        cls.UIA.initDriver()
        #传入stuId,cityCode,courseLevelId清除学生该关卡的答题数据
        rsps = common.CommonLib.clearData('ceb602cf9d44eec765349c81d783a6a2', '010', 'ff8080816af91c2d016afe3aeed608c0')
        if rsps:
            print('\n' + '清除学生该关卡的答题数据成功！')
        else:
            print('\n' + '清除数据接口异常，请确认！')

    @classmethod
    def tearDownClass(cls):
        cls.UIA.quitDriver()

    def test_fillInBlank_0(self):
        self.UIA.beforeAnswer()

    def test_fillInBlank_1(self):

        print('\n' + '数学填空题 '+ time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        self.UIA.saveScreen(self.screenPath, self.screenName)
        # 进入第一课：单选题和填空题
        self.UIA.waitForElement('lesson1',5)
        self.UIA.clickElement('lesson1')
        self.UIA.clickElement('数学填空题')

        # 点击开始闯关
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.waitForElement('开始闯关',5)
        self.UIA.clickElement('开始闯关')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        # 第一道题，答案6,7,8,9,10
        # 通过相对坐标点击弹出键盘
        self.UIA.waitForElement('交卷',5)
        print('\n' + '开始作答第一道填空题... ')
        self.UIA.tapByCoordinate(173,152)
        self.UIA.tapByCoordinate(173,152)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.waitForElement('6',5)
        self.UIA.clickElement('6')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.tapByCoordinate(258,162)
        self.UIA.tapByCoordinate(258,162)

        self.UIA.waitForElement('6',5)
        self.UIA.clickElement('7')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.tapByCoordinate(65,197)
        self.UIA.tapByCoordinate(65, 197)

        self.UIA.waitForElement('8',5)
        self.UIA.clickElement('8')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.tapByCoordinate(150,197)
        self.UIA.tapByCoordinate(150, 197)

        self.UIA.waitForElement('9',5)
        self.UIA.clickElement('9')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.tapByCoordinate(230,197)
        self.UIA.tapByCoordinate(230, 197)

        self.UIA.clickElement('1')
        self.UIA.clickElement('0')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_fillInBlank_2(self):
        # 第二道题，答案：1单元，x=1（操作不了输入法键盘无法输入中文，send_keys也不行
        print('\n' + '开始作答第二道填空题... ')
        self.UIA.tapByCoordinate(65,179)
        self.UIA.tapByCoordinate(65,179)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('1')
        self.UIA.clickElement('abc')
        self.UIA.clickElement('d')
        self.UIA.clickElement('y')
        self.UIA.saveScreen(self.screenPath, self.screenName)


        self.UIA.tapByCoordinate(145,190)
        self.UIA.tapByCoordinate(145,190)
        self.UIA.clickElement('abc')
        self.UIA.clickElement('x')
        self.UIA.clickElement('常用')
        self.UIA.clickElement('=')
        self.UIA.clickElement('2') #输入1时会找到左边的框，暂时输入2，错误的内容（可以用xpath解决）
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_fillInBlank_3(self):
        #第三道题答案：整数有0、-30、+20，负数-3/8、-2.6
        print('\n' + '开始作答第三道填空题... ')
        #找到第1个空
        self.UIA.tapByCoordinate(285,194)
        self.UIA.tapByCoordinate(285,194)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #选择三个整数
        self.UIA.tapByCoordinate(103,420)
        self.UIA.tapByCoordinate(142,420)
        self.UIA.tapByCoordinate(255,420)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #找到第2个空
        self.UIA.tapByCoordinate(80,250)
        self.UIA.tapByCoordinate(80,250)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #选择两个负数
        self.UIA.tapByCoordinate(43,408)
        self.UIA.tapByCoordinate(167,518)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_fillInBlank_4(self):
        #第四道题答案：(x+7)(x-7)
        print('\n' + '开始作答第四道填空题... ')
        self.UIA.tapByCoordinate(248,152)
        self.UIA.tapByCoordinate(248,152)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #输入答案(x+7)(x-7)
        self.UIA.clickElement('公式')
        self.UIA.clickElement('(')
        self.UIA.clickElement('abc')
        self.UIA.clickElement('x')
        self.UIA.clickElement('常用')
        self.UIA.clickElement('+')
        self.UIA.clickElement('7')
        self.UIA.clickElement('公式')
        self.UIA.clickElement(')')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(102,414)
        self.UIA.clickElement('abc')
        self.UIA.tapByCoordinate(100,526)
        self.UIA.clickElement('常用')
        self.UIA.clickElement('-')
        self.UIA.tapByCoordinate(107,369)
        self.UIA.clickElement('公式')
        self.UIA.tapByCoordinate(157,414)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_fillInBlank_5(self):
        #第五道题答案：ab(a+2)(a-2);(x+y-1)(x-y+1)
        #找到第一个空
        print('\n' + '开始作答第五道填空题...')
        self.UIA.tapByCoordinate(230,214)
        self.UIA.tapByCoordinate(230,214)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #输入ab(a+2)(a-2)
        self.UIA.clickElement('abc')
        self.UIA.clickElement('a')
        self.UIA.clickElement('b')
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('公式')
        self.UIA.clickElement('(')
        self.UIA.clickElement('abc')
        self.UIA.tapByCoordinate(50,451) #a
        self.UIA.clickElement('常用')
        self.UIA.clickElement('+')
        self.UIA.tapByCoordinate(182,478) #2
        self.UIA.saveScreen(self.screenPath, self.screenName)
        #self.UIA.clickElement('2') #用这种方式点2报错
        self.UIA.clickElement('公式')
        self.UIA.clickElement(')')
        self.UIA.tapByCoordinate(102,414) #(
        self.UIA.clickElement('abc')
        self.UIA.tapByCoordinate(50,451)
        self.UIA.clickElement('常用')
        self.UIA.clickElement('-')
        self.UIA.tapByCoordinate(182,478)
        self.UIA.clickElement('公式')
        self.UIA.tapByCoordinate(157,414) #)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #找到第2个空
        time.sleep(1)
        self.UIA.tapByCoordinate(302,292) #84+178+40=302 282+10=292
        self.UIA.tapByCoordinate(302,292)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        #输入答案(x+y-1)(x-y+1)
        self.UIA.clickElement('公式')
        self.UIA.tapByCoordinate(102,414) #(
        self.UIA.clickElement('abc')
        self.UIA.clickElement('x')
        self.UIA.clickElement('常用')
        self.UIA.tapByCoordinate(43,369) # +
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.clickElement('abc')
        self.UIA.clickElement('y')
        self.UIA.clickElement('常用')
        self.UIA.tapByCoordinate(43,424) # -
        self.UIA.tapByCoordinate(108,478) # 1
        #self.UIA.clickElement('1')
        self.UIA.clickElement('公式')
        self.UIA.tapByCoordinate(157,414) # )
        self.UIA.saveScreen(self.screenPath, self.screenName)
        self.UIA.tapByCoordinate(102,414) # (
        self.UIA.clickElement('abc')
        self.UIA.tapByCoordinate(100,526) #x
        self.UIA.clickElement('常用')
        self.UIA.tapByCoordinate(43,424) #-
        self.UIA.clickElement('abc')
        self.UIA.tapByCoordinate(200,375) #y
        self.UIA.clickElement('常用')
        self.UIA.tapByCoordinate(43,369) #+
        self.UIA.tapByCoordinate(108,478) #1
        self.UIA.clickElement('公式')
        self.UIA.tapByCoordinate(157,414) #)
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.UIA.clickElement('确定')

    def test_fillInBlank_6(self):

        self.UIA.endAnswer(self.screenPath)

        #回到全部任务页
        self.UIA.waitForElement('切换班级',5)
        text = self.UIA.getTextOfElement('切换班级')
        self.UIA.saveScreen(self.screenPath, self.screenName)

        self.assertEqual(text,'切换班级')

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(testFillInBlank)
    unittest.TextTestRunner(verbosity=2).run(suite)