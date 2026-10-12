# Python 环境安装与管理指南（macOS / Windows）

这份指南面向第一次配置 Python 和 Jupyter 的同学。课堂推荐统一使用：

**Python + `venv` 虚拟环境 + `pip` 依赖管理 + Jupyter Lab / VS Code**

最重要的原则是：**每个项目使用独立虚拟环境，不要把课程依赖全部安装到系统 Python 中。**

## 1. 从哪里下载 Python

### macOS

推荐从 Python 官方网站下载：

- [Python 官方 macOS 下载页](https://www.python.org/downloads/macos/)
- 选择最新的稳定版本，不要选择名称中带有 `alpha`、`beta` 或 `rc` 的测试版本。
- Apple Silicon（M1、M2、M3、M4 等）和 Intel Mac 均可使用官方提供的 macOS 通用安装包。

也可以使用 [Homebrew](https://brew.sh/) 管理 Python：

```bash
brew install python
```

初学者只需选择一种安装方式。不要同时混用官网安装器、Homebrew、Conda 等多个来源，否则容易出现“终端与 Jupyter 使用了不同 Python”的问题。

### Windows

推荐从 Python 官方网站下载：

- [Python 官方 Windows 下载页](https://www.python.org/downloads/windows/)
- 普通 64 位 Windows 电脑选择 **Windows installer (64-bit)**。
- 安装界面建议勾选 **Add python.exe to PATH**。
- 安装完成后可使用 Windows 自带的 Python Launcher，即 `py` 命令。

不建议从不明网站下载 Python 安装包。

## 2. 检查安装是否成功

### macOS

打开“终端 Terminal”，运行：

```bash
python3 --version
python3 -m pip --version
which python3
```

### Windows

打开 PowerShell，运行：

```powershell
py --version
py -m pip --version
where.exe python
```

只要能够显示 Python 和 pip 的版本，基本安装就已经完成。如果 Windows 找不到 `python`，优先尝试 `py`。

## 3. 为项目创建虚拟环境

先在终端中进入项目目录。路径中有空格或中文时，请给路径加引号。

### macOS

```bash
cd "/项目所在目录/ZXY补课_English_Notebooks"
python3 -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
cd "C:\项目所在目录\ZXY补课_English_Notebooks"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

如果 PowerShell 阻止激活脚本，可仅为当前用户设置一次：

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

然后重新执行激活命令。不要随意把执行策略改成 `Unrestricted`。

激活成功后，命令行开头通常会出现 `(.venv)`。使用下面的命令确认当前 Python：

```bash
python --version
python -c "import sys; print(sys.executable)"
```

输出路径应当位于当前项目的 `.venv` 文件夹中。

## 4. 安装项目依赖

虚拟环境激活后，建议始终使用 `python -m pip`，这样可以确保 pip 和当前 Python 属于同一环境。

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

如果项目没有 `requirements.txt`，可按需安装：

```bash
python -m pip install numpy matplotlib pillow ipykernel jupyterlab
```

查看已经安装的软件包：

```bash
python -m pip list
```

导出当前依赖：

```bash
python -m pip freeze > requirements.txt
```

课程项目通常应优先维护一份经过验证的 `requirements.txt`，而不是让每位同学随意安装不同版本。

## 5. 启动 Jupyter Lab

先进入项目目录并激活 `.venv`，然后运行：

```bash
python -m jupyter lab
```

停止 Jupyter：回到启动它的终端，按 `Ctrl + C`，再按提示确认。

退出虚拟环境：

```bash
deactivate
```

## 6. 在 VS Code 中使用正确环境

1. 安装 VS Code 的 **Python** 与 **Jupyter** 扩展。
2. 打开项目文件夹，而不是只打开单个 `.ipynb` 文件。
3. 打开 Notebook 后，点击右上角的内核名称。
4. 选择当前项目中的 `.venv`。
5. 在 Notebook 中运行以下代码确认路径：

```python
import sys
print(sys.version)
print(sys.executable)
```

`sys.executable` 应指向：

- macOS：`项目目录/.venv/bin/python`
- Windows：`项目目录\.venv\Scripts\python.exe`

## 7. 日常环境管理

每次开始学习：

```text
进入项目目录 → 激活 .venv → 启动 Jupyter 或 VS Code → 检查内核
```

安装新包：

```bash
python -m pip install 包名
```

更新某个包：

```bash
python -m pip install --upgrade 包名
```

查看某个包的信息：

```bash
python -m pip show 包名
```

卸载某个包：

```bash
python -m pip uninstall 包名
```

`.venv` 是可重新生成的目录，通常不要发送给别人，也不要提交到 Git。共享项目时，应共享代码和 `requirements.txt`。

## 8. 虚拟环境损坏时如何处理

如果出现以下错误：

```text
bad interpreter
no such file or directory: .venv/bin/python
```

通常表示创建 `.venv` 的 Python 已被删除或升级。不要手动修改虚拟环境里的 Python 链接，直接重建更可靠。

### macOS

```bash
deactivate
mv .venv .venv_broken
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows PowerShell

```powershell
deactivate
Rename-Item .venv .venv_broken
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

确认新环境正常后，再删除 `.venv_broken`。

## 9. 常见问题速查

### `python` 或 `py` 命令找不到

- macOS：尝试 `python3`，并检查 `which python3`。
- Windows：优先尝试 `py`；若仍找不到，重新运行官方安装器并检查 PATH 设置。

### 安装了包，但 Notebook 中仍然提示 `ModuleNotFoundError`

通常是“安装包的 Python”和“Notebook 内核的 Python”不是同一个。运行：

```python
import sys
print(sys.executable)
```

然后在 Notebook 中使用当前内核安装：

```python
import sys
!{sys.executable} -m pip install 包名
```

完成后重启内核。

### 不要使用 `sudo pip install`

这可能修改系统 Python 并造成权限问题。遇到权限错误时，应先检查是否已经激活 `.venv`。

### 文件夹含有中文或空格可以吗？

现代 Python 通常可以正常处理中文路径。终端中切换目录时给完整路径加引号即可：

```bash
cd "/Users/用户名/Documents/课程文件夹"
```

为了减少旧软件兼容问题，也可以使用简短的英文项目路径，但这不是使用 Python 的硬性要求。

## 10. 官方参考资料

- [Python macOS 下载](https://www.python.org/downloads/macos/)
- [Python Windows 下载](https://www.python.org/downloads/windows/)
- [Python `venv` 官方文档](https://docs.python.org/3/library/venv.html)
- [Python Packaging User Guide：安装软件包](https://packaging.python.org/en/latest/tutorials/installing-packages/)

