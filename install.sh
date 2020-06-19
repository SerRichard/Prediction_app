cd /
cd /usr/lib64
mkdir prediction_app
cd prediction_app

sudo wget -O requirements.txt https://raw.githubusercontent.com/SerRichard/Prediction_app/master/requirements.txt
sudo wget -O prediction_app.py https://raw.githubusercontent.com/SerRichard/Prediction_app/master/prediction_app.py

sudo wget -O squat.png https://raw.githubusercontent.com/SerRichard/Prediction_app/master/squat.png
sudo wget -O bench.png https://raw.githubusercontent.com/SerRichard/Prediction_app/master/bench.png
sudo wget -O deadlift.png https://raw.githubusercontent.com/SerRichard/Prediction_app/master/deadlift.png
sudo wget -O male.png https://raw.githubusercontent.com/SerRichard/Prediction_app/master/male.png
sudo wget -O female.png https://raw.githubusercontent.com/SerRichard/Prediction_app/master/female.png
sudo wget -O trans.png https://raw.githubusercontent.com/SerRichard/Prediction_app/master/trans.png

sudo wget -O Bench_Model_1.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Bench_Model_1.sav
sudo wget -O Bench_Model_2.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Bench_Model_2.sav
sudo wget -O Bench_Model_3.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Bench_Model_3.sav

sudo wget -O Squat_Model_1.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Squat_Model_1.sav
sudo wget -O Squat_Model_2.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Squat_Model_2.sav
sudo wget -O Squat_Model_3.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Squat_Model_3.sav

sudo wget -O Deadlift_Model_1.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Squat_Model_1.sav
sudo wget -O Deadlift_Model_2.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Squat_Model_2.sav
sudo wget -O Deadlift_Model_3.sav https://raw.githubusercontent.com/SerRichard/Prediction_app/master/Squat_Model_3.sav

sudo pip3 install -r requirements.txt
sudo chmod +x prediction_app.py

cd /
cd ~/Desktop

sudo wget -O prediction_launcher.desktop https://raw.githubusercontent.com/SerRichard/Prediction_app/master/prediction_launcher.desktop
