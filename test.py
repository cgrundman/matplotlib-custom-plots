import numpy as np

from custom_plots import CustomPlot

# Trouble Shooting
history_1 = {
    'loss': list(np.random.rand(10)),
    'accuracy': list(np.random.rand(10)),
    'val_loss': list(np.random.rand(10)),
    'val_accuracy': list(np.random.rand(10))
}

history_2 = {
    'loss': list(np.random.rand(10)),
    'accuracy': list(np.random.rand(10)),
    'val_loss': list(np.random.rand(10)),
    'val_accuracy': list(np.random.rand(10))
}

list_of_histories = [history_1, history_2]
models = ["His1", "His2"]

CustomPlot.compare_model_performance_accuracy(
    history_list=list_of_histories, 
    model_name_list=models
)