#!/usr/bin/env python3

# -- code --
# @author Sean Hoyal
#
# An app that will take set inputs about a Athlete and then make a prediction
# about that athlete abilities on a chosen lift. Uses RFregression models
# based on a previous project to do this.
# 
# Imports
from PyQt5.QtWidgets import QPushButton, QMainWindow, QVBoxLayout, QApplication, QPushButton, QHBoxLayout
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QIcon
from sklearn import model_selection
from sklearn.ensemble import RandomForestRegressor
import pickle
import sys

# Athlete is the object parsed through the various pages and functions. It represents the 
# individual the app is predicting for.
class athlete(object):
	
	def __init__(self):
		self.age = None
		self.weight = None
		self.lift = None
		self.history = None
		self.sex = None
		self.equipment = None
		self.check1 = None
		self.check2 = None
		self.score = None
		self.lift1 = None
		self.lift2 = None
		self.result = None

# The first page of the app. A basic layout attributes that can be filled with clicking a button.
# Directories used in the code are built by the installation file.
#
# The UIHome and UISecond classes are responsible for the app layout, not the functionality.
class UIHome(object):
	def setupUI(self, MainWindow):
		MainWindow.setWindowIcon(QtGui.QIcon("/usr/lib64/prediction_app/squat.png"))
		MainWindow.setGeometry(300, 300, 500, 500)
		MainWindow.setFixedSize(500, 500)
		MainWindow.setWindowTitle("prediction_app")
		
		# Base layer, 'layout' is placed on top of the base.
		# Buttons are affixed to their own labels which are
		# then added to 'layout'.
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setStyleSheet("background-color: white")

		self.details = QtWidgets.QLabel(self.centralwidget)
		self.details.setGeometry(50, 50, 400, 450)
		
		self.layout1 = QVBoxLayout()

		# Lift buttons.
		self.btn_lbl = QtWidgets.QLabel(self.centralwidget)
		self.btn_lyt = QHBoxLayout()
		
		self.btn_sqt = QtWidgets.QPushButton(self.btn_lbl)
		self.btn_sqt.setObjectName('squat')
		self.btn_sqt.setIcon(QIcon('/usr/lib64/prediction_app/squat.png'))
		self.btn_sqt.setIconSize(QtCore.QSize(90, 90))
		self.btn_sqt.setFixedSize(120, 77)
		self.btn_sqt.setStyleSheet("background-color: darkGray")
		self.btn_lyt.addWidget(self.btn_sqt)

		self.btn_bench = QtWidgets.QPushButton(self.btn_lbl)
		self.btn_bench.setObjectName('bench')
		self.btn_bench.setIcon(QIcon('/usr/lib64/prediction_app/bench.png'))
		self.btn_bench.setIconSize(QtCore.QSize(90, 90))
		self.btn_bench.setFixedSize(120, 77)
		self.btn_bench.setStyleSheet("background-color: darkGray")
		self.btn_lyt.addWidget(self.btn_bench)

		self.btn_dead = QtWidgets.QPushButton(self.btn_lbl)
		self.btn_dead.setObjectName('deadlift')
		self.btn_dead.setIcon(QIcon('/usr/lib64/prediction_app/deadlift.png'))
		self.btn_dead.setIconSize(QtCore.QSize(80, 80))
		self.btn_dead.setFixedSize(120, 77)
		self.btn_dead.setStyleSheet("background-color: darkGray")
		self.btn_lyt.addWidget(self.btn_dead)

		self.btn_lbl.setLayout(self.btn_lyt)
		self.layout1.addWidget(self.btn_lbl)

		# Labels and buttons for equipment.
		self.equipment_lbl = QtWidgets.QLabel(self.centralwidget)
		self.equipment_layout = QHBoxLayout()

		self.btn_raw = QtWidgets.QPushButton("Raw", self.equipment_lbl)
		self.btn_raw.setFixedSize(70, 77)
		self.btn_raw.setStyleSheet("background-color: darkGray")
		self.equipment_layout.addWidget(self.btn_raw)

		self.btn_wraps = QtWidgets.QPushButton("Wraps", self.equipment_lbl)
		self.btn_wraps.setFixedSize(70, 77)
		self.btn_wraps.setStyleSheet("background-color: darkGray")
		self.equipment_layout.addWidget(self.btn_wraps)

		self.btn_straps = QtWidgets.QPushButton("Straps", self.equipment_lbl)
		self.btn_straps.setFixedSize(70, 77)
		self.btn_straps.setStyleSheet("background-color: darkGray")
		self.equipment_layout.addWidget(self.btn_straps)

		self.btn_sply = QtWidgets.QPushButton("Single-Ply", self.equipment_lbl)
		self.btn_sply.setFixedSize(70, 77)
		self.btn_sply.setStyleSheet("background-color: darkGray")
		self.equipment_layout.addWidget(self.btn_sply)

		self.btn_mply = QtWidgets.QPushButton("Multi-Ply", self.equipment_lbl)
		self.btn_mply.setFixedSize(70, 77)
		self.btn_mply.setStyleSheet("background-color: darkGray")
		self.equipment_layout.addWidget(self.btn_mply)

		self.equipment_lbl.setLayout(self.equipment_layout)
		self.layout1.addWidget(self.equipment_lbl)

		# Labels and buttons related to Sex.
		self.sex_lbl = QtWidgets.QLabel(self.centralwidget)
		self.sex_layout = QHBoxLayout()
		
		self.btn_male = QtWidgets.QPushButton(self.sex_lbl)
		self.btn_male.setObjectName('male')
		self.btn_male.setIcon(QIcon('/usr/lib64/prediction_app/male.png'))
		self.btn_male.setIconSize(QtCore.QSize(40, 40))
		self.btn_male.setFixedSize(120, 77)
		self.btn_male.setStyleSheet("background-color: darkGray")
		self.sex_layout.addWidget(self.btn_male)
		
		self.btn_fmale = QtWidgets.QPushButton(self.sex_lbl)
		self.btn_fmale.setObjectName('female')
		self.btn_fmale.setIcon(QIcon('/usr/lib64/prediction_app/female.png'))
		self.btn_fmale.setFixedSize(120, 77)
		self.btn_fmale.setIconSize(QtCore.QSize(50, 50))
		self.btn_fmale.setStyleSheet("background-color: darkGray")
		self.sex_layout.addWidget(self.btn_fmale)
		
		self.btn_trans = QtWidgets.QPushButton(self.sex_lbl)
		self.btn_trans.setObjectName('trans')
		self.btn_trans.setIcon(QIcon('/usr/lib64/prediction_app/trans.png'))
		self.btn_trans.setFixedSize(120, 77)
		self.btn_trans.setIconSize(QtCore.QSize(60, 60))
		self.btn_trans.setStyleSheet("background-color: darkGray")
		self.sex_layout.addWidget(self.btn_trans)
		
		self.sex_lbl.setLayout(self.sex_layout)
		self.layout1.addWidget(self.sex_lbl)

		# Labels and buttons related to history. History
		# buttons are related to whether the user has a previous
		# Wilks, McCulloch, or recent lifts to provide to the 
		# prediction model.
		self.sth_lbl = QtWidgets.QLabel(self.centralwidget)
		self.sth_layout = QHBoxLayout()

		self.btn_wlk = QtWidgets.QPushButton("Wilks", self.sex_lbl)
		self.btn_wlk.setFixedSize(120, 77)
		self.btn_wlk.setStyleSheet("background-color: darkGray")
		self.sth_layout.addWidget(self.btn_wlk)

		self.btn_mcc = QtWidgets.QPushButton("McCulloch", self.sex_lbl)
		self.btn_mcc.setFixedSize(120, 77)
		self.btn_mcc.setStyleSheet("background-color: darkGray")
		self.sth_layout.addWidget(self.btn_mcc)

		self.btn_lft = QtWidgets.QPushButton("Lifts", self.sex_lbl)
		self.btn_lft.setFixedSize(120, 77)
		self.btn_lft.setStyleSheet("background-color: darkGray")
		self.sth_layout.addWidget(self.btn_lft)

		self.sth_lbl.setLayout(self.sth_layout)
		self.layout1.addWidget(self.sth_lbl)


		# Label and button for next. Next button goes to the second page
		# of the app.
		self.lbl_next = QtWidgets.QLabel(self.centralwidget)
		self.lyt_next = QVBoxLayout()

		self.btn_next = QtWidgets.QPushButton('Next', self.lbl_next)
		self.btn_next.setStyleSheet("background-color: darkGray")
		self.btn_next.setFixedSize(385, 30)
		self.lyt_next.addWidget(self.btn_next)

		self.sth_lbl.setLayout(self.lyt_next)
		self.layout1.addWidget(self.lbl_next)

		# Attach to base
		self.details.setLayout(self.layout1)
		MainWindow.setCentralWidget(self.centralwidget)

