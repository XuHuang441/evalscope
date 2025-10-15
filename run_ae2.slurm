#!/bin/bash
#SBATCH --account=yejin
#SBATCH -p hai-lo
#SBATCH --gres=gpu:1
#SBATCH --job-name=vllm_serve
#SBATCH --output=o_eval.log
#SBATCH --mem=128G

/hai/scratch/fangwu97/miniconda3/envs/evalscope/bin/python run_ae2.py