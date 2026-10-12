#!/usr/bin/env python3
# ## 题 4｜斜抛运动轨迹
#
# **场景：** 一个物体从原点斜向上抛出。忽略空气阻力，需要计算它从出手到再次落地的完整轨迹。
#
# **你要完成的任务：** 生成飞行过程中的时间、水平位置和竖直位置，并计算最高点和水平射程，最后画出轨迹。
#
# **输入：**
#
# - `speed_ms`：初速度，单位是 `m/s`；
# - `angle_rad`：抛射角，使用弧度；
# - `gravity`：重力加速度，默认是 `9.81 m/s²`。
#
# **计算顺序：** 先计算总飞行时间，再生成从 0 到落地时刻的一组时间，最后计算每个时刻的 `x` 和 `y`。
#
# **返回：** `plot_projectile(...)` 返回 `(time_s, x_m, y_m, max_height_m, range_m, fig)`。
#
# **图像要求：** 在一个坐标轴中画出 `x_m` 与 `y_m` 的关系。
#
# **作答位置：** 下一格的 `plot_projectile(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

def plot_projectile(speed_ms, angle_rad, gravity=9.81):
    """返回斜抛运动的时间、坐标、最高点、射程和图像。"""
    raise NotImplementedError('请完成 plot_projectile')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_04():
    import numpy as np
    angle = np.pi / 6
    time, x, y, height, distance, fig = plot_projectile(10.0, angle)
    expected_time = 2 * 10 * np.sin(angle) / 9.81
    assert np.isclose(time[-1], expected_time)
    assert np.isclose(height, (10 * np.sin(angle))**2 / (2 * 9.81))
    assert np.isclose(distance, 10**2 * np.sin(2 * angle) / 9.81)
    assert np.isclose(y[0], 0) and np.isclose(y[-1], 0)
    assert len(fig.axes) == 1

try:
    test_exercise_04()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
