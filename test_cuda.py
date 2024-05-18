import torch

print(f"PyTorch version: {torch.__version__}")          # Should not include '+cpu'
print(f"CUDA version: {torch.version.cuda}")            # Should return the CUDA version
print(f"cuDNN version: {torch.backends.cudnn.version()}")  # Should return the cuDNN version
print(f"Is CUDA available: {torch.cuda.is_available()}")  # Should return True

if torch.cuda.is_available():
    print(f"Current CUDA device: {torch.cuda.current_device()}")  # Should return the current CUDA device id
    print(f"CUDA device name: {torch.cuda.get_device_name(0)}")   # Should return the name of your GPU
