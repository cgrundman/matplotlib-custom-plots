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
