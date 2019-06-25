#!/usr/local/bin/python3
#coding:utf-8

import unittest
from HTMLTestRunner import *
import sys
sys.path.append('../')
from common.uiAutoIos import *
sys.path.append('../')
#from common.sendEmail import *

# 运行报告的路径和名称
result = parentPATH('testResult/testReport.html')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 互动题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.interactiveQuestion.testInteractiveQuestion']))

    with open(result,'w') as f:
        runner = HTMLTestRunner(
            stream = f,
            title = '答题流程测试结果',
            description = '用例执行情况：',
            verbosity = 2
        )
        runner.run(suite)

    # SendMail(result)
