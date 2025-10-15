from evalscope import TaskConfig, run_task
from evalscope.constants import EvalType, JudgeStrategy
import os

api_key = os.getenv("OPEN_ROUTER_API_KEY")  # 获取环境变量 API_KEY 的值
if not api_key:
    raise ValueError("未设置 API_KEY 环境变量")

task_cfg = TaskConfig(
    model='/hai/scratch/fangwu97/xu/RL_agent_data_augment/gemma-2-9b-it-DPO-10k-original',
    datasets=[
        'alpaca_eval'
    ],
    eval_batch_size=12,
    judge_worker_num=12,
    # limit=5,
    judge_strategy=JudgeStrategy.AUTO,
    judge_model_args={
        'model_id': 'gpt-5-mini',
        'generation_config': {"reasoning_effort": "minimal"},
        'api_url': 'https://openrouter.ai/api/v1',
        'api_key': api_key,
    },
#    use_cache="/alloc/xu/evalscope/outputs/20250924_151921"
)

run_task(task_cfg=task_cfg)
