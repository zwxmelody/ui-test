# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Name:        UiAuto
# Created:     14/05/2019
#-------------------------------------------------------------------------------

import os
import time
from common.CommonLib import *
from appium import webdriver
import configparser
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction

class UiAuto:
    remoteHost = "http://127.0.0.1:4723/wd/hub"
    def __init__(self, configPath, section):
        self.desired_caps = {}
        self._driver = None
        config = configparser.ConfigParser()
        config.read(configPath, encoding='utf-8')
        options = config.options(section)
        try:
            for option in options:
                if(option == 'app'):
                    self.desired_caps[option] = CommonLib.PATH(config.get(section,option))
                elif(option == 'remoteHost'):
                    self.remoteHost = config.get(section,option)
                else:
                    self.desired_caps[option] = config.get(section,option)
        except:
            print('no such section or option error')

    def initDriver(self):
        self._driver = webdriver.Remote(self.remoteHost, self.desired_caps)

    def quitDriver(self):
        if(self._driver):
            self._driver.quit()

    """
    给定控件的xpath, id 或者name来查找控件

    Args:
         - controlInfo: 控件的信息，可以是xpath,id或者其他属性
    """
    def findElement(self, controlInfo):
        if(controlInfo.startswith("(//") or controlInfo.startswith("//")):
            try:
                element = self._driver.find_element_by_xpath(controlInfo)
            except:
                return
        else:
            #剩下的字符串没有特点，无法区分，因此先尝试通过accessibility_id查找
            try:
                element = self._driver.find_element_by_accessibility_id(controlInfo)
            except:
                try:
                    element = self._driver.find_element_by_name(controlInfo)
                except:
                    #如果通过名称不能找到则通过class name查找
                    element = self._driver.find_element_by_class_name(controlInfo)

        return element

    """
    在一个已知的控件中通过给定控件的xpath, id 或者name来查找子控件

    :Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性
    """
    def findElementInParentElement(self, parentElement, childElementInfo):
        element = ""
        if(childElementInfo.startswith("//")):
            element = parentElement.find_element_by_xpath(childElementInfo)
        else:
            #剩下的字符串没有特点，无法区分，因此先尝试通过名称查找
            try:
                element = parentElement.find_element_by_accessibility_id(childElementInfo)
            except NoSuchElementException:
                element = parentElement.find_element_by_name(childElementInfo)
            except:
                #如果通过名称不能找到则通过class name查找
                element = parentElement.find_element_by_class_name(childElementInfo)

        return element

    """
    滑动操作

    Args:
         - t: 多长时间内完成该操作,单位是毫秒，默认0.5秒
         - n: 滑动次数，默认为1
    Usage:
        self.swipeUp(t=1,n=10)
    """
    def swipeUp(self, t=500, n=1):
        '''向上滑动屏幕'''
        l = self._driver.get_window_size()
        x1 = l['width'] * 0.5     # x坐标
        y1 = l['height'] * 0.75   # 起始y坐标
        y2 = l['height'] * 0.5   # 终点y坐标
        for i in range(n):
            self._driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, t=500, n=1):
        '''向下滑动屏幕'''
        l = self._driver.get_window_size()
        x1 = l['width'] * 0.5          # x坐标
        y1 = l['height'] * 0.5        # 起始y坐标
        y2 = l['height'] * 0.7        # 终点y坐标
        for i in range(n):
            self._driver.swipe(x1, y1, x1, y2,t)

    def swipeLeft(self, t=500, n=1):
        '''向左滑动屏幕'''
        l = self._driver.get_window_size()
        x1 = l['width'] * 0.75  #起始x坐标
        y1 = l['height'] * 0.5  #起始y坐标
        x2 = l['width'] * 0.05  #终点x坐标
        for i in range(n):
            self._driver.swipe(x1, y1, x2, y1, t)

    def swipeRight(self, t=500, n=1):
        '''向右滑动屏幕'''
        l = self._driver.get_window_size()
        x1 = l['width'] * 0.05  #起始x坐标
        y1 = l['height'] * 0.5  #起始y坐标
        x2 = l['width'] * 0.75  #终点x坐标
        for i in range(n):
            self._driver.swipe(x1, y1, x2, y1, t)

    """
    上滑直到查找的元素出现
    Args:
     - n：向上滑的次数，超过这个次数，即使没找到元素，也退出
     - e：要查找的元素对象，id,name,xpath等

    Usage:
        self.swipeToFindElement(10,'com.xp.tugele:id/tv_bq_toutiao_title')
    """
    def swipeToFindElement(self, n, e):
        for i in range(n):
            try:
                element = self.findElement(e)
                return element
            except:
                self.swipeUp()

    """
    长按点击操作
    Args:
     - x,y： 长按点的坐标
     - peroid: 多长时间内完成该操作,单位是毫秒

    Usage:
        self.longPress(50, 50, 500)
    """
    def longPress(self, x, y, peroid):
        self._driver.tap([(x, y)], peroid)

    """
    点击某一个控件，如果该控件不存在则会抛出异常

    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    """
    def clickElement(self, elementInfo):
        element = self.findElement(elementInfo)
        element.click()

    """
    获取某个控件显示的文本，如果该控件不能找到则会抛出异常

    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性

    """
    def getTextOfElement(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.text

    """
    清除文本框里面的文本

    Usage:
        self.clearTextEdit(elementInfo)
    """
    def clearTextEdit(self, elementInfo):
        element = self.findElement(elementInfo)
        element.clear()

    """
    等待某个控件显示

    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
         - period：等待的秒数
    """
    def waitForElement(self, elementInfo, period):
        for i in range(0, period):
            time.sleep(1)
            try:
                self.findElement(elementInfo)
                return
            except:
                continue

        raise Exception("Cannot find %s in %d seconds" %(elementInfo,period))

    """
    等待某个控件不再显示

    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
         - period：等待的秒数
    """
    def waitForElementNotPresent(self, elementInfo, period):
        for i in range(0, period):
            time.sleep(1)
            #不存在了则返回
            if(not self.checkElementIsShown(elementInfo)):
                return
            else:
                continue

        raise Exception("Cannot find %s in %d seconds" %(elementInfo,period))

    """
    判断某个控件是否显示

    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    Return:
        True: 如果当前画面中期望的控件能被找到
    """
    def checkElementIsShown(self, elementInfo):
        try:
            self.findElement(elementInfo)
            return True
        except:
            return False

    """
    判断某个控件是否显示在另外一个控件中

    Args:
        - parentElement: 父控件，是一个已知的WebElement
        - childElementInfo: 子控件的信息，可以是xpath,id或者其他属性
    Return:
        True: 如果当前画面中期望的控件能被找到
    """
    def checkElementShownInParentElement(self, parentElement, childElementInfo):
        try:
            self.findElementInParentElement(parentElement, childElementInfo)
            return True
        except:
            return False

    """
    判断某个控件是否被选中

    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    Return:
        True: 如果当前画面中期望的控件能被选中
    """
    def checkElementIsSelected(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.is_selected()


    """
    判断某个开关控件是否被选中

    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    Return:
        True: 如果当前画面中期望的控件能被选中
    """
    def checkElementIsChecked(self, elementInfo):
        element = self.findElement(elementInfo)
        if(element.get_attribute("checked") == "false"):
            return False
        else:
            return True

    """
    判断某个控件是否enabled
    Args:
         - elementInfo: 控件的信息，可以是xpath,id或者其他属性
    Return:
        True: 如果当前画面中期望的控件enabled
    """
    def checkElementIsEnabled(self, elementInfo):
        element = self.findElement(elementInfo)
        return element.get_attribute("enabled")

    """
    启动测试程序
    """
    def launchApp(self):
        self._driver.launch_app()

    """
    关闭测试程序
    """
    def closeApp(self):
        self._driver.close_app()

    """
    获取测试设备的OS

    :Return: Android或者ios
    """
    def getDeviceOs(self):
        return self.desired_caps['platformName']

    """
    获取context
    """
    def getContext(self):
        return self._driver.contexts


    def switchContext(self, contextName):
        self._driver.switch_to.context(contextName)

    """
    根据相对坐标点击屏幕位置
    """
    def tapByCoordinate(self,x1,y1):
        # 设定系数,控件在当前手机的坐标位置除以当前手机的最大坐标就是相对的系数了
        x2 = 375 #采样测试手机：iphone6，x2,y2为采样手机的屏幕大小
        y2 = 667
        a1 = x1 / x2 #x1,y1为绝对坐标
        b1 = y1 / y2
        # 获取当前手机屏幕大小X,Y
        X = self._driver.get_window_size()['width']
        Y = self._driver.get_window_size()['height']
        # 屏幕坐标乘以系数即为用户要点击位置的具体坐标
        self._driver.tap([(a1 * X, b1 * Y)])

    """
    点击给定的x,y位置
    """
    def singleTap(self,x,y):
        self._driver.tap([(x,y)])

    """
    给元素赋值send_keys
    """
    def sendKeys(self,elementInfo,value):
        element = self.findElement(elementInfo)
        element.send_keys(value)

    """
    从位置A(x1,y1)拖拽到位置B(x2,y2),通过坐标
    """
    def dragFromDownToUp(self, x1,y1,x2,y2, period=1):

        self._driver.execute_script('mobile: dragFromToForDuration',{'duration': period, 'fromX': x1, 'fromY': y1, 'toX': x2, 'toY': y2,})

    """
    开始答题前环境准备：从启动APP处理各种可能弹窗到点击全部任务进入全部任务页面
    """

    def beforeAnswer(self):
        # 首次启动可能会弹引导页
        try:
            self.clickElement('xcl studyhome guide confirm bu')
        except:
            pass

        # 每天首次启动可能会弹升级弹窗
        try:
            self.clickElement('暂不升级')
        except:
            pass

        # 处理神策的弹窗
        try:
            self.waitForElement('确定', 5)
            self.clickElement('确定')
        except:
            pass

        # 进入全部任务页面
        try:
            self.waitForElement('全部任务', 5)
            self.clickElement('全部任务')
        except:
            raise Exception("没有找到全部任务按钮！")

    """
    点击交卷后处理积分等一些弹窗
    为了保存截屏，传个路径进来
    """
    def endAnswer(self, path):
        #交卷
        self.waitForElement('交卷', 8)
        print('\n' + '作答完毕，点击交卷')
        # 在真机上有小手的引导时，点不了交卷，sleep一会
        time.sleep(5)
        self.clickElement('交卷')

        #确认交卷
        self.waitForElement('确定要交卷吗?',5)
        self.saveScreen(path, 'commintButton')
        self.clickElement('(//XCUIElementTypeButton[@name="确定"])[1]')

        #作答正确后可能会出现玩一把页面，点击玩一把
        try:
            self.waitForElement('Great!',5)
            self.saveScreen(path, 'wanyiba')
            self.clickElement('玩一把')
        except:
            print('没有出现玩一把！')
            self.saveScreen(path, 'nowanyiba')

        try:
            #首次玩可能会有大转盘抽积分的页面
            self.waitForElement('turnTable begin btn', 5)
            self.saveScreen(path, 'dazhuanpan')
            self.clickElement('turnTable begin btn')
            self.saveScreen(path, 'clickzhuanpan')
        except:
            print('没有出现大转盘抽积分！')
            self.saveScreen(path, 'nozhuanpan')

            try:
                self.waitForElement('(//XCUIElementTypeImage[@name="allnewalert_img_cardgame_cardbg"])[2]', 5)
                self.clickElement('(//XCUIElementTypeImage[@name="allnewalert_img_cardgame_cardbg"])[2]')
                self.saveScreen(path, 'fanpai')
            except:
                print('没有出现翻牌抽积分！')


        # 出现作答结果页面，点击×。如果重复玩，由于积分没有清，则可能不会出现这个页面。
        try:
            print('\n' + '关闭作答结果页面，结束： ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            self.waitForElement('allnewalert btn answeralert cl',10)
            self.saveScreen(path, 'closeButton')
            self.clickElement('allnewalert btn answeralert cl')
        except:
            print('没有找到关闭按钮！')
            self.saveScreen(path, 'noCloseButton')

    """
    截屏，传入截图保存的路径和图片名字
    """
    def saveScreen(self, path, name):

        imgName = path + '/' + name + '_' + str(round(time.time()*1000)) + '.png'
        self._driver.get_screenshot_as_file(imgName)
        return

    """
    从位置(x1,y1)拖动到位置(x2,y2)
    """
    def touchAction(self,x1,y1,x2,y2):
        TouchAction(self._driver).press(x=x1,y=y1).wait(700)\
        .move_to(x=x2,y=y2).wait(700).release().perform()
