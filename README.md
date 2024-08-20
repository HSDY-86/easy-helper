# easy helper
 

## 设计思路：
语音助手的设计旨在通过语音输入和语音输出提供人机交互的方式。它能够根据用户的语音指令识别用户的需求，并提供相应的回答或指导。


## 功能实现：

语音助手使用了两个模块：'demo'和'demo2'，并结合了语音录制和语音识别的功能。

首先，基于'demo'模块，语音助手通过record_audio函数录制用户的语音输入，将其保存在名为"录音.wav"的文件中。

```python
# demo

import wave
import pyaudio


# 拾音 / 通过代码 来获取音频
def record_audio(filename):
    mic = pyaudio.PyAudio()  # 创建一个是实例化对象
    stream = mic.open(
        format=pyaudio.paInt16,  # 音频样本使用16位整数，更高的音质，常见的音频格式
        channels=1,  # 音频流的声道数量，1是单声道，2是立体声
        rate=44100,  # 每秒钟采集的音频样本数量，44.1Hz，CD的标准采样率
        input=True,  # 指定的流是输入还是输出，
        frames_per_buffer=8192)  # 缓冲区的大小，每次从麦克风读取的音频数据帧数
    # 缓冲区越大，程序相应会稍慢

    print("开始录音...")
    frame = []  # 用于存储录音过程中的音频数据块
    for _ in range(0, int(44100 / 8192 * 5)):  # 以多少的采样率 录制多少秒
        data = stream.read(8192)
        frame.append(data)
    stream.stop_stream()  # 停止音频流
    stream.close()  # 关闭通道
    mic.terminate()  # 终止麦克风

    wf = wave.open(filename, 'wb')  # 写入数据
    wf.setnchannels(1)
    wf.setsampwidth(mic.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frame))
    wf.close()


record_audio('录音.wav')
```

接下来，基于'demo2'模块，语音助手调用recognize函数对录制好的音频文件进行识别，将识别结果保存在temp变量中。
然后，语音助手根据temp变量中包含的关键词判断用户的需求，并根据关键词提供相应的回答或提示。如果用户的语音输入中包含"天气"，语音助手会根据设定好的提示字典输出天气的提示信息；如果用户的语音输入中包含"酒店"，语音助手会输出去吃饭的提示信息；如果用户的语音输入中包含"星座"，语音助手会输出它个人的星座信息。如果用户的语音输入不包含以上关键词，语音助手会提示用户再次清晰地表达需求。
```python
# demo2


# 打开音频文件
wf = wave.open(audio_file, "rb")

# 初始化识别器
recognizer = KaldiRecognizer(model, wf.getframerate())

# 处理音频流
result = " "
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        res = recognizer.Result()
        result += json.loads(res)['text'] + " "

# 获取到最后的结果部分
final_res = recognizer.FinalResult()
result += json.loads(final_res)['text']
print('识别结果')
print(result)

# 关闭文件
wf.close()
```




## 问题及解决方案：

在开发过程中遇到了路径字符的报错以及环境的缺失，
通过对路径中的中文字符进行修改以及对环境的重新部署解决。

 
