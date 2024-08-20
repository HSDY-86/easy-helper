# 1. 获取用户语音输入
# 2. 语音识别
# 3. 识别到 对应的指令 可以给出 不一样的反馈
#
# 比如：“查天气” 反馈 杭州今日天气
# 比如：“吃饭” 反馈“你太胖了 该减肥了”


from demo import record_audio
from demo2 import recognize

hint_dict = {
    '天气': '最近的气温太热了，真反常。',
    '酒店': '去吃饭嘞。',
    '星座': '我的是人马座。'
}

while True:
    print('快来一起聊天吧！')
    record_audio('录音.wav')
    temp = recognize()
    if '天气' in temp:
        print(hint_dict.get('天气'))
    elif '酒店' in temp:
        print(hint_dict.get('酒店'))
    elif '星座' in temp:
        print(hint_dict.get('星座'))
    else:
        print('没听清，请再说一遍。')

