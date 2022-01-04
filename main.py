# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
# 获取高德地区数据
from GaoDeArea import GetData

GetData.get_data("重庆", "3")
