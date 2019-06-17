#!/usr/local/bin/python3
#coding:utf-8

import unittest
from HTMLTestRunner import *
import sys
sys.path.append('../')
from common.uiAutoIos import *
sys.path.append('../')
from common.sendEmail import *

# 运行报告的路径和名称
result = parentPATH('testResult/testReport.html')

if __name__ == '__main__':
    suite = unittest.TestSuite()
    # 互动题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.interactiveQuestion.testInteractiveQuestion']))
    # 填空题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.fillInBlank.testFillInBlank']))
    # 选择题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.choiceQuestion.testChoice']))
    # 复合判断题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.compoundJudgement.testCompoundJudgement']))
    # 主观题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.subjectiveQuestion.testSubjectiveQuestion']))
    # 幼儿游戏题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.babyGame.testBabyGame']))
    # 竖式填空题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.fillInBlank2.testFillInBlank2']))
    # 小低游戏题
    suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes.childGame.testChildGame']))
    # 口述题和视频题只能在真机上运行，模拟器不支持录视频
    #suite.addTests(unittest.TestLoader().loadTestsFromNames(['mathes,videoPaper.testVideoPaper']))

    with open(result,'w') as f:
        runner = HTMLTestRunner(
            stream = f,
            title = '答题流程测试结果',
            description = '用例执行情况：',
            verbosity = 2
        )
        runner.run(suite)

    # SendMail(result)
