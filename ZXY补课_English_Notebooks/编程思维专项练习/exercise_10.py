#!/usr/bin/env python3
# ## 题 10｜冲击加速度记录中的超限时刻
#
# **场景：** 冲击试验记录了一组加速度。无论正方向还是负方向，只要加速度的绝对值超过限值，就算一次超限。
#
# **你要完成的任务：** 标记所有超限点，统计超限数量，找出第一次超限的时间，并画图显示结果。
#
# **输入：**
#
# - `time_s`：采样时间数组；
# - `acceleration_ms2`：与时间一一对应的加速度数组；
# - `limit_ms2`：超限阈值，默认是 `20.0 m/s²`。
#
# **超限条件：** `abs(acceleration_ms2[i]) > limit_ms2`。刚好等于限值不算超限。
#
# **返回：** `analyse_shock_record(...)` 返回 `(risk_mask, risk_count, first_risk_time, fig)`；没有超限时，`first_risk_time` 返回 `None`。
#
# **要求：** 掩码可以用 NumPy 计算；第一次超限时间用 `for` 和 `if` 查找；`fig` 包含两个坐标轴。
#
# **作答位置：** 下一格的 `analyse_shock_record(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

def analyse_shock_record(time_s, acceleration_ms2, limit_ms2=20.0):
    """返回超限掩码、数量、首次超限时间和图像。"""
    raise NotImplementedError('请完成 analyse_shock_record')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_10():
    import numpy as np
    time = np.array([0, 1, 2, 3, 4], dtype=float)
    acceleration = np.array([5, 21, -25, 20, 0], dtype=float)
    mask, count, first, fig = analyse_shock_record(time, acceleration)
    assert np.array_equal(mask, [False, True, True, False, False])
    assert count == 2 and first == 1.0 and len(fig.axes) == 2

try:
    test_exercise_10()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
