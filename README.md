# Udacity Reinforcement learning Nanodegree project 3 - Collaboration and competition

## Introduction
This is the third and final project that is given in the reinforcement learning nanodegree offered by udacity.

Broadly speaking the goal of the project is to train a pair of tennis/ping pong playing agents to maintain a rally across the net. Contrary to standard tennis rules, the agent can keep the ball in the air for as long as is required to get the ball over the net.

## Project Description
Being more precise, the task of the project is the train a pair of tennis playing agents to keep a ball in the air (or to keep a rally going). 

* The material goal of the task is reflected on the **reward** function by giving an agent a reward of +0.1 for each time it hits the ball over the net, whilst penalising the agent -0.1 for each time it lets the ball drop to the table. The score associated to an episode is the maximum of the two agents.

* The **state space** of the agent is 24 dimensional and contains the agent's (the racket) position and the velocity of ball and racket.

* The space of **actions** that each agent can take is 2 dimensional and are continous. They correspond to forward/backward movements towards and away from the net, and up/down movements corresponding to jumping.

* The task is deemed solved if the agent gets an average score of +0.5 over 100 consecutive episodes.

## Setup
* A complete set-up of python, the machine learning agents, openAI and much more can be found in https://github.com/udacity/deep-reinforcement-learning#dependencies. Of particular relevance will be unityagents from within the python folder in the corresponding repository.

* The tennis application itself can be downloading from the following locations:
    * win x64 : https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip
    * win x32 : https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip
    * Linux : https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip
    * Mac : https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip

* We employ the use of environment variables so as to not distribute personal computer information. As a result, please set 

    * \_DRL_LOCATION_ : The path of the python subfolder in the deep reinforcement learning rep descirbed above, generically this would be "...\drlnd\deep-reinforcement-learning\python"
    * \_TENNIS_LOCATION_ : The path to the banana executable, this generically would look like "...\Banana_Windows_x86_64\Banana.exe"

## Code and result structure
There are three components to the solution. The first is the source code itself which implements the agent, the underlying model and further nessecary componenents. The second is the results folder, which contains the results of the training of the various models studied. Finally, the jupyter notebook named navigation.ipynb which acts as interface between the source code and the results folder, whilst itself displaying the results.

The detailed rundown is as follows:
* **The source code** can be found in the folder `\src` and include four python files:
    * `maddpg_agent.py` : Contains the complete agent implementation subject the underlying model chosen.
    * `agents.py` : Since we have multiple agents, this class is a container for multiple agents.
    * `environment.py` : Is a very rudimentary wrapper for the environment to make it feel a little more like the OpenAI environments.
    * `model.py` :  The model implementations - in this case a neural network.
    * `replaybuffer.py` : The replay buffer implmentation for memory.
    * `noise.py` : A stochastic (Ornstein-Uhlenbeck process) noise implemenation for to provide some noise to the actions chosen.
    * `folder_util.py` : A utility class for folder handling for the dynamic creation of the results/run folder structure.

* **The results folder** contains subfolders associated to the date that the exercise was run, together with further subfolders associated to the run number for that date. Within these folders, there as checkpoints.pth files for the model employed, thus an example of where the stored model data is held is 'results/20190825/run_1'. Since we use the actor-critic model and there are two agents, we save the model as
    * checkpoint_action_##_0.pth
    * checkpoint_action_##_1.pth
    * checkpoint_critic_##_0.pth
    * checkpoint_critic_##_1.pth
where ## can be 'solved' or 'not_solved'.

* **The interfacing jupyter notebook** is considered the interface layer in which the user can decide on what precise architectures and models to use for the model. With each trained model, the scores against episodes is plotted, with the results forwared to the relevant results subfolder. The modelled agent can also be played from here to the see the solved task at work. 


## Models
* In this project, we study the multiple agent deterministic deep policy gradient method (MADDPG).

Below is displayed the resulting policy
![](play.gif)