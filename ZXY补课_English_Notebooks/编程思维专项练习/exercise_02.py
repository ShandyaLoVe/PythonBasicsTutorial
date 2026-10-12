#!/usr/bin/env python3
# ## 题 2｜拉伸试验状态统计
#
# **场景：** 文本文件记录了多次拉伸试验的状态。字符 `E` 表示试件仍处于弹性阶段，字符 `F` 表示试件已经失效。
#
# **你要完成的任务：** 读取文件，统计 `E`、`F` 和无效字符的数量，再把统计结果写入报告文件。
#
# **输入：**
#
# - `log_path`：需要读取的记录文件路径；
# - `report_path`：需要写入的报告文件路径。
#
# **处理规则：**
#
# - 遇到 `E`，弹性记录数加 1；
# - 遇到 `F`，失效记录数加 1；
# - 换行符不计数；
# - 除以上字符外，其他字符都算无效记录。
#
# **返回：** `summarize_specimen_log(log_path, report_path)` 返回 `(elastic, failed, invalid)`。
#
# **报告内容：** 按顺序写出 `elastic=...`、`failed=...`、`invalid=...` 三行。
#
# **要求：** 只使用文件的 `read()`、循环、判断和计数器。
#
# **作答位置：** 下一格的 `summarize_specimen_log(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
def summarize_specimen_log(log_path, report_path):
    """逐行读取试验状态，返回两类数量和无效行数量。"""
    raise NotImplementedError('请完成 summarize_specimen_log')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_02():
    log_path = 'exercise_02_input.txt'
    report_path = 'exercise_02_report.txt'
    assert summarize_specimen_log(log_path, report_path) == (2, 2, 1)
    with open(report_path, encoding='utf-8') as file:
        report = file.read()
    assert report == 'elastic=2\nfailed=2\ninvalid=1\n'

try:
    test_exercise_02()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
