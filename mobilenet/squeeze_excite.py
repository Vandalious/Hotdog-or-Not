import torch.nn as nn
from mobilenet.hard_activations import HSigmoid


class SqueezeExcite(nn.Module):
    def __init__(self, input_channels, squeeze = 4):
        super().__init__()

        self.SE = nn.Sequential(
            nn.AdaptiveAvgPool2d(output_size=1),
            nn.Conv2d(input_channels, out_channels=input_channels//squeeze, kernel_size=1, stride=1, bias=False),
            nn.BatchNorm2d(input_channels//squeeze),
            nn.ReLU(inplace=True),
            nn.Conv2d(input_channels//squeeze, input_channels, kernel_size=1, stride=1, bias=False),
            nn.BatchNorm2d(input_channels),
            HSigmoid(),
        )
    
    def forward(self, x):
        x = x * self.SE(x)
        return x
