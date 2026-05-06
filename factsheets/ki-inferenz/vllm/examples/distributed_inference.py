# Example for distributed inference with vLLM
# Use tensor parallel to shard the model across multiple GPUs

# Command to run:
# python -m vllm.entrypoints.openai.api_server \
#     --model facebook/opt-6.7b \
#     --tensor-parallel-size 2

print("To run distributed inference, use the --tensor-parallel-size <N> flag.")