# Second page of the app. One of either two pages will be built,
# depending on what historical information about the athletes lifts
# are available.
class UISecond(object):
	def setupUI(self, MainWindow, athlete):
		MainWindow.setFixedSize(500, 500)
		MainWindow.setWindowTitle("prediction_app")

		# If the athlete can provide either a recent Wilks or McCulloch, then everything
		# within this if statement will be built. Else, see line 277.
		if (athlete.history == 'Wilks') or (athlete.history == 'McCulloch'):
			
			# Base layer, 'layout' is placed on top of the base.
			# Buttons are affixed to their own labels which are
			# then added to 'layout'.
			self.centralwidget = QtWidgets.QWidget(MainWindow)
			self.centralwidget.setStyleSheet("background-color: white")

			self.base = QtWidgets.QLabel(self.centralwidget)
			self.base.setGeometry(30, 50, 400, 400)

			self.layout = QVBoxLayout()

			# Labels and buttons for age and weight. Two text boxes for the user
			# to input both the athletes age and weight(kg). An enter button set to the right
			# to input info from both of these boxes.
			self.age_label = QtWidgets.QLabel(self.centralwidget)
			self.lbl_age = QtWidgets.QLabel("Age: ", self.age_label)
			self.txt_age = QtWidgets.QLineEdit(self.age_label)
			
			self.lbl_weight = QtWidgets.QLabel("Weight (kg): ", self.age_label)
			self.le_weight = QtWidgets.QLineEdit(self.age_label)

			self.age_layout = QHBoxLayout()
			self.age_layout.addWidget(self.lbl_age)
			self.age_layout.addWidget(self.txt_age)
			self.age_layout.addWidget(self.lbl_weight)
			self.age_layout.addWidget(self.le_weight)

			self.btn_enter = QPushButton('Enter', self.centralwidget)
			self.btn_enter.setStyleSheet("background-color: darkGray")
			self.age_layout.addWidget(self.btn_enter)

			self.age_label.setLayout(self.age_layout)

			self.layout.addWidget(self.age_label)

			# Wilks or McCulloch score. An input box again with a button for entry
			# set to the right hand side.
			self.score_lbl = QtWidgets.QLabel(self.centralwidget)
			self.score_layout = QHBoxLayout()

			self.label = QtWidgets.QLabel("Input score: ", self.score_lbl)
			self.score_layout.addWidget(self.label)

			self.score_le = QtWidgets.QLineEdit(self.score_lbl)
			self.score_layout.addWidget(self.score_le)
			self.score_btn = QtWidgets.QPushButton("Enter score", self.score_lbl)
			self.score_btn.setStyleSheet("background-color: darkGray")
			self.score_layout.addWidget(self.score_btn)

			self.score_lbl.setLayout(self.score_layout)
			self.layout.addWidget(self.score_lbl)

			# Prediction and Reset buttons. Prediction button will display the 
			# prediction result in the results section. Reset button will
			# return to the first page, and reset athlete variables.
			self.pred_lbl = QtWidgets.QLabel(self.centralwidget)

			self.pred_lay = QHBoxLayout()

			self.btn_predict = QtWidgets.QPushButton("Predict!", self.pred_lbl)
			self.btn_predict.setStyleSheet("background-color: darkGray")
			self.res_btn = QtWidgets.QPushButton("Reset!", self.pred_lbl)
			self.res_btn.setStyleSheet("background-color: darkGray")
			self.pred_lay.addWidget(self.btn_predict)
			self.pred_lay.addWidget(self.res_btn)

			self.pred_lbl.setLayout(self.pred_lay)
			self.layout.addWidget(self.pred_lbl)
			
			# Results section, this is a txt field that will display the 
			# prediction output.
			self.res_label = QtWidgets.QLabel(self.centralwidget)
			self.res_txt = QtWidgets.QPlainTextEdit(self.res_label)
			self.res_txt.setFixedSize(386, 50)
			self.res_txt.setReadOnly(True)
			
			self.layout.addWidget(self.res_label)

		# Else.
		else:

			# Base layer, 'layout' is placed on top of the base.
			# Buttons are affixed to their own labels which are
			# then added to 'layout'.
			self.centralwidget = QtWidgets.QWidget(MainWindow)
			self.centralwidget.setStyleSheet("background-color: white")

			self.base = QtWidgets.QLabel(self.centralwidget)
			self.base.setGeometry(30, 50, 400, 400)

			self.layout = QVBoxLayout()

			# Labels and buttons for age and weight. Two text boxes for the user
			# to input both the athletes age and weight(kg). An enter button set to the right
			# to input info from both of these boxes.
			self.age_label = QtWidgets.QLabel(self.centralwidget)
			self.lbl_age = QtWidgets.QLabel("Age: ", self.age_label)
			self.txt_age = QtWidgets.QLineEdit(self.age_label)
			
			self.lbl_weight = QtWidgets.QLabel("Weight (kg): ", self.age_label)
			self.le_weight = QtWidgets.QLineEdit(self.age_label)

			self.age_layout = QHBoxLayout()
			self.age_layout.addWidget(self.lbl_age)
			self.age_layout.addWidget(self.txt_age)
			self.age_layout.addWidget(self.lbl_weight)
			self.age_layout.addWidget(self.le_weight)

			self.btn_enter = QPushButton('Enter', self.centralwidget)
			self.btn_enter.setStyleSheet("background-color: darkGray")
			self.age_layout.addWidget(self.btn_enter)

			self.age_label.setLayout(self.age_layout)

			self.layout.addWidget(self.age_label)

			# First previous lift, an input box with an enter button set to the right.
			# The lift required for input will change depending on what lift you are
			# trying to predict.
			self.first_lbl = QtWidgets.QLabel(self.centralwidget)
			self.first_layout = QHBoxLayout()

			self.label = QtWidgets.QLabel("Input recent max {}:".format(athlete.check1), self.first_lbl)
			self.first_layout.addWidget(self.label)

			self.le_lift1 = QtWidgets.QLineEdit(self.first_lbl)
			self.btn_one = QtWidgets.QPushButton("Enter {}".format(athlete.check1), self.first_lbl)
			self.btn_one.setStyleSheet("background-color: darkGray")
			self.first_layout.addWidget(self.le_lift1)
			self.first_layout.addWidget(self.btn_one)

			self.first_lbl.setLayout(self.first_layout)			
			self.layout.addWidget(self.first_lbl)

			# Second previous lift, another input box with an enter button set to the right.
			# The lift required for input will change depending on what lift you are
			# trying to predict.
			self.second_lbl = QtWidgets.QLabel(self.centralwidget)
			self.second_layout = QHBoxLayout()

			self.label_2 = QtWidgets.QLabel("Input recent max {}:".format(athlete.check2), self.second_lbl)
			self.second_layout.addWidget(self.label_2)

			self.le_lift2 = QtWidgets.QLineEdit(self.second_lbl)
			self.btn_two = QtWidgets.QPushButton("Enter {}".format(athlete.check2), self.second_lbl)
			self.btn_two.setStyleSheet("background-color: darkGray")
			self.second_layout.addWidget(self.le_lift2)
			self.second_layout.addWidget(self.btn_two)

			self.second_lbl.setLayout(self.second_layout)			
			self.layout.addWidget(self.second_lbl)

			# Prediction and Reset buttons. Prediction button will display the 
			# prediction result in the results section. Reset button will
			# return to the first page, and reset athlete variables.
			self.pred_lbl = QtWidgets.QLabel(self.centralwidget)

			self.pred_lay = QHBoxLayout()

			self.btn_predict = QtWidgets.QPushButton("Predict!", self.pred_lbl)
			self.btn_predict.setStyleSheet("background-color: darkGray")
			self.res_btn = QtWidgets.QPushButton("Reset!", self.pred_lbl)
			self.res_btn.setStyleSheet("background-color: darkGray")
			self.pred_lay.addWidget(self.btn_predict)
			self.pred_lay.addWidget(self.res_btn)

			self.pred_lbl.setLayout(self.pred_lay)
			self.layout.addWidget(self.pred_lbl)
			
			# Results section, this is a txt field that will display the 
			# prediction output.
			self.res_label = QtWidgets.QLabel(self.centralwidget)
			self.res_txt = QtWidgets.QPlainTextEdit(self.res_label)
			self.res_txt.setFixedSize(386, 50)
			self.res_txt.setReadOnly(True)
			
			self.layout.addWidget(self.res_label)

		# Attach to base. Whichever page is built will get attached 
		# to the base layer of the second page.
		self.base.setLayout(self.layout)
		MainWindow.setCentralWidget(self.centralwidget)

