# 这段代码实现了一个简单的PID控制器，根据给定的目标值和PID参数，计算控制信号并模拟控制过程。
# 在波形展示部分，展示了PID控制输出的波形变化以及PID控制器中P、I、D三个部分的波形变化。
# 可以通过调整PID参数和目标值，观察控制过程的波形变化。
import numpy as np
import matplotlib.pyplot as plt

# PID参数
Kp = 1.0
Ki = 0.1
Kd = 0.01

# 目标值
setpoint = 10.0

# 初始化变量
dt = 0.01
integral = 0.0
prev_error = 0.0
prev_time = 0.0
output = []
time = []

# 模拟PID控制过程
for t in np.arange(0, 10, dt):
    error = setpoint - t
    integral += error * dt
    derivative = (error - prev_error) / dt

    control = Kp * error + Ki * integral + Kd * derivative

    output.append(control)
    time.append(t)

    prev_error = error

# 绘制波形
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, output)
plt.title('PID Control Output')
plt.xlabel('Time')
plt.ylabel('Control Signal')

plt.subplot(2, 1, 2)
plt.plot(time, [setpoint - t for t in time], label='Error')
plt.plot(time, [Kp * (setpoint - t) for t in time], label='P-Term')
plt.plot(time, [Ki * integral for t in time], label='I-Term')
plt.plot(time, [Kd * derivative for t in time], label='D-Term')
plt.legend()
plt.title('PID Components')
plt.xlabel('Time')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()