import numpy as np
import matplotlib.pyplot as plt

# 生成信号的时间序列
fs = 1000  # 采样频率为1000Hz
t = np.arange(0, 2, 1/fs)  # 生成时间序列，持续1秒

# 不同阶段的频率和振幅列表
frequencies_list = [[10, 20, 30], [15, 25, 35, 45], [12, 22, 32, 42, 52]]
amplitudes_list = [[1, 0.5, 0.3], [1, 0.7, 0.4, 0.2], [1, 0.8, 0.6, 0.4, 0.2]]

for frequencies, amplitudes in zip(frequencies_list, amplitudes_list):
    # 生成信号
    x = np.zeros_like(t)
    for freq, amp in zip(frequencies, amplitudes):
        x += amp * np.sin(2 * np.pi * freq * t)  # 各频率成分的正弦波信号相加得到最终信号

    # 绘制原始信号波形
    plt.figure()
    plt.subplot(2, 1, 1)
    plt.plot(t, x)
    plt.title(f'Signal with {len(frequencies)} Frequencies')
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
    plt.xlim(0, max(frequencies) + 10)  # 限制频率范围

    plt.tight_layout()
    plt.show()
