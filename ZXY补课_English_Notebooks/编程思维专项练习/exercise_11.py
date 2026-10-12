#!/usr/bin/env python3
# ## 题 11｜冒泡排序：整理结构的固有频率
#
# **场景：** 模态试验得到一组顺序杂乱的固有频率，需要在不使用现成排序函数的情况下从小到大整理。
#
# **你要完成的任务：** 使用冒泡排序生成一个新的有序频率列表。
#
# **输入：** `frequencies_Hz`，固有频率列表；可能包含重复值。
#
# **冒泡排序规则：** 从左到右比较相邻的两个数。如果左边大于右边，就交换它们。一轮结束后，本轮最大的数会移动到尚未排好部分的最右端。
#
# **返回：** `bubble_sort_frequencies(frequencies_Hz)` 返回从小到大排列的新列表。
#
# **要求：** 不能修改原列表，不能使用 `sorted()` 或列表的 `sort()`。
#
# **作答位置：** 下一格的 `bubble_sort_frequencies(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
def bubble_sort_frequencies(frequencies_Hz):
    """使用冒泡排序返回从小到大排列的新列表。"""
    raise NotImplementedError('请完成 bubble_sort_frequencies')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_11():
    values = [12.5, 4.0, 8.2, 4.0, 20.1]
    before = values.copy()
    assert bubble_sort_frequencies(values) == [4.0, 4.0, 8.2, 12.5, 20.1]
    assert values == before
    assert bubble_sort_frequencies([]) == []
    assert bubble_sort_frequencies([7.5]) == [7.5]

try:
    test_exercise_11()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
