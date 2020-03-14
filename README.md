# dog-breed-classifier

This is a project from the [Udacity AI Programming with Python Nanodegree](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089). 

It is an image classifier that can be used to predict the breed of a dog by passing an image of the dog through the model. The classifier makes use of three different architectures in order to compare the accuracy of each:

1. resnet
2. alexnet
3. vgg

### Running a prediction

To run an image through the model you need to insert an jpg image of the dog in the 'uploaded images folder'.

In order to run the classifier you can use the following command:

````bash
sh run_models_batch.sh
````

This will run the models an output the results to the following files in the root of the project:

resnet_pet-images.txt
alexnet_pet-images.txt
vgg_pet-images.txt

### Other

Please note that this porject was created for the [Udacity AI Programming with Python Nanodegree](https://www.udacity.com/course/ai-programming-python-nanodegree--nd089), the code contains initial scaffolding provided by the course instructors, which I then added to in order to finish the project as per requirements. The authors of each file are added to the top of them respectively for reference.
