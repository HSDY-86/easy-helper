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