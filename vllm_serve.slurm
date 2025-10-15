#!/bin/bash
#SBATCH --account=yejin
#SBATCH -p hai-lo
#SBATCH --gres=gpu:1
#SBATCH --job-name=vllm_serve
#SBATCH --output=vllm.log
#SBATCH --mem=128G

/hai/scratch/fangwu97/miniconda3/envs/evalscope/bin/python -m vllm.entrypoints.openai.api_server \
--model /hai/scratch/fangwu97/xu/RL_agent_data_augment/gemma-2-9b-it-DPO-10k-original \
--served-model-name dpo \
--trust_remote_code \
--port 8801

