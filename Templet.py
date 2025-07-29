from pathlib import Path
import logging
project_name = "cnnClassifier"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

list_of_files = [
    ".github/workflows/.gitkeep",

    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",

    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]
for filepath in list_of_files:
    file = Path(filepath)
    if not file.parent.exists():
        file.parent.mkdir(parents=True, exist_ok=True)
        logging.info(f"Created directory: {file.parent}")

    if not file.exists() or file.stat().st_size == 0:
        file.touch()
        logging.info(f"Created empty file: {file}")
    else:
        logging.info(f"File already exists: {file}")

