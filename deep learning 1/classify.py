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