#!/usr/bin/env python3
# ## 题 1｜分段弹簧的载荷记录
#
# **场景：** 对一根弹簧做多次加载试验。弹簧在位移较小时比较软，位移超过 `0.01 m` 后变硬，所以要分两段计算载荷。
#
# **你要完成的任务：** 逐个计算每次加载对应的载荷，并求出这一批载荷的总和。
#
# **输入：** `displacement_m`，一个由多次位移组成的列表，单位是 `m`。
#
# **每个位移 `x` 的计算规则：**
#
# - `x = 0` 时，`F = 0`；
# - `0 < x <= 0.01` 时，`F = 1000 * x`；
# - `x > 0.01` 时，`F = 10 + 1800 * (x - 0.01)`；
# - 位移小于 0 时，抛出 `ValueError`。
#
# **返回：** `calculate_spring_forces(displacement_m)` 返回 `(forces, total)`：
#
# - `forces`：每个位移对应的载荷列表；
# - `total`：`forces` 中所有载荷的总和。
#
# **要求：** 使用 `for` 循环和分段 `if` 逐个处理。
#
# **作答位置：** 下一格的 `calculate_spring_forces(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
def calculate_spring_forces(displacement_m):
    """返回每次加载的力列表和力值总和。"""
    raise NotImplementedError('请完成 calculate_spring_forces')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_01():
    force, total = calculate_spring_forces([0, 0.005, 0.01, 0.02])
    assert force == [0, 5, 10, 28]
    assert total == 43
    assert calculate_spring_forces([]) == ([], 0)
    try:
        calculate_spring_forces([-0.1])
    except ValueError:
        pass
    else:
        raise AssertionError('负位移应抛出 ValueError')

try:
    test_exercise_01()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
