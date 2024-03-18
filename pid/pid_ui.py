# 这段代码实现了一个具有调参界面和实时显示功能的PID控制器。在GUI界面中，可以通过滑动条调节PID参数，实时更新控制器的输出波形。
# 在实时显示的波形图中，可以观察PID控制器输出信号随时间的变化。
# 通过调节滑动条，可以实时调整PID参数，并观察控制效果的变化。
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import Scale

# 初始化参数
Kp = 1.0
Ki = 0.1
Kd = 0.01
setpoint = 10.0

# 创建GUI界面
root = tk.Tk()
root.title('PID Controller')

# 创建滑动条用于调节PID参数
scale_Kp = Scale(root, label='Kp', from_=0, to=2, resolution=0.1, orient='horizontal')
scale_Kp.set(Kp)
scale_Kp.pack()

scale_Ki = Scale(root, label='Ki', from_=0, to=0.2, resolution=0.01, orient='horizontal')
scale_Ki.set(Ki)
scale_Ki.pack()

scale_Kd = Scale(root, label='Kd', from_=0, to=0.02, resolution=0.001, orient='horizontal')
scale_Kd.set(Kd)
scale_Kd.pack()

# 创建画布用于实时显示波形
fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(0, 10)
ax.set_ylim(-5, 5)

# 更新函数，用于实时更新波形
def update(frame):
    global Kp, Ki, Kd
    Kp = scale_Kp.get()
    Ki = scale_Ki.get()
    Kd = scale_Kd.get()

    output = []
    time = []

    dt = 0.01
    integral = 0.0
    prev_error = 0.0

    for t in np.arange(0, 10, dt):
        error = setpoint - t
        integral += error * dt
        derivative = (error - prev_error) / dt

        control = Kp * error + Ki * integral + Kd * derivative

        output.append(control)
        time.append(t)

        prev_error = error

    line.set_data(time, output)
    return line,

# 创建动画
ani = FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# 启动GUI界面
tk.mainloop()
