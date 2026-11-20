from huggingface_hub import HfApi

api = HfApi()
# Replace with the specific model ID you want to look up
model_info = api.model_info("bogdanrivera/legal_oaxaca_llama3-3_70B_lora")

print(f"Downloads: {model_info.downloads}")
print(f"Pipeline Tag: {model_info.pipeline_tag}")
