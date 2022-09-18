# coding：utf-8 -*-
# author 小红帽
# time: 2022/9/5 14:43


import statsmodels.api as sm
from pandas import DataFrame

dataDict = {'name': [], 'describe_short': []}

for modstr in dir(sm.datasets):
    try:
        mod = eval('sm.datasets.%s' % modstr)
        dataDict['describe_short'].append(mod.DESCRSHORT)
        dataDict['name'].append(modstr)
    except Exception as e:
        print("该模块无 DESCRSHORT 属性:\n", e)
        continue

dataDf = DataFrame({'describe_short': dataDict['describe_short']}, index=dataDict['name'])

print(dataDf)
