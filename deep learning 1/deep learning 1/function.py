import requests
from bs4 import BeautifulSoup
import time

def getClassify(c):
    if c == '演唱会':
        return '/yanchanghui'
    elif c == '音乐会':
        return '/yinyuehui'
    elif c == '话剧歌剧':
        return '/huajugeju'
    elif c == '舞蹈芭蕾':
        return '/wudaobalei'
    elif c == '曲苑杂坛':
        return '/wuyuanzatan'
    elif c == '度假休闲':
        return '/dujiaxiuxian'
    else:
        return ''

def single_get_first(unicode1):
    str1 = unicode1.encode('gbk')
    try:
        ord(str1)
        return str1
    except:
        asc = str1[0] * 256 + str1[1] - 65536
        if asc >= -20319 and asc <= -20284:
            return 'a'
        if asc >= -20283 and asc <= -19776:
            return 'b'
        if asc >= -19775 and asc <= -19219:
            return 'c'
        if asc >= -19218 and asc <= -18711:
            return 'd'
        if asc >= -18710 and asc <= -18527:
            return 'e'
        if asc >= -18526 and asc <= -18240:
            return 'f'
        if asc >= -18239 and asc <= -17923:
            return 'g'
        if asc >= -17922 and asc <= -17418:
            return 'h'
        if asc >= -17417 and asc <= -16475:
            return 'j'
        if asc >= -16474 and asc <= -16213:
            return 'k'
        if asc >= -16212 and asc <= -15641:
            return 'l'
        if asc >= -15640 and asc <= -15166:
            return 'm'
        if asc >= -15165 and asc <= -14923:
            return 'n'
        if asc >= -14922 and asc <= -14915:
            return 'o'
        if asc >= -14914 and asc <= -14631:
            return 'p'
        if asc >= -14630 and asc <= -14150:
            return 'q'
        if asc >= -14149 and asc <= -14091:
            return 'r'
        if asc >= -14090 and asc <= -13119:
            return 's'
        if asc >= -13118 and asc <= -12839:
            return 't'
        if asc >= -12838 and asc <= -12557:
            return 'w'
        if asc >= -12556 and asc <= -11848:
            return 'x'
        if asc >= -11847 and asc <= -11056:
            return 'y'
        if asc >= -11055 and asc <= -10247:
            return 'z'
        return ''

def getPinyin(string):
    if string == None:
        return None
    lst = list(string)
    charLst = []
    for l in lst:
        charLst.append(single_get_first(l))
    return '/'+''.join(charLst)


#城市经纬度
def getLL(city):
    if city == '北京':
        return 116.405289,39.904987
    if city == '上海':
        return 121.472641,31.231707
    if city == '广州':
        return 113.28064,23.125177
    if city == '深圳':
        return 114.064552,22.548457
    if city == '重庆':
        return 106.504959,29.533155
    if city == '成都':
        return 104.065735,30.659462
    if city == '天津':
        return 117.190186,39.125595
    if city == '南京':
        return 118.76741,32.041546
    if city == '郑州':
        return 113.665413,34.757977
    if city == '西安':
        return 108.948021,34.263161
    if city == '武汉':
        return 114.298569,30.584354
    if city == '长沙':
        return 112.982277,28.19409
    if city == '合肥':
        return 17.283043,31.861191
    if city == '杭州':
        return 120.15358,30.287458
    if city == '石家庄':
        return 114.502464,38.045475
    if city == '青岛':
        return 120.369557,36.094406
    if city == '南昌':
        return 115.892151,28.676493
    if city == '厦门':
        return 118.08233,24.44543
    if city == '福州':
        return 119.306236,26.075302
    if city == '昆明':
        return 102.71225,25.040609
    if city == '沈阳':
        return 123.429092,41.796768
    if city == '哈尔滨':
        return 126.642464,45.756966
    if city == '太原':
        return 112.549248,37.857014
    if city == '长春':
        return 125.324501,43.886841
    if city == '济南':
        return 117.000923,36.675807
    return 116.405289,39.904987

#获取地址中的城市
def getCity(loc):
    str_0 = str(loc)
    str_1 = str_0.partition("[")
    str_2 = str(str_1[2]).partition("]")
    return str_2[0]

#city = getCity('[上海]上海东方体育中心')
#longitude,latitude = getLL(city)
#print(str(longitude) + ',' + str(latitude))

#去掉广告
def deleteAD(name,time,location,placard,length):
    if name[0] == '有票礼品卡(礼品馈赠典雅之选)':
        for i in range(length-1):
            name[i] = name[i+1]
            time[i] = time[i+1]
            location[i] = location[i+1]
            placard[i] = placard[i+1]
    return name,time,location,placard

#提取图片下载地址
def getimg(result_img):
    str_0 = str(result_img)
    str_1 = str_0.partition("\"")
    str_2 = str(str_1[2]).partition("\"")
    str_3 = str(str_2[2]).partition("\"")
    str_4 = str(str_3[2]).partition("\"")
    str_5 = str(str_4[2]).partition("\"")
    str_6 = str(str_5[2]).partition("\"")
    return str_6[0]
