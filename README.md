## Full tutorial to train Haar Cascade using opencv3 on MacOS


__*Material:*__
	
* MacOS(Over Catalina10.15)
* CMake
* Homebrew
* Python3
* Datasets-Over 1000 positive images and negative images


### 1.Install Supports(Homebrew,Cmake,OpenCV)
Install HomeBrew
> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

Install Cmake

> brew install cmake git subversion wget
> echo "export PATH=/usr/local/bin:$PATH" >> ~/.bashrc
> source ~/.bashrc

Install Python3
> brew install python3

Install Opencv3
> brew install opencv@3


### 2.Get ready datasets
-
For the training you need over 1000 positive images and negative images, positive images are images that **only** contains the item you want to detect and the negative images could be any image.
You Could download these images from the following website just simpily search it up:

1. www.kaggle.com
2. https://datasetsearch.research.google.com

Then make a training folder and make another 2 folder named pos and neg in it.
> mkdir train
> 
> cd train
> 
> mkdir pos
> 
> mkdir neg


Put all the positive images in to pos and negatives into neg

Reminder:Make sure the size of the positives are all equal and recommanded sizes are 20x20,45x45,100x100

### 3.Create Samples
-
We need some sample for the training business and we will be using the opencv_createsample program to do it.

First,we have to get the path where you opencv3 is installed at so run the following command:

> brew --prefix opencv@3  

The output should be like:

> (base) mac@mac train % brew --prefix opencv@3 
> 
> /usr/local/opt/opencv@3

Make sure you are in the training folder to generate these codes.

This generate the path for the positives
>ls ./neg/*.*>neg.txt

This generate the path for the negatives
>ls pos/*.* > pos.info

Open pos.txt and it should be like:

> ./pos/apple_1.jpg
> 
> ./pos/apple_10.jpg
> 
> ./pos/apple_100.jpg
> 
> ./pos/apple_1000.jpg

Go to tools and replace, search jpg up and replace them with :
jpg 1 0 0 yourheight yourwidth

Now Use this template:
> **YourPathToOpenCV**opencv_createsamples -bg neg.txt -info pos.info -num 10000 **-Your Width** **-Your Height** -vec pos.vec


###4.opencv_traincascade 
-

You should be result with a .vec files now then fill in this template to begin cascade training.

> mkdir data
> 
> **Your Path to opencv**opencv_traincascade -data data -vec positives.vec -bg neg.txt -numPos 1000 -numNeg 1000 -numStages 8 **-your width** **-your height** -minhitrate 0.99 -maxFalseAlarmRate 0.3 -precalcValBufSize 1024 -precalcIdxBufSize 1024 -numThreads 6
> 

This Would get you training and after it finish it should give you a .xml file in your data folder.

 