# Class main window, this is where the user interface and special button functions have
# been programmed.
class MainWindow(QMainWindow):

	# Initiate objects needed for app.
	def __init__(self):
		super(MainWindow, self).__init__()
		self.athlete = athlete()
		self.uiHome = UIHome()
		self.uiSecond = UISecond()
		self.startUIHome()

	# Runs at start up. Programmes all of the buttons on the uiHome.
	def startUIHome(self):
		self.uiHome.setupUI(self)
		self.uiHome.btn_sqt.clicked.connect(self.lft_clk)
		self.uiHome.btn_bench.clicked.connect(self.lft_clk)		
		self.uiHome.btn_dead.clicked.connect(self.lft_clk)

		self.uiHome.btn_male.clicked.connect(self.sex_clk)
		self.uiHome.btn_fmale.clicked.connect(self.sex_clk)
		self.uiHome.btn_trans.clicked.connect(self.sex_clk)
		
		self.uiHome.btn_wlk.clicked.connect(self.hst_clk)
		self.uiHome.btn_mcc.clicked.connect(self.hst_clk)
		self.uiHome.btn_lft.clicked.connect(self.hst_clk)

		self.uiHome.btn_raw.clicked.connect(self.equ_clk)
		self.uiHome.btn_wraps.clicked.connect(self.equ_clk)
		self.uiHome.btn_straps.clicked.connect(self.equ_clk)
		self.uiHome.btn_sply.clicked.connect(self.equ_clk)
		self.uiHome.btn_mply.clicked.connect(self.equ_clk)		

		self.uiHome.btn_next.clicked.connect(self.startUISecond)
		self.show()

	# Runs all the buttons required for whichever uiSecond page was built.
	def startUISecond(self):
		self.uiSecond.setupUI(self, self.athlete)

		self.uiSecond.btn_enter.clicked.connect(self.btn_clk)

		x = [self.athlete.lift, self.athlete.history]

		if (self.athlete.history == 'Wilks') or (self.athlete.history == 'McCulloch'):
			self.uiSecond.score_btn.clicked.connect(self.btn_clk)
		else:
			self.uiSecond.btn_one.clicked.connect(self.btn_clk)
			self.uiSecond.btn_two.clicked.connect(self.btn_clk)

		self.uiSecond.btn_predict.clicked.connect(self.btn_clk)
		self.uiSecond.res_btn.clicked.connect(self.startUIHome)
		self.show()

	# Function for setting the correct lift and checks for each athlete.
	def lft_clk(self):
		sender = self.sender()
		if sender.objectName() == 'squat':
			self.athlete.lift = 'Squat'
			self.athlete.check1 = 'Bench'
			self.athlete.check2 = 'Deadlift'
			print(self.athlete.lift)
			return(self.athlete.lift, self.athlete.check1, self.athlete.check2)
	
		if sender.objectName() == 'bench':
			self.athlete.lift = 'Bench'
			self.athlete.check1 = 'Squat'
			self.athlete.check2 = 'Deadlift'
			print(self.athlete.lift)
			return(self.athlete.lift, self.athlete.check1, self.athlete.check2)
		
		if sender.objectName() == 'deadlift':
			self.athlete.lift = 'Deadlift'
			self.athlete.check1 = 'Squat'
			self.athlete.check2 = 'Bench'
			print(self.athlete.lift)
			return(self.athlete.lift, self.athlete.check1, self.athlete.check2)

	# Function for setting the sex of the athlete.
	def sex_clk(self):
		sender = self.sender()
		if sender.objectName() == 'male':
			self.athlete.sex = 0
			print(self.athlete.sex)
			return(self.athlete.sex)
	
		if sender.objectName() == 'female':
			self.athlete.sex = 1
			print(self.athlete.sex)
			return(self.athlete.sex)
	
		if sender.objectName() == 'trans':
			self.athlete.sex = 2
			print(self.athlete.sex)
			return(self.athlete.sex)
	
	# Function for setting the equipment of an athlete.
	def equ_clk(self):
		sender = self.sender()
		if sender.text() == 'Raw':
			self.athlete.equipment = 0
			print(self.athlete.equipment)
			return(self.athlete.equipment)
		
		if sender.text() == 'Wraps':
			self.athlete.equipment = 1
			print(self.athlete.equipment)
			return(self.athlete.equipment)
		
		if sender.text() == 'Straps':
			self.athlete.equipment = 4
			print(self.athlete.equipment)
			return(self.athlete.equipment)

		if sender.text() == 'Single-Ply':
			self.athlete.equipment = 3
			print(self.athlete.equipment)
			return(self.athlete.equipment)

		if sender.text() == 'Multi-Ply':
			self.athlete.equipment = 2
			print(self.athlete.equipment)
			return(self.athlete.equipment)

	# Function for setting the history of an athlete.
	def hst_clk(self):
		sender = self.sender()
		if sender.text() == 'Wilks':
			self.athlete.history = 'Wilks'
			print(self.athlete.history)
			return(self.athlete.history)

		if sender.text() == 'McCulloch':
			self.athlete.history = 'McCulloch'
			print(self.athlete.history)
			return(self.athlete.history)

		if sender.text() == 'Lifts':
			self.athlete.history = 'Lifts'
			print(self.athlete.history)
			return(self.athlete.history)

	# Function for the buttons in startUISecond.
	def btn_clk(self):
		sender = self.sender()
		if sender.text() == "Enter":
			self.athlete.age = int(self.uiSecond.txt_age.text())
			self.athlete.weight = int(self.uiSecond.le_weight.text())
			print(self.athlete.age)
			print(self.athlete.weight)
			return(self.athlete.age, self.athlete.weight)
		if sender.text() == "Enter score":
			self.athlete.score = int(self.uiSecond.score_le.text())
			print(self.athlete.score)
			return(self.athlete.score)
		if sender.text() == "Enter {}".format(self.athlete.check1):
			self.athlete.lift1 = int(self.uiSecond.le_lift1.text())
			print(self.athlete.lift1)
			return(self.athlete.lift1)
		if sender.text() == "Enter {}".format(self.athlete.check2):
			self.athlete.lift2 = int(self.uiSecond.le_lift2.text())
			print(self.athlete.lift2)
			return(self.athlete.lift2)
		if sender.text() == "Predict!":
			self.athlete.result = self.makePrediction()
			self.uiSecond.res_txt.setPlainText(self.athlete.result)

	# Function for taking all of the relevant information about the athlete
	# and parse it to the correct regression model. Take the result, and return
	# the result.	
	def makePrediction(self):
	
		y = [self.athlete.sex, self.athlete.age, self.athlete.weight, self.athlete.equipment]

		if self.athlete.history == 'Wilks':
			tier = 1
			y.append(self.athlete.score)
		elif self.athlete.history == 'McCulloch':
			tier = 2
			y.append(self.athlete.score)
		else:
			tier = 3
			y.append(self.athlete.lift1)
			y.append(self.athlete.lift2)

		model = pickle.load(open('/usr/lib64/prediction_app/{}_Model_{}.sav'.format(self.athlete.lift, tier), 'rb'))

		result = str(model.predict([y]))
		result = result.replace("[", "")
		result = result.replace("]", "")

		print(result)
		return(result)

# Start the home window, this is the 'main' for the programme.
def home_window():
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())

home_window()