# 这段代码将生成12个不同音符的音频信号，每个音符持续2秒，并将它们合成为一个音频文件audio_notes.wav。
# 然后加载音频文件，绘制音频信号的波形图和频谱图。运行此代码后，可以听到包含12个不同音符的音频，
# 并查看其波形和频谱。
import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# 定义12个音符的频率（A4至A5）
notes_freq = [440, 466.16, 493.88, 523.25, 554.37, 587.33, 622.25, 659.25, 698.46, 739.99, 783.99, 830.61]

# 生成音频信号
fs = 44100  # 采样频率为44100Hz
duration = 2  # 每个音符持续2秒
t = np.linspace(0, duration, int(fs*duration), endpoint=False)

audio_signal = np.zeros(fs*12*duration)  # 初始化音频信号数组

for i, freq in enumerate(notes_freq):
    note_signal = 0.5 * np.sin(2 * np.pi * freq * t)  # 生成每个音符的正弦波信号
    audio_signal[i*fs*duration:(i+1)*fs*duration] = note_signal  # 将每个音符信号添加到总音频信号中

# 写入音频文件
file_path = 'audio_notes.wav'
sf.write(file_path, audio_signal, fs)

print(f'音频文件已生成：{file_path}')

# 加载音频文件
data, fs = sf.read(file_path)
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
