# vllm
/home/hubing/.conda/envs/evalscope/bin/evalscope eval \
--model gemma-2-9b-it \
--api-url http://127.0.0.1:8801/v1 \
--api-key EMPTY \
--eval-type openai_api \
--datasets ifeval gpqa_diamond gsm8k mmlu_redux truthful_qa hellaswag \
--dataset-args '{"mmlu_redux": {"local_path": "/home/hubing/evalscope/cache/mmlu-redux-2.0"}}' \
# --limit 5