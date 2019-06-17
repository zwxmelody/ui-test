#!/usr/local/bin/python3
#coding:utf-8

import requests
import json
import os
import configparser


# 当前路径+p 用法：PATH(fillInBlank.py)

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# 上级目录+p
parentPATH = lambda p : os.path.abspath(
    os.path.join(os.path.dirname(os.getcwd()),p)
)

# 上上级目录+p
superPATH = lambda p : os.path.abspath(
    os.path.join(os.path.dirname(os.path.dirname(os.getcwd())),p)
)

"""
清旧关卡的除答题数据
"""

def clearData(stuId, city, taskItemId):
    url = r'http://ipsapi-fz.speiyou.cn/stone-ips-rest/repairData/removeStudentDataByCourseLevel'
    reqHeader = {}
    reqParam = {}

    reqHeader['area'] = '010'
    reqHeader['ics-token'] = '446a654cf768818ef76645fd8a09eacd'
    reqHeader['Content-Type'] = 'application/x-www-form-urlencoded'

    reqParam['stuLoginName'] = stuId
    reqParam['cityCode'] = city
    reqParam['courseLevelId'] = taskItemId

    rsps = requests.get(url=url, headers=reqHeader, params=reqParam)

    data = json.loads(rsps.content)['data']

    if rsps.status_code == 200 and data == '清除成功':

        return True
    else:
        return False

"""
初始化旧关卡数据（使用clearData操作时偶尔会遇到清除答题数据失败的情况，调用初始化接口一下
"""
def initStudent(stuId, city, classId):
    url = r'http://ipsapi-fz.speiyou.cn/stone-ips-rest/levelToNewTaskServer/addInitStudentAll'
    reqHeader = {}
    reqParam = {}

    reqHeader['area'] = '010'
    reqHeader['ics-token'] = '446a654cf768818ef76645fd8a09eacd'
    reqHeader['Content-Type'] = 'application/x-www-form-urlencoded'

    reqParam['studentIds'] = stuId
    reqParam['cityCode'] = city
    reqParam['classId'] = classId

    rsps = requests.post(url=url, headers=reqHeader, params=reqParam)

    code = json.loads(rsps.content)['code']

    if rsps.status_code == 200 and code == '000000':
        return True
    else:
        return False

"""
删除文件夹下的所有文件
"""
def delFile(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            delFile(c_path)
        else:
            os.remove(c_path)


"""
获取要保存的截屏的路径，如果目录非空则清空目录，如果目录不存在则创建目录
"""
def getScreenShotDir(subject,file):
    # testSuite中执行和testCases下执行生成的screenShot的路径会不一样
    subjectPath = parentPATH('screenShot' + '/' + subject)
    filePath = subjectPath + '/' + file
    if os.path.exists(filePath):
        if not os.listdir(filePath): # 如果filePath目录为空
            pass
        else:
            delFile(filePath) # 先删除filePath目录的图片文件
    else:
        os.makedirs(filePath, mode=0o777, exist_ok=True) # 如果目录不存在直接创建目录
    return filePath

"""
获取给定配置文件的给定section的optionList
主要给坐标用，坐标写在与paper对应的配置文件，用逗号隔开
"""
def getOptionList(path, section):
    config = configparser.ConfigParser()
    config.read(path, encoding='utf-8')
    options = config.options(section)
    optionList = []
    for o in options:
        val = config.get(section, o).split(',')
        optionList.append(val)

    return optionList

"""
从config/runner中获取运行时的环境runType 和 phoneType
"""
def getRuntimeConfig(section):
    type = []
    # 通过testSuite执行
    file = parentPATH('config/runner')
    # 通过单文件调试
    #file = superPATH('config/runner')
    config = configparser.ConfigParser()
    config.read(file, encoding='utf-8')
    rt = config.get(section, 'runType')
    type.append(int(rt))
    pt = config.get(section, 'phoneType')
    type.append(pt)
    return type
