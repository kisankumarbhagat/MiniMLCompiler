import torch
import torch.nn as nn

class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(784, 10)

    def forward(self, x):
        return self.linear(x)

model = SimpleModel()
dummy_input = torch.randn(1, 784)

torch.onnx.export(
    model,
    dummy_input,
    "models/sample_model.onnx",  # Save yahin hoga
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}},
    opset_version=11
)

print("ONNX model exported successfully to models/sample_model.onnx")
