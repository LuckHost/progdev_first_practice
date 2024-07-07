## Installation
Just download this project to your computer

## launch
---
### Windows
follow this commands from the project folder 

conda env create -f environment.yml
conda activate env_py37

python.exe ./Main.py


### Linux

conda create --name env_py37 python=3.7.12 -y
source $(conda info --base)/etc/profile.d/conda.sh
conda activate env_py37

pip install -r requirements.txt

python.exe ./Main.py
