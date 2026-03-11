# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "pyyaml>=6.0.3",
# ]
# ///

import sys
# import os
from pathlib import Path
import subprocess

library_loc = str(Path(r'C:/Users/phegl/devops/repos/perman/lib/new-git-remote.md'))
vscode_exe = str(Path(r'C:/Users/phegl/AppData/Local/Programs/Microsoft VS Code/bin/code.cmd'))

if sys.argv[1] == "new-git-remote":
    subprocess.run([vscode_exe, library_loc])
else:
    print(f'No perman help page exists for option: {sys.argv[1]}')


# End of File
