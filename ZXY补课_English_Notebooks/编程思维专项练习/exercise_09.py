#!/usr/bin/env python3
# ## 题 9｜梁上多个集中力的合力与作用位置
#
# **场景：** 一根梁上作用着多个竖直集中力。每个力都有自己的作用位置。向上的力记为正，向下的力记为负。
#
# **你要完成的任务：** 先计算每个力对梁左端的力矩，再求所有力的合力、总力矩以及合力的等效作用位置。
#
# **输入：**
#
# - `force_N`：一维 NumPy 数组，保存各个集中力，单位是 `N`；
# - `position_m`：一维 NumPy 数组，保存每个力到梁左端的距离，单位是 `m`；
# - 两个数组必须非空且长度相同。
#
# **计算规则：**
#
# - 第 `i` 个力的力矩：`moment_i = force_N[i] * position_m[i]`；
# - 合力：`resultant_force_N = sum(force_N)`；
# - 总力矩：`total_moment_Nm = sum(moment_Nm)`；
# - 合力不为 0 时，等效作用位置：`resultant_position_m = total_moment_Nm / resultant_force_N`；
# - 合力为 0 时，不存在有限的等效作用位置，返回 `None`。
#
# **返回：** `combine_parallel_forces(...)` 返回 `(moment_Nm, resultant_force_N, total_moment_Nm, resultant_position_m)`。
#
# **要求：** 不能修改输入数组；数组为空或长度不同时抛出 `ValueError`。
#
# **作答位置：** 下一格的 `combine_parallel_forces(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
import numpy as np

def combine_parallel_forces(force_N, position_m):
    """返回各力矩、合力、总力矩和合力作用位置。"""
    raise NotImplementedError('请完成 combine_parallel_forces')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_09():
    import numpy as np
    force = np.array([10.0, -4.0, 6.0])
    position = np.array([0.0, 2.0, 5.0])
    force_before = force.copy()
    position_before = position.copy()
    moment, resultant, total_moment, resultant_position = combine_parallel_forces(
        force, position
    )
    assert np.allclose(moment, [0, -8, 30])
    assert np.isclose(resultant, 12)
    assert np.isclose(total_moment, 22)
    assert np.isclose(resultant_position, 22 / 12)
    assert np.array_equal(force, force_before)
    assert np.array_equal(position, position_before)
    assert combine_parallel_forces(
        np.array([5.0, -5.0]), np.array([0.0, 2.0])
    )[3] is None
    try:
        combine_parallel_forces(np.array([1.0, 2.0]), np.array([0.0]))
    except ValueError:
        pass
    else:
        raise AssertionError('数组长度不同时应抛出 ValueError')

try:
    test_exercise_09()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
