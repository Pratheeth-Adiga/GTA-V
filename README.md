# Self driving vehicle in GTA V

#### Pre-requisites:

- Tensorflow
- TF Learn
- Panda
- Numpy
- OpenCV2


#### To start running this program:

- First install GTA V(or any game with driving mechanics) and resize it to 800*600 resolution and move that screen to top left of the screen.
- Run Powershell/Command prompt/Terminal in administrative mode and run create_training_data.py, press 'T' to pause and resume during the game.
- It will update in the console every 1000 frames that has been captured, ideally a data set of 100,000 frames is prefered.
- Run balance_data.py  
- Now run the train_model.py, it will take few minutes to train and it will post the accuracy of the model in the console while doing so or alternatively you can use `tensorboard --logdir=foo:C:/path/to/log` for a GUI interface of the trained model.
- Now run command Powershell/Command prompt/Terminal in administrative mode and run test_model.py and after a timer of 5 seconds the program will start to press the keys(W,A,S,D) based on its predictions.

****

### Working

#### create_training_data.py
 - It checks for the player input which is taken as a array and the screen and stores them.
 - It is mentioned in the code to record the screen from 0,40 to 800 * 640 when we are using 800 * 600 resolution because those 20 pixels account for the top bar of the application.   
 - screen resolution is dropped to 120*160 and converted to mono for faster computation.
 - It waits for 5 seconds beforing starting and updates every 1000 frames which can be changed in the for loop and the if condition.
 - 'T' is the key used to pause and unpause the game which can also be changed.
 - It appends the data of the next session to the same file and creates a new file if it isn't already present.
 
#### balance_data.py
It reduces the dataset to the least used key so that the key that is used multiple times won't be the most predictable ones.

#### alexnet.py
A conventional neural network algorithm designed by Alex Krizhevsky in collaboration with Ilya Sutskever and Geoffrey Hinton.
 
#### directkeys.py
This was one of the main obstacles which was experienced that the keys were being pressed but it didn't work in the game, its because the game uses DirectX libraries which takes the inputs in a different hexadecimal so used a code snippet which worked to solve my problem.
 
#### getkeys.py
Takes the keys which are pressed and logs it.

#### grabscreen.py
 - Gets the pixel co-ordinates from win32api.
 - Grabs the screen in a particular frame and converts the colour scheme from BGRA where this A is alpha which accounts for the opacity and anti-aliasing
 
#### train_model.py
 - It supports multiple balanced data to be trained at the same time.
 - It takes 100 frames as the testing data in each epoch which is used to test the accuracy of the model.
 - Then the trained data is saved.
 
#### test_model.py
- Waits for 5 seconds before starting.
- Here the neural network predicts the what is the probability of what key to be pressed to each frame, then if it crosses the threshold then the key press is executed.
- Here the I did some tweaking and found that the threshold for forward movement = 0.75, turning movement = 0.52, reverse movement = 0.12 worked good for my dataset but it may differ with the variable playstyle and that dataset.
- each movement (forward,left,right,reverse) are a result of various key presses, so this can further be tweaked and improve it's playablility.
- It shows what the probablity of each funtion was in the console in the form of an array.
- Kept the straight function as the default if the prediction is unable to reach any threshold values.


 
