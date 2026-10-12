#!/usr/bin/env python3
# ## 题 3｜应变计电压的零点校准
#
# **场景：** 应变计输出的是电压。传感器在没有应变时仍有 `0.002 V` 的零点电压，因此必须先减去零点，再乘标定系数，才能得到应变。
#
# **你要完成的任务：** 把一组原始电压全部换算成应变，并取出前三项以及全部应变的平均值。
#
# **输入：**
#
# - `raw_voltage`：一维 NumPy 电压数组；
# - `zero_voltage`：零点电压，默认是 `0.002 V`；
# - `gauge_factor`：标定系数，默认是 `2.0`。
#
# **计算规则：** 对数组中的每个电压 `v` 计算 `strain = gauge_factor * (v - zero_voltage)`。
#
# **返回：** `calibrate_strain_voltage(...)` 返回 `(strain, first_three, mean_strain)`：
#
# - `strain`：全部校准后的应变；
# - `first_three`：`strain` 的前三项；
# - `mean_strain`：全部应变的平均值。
#
# **要求：** 不能修改传入的 `raw_voltage`。
#
# **作答位置：** 下一格的 `calibrate_strain_voltage(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
import numpy as np

def calibrate_strain_voltage(raw_voltage, zero_voltage=0.002,
                             gauge_factor=2.0):
    """返回应变数组、前三项和平均应变，不修改原始电压。"""
    raise NotImplementedError('请完成 calibrate_strain_voltage')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_03():
    import numpy as np
    raw = np.array([0.002, 0.007, 0.012, 0.004, 0.010])
    before = raw.copy()
    strain, first_three, mean = calibrate_strain_voltage(raw)
    expected = 2.0 * (raw - 0.002)
    assert np.allclose(strain, expected)
    assert np.allclose(first_three, expected[:3])
    assert np.isclose(mean, expected.mean()) and np.array_equal(raw, before)

try:
    test_exercise_03()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
