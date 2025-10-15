```bash
# 建议使用 python 3.10
conda create -n evalscope python=3.10

# 激活conda环境
conda activate evalscope

# 确保在evalscope文件夹中（当前文件夹）
pip install -e .

pip install torch==2.7.0 torchvision==0.22.0 torchaudio==2.7.0 --index-url https://download.pytorch.org/whl/cu128
pip install vllm==0.9.0
pip install "transformers<4.54.0"
pip install https://github.com/Dao-AILab/flash-attention/releases/download/v2.8.0.post2/flash_attn-2.8.0.post2+cu12torch2.7cxx11abiFALSE-cp310-cp310-linux_x86_64.whl  
pip install accelerate==0.29.2 

```

download dataset：mmlu_redux
```shell
huggingface-cli download edinburgh-dawg/mmlu-redux-2.0 --local-dir /home/hubing/evalscope/cache/mmlu-redux-2.0 --repo-type dataset
```