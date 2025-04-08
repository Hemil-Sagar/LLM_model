import torch

# Check if CUDA is available
if torch.cuda.is_available():
    print("CUDA is available! Using GPU:", torch.cuda.get_device_name(0))

    # Example: Perform a simple tensor operation on GPU
    device = torch.device("cuda")  # Set device to GPU
    a = torch.tensor([1.0, 2.0, 3.0]).to(device)
    b = torch.tensor([4.0, 5.0, 6.0]).to(device)
    c = a + b  # Element-wise addition
    print("Result of CUDA computation:", c)

else:
    print("CUDA is not available. Using CPU instead.")
