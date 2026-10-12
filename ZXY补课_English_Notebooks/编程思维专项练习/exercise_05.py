#!/usr/bin/env python3
# ## 题 5｜力—位移曲线的功与能量
#
# **场景：** 试验记录了不同位置处的力。要估算力做的功，可以把相邻两个采样点之间的曲线看成梯形。
#
# **你要完成的任务：** 逐段计算功，记录从起点累计到每个位置的功，并找出哪一段做功最多。
#
# **输入：**
#
# - `force_N`：各采样点的力；
# - `position_m`：对应的位置，必须按非递减顺序排列；
# - 两个列表长度相同。
#
# **第 `i` 段的计算规则：** `work = (force_N[i] + force_N[i+1]) / 2 * (position_m[i+1] - position_m[i])`。
#
# **返回：** `summarize_work(...)` 返回 `(segment_work, cumulative_work, total_work, peak_segment_index)`：
#
# - `segment_work`：每一段的功；
# - `cumulative_work`：从 0 开始的累计功；
# - `total_work`：总功；
# - `peak_segment_index`：最大分段功在 `segment_work` 中的下标。
#
# **要求：** 使用 `for` 循环和列表，不使用 `np.diff` 或 `np.cumsum`。
#
# **作答位置：** 下一格的 `summarize_work(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
def summarize_work(force_N, position_m):
    """用循环和列表返回分段功、累计功、总功和最大分段功下标。"""
    raise NotImplementedError('请完成 summarize_work')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_05():
    force = [0.0, 10.0, 10.0]
    position = [0.0, 1.0, 2.0]
    segment, cumulative, total, peak = summarize_work(force, position)
    assert segment == [5, 10]
    assert cumulative == [0, 5, 15]
    assert total == 15 and peak == 1

try:
    test_exercise_05()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
