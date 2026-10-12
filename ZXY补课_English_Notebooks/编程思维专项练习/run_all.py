#!/usr/bin/env python3
"""依次运行 12 道力学专项练习。"""

import subprocess
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
failed = False
for index in range(1, 13):
    filename = HERE / f'exercise_{index:02d}.py'
    print(f'\n===== {filename.name} =====', flush=True)
    result = subprocess.run(
        [sys.executable, str(filename)], cwd=HERE,
        capture_output=True, text=True,
    )
    print(result.stdout, end='')
    if result.stderr:
        print(result.stderr, end='')
    failed = failed or result.returncode != 0 or '成功' not in result.stdout

raise SystemExit(1 if failed else 0)
