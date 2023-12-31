import requests
from bs4 import BeautifulSoup
from PIL import Image
import pandas as pd
import numpy as np

import streamlit as st

import function as fun

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
Chrome/55.0.2883.87 Safari/537.36'}


def generate():
    city_list = ['北京','上海','广州','深圳','重庆','成都','天津','南京','郑州','西安','武汉','长沙','合肥',
                 '杭州','石家庄','青岛','南昌','厦门','福州','昆明','沈阳','哈尔滨','太原','长春','济南']
    classify_list = ['演唱会','音乐会','话剧歌剧','舞蹈芭蕾','曲苑杂坛','度假休闲']
    st.header('演出查询程序')
    st.markdown('designer : YiLight(陈艺雨)')
    st.sidebar.expander('')
    st.sidebar.subheader('查询设置') 
    city_ = st.sidebar.selectbox('选择你所在的城市', city_list)
    classify_ = st.sidebar.selectbox('选择你查询的演出类型', classify_list)
    return city_,classify_
    
def crawler(city,sort):
    url = 'https://www.ypiao.com' + city + sort
    print(url)
    bs = BeautifulSoup(requests.get(url).content)
    result_l = bs.find_all(class_="xm-l l")  
    lenth = len(result_l)
    name = {}   #演出名称
    time = {}   #演出时间
    location = {}   #演出地点
    for i in range(lenth):
        item = result_l[i].find(class_="cc-title")
        name[i] = str(item.text).strip()
        item = result_l[i].find(class_="blc cc-time")
        time[i] = str(item.text).strip()
        item = result_l[i].find(class_="blc cc-changguan")
        location[i] = str(item.text).strip()
    name,time,location = fun.deleteAD(name,time,location,lenth)
    for i in range(lenth):
        col1 , col2 = st.columns([1,2])
        with col1:
            image = Image.open('1.jpg')
            st.image(image, caption='Sunrise by the mountains',width=200)
        with col2:
            st.subheader(name[i])
            st.markdown('演出时间: ' + time[i])
            st.markdown('演出地点: ' + location[i])

yi_city,yi_classify = generate()
crawler(fun.getPinyin(yi_city),fun.getClassify(yi_classify))
