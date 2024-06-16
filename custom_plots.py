import matplotlib.pyplot as plt

class CustomPlot():

    # Function for showing model perfomance, model has 'accuracy' metric
    def plot_model_performance_accuracy(history, model_name="[Insert Model Name Here]"):
        f, ax = plt.subplots(1,2)

        # Set figure size
        f.set_figheight(5)
        f.set_figwidth(15)

        # Set x-axis range
        x_axis_range = range(1, len(history['accuracy']) + 1)

        # Set plot overall title
        f.suptitle(f"{model_name} Performance", weight='bold')

        epoch_range = range(1,len(history['accuracy']) + 1)

        # Plot Accuracy
        ax[0].plot(epoch_range, history['accuracy'])
        ax[0].plot(epoch_range, history['val_accuracy'])
        ax[0].legend(['Training accuracy', 'Validation Accuracy'])
        ax[0].set_ylabel('Accuracy', weight='bold')
        ax[0].set_xlabel('Epoch', weight='bold')
        ax[0].set_xticks(x_axis_range)
        ax[0].set_facecolor((0.9, 0.9, 0.9))
        ax[0].grid()

        # Plot Loss
        ax[1].plot(epoch_range, history['loss'])
        ax[1].plot(epoch_range, history['val_loss'])
        ax[1].legend(['Training loss', 'Validation loss'])
        ax[1].set_ylabel('Loss', weight='bold')
        ax[1].set_xlabel('Epoch', weight='bold')
        ax[1].set_xticks(x_axis_range)
        ax[1].set_facecolor((0.9, 0.9, 0.9))
        ax[1].grid()

        plt.savefig(f'{model_name}.png')


# Trouble Shooting
history = {
    'loss': [
        1.0005149841308594,
        0.6663402318954468,
        0.39622268080711365,
        0.25909510254859924,
        0.1677960753440857,
        0.12420839816331863,
        0.09730126708745956,
        0.07770370692014694,
        0.06278955936431885,
        0.051356326788663864
    ],
    'accuracy': [  
        0.5958750247955322,
        0.9111250042915344,
        0.9978749752044678,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0
    ],
    'val_loss': [
        0.8140411972999573,
        0.5009025931358337,
        0.316132515668869,
        0.20457147061824799,
        0.14102952182292938,
        0.10901696979999542,
        0.08643627911806107,
        0.06949219107627869,
        0.056521207094192505,
        0.0464381314814090
    ],
    'val_accuracy': [
        0.6729999780654907,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0,
        1.0
    ]
}

CustomPlot.plot_model_performance_accuracy(
    history=history, 
    model_name="Troubleshooting"
)