Practical 3: Classifying Dog Breeds 
=

Due: 6. April (23:59)

![](http://www.pngpix.com/wp-content/uploads/2016/02/Dog-PNG-Image-1-500x290.png)
##### Image from [here](http://www.pngpix.com/download/dog-png-image-2).

Overview
-

Identifying the breed of a dog is often a tedious process when the owner isn't nearby. You have to follow a classification tree of the dog's features one by one which is an arduous process. As a deep learning student, you realize that with your new found knowledge of convolutional neural networks, you can automate this process entirely. People can simply take a picture of the dog and your model can output what it thinks the breed of the dog is. Luckily, Udacity even has trianing data for this exact task that you can use.

You will turn in the assigment using the submit server. Please make sure your zip file follows the format `project_N_firstname_lastname.zip`. Where `N` is the project number (in this case 1 for the first one), `firstname` is your first name, and `lastname` is your last name. Failing to follow this will result in a 5 point deduction.

Assignment
-
Using what you've learnt in the class, build a convolutional neural network model that accomplishes this. It should output 133  values which sum up to 1 and are each the probability that the dog is of the respective breed. As you can guess, this is a multi-class classification problem. You can take advantage of Keras and any other preprocessing or data libraries in your code.

#### Notes
Since convolutional neural networks train on images, they take significantly longer to train than the standard neural nets we have dealt with before. To speed up trianing time, either resize images to a smaller size (try not to go below `32x32`), train your models using AWS or Google Colab, or use transfer learning (extra credit). We didn't talk much about transfer learning in class due to time constraints but you can learn more about it here:
* https://blog.keras.io/building-powerful-image-classification-models-using-very-little-data.html
* https://towardsdatascience.com/transfer-learning-using-keras-d804b2e04ef8
* https://www.learnopencv.com/keras-tutorial-transfer-learning-using-pre-trained-models/

#### Downloading the Data
This project uses data provided by Udacity that is too large to upload to GitHub. To download the data, download the `dogImages` zip file from [here](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip) and extract it to your project directory. Make sure that the `dogImages` directory is in the project directory and contains the `train`, `test`, and `validation` directories.

#### Coding (35 points):
This project is more open ended for implementation as in the real world you won't be given templates to fill your code in. We do however provide a Jupyter Notebook `Practical 2 Code.ipynb` containing a framework for implementing the code that you should follow. All of your code should be written in the Jupyter notebook.

Tne provided notebook is split into 4 different sections for each of the following tasks with each section titled "Section 1", "Section 2", etc. Make sure at the top of the section under the header, you give an explanation (minimum of 3 sentences) explaining what you did. The four sections are:

1. **Loading the dataa**: Nothing to code.
2. **Building the model**: Fill in **at least** two data augmentation methods to be used when training the model. An example of flipping the image has already been completed for you.
3. **Training the model**: Nothing to code.
4. **Testing the model and results**: In this section you will train the model and compute the accuracy of your model on the test data from Section 0. Make sure you very clearly have a cell that outputs and prints the percentage accuracy of your model. You will also include any code used to analyze the results here.

**WARNING**: We keep have a list of all the implementations and tutorials building models for this on the web. Copying code from them is considered academic dishonesty and will result in a report to the student honor council. However, please feel free to understand the logic behind their code and emulate it yourself. If you do this, please cite any articles in the `README.md`.

#### Analysis (15 points):
1. What were the results of your model? Report any scores or figures you feel neccessary to explain your point. Solely reporting the accuracy will result in a minimal grade. We highly reccomend using figures, additional scores, and data analysis (e.g. which features are the best?).
2. How did you decide on the best data augmentations for your model?
3. How did you choose the parameters for your model (e.g. parameter sweep)?
4. Did you notice anything interesting about the model performance?
5. What challenges did you face when completing this task?

#### Extra credit:
1. Use transfer learning by retraining a pretrained model on ImageNet on the data and evaluate the change in performance in trianing time.

What to turn in
-

1. Your `Practical 3 Code.ipynb` Jupyter notebook file containing your code. Please make sure you run all your cells before submitting so I don't have to run them on my end.
2. Your `model.h5` and `model.json` files that are saved after training.
3. A `README.md` listing any extra packages that I need to run your code. Also contains any blogs or tutorials you looked at. 
4. An `analysis.pdf` file
    - pictures are better than text
    - include your name at the top of the PDF

Hints
-

1. Follow the notebooks posted on the class webpage as a framework for how to load the data, process it, etc.
2. Library documentation is your friend.


###### Thanks to Udacity for the Dog Breed Dataset and code to load it available <a href="https://github.com/mahavird/dog-project">here</a>.
