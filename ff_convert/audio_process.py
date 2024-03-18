import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# 加载音频文件
file_path = 'audio.wav'
data, fs = sf.read(file_path)

# 提取左声道或右声道的音频信号（如果是双声道音频）
# 如果是双声道音频，可以选择提取左声道data[:, 0]或右声道data[:, 1]
audio_signal = data

# 生成时间序列
t = np.arange(0, len(audio_signal)/fs, 1/fs)

# 绘制音频信号波形图
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, audio_signal)
plt.title('Audio Signal Waveform')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 对音频信号进行傅里叶变换
N = len(audio_signal)
X = np.fft.fft(audio_signal)
freq = np.fft.fftfreq(N, 1/fs)

# 绘制音频信号频谱图
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(X))
plt.title('Audio Signal Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, fs/2)  # 限制频率范围在0到采样频率的一半之间

plt.tight_layout()
plt.show()
