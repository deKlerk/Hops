# Deploying the Flask app to Heroku

This tutorial summarizes the steps required to deploy your Flask app to Heroku, taking the post [**"Create and Deploy a Simple Web Application with Flask and Heroku"**](https://towardsdatascience.com/create-and-deploy-a-simple-web-application-with-flask-and-heroku-103d867298eb) by [Naveen Venkatesan](https://naveenvenkatesan.medium.com/?source=post_page-----103d867298eb--------------------------------) as a reference.

It assumes you already have Git installed on your machine, a Github account and Heroku account.

Deploying your Flask app to Heroku can be done in a simple way, following the steps below:

## Setup

You will start by setting up the basis for your app to be developed:

1. Create a [Github](https://github.com/) repository for your application;
2. Clone your newly created repository using `git clone https://github.com/your_name/repo_name` and cd into the folder `repo_name`;
3. Create a virtual environment for your application with `python3 -m venv venv` (for example) and activate it.
4. pip install the following modules:
   1. [flask](https://palletsprojects.com/p/flask/)
   2. [gunicorn](https://gunicorn.org/)
   3. [ghhops-server](https://github.com/mcneel/compute.rhino3d/tree/master/src/ghhops-server-py)
   4. [rhino3dm](https://www.rhino3d.com/features/rhino3dm/) (this is optional)
   5. [*your_additional_modules*](https://pypi.org/) (also optional)

## Development

Now comes the fun part: developing your app! You can follow the [**Quick Start**](https://github.com/mcneel/compute.rhino3d/tree/master/src/ghhops-server-py#quick-start) guide in McNeel's Github repository.

5. Develop and test your Flask app;

## Essential Files

6. Create a **`requirements.txt`** file, where all necessary modules will be listed. You can use `pip freeze > requirements.txt` to automatically write all modules and versions you have installed via pip;
7. Create a **`Procfile`** with the following content: `web: gunicorn app:app`, a list of instructions for Heroku to run your application considering you are using `gunicorn` and that you named your app `app`;
8. Create a **`runtime.txt`** file with the following content: `python-3.9.2` (this will force Heroku to install Python version 3.9.2 - my case). The version should match the one you are using for development - remember that Hops-Server [requires **Python 3.8** or above.](https://discourse.mcneel.com/t/create-cpython-components-using-hops-in-grasshopper/120517)

## Push and Deploy

9. Now you need to stage these changes in git with `git add .` (if you want to add all unstaged changes at the same time), commit them with `git commit -m "Meaningful commit message"` and push them to the application's Github repo `git push origin main` (VS Code has plugins that make these steps a breeze).
10. Login to your Heroku account and select the option to create a new app, give it a name and choose an adequate region. Then just click the button `Create app` below;
11. On your application dashboard click the tab `Deploy` and on the section `Deployment method` choose to connect Heroku to your application's Github repository;
12. Choose one of the following options and... **deploy!**
    1. Automatic deploys - everytime there's a change to the selected branch on Github, Heroku automatically runs the process;
    2. Manual deploy - you choose when to deploy the content from Github, with the push of a button.

You can check the activity feed and follow the deployment in progress (click the link of the last entry).

**Congratulations, you're done!**

Now, all that is left for you to do is click the button `Open app` on the top-right corner of Heroku and see it working. If all went well, you should now be able to feed the URL of your app's component's endpoints to the Hops Component's path in Grasshopper.
