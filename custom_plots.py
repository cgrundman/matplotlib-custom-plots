import matplotlib.pyplot as plt

class CustomPlot():

    # Function for showing model perfomance, model has 'accuracy' metric
    def plot_model_performance_accuracy(history, model_name="[Insert Model Name Here]"):
        f, ax = plt.subplots(1,2)

        # Set figure size
        f.set_figheight(5)
        f.set_figwidth(15)

        # Set x-axis range
        epoch_range = range(1,len(history['accuracy']) + 1)

        # Set plot overall title
        f.suptitle(f"{model_name} Performance", weight='bold')

        # Plot Accuracy
        ax[0].plot(epoch_range, history['accuracy'])
        ax[0].plot(epoch_range, history['val_accuracy'])
        ax[0].legend(['Training accuracy', 'Validation Accuracy'])
        ax[0].set_ylabel('Accuracy', weight='bold')
        ax[0].set_xlabel('Epoch', weight='bold')
        ax[0].set_xticks(epoch_range)
        ax[0].set_facecolor((0.9, 0.9, 0.9))
        ax[0].grid()

        # Plot Loss
        ax[1].plot(epoch_range, history['loss'])
        ax[1].plot(epoch_range, history['val_loss'])
        ax[1].legend(['Training loss', 'Validation loss'])
        ax[1].set_ylabel('Loss', weight='bold')
        ax[1].set_xlabel('Epoch', weight='bold')
        ax[1].set_xticks(epoch_range)
        ax[1].set_facecolor((0.9, 0.9, 0.9))
        ax[1].grid(True)

        plt.savefig(f'{model_name}.png')

    # Function for comparing model perfomance, models have 'accuracy' metric
    def compare_model_performance_accuracy(history_list, model_name_list=["[Model 1]", "[Model 2]"]):

        f, axs = plt.subplots(2,2)

        # Set figure size
        f.set_figheight(10)
        f.set_figwidth(15)

        # Set plot overall title
        title = ""
        for i in range(len(model_name_list)):
            if title == "":
                title = model_name_list[i]
            else:
                title += " vs. " + model_name_list[i]
        title += " Performance"
        f.suptitle(title, weight='bold', y=.93, size=20)

        # Set range of epochs for model training
        epoch_range = range(1,len(history_list[0]['accuracy']) + 1)

        # Create lists of metrics, partial and full names
        list_of_metrics = ['accuracy', 'val_accuracy', 'loss', 'val_loss']
        list_of_metrics_fn = ['Accuracy', 
                                'Validation Accuracy', 
                                'Loss', 
                                'Validation Loss']

        # Iterate through subplots
        for i in range(len(list_of_metrics)):
            for j in range(len(model_name_list)):
                # Plot the trainingdata
                axs.flat[i].plot(epoch_range, history_list[j][list_of_metrics[i]])

                # Set commmon plot styling and labels
                axs.flat[i].legend(model_name_list)
                axs.flat[i].set_xticks(epoch_range)
                axs.flat[i].set_ylabel(list_of_metrics_fn[i], weight='bold')
                axs.flat[i].set_xlabel('Epoch', weight='bold')
                axs.flat[i].set_facecolor((0.9, 0.9, 0.9))
                axs.flat[i].grid(True)


        # Set filename
        filename = ""
        for i in range(len(model_name_list)):
            if filename == "":
                filename = "comp_" + model_name_list[i]
            else:
                filename += "_" + model_name_list[i]
        filename += " .png"

        # Save the file image
        plt.savefig(filename)

