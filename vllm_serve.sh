/home/hubing/.conda/envs/evalscope/bin/python -m vllm.entrypoints.openai.api_server \
--model XuHuang/gemma-2-9b-it-simpo-20k \
--served-model-name simpo \
--trust_remote_code \
--port 8801 \
--tensor-parallel-size 8 \
--gpu-memory-utilization 0.9