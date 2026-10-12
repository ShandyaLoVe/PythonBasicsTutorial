UL2ME007 – Bilingual Course Notebooks｜UL2ME007 – 中英双语课程 Notebook

This directory contains the revised Jupyter versions of the complete course set in
/Users/Apple/Documents/ZXY补课. Each notebook was checked against its corresponding
French HTML or PDF source. Original source files were not modified.

本目录包含 /Users/Apple/Documents/ZXY补课 整套课程的优化版 Jupyter notebook。
每份文件均与对应的法语 HTML 或 PDF 原稿核对，原始资料未被修改。

The bilingual text is interwoven by meaning rather than split into rigid translation
columns. Original topics and exercises are retained, terminology and code are corrected,
and every notebook ends with an integrated summary.

双语内容按语义自然衔接，不采用生硬的逐句对照栏。原有主题和练习均予以保留，
同时修正术语与代码，并在每份 notebook 末尾加入内容串联总结。

Course files｜课程文件

C1_Introduction_v2509_EN.ipynb       30 markdown + 22 code cells
C2_IntroNumpy_v2509_EN.ipynb         16 markdown + 11 code cells
C3_IntroMatplotlib_v2509_EN.ipynb    13 markdown + 10 code cells
C4_Vectorisation_v2609_EN.ipynb      24 markdown + 29 code cells
C5_Masques_v2609_EN.ipynb            20 markdown + 14 code cells
C6_Lecture_images_EN.ipynb           11 markdown + 5 code cells
C7_Fonctions_v2509_EN.ipynb          12 markdown + 10 code cells
TP1 问_EN.ipynb                       13 markdown + 8 code cells
TP2 问_EN.ipynb                       10 markdown + 7 code cells
TP3_Questions_EN.ipynb                7 markdown + 10 code cells
TP4 问_EN.ipynb                       14 markdown + 17 code cells

Environment｜运行环境

Activate the prepared virtual environment from this directory:

    source .venv/bin/activate

Start JupyterLab with:

    jupyter lab

The pinned packages are listed in requirements.txt. To rebuild the environment:

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements.txt

Missing course assets｜缺失的课程素材

The original project does not include TP4_gray_scale.tiff or TP4_KH_2_gray.tiff.
TP4 reports these missing files clearly and keeps all image-analysis instructions, but
the original TIFF files must be obtained before completing the image measurements.

原项目没有提供 TP4_gray_scale.tiff 与 TP4_KH_2_gray.tiff。TP4 会明确提示素材缺失，
并保留完整分析步骤；要完成真实图像测量，仍需从课程资料中补充原始 TIFF 文件。

Verification｜验证状态

All 11 notebooks have unique cell IDs, contain both Chinese and English teaching text,
include a final synthesis, convert successfully to HTML, and pass sequential execution
with the supplied environment. Exercise starter cells remain runnable and use TODO
prompts instead of notebook-stopping NotImplementedError placeholders.

11 份 notebook 均已检查单元 ID、双语内容和末尾总结，可成功导出 HTML，并能在现有
环境中按顺序执行。练习单元保留 TODO 答题脚手架，不再使用会中断运行的
NotImplementedError 占位符。
