#!/usr/bin/env python3
# ## 题 12｜二分查找：第一个达到载荷阈值的位置
#
# **场景：** 加载试验的载荷已经从小到大排列。现在要快速找到第一条达到指定阈值的记录。
#
# **你要完成的任务：** 使用二分查找，找到第一个满足 `load >= threshold_N` 的下标。
#
# **输入：**
#
# - `sorted_loads_N`：按非递减顺序排列的载荷列表；
# - `threshold_N`：需要查找的载荷阈值。
#
# **需要注意：** 列表可能有重复值。例如 `[10, 20, 20, 35]` 查找 20 时，必须返回第一个 20 的下标 1。
#
# **返回：** `first_load_at_or_above(...)` 返回满足条件的第一个下标；不存在时返回 `-1`。
#
# **要求：** 使用二分查找，不能从头到尾逐项查找。
#
# **作答位置：** 下一格的 `first_load_at_or_above(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
def first_load_at_or_above(sorted_loads_N, threshold_N):
    """二分查找第一个大于等于阈值的载荷下标。"""
    raise NotImplementedError('请完成 first_load_at_or_above')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_12():
    loads = [10, 20, 20, 20, 35, 50]
    assert [first_load_at_or_above(loads, x) for x in [20, 21, 50, 60]] == [1, 4, 5, -1]
    assert first_load_at_or_above([], 10) == -1

try:
    test_exercise_12()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
