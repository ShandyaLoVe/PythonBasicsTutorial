#!/usr/bin/env python3
# ## 题 6｜轴向构件的应力安全检查
#
# **场景：** 一批拉杆承受不同的轴向力，并且截面积也不同。需要计算每根拉杆的应力，判断是否低于许用应力。
#
# **你要完成的任务：** 计算应力、许用应力、安全判断、合格数量和最小安全余量。
#
# **输入：**
#
# - `force_N`：每根拉杆的轴向力数组，单位是 `N`；
# - `area_mm2`：对应的截面积数组，单位是 `mm²`；
# - `yield_strength_MPa`：材料屈服强度；
# - `safety_factor`：安全系数，默认是 `1.5`。
#
# **计算规则：** `stress = force_N / area_mm2`，`allowable = yield_strength_MPa / safety_factor`。由于 `N/mm² = MPa`，不需要额外换算单位。
#
# **安全条件：** `stress <= allowable`。
#
# **返回：** `check_stress_safety(...)` 返回 `(stress_MPa, allowable_MPa, safe_mask, safe_count, min_margin_MPa)`。
#
# **作答位置：** 下一格的 `check_stress_safety(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
import numpy as np

def check_stress_safety(force_N, area_mm2, yield_strength_MPa,
                        safety_factor=1.5):
    """返回应力、许用应力、合格掩码、合格数和最小余量。"""
    raise NotImplementedError('请完成 check_stress_safety')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_06():
    import numpy as np
    force = np.array([1000.0, 1500.0, 2400.0])
    area = np.array([20.0, 20.0, 30.0])
    stress, allowable, mask, count, margin = check_stress_safety(
        force, area, 180.0, safety_factor=1.5
    )
    assert np.allclose(stress, [50, 75, 80])
    assert np.isclose(allowable, 120)
    assert np.array_equal(mask, [True, True, True])
    assert count == 3 and np.isclose(margin, 40)

try:
    test_exercise_06()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
