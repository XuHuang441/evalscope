from evalscope import TaskConfig, run_task
from evalscope.constants import EvalType, JudgeStrategy

task_cfg = TaskConfig(
    model='/hai/scratch/fangwu97/xu/RL_agent_data_augment/gemma-2-9b-it-DPO-10k-original',
    datasets=[
        'alpaca_eval'
    ],
    eval_batch_size=12,
    judge_worker_num=12,
    limit=5,
    judge_strategy=JudgeStrategy.AUTO,
    judge_model_args={
        'model_id': 'gpt-5-mini',
        'generation_config': {"reasoning_effort": "minimal"},
        'api_url': 'https://openrouter.ai/api/v1',
        'api_key': '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',
    },
#    use_cache="/alloc/xu/evalscope/outputs/20250924_151921"
)

run_task(task_cfg=task_cfg)
