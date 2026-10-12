#!/usr/bin/env python3
# ## 题 8｜阻尼振动与首次进入位移限值
#
# **场景：** 一个振动系统的振幅随时间逐渐减小。工程上需要知道，在给定的采样时刻中，它第一次进入位移限值是什么时候。
#
# **你要完成的任务：** 计算所有采样时刻的位移，并从前往后找到第一个满足限值的时刻。
#
# **输入：**
#
# - `times_s`：非负、非递减的采样时间数组；
# - `amplitude_m`：初始振幅；
# - `omega_rad_s`：圆频率；
# - `damping_per_s`：阻尼系数；
# - `limit_m`：位移绝对值限值。
#
# **位移公式：** `x(t) = amplitude_m * exp(-damping_per_s*t) * cos(omega_rad_s*t)`。
#
# **达到限值的条件：** `abs(x(t)) <= limit_m`。
#
# **返回：** `damped_oscillation(...)` 返回 `(displacement_m, first_time_s)`；所有采样点都未达到限值时，`first_time_s` 返回 `None`。
#
# **要求：** 位移数组使用 NumPy 计算，首次时刻使用 `for` 和 `if` 查找。
#
# **作答位置：** 下一格的 `damped_oscillation(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
import numpy as np

def damped_oscillation(times_s, amplitude_m, omega_rad_s,
                       damping_per_s, limit_m):
    """返回阻尼振动位移和首次进入位移限值的时间。"""
    raise NotImplementedError('请完成 damped_oscillation')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_08():
    import numpy as np
    times = np.array([0, 0.5, 1.0, 1.5, 2.0])
    displacement, first = damped_oscillation(times, 0.1, np.pi, 0.5, 0.04)
    expected = 0.1 * np.exp(-0.5 * times) * np.cos(np.pi * times)
    assert np.allclose(displacement, expected)
    assert first == 0.5
    assert damped_oscillation(times, 0.1, np.pi, 0.5, 0.0)[1] is None

try:
    test_exercise_08()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
