import torch
import torch.nn as nn
import os

# Simple linear model: input 10 features -> output 1 score
class DummyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(10, 1)
    
    def forward(self, x):
        return self.linear(x)

def main():
    model = DummyModel()
    model.eval()
    
    # Save as TorchScript for easy serving
    example = torch.rand(1, 10)
    traced_model = torch.jit.trace(model, example)
    traced_model.save("model.pt")
    print("✅ Dummy model saved to model.pt")
    
    # Also save a small test set
    torch.save({"input": example, "output": traced_model(example)}, "sample_input.pt")

if __name__ == "__main__":
    main()