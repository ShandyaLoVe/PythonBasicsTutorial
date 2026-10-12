#!/usr/bin/env python3
# ## 题 7｜从材料表面图像数出裂纹段
#
# **场景：** 灰度图中，正常表面较亮，裂纹较暗。现在只分析图像中的一个矩形区域，并统计该区域中间一行出现了几段彼此分开的裂纹。
#
# **你要完成的任务：** 切出分析区域、找出裂纹像素、统计裂纹像素数和裂纹段数，并生成红色标注图。
#
# **输入：** `image`，二维 NumPy 灰度数组；灰度值小于 `threshold` 的像素算裂纹，`threshold` 默认是 100。
#
# **处理范围：** 使用 `image[2:7, 1:12]` 作为分析区域。
#
# **裂纹段的含义：** 在分析区域的中间一行中，一串连续的裂纹像素算一段；中间被正常像素隔开就算新的裂纹段。
#
# **返回：** `analyze_crack_image(...)` 返回 `(roi, mask, pixels, segments, rgb, fig)`：
#
# - `roi`：分析区域；
# - `mask`：分析区域的裂纹布尔掩码；
# - `pixels`：分析区域中的裂纹像素总数；
# - `segments`：中间一行的裂纹段数；
# - `rgb`：把原图裂纹像素标成红色后的 RGB 图；
# - `fig`：包含原图和标注图的图像对象。
#
# **作答位置：** 下一格的 `analyze_crack_image(...)` 函数。

# ===== 作答区：只修改下面的函数 =====
import matplotlib
matplotlib.use("Agg")

import numpy as np
import matplotlib.pyplot as plt

def analyze_crack_image(image, threshold=100):
    """切片、阈值分割并统计材料表面裂纹。"""
    raise NotImplementedError('请完成 analyze_crack_image')

# ===== 测试区：直接运行本文件即可检查 =====
def test_exercise_07():
    import numpy as np
    image = np.full((8, 12), 220, dtype=np.uint8)
    image[2:7, 2:4] = 30
    image[2:7, 6:7] = 30
    image[2:7, 9:11] = 30
    roi, mask, pixels, segments, rgb, fig = analyze_crack_image(image)
    assert roi.shape == (5, 11) and np.array_equal(mask, roi < 100)
    assert pixels == 25 and segments == 3
    assert rgb.shape == (8, 12, 3) and len(fig.axes) == 2

try:
    test_exercise_07()
except AssertionError as error:
    print(f'失败：{error}')
except Exception as error:
    print(f'报错：{type(error).__name__}: {error}')
else:
    print('成功')
