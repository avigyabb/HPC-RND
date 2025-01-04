import torch

if torch.cuda.is_available():
    print(f"Number of GPUs available: {torch.cuda.device_count()}")
else:
    print("CUDA is not available. No GPUs detected.")