import numpy as np
import matplotlib.pyplot as plt

# 生成包含3个频率成分的信号
fs = 1000  # 采样频率为1000Hz
t = np.arange(0, 2, 1/fs)  # 生成时间序列，持续1秒
frequencies = [10, 20, 30]  # 3个频率成分分别为10Hz, 20Hz, 30Hz
amplitudes = [1, 0.5, 0.3]  # 对应的振幅
x = np.zeros_like(t)  # 初始化信号

for freq, amp in zip(frequencies, amplitudes):
    x += amp * np.sin(2 * np.pi * freq * t)  # 将各频率成分的正弦波信号相加得到最终信号

# 绘制原始信号波形
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Signal with 3 Frequencies')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 对信号进行傅里叶变换
N = len(x)  # 信号长度
X = np.fft.fft(x)  # 进行傅里叶变换
freq = np.fft.fftfreq(N, 1/fs)  # 计算频率轴

# 绘制频谱图
plt.subplot(2, 1, 2)
plt.plot(freq, np.abs(X))
plt.title('Frequency Spectrum')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 50)  # 限制频率范围

plt.tight_layout()
plt.show()
