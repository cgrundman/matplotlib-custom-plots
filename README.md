# Custom Plots for Matplotlib

Repository for custom matplotlib plotting that can be called by Colab or Jupyter notebook.


## How to Implement in Jupyter Notebook/Colab

Clone the notebook to your instance:

```!git clone https://github.com/cgrundman/matplotlib-custom-plots.git```

Pull the path to the python file:

```
import sys
sys.path.append('/content/matplotlib-custom-plots')
```

Import a class, eg. CustomPlot, from the file:

```from custom_plots import CustomPlot```

An example of a function call with this file:

```
CustomPlot.plot_model_performance_accuracy(history=history_nn.history, 
                                model_name="Neural Network")
```

where ```history``` is a model history returned from model.fit in TensorFlow and ```model_name``` is the name you assign to your model.
