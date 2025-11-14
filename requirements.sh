ENVIRONMENT_PATH="~/alanz21/jobs/sam"

module load python/3.11.5
module load cuda/12.6
module load opencv/4.12.0

virtualenv --no-download ${ENVIRONMENT_PATH}

source ${ENVIRONMENT_PATH}

pip install --no-index --upgrade pip

pip install pycocotools matplotlib onnxruntime onnx
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu126

