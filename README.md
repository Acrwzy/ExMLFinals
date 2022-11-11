# ExML Finals Writeup
Prepared by Samkit Jain, Aarav Kaushik [DPS Bhopal]

## Preparing the dataset
Preparing the dataset wasn't much of a problem since many open source datasets exist for dog and cat breeds.So we decided to mix these datasets with images scraped from google(for the breeds which have less data)-

* [Dog Breed Identification](https://www.kaggle.com/c/dog-breed-identification)
* [Cat Breeds Dataset](https://www.kaggle.com/datasets/ma7555/cat-breeds-dataset)

## Data preprocessing
To increase the size of data we scraped the internet for around 400 images and then augmented them using tensorflow keras

### Data augmentation and google image scraping
For data preprocessing we rolled out all 12 breeds(6+6) into a single folder and did a train validation split of 80:20 

The final dataset is - [cat_dog_breedz](https://www.kaggle.com/datasets/samkitjain101/cat-dog-breedz)

## Training
So training was pretty challenging because of the conditions laid out by you people I wasted one full day trying to make stuff with tensorflow which sux.

Then you told me other frameworks are allowed so I've been making models with  pytorch and fastai for the last 3 hours[not the best results :(]

### Approach I - Training with TensorFlow
So the best validation accuracy we got with tensorflow was 34% we tried everything but it didn't work. Also this weird problem with it being capped at 50% I swear we tried everything :(( 

![tf](https://cdn.discordapp.com/attachments/861575248603381760/1040700639409340416/unknown.png)


### Approach II - Training with fast.ai

!["fastai layers"](https://cdn.discordapp.com/attachments/1040704720844640377/1040704911580598324/image.png)
This one is a better approach but fast.ai works best for transfer learning tasks.
!["faaaaaaaaast"](https://cdn.discordapp.com/attachments/861575248603381760/1040703295456559186/image.png)

Sadly training on this took aloot of time 30 minutes for 3 epochs lul.

PS - Resnet50 gave 80% validation accuracy right off the bat

### Approach III - Training with PyTorch [Final]

Model - !['torchmodel'](https://cdn.discordapp.com/attachments/861575248603381760/1040704549767360556/image.png)


So training with PyTorch was our final approach we managed to get ~ 45% validation accuracy with this. IT was pretty straight forward and didn't take much time to train as well therefore, we decided to submit this model.

!['toorch'](https://media.discordapp.net/attachments/861575248603381760/1040703646146494565/image.png)

We are going to add all the 3 approaches in the github repository if you are interested in going through them

Thank you for reading and letting us participate very kewl event(didnt like the layer cap tho :( )
