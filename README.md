# Prediction App

App using ML regression to predict your lifts.

ML Models not built from, but based on a previous project.
Repo: https://github.com/SerRichard/powerliftingrepo

**Installation Linux Systems**

In terminal, navigate to your downloads, directory.
```
sudo wget -O install.sh https://raw.githubusercontent.com/SerRichard/Prediction_app/master/install.sh
sudo chmod +x install.sh
```

Before running the script, open in nano.
```
sudo nano install.sh
```

Change username to your username in the DST_DIR. Else the desktop icon won't be created.
If  you username is peanuts, the change will be.
```
DST_DIR="$ROOT/home/username/Desktop"
to
DST_DIR="$ROOT/home/peanuts/Desktop"
```
Ctrl+X and save to exit nano.

Now execute the file.
```
sudo ./install.sh
```

The app will now be installed into */usr/lib64/prediction_app*, and a desktop icon created. 
The icon image may not appear on all distributions, so you may need to set it manually with the squat.png file downloaded into the aformentioned directory.

**App use**

App is basic and easy to use.
> Select the lift you wish to predict.
> Select any equipment used.
> Select your sex.
> Select your history.
 *Lifter's history is either a recent WILKS or McCulloch score. However, in absence of those the lifter can use their most recent max lifts to make a prediction.

> Next
> You will be prompted to input age and weight. *Weight input is in kilograms.
> You will either need to now input you recent score, or the recent lifts necessary.
> Predict.
> Prediction results displayed below. Reset to carry out another prediction.

**App notes**

App has basic utility, possible additional features would be implementing the above App use instructions into the application itself. I'll aim to do that, and also improve interface layout.
