import numpy as np

from custom_plots import CustomPlot

# Trouble Shooting
history = {
    'loss': list(np.random.rand(10)),
    'accuracy': list(np.random.rand(10)),
    'val_loss': list(np.random.rand(10)),
    'val_accuracy': list(np.random.rand(10))
}

CustomPlot.plot_model_performance_accuracy(
    history=history, 
    model_name="Troubleshooting"
)