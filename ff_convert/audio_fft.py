import numpy as np
import matplotlib.pyplot as plt

# 生成一个简单的正弦波信号
fs = 1000  # 采样频率为1000Hz
t = np.arange(0, 1, 1/fs)  # 生成时间序列，持续1秒
f = 10  # 正弦波频率为10Hz
x = np.sin(2 * np.pi * f * t)  # 生成正弦波信号

# 绘制原始信号波形
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')

# 对信号进行周期采样
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
