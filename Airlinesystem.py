from PyQt5.QtCore import *
from PyQt5.QtGui import *
import config
from PyQt5.QtWidgets import *
import sys
import mysql.connector

from PyQt5.uic import loadUiType

ui, _ = loadUiType('airline.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_Buttons()
        self.Handel_Ui_Changes()

    def Handel_Ui_Changes(self):
        self.tabWidget_2.tabBar().setVisible(False)
        self.tabWidget_3.tabBar().setVisible(False)
        self.tabWidget.tabBar().setVisible(False)

    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Admin_Airline)
        self.pushButton_2.clicked.connect(self.Admin_passenger)
        self.pushButton_3.clicked.connect(self.Admin_route)
        self.pushButton_4.clicked.connect(self.Admin_user)
        self.pushButton_5.clicked.connect(self.Admin_settings)
        self.pushButton_46.clicked.connect(self.User_booking)
        self.pushButton_45.clicked.connect(self.User_route)
        self.pushButton_44.clicked.connect(self.User_ticket)
        self.pushButton_54.clicked.connect(self.User_settings)
        self.pushButton_47.clicked.connect(self.Admin_logout)
        self.pushButton_48.clicked.connect(self.User_logout)
        self.pushButton_138.clicked.connect(self.New_User_logout)
        self.pushButton_40.clicked.connect(self.Airline_Search)
        self.pushButton_8.clicked.connect(self.Airline_Add)
        self.pushButton_6.clicked.connect(self.Airline_Search)
        self.pushButton_9.clicked.connect(self.Airline_delete)
        self.pushButton_10.clicked.connect(self.Passenger_Search)
        self.pushButton_11.clicked.connect(self.Booking_search)
        self.pushButton_16.clicked.connect(self.Route_Search)
        self.pushButton_17.clicked.connect(self.Route_add)
        self.pushButton_29.clicked.connect(self.Route_remove)
        self.pushButton_19.clicked.connect(self.User_Search)
        self.pushButton_39.clicked.connect(self.User_add)
        self.pushButton_38.clicked.connect(self.User_remove)
        self.pushButton_40.clicked.connect(self.Admin_details)
        self.pushButton_42.clicked.connect(self.Admin_Update)
        self.pushButton_41.clicked.connect(self.Admin_add)
        self.pushButton_43.clicked.connect(self.User_Route_Search)
        self.pushButton_49.clicked.connect(self.User_Booking)
        self.pushButton_50.clicked.connect(self.User_Cancel_Booking)
        self.pushButton_56.clicked.connect(self.User_generate)
        self.pushButton_51.clicked.connect(self.User_details)
        self.pushButton_53.clicked.connect(self.User_password)
        self.pushButton_52.clicked.connect(self.Welcome_User_details)
        self.pushButton_57.clicked.connect(self.Login)
        self.pushButton_137.clicked.connect(self.new_user)
        self.pushButton_55.clicked.connect(self.Admin_delete)
        #self.pushButton_59.clicked.connect(self.User_Booking1)
        self.pushButton_58.clicked.connect(self.fun1)
        self.pushButton_60.clicked.connect(self.fun2)
        self.pushButton_61.clicked.connect(self.fun3)

    #######################################################################
    ##############################Home_button#####################################
    def Login(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        key = self.comboBox_4.currentText()
        name = self.lineEdit_106.text()
        name1 =(name,)
        password = self.lineEdit_100.text()
        self.lineEdit_100.setText('')
        self.lineEdit_106.setText('')
        if  name or password:
            if key == 'Admin Login':
                try:
                    self.cur.execute('''select admin_name from admin''')
                    sData = self.cur.fetchall()
                    if name1 in sData:
                        self.cur.execute('''select admin_password from admin where admin_name = %s''', (name,))
                        Data = self.cur.fetchall()
                        if (password,) in Data:
                            self.tabWidget.setCurrentIndex(1)
                            self.statusBar().showMessage('Admin Login Successful', 3000)
                        else:
                            self.statusBar().showMessage('Wrong Password', 3000)
                    else:
                        self.statusBar().showMessage('Admin does not exist', 3000)
                except:
                    self.statusBar().showMessage('Wrong Credentials ', 3000)

            else:
                try:
                    self.cur.execute('''select user_name from user''')
                    sData = self.cur.fetchall()
                    if name1 in sData:
                        self.cur.execute('''select passward from user where user_name = %s''', (name,))
                        Data = self.cur.fetchall()
                        if (password,) in Data:
                            self.tabWidget.setCurrentIndex(2)
                            self.statusBar().showMessage('User Login Successful', 3000)
                        else:
                            self.statusBar().showMessage('Wrong Password', 3000)
                    else:
                        self.statusBar().showMessage('User does not exist Click on New User to register', 3000)
                except:
                    self.statusBar().showMessage('Wrong Credentials ', 3000)
        else:
            self.statusBar().showMessage('Enter Credentials ', 3000)


    def new_user(self):
        self.tabWidget.setCurrentIndex(3)

    #######################################################################
    ##############################Admin_button#####################################

    def Admin_Airline(self):
        self.tabWidget_2.setCurrentIndex(0)

    def Admin_passenger(self):
        self.tabWidget_2.setCurrentIndex(1)

    def Admin_route(self):
        self.tabWidget_2.setCurrentIndex(2)

    def Admin_user(self):
        self.tabWidget_2.setCurrentIndex(3)

    def Admin_settings(self):
        self.tabWidget_2.setCurrentIndex(4)

    def User_route(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()
        self.tabWidget_3.setCurrentIndex(1)
        try:
            self.cur.execute('''select  rfrom from route''')
            fData = self.cur.fetchall()
            self.cur.execute('''select  rto from  route''')
            tData = self.cur.fetchall()
            self.comboBox_16.clear()
            self.comboBox_16.addItem('--From--')
            self.comboBox_17.clear()
            self.comboBox_17.addItem('--To--')
            for i in fData:
                self.comboBox_16.addItem(i[0])
            for i in tData:
                self.comboBox_17.addItem(i[0])
        except:
            self.statusBar().showMessage('Unable to set end station combobox')

    def User_booking(self):
        self.tabWidget_3.setCurrentIndex(0)

    def User_ticket(self):
        self.tabWidget_3.setCurrentIndex(2)

    def User_settings(self):
        self.tabWidget_3.setCurrentIndex(3)

    def Admin_logout(self):
        self.tabWidget.setCurrentIndex(0)

    def User_logout(self):
        self.tabWidget.setCurrentIndex(0)

    def New_User_logout(self):
        self.tabWidget.setCurrentIndex(0)

    #def User_Booking1(self):
        #no = self.comboBox_8.currentText()
        #if no == '1':
            #self.tabWidget_3.setCurrentIndex(4)
        #elif no == '2':
            #self.tabWidget_3.setCurrentIndex(5)
       # else:
            #self.tabWidget_3.setCurrentIndex(6)

    ###################################################
    ##################Admin_airline#####################

    def Airline_Search(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        key = self.comboBox.currentText()
        feature = self.lineEdit_2.text()
        if feature:
            id = int(feature)
            id1= tuple([id])
        self.lineEdit_2.setText('')
        if key == 'ALL':
            try:
                self.cur.callproc('Airline_Search')

                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)

                for row, form in enumerate(self.cur.stored_results()):
                    #print(row) gives the no of iterates
                    #print(form) gives point of data at
                    for row2, item in enumerate(form):
                        #print (row2) gives the row count
                        # print(item) gives the its start tuple
                        for col, item1 in enumerate(item):
                            #print(col) gives the col count
                            #print(items1) gives the items one ny one
                            self.tableWidget.setItem(row2, col, QTableWidgetItem(str(item1)))
                            col += 1

                        rowPos = self.tableWidget.rowCount()
                        self.tableWidget.insertRow(rowPos)

            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        else:
            try:
                self.cur.execute('''select airline_id from airline''')
                sData = self.cur.fetchall()
                if id1 in sData:
                    self.cur.callproc('Airline', [feature, ])
                    self.tableWidget.setRowCount(0)
                    self.tableWidget.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        #print(row) gives the no of iterates
                        #print(form) gives point of data at
                        for row2, item in enumerate(form):
                            #print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                #print(col) gives the col count
                                #print(items1) gives the items one ny one
                                self.tableWidget.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget.rowCount()
                            self.tableWidget.insertRow(rowPos)
                else:
                    self.tableWidget.setRowCount(0)
                    self.tableWidget.insertRow(0)
                    self.statusBar().showMessage('ID does not Exists', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)



    def Airline_Add(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()
        name = self.lineEdit.text()
        arrival = self.lineEdit_3.text()
        departure = self.lineEdit_4.text()
        capacity = self.lineEdit_5.text()
        economy_cost = self.lineEdit_12.text()
        business_cost = self.lineEdit_15.text()

        if (int(capacity) == int(economy_cost) + int(business_cost)):
            try:
                self.cur.execute(''' INSERT INTO airline(airline_name, airline_arrival, airline_departure, airline_capacity, economy_seats, business_seats) VALUE ( %s, %s, %s, %s, %s, %s)
                 ''', (name, arrival, departure, capacity, economy_cost, business_cost))
                self.cur.execute(''' select airline_id from airline where airline_capacity = %s and economy_seats =%s and business_seats = %s''',
                                 (capacity,economy_cost,business_cost))
                Data = self.cur.fetchall()
                id3 = Data[0]
                id4 = id3[0]
                print('check Count')
                self.cur.execute(''' INSERT INTO count (airline_id, economy_count,business_count) values (%s,%s,%s)''',
                                 (id4, economy_cost, business_cost))
                self.db.commit()
                self.statusBar().showMessage('Added Successfully', 3000)
                self.lineEdit.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_12.setText('')
                self.lineEdit_15.setText('')

            except:
                self.statusBar().showMessage('Could Not Add Same Data present', 3000)
                self.lineEdit.setText('')
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
                self.lineEdit_5.setText('')
                self.lineEdit_12.setText('')
                self.lineEdit_15.setText('')

        else:
            self.statusBar().showMessage('Capacities Does not match', 3000)
            self.lineEdit.setText('')
            self.lineEdit_3.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_12.setText('')
            self.lineEdit_15.setText('')

    def Airline_delete(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        id = self.lineEdit_26.text()
        id2 = int(id)
        id1 = tuple([id2])
        try:
            self.cur.execute('''select airline_id from airline''')
            sData = self.cur.fetchall()
            if id1 in sData:
                self.cur.execute(''' DELETE FROM airline WHERE airline_id = %s ''', (id,))
                self.db.commit()
                self.lineEdit_26.setText('')
                self.statusBar().showMessage('Deleted Successfully', 3000)
            else:
                self.statusBar().showMessage('Id does not exist', 3000)
                self.lineEdit_26.setText('')
        except:
            self.lineEdit_26.setText('')
            self.statusBar().showMessage('Not Deleted ', 3000)

    ###################################################
    ##################Admin_passenger#####################

    def Passenger_Search(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        key = self.comboBox_3.currentText()
        feature = self.dateEdit_5.dateTime()
        date = feature
        print(date)
        date6 = str(date).split('.')  # concert tostring and split the pt statement
        print(date6)
        date1 = date6[2].split('(')  # select the input in () and split the into 3
        print(date1)
        date2 = date1[1].split(',')  # now split the data to y, m, d)
        print(date2)
        date3 = date2[2].split(')')  # now d) to d
        print(date3)
        if int(date2[1]) < 10 or int(date3[0]) < 10:
            if int(date2[1]) < 10:
                date12 = '0' + date2[1]
                date12 = date12.replace(" ", "")
                print(date12)
            if int(date3[0]) < 10:
                date30 = '0' + date3[0]
                date30 = date30.replace(" ", "")

            date4 = date2[0] + date12 + date30  # add y m d
            date7 = date2[0] + '-' + date12 + '-' + date30
        else:
            date4 = date2[0] + date2[1] + date3[0]  # add y m d
            date7 = date2[0] + '-' + date2[1] + '-' + date3[0]  # add y m d
        print(date4)
        date5 = date4.replace(" ", "")  # ymd removing spaces
        date8 = date7.replace(" ", "-")  # ymd removing spaces
        print(date5)

        if key == 'ALL':
            try:
                self.cur.callproc('passenger')
                print('hi')
                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.insertRow(0)

                for row, form in enumerate(self.cur.stored_results()):
                    # print(row) gives the no of iterates
                    # print(form) gives point of data at
                    for row2, item in enumerate(form):
                        # print (row2) gives the row count
                        # print(item) gives the its start tuple
                        for col, item1 in enumerate(item):
                            # print(col) gives the col count
                            # print(items1) gives the items one ny one
                            self.tableWidget_3.setItem(row2, col, QTableWidgetItem(str(item1)))
                            col += 1

                        rowPos = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(rowPos)

            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        else:
            try:
                print('hihi')
                self.cur.callproc('pass_id2', [date5, ])
                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.insertRow(0)
                print('hi')
                for row, form in enumerate(self.cur.stored_results()):
                    # print(row) gives the no of iterates
                    # print(form) gives point of data at
                    for row2, item in enumerate(form):
                        # print (row2) gives the row count
                        # print(item) gives the its start tuple
                        for col, item1 in enumerate(item):
                            # print(col) gives the col count
                            # print(items1) gives the items one ny one
                            self.tableWidget_3.setItem(row2, col, QTableWidgetItem(str(item1)))
                            col += 1

                        rowPos = self.tableWidget_3.rowCount()
                        self.tableWidget_3.insertRow(rowPos)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)


    def Booking_search(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        key = self.comboBox_7.currentText()
        feature = self.dateEdit_4.dateTime()
        date = feature
        print(date)
        date6 = str(date).split('.')  # concert tostring and split the pt statement
        print(date6)
        date1 = date6[2].split('(')  # select the input in () and split the into 3
        print(date1)
        date2 = date1[1].split(',')  # now split the data to y, m, d)
        print(date2)
        date3 = date2[2].split(')')  # now d) to d
        print(date3)
        if int(date2[1]) < 10 or int(date3[0]) < 10:
            if int(date2[1]) < 10:
                date12 = '0' + date2[1]
                date12 = date12.replace(" ", "")
                print(date12)
            if int(date3[0]) < 10:
                date30 = '0' + date3[0]
                date30 = date30.replace(" ", "")

            date4 = date2[0] + date12 + date30  # add y m d
            date7 = date2[0] + '-' + date12 + '-' + date30
        else:
            date4 = date2[0] + date2[1] + date3[0]  # add y m d
            date7 = date2[0] + '-' + date2[1] + '-' + date3[0]  # add y m d
        print(date4)
        date5 = date4.replace(" ", "")  # ymd removing spaces
        date8 = date7.replace(" ", "-")  # ymd removing spaces
        print(date5)
        if key == 'ALL': #and date5 > '20210201':
            try:
                self.cur.callproc('booking')

                self.tableWidget_4.setRowCount(0)
                self.tableWidget_4.insertRow(0)

                for row, form in enumerate(self.cur.stored_results()):
                    # print(row) gives the no of iterates
                    # print(form) gives point of data at
                    for row2, item in enumerate(form):
                        # print (row2) gives the row count
                        # print(item) gives the its start tuple
                        for col, item1 in enumerate(item):
                            # print(col) gives the col count
                            # print(items1) gives the items one ny one
                            self.tableWidget_4.setItem(row2, col, QTableWidgetItem(str(item1)))
                            col += 1

                        rowPos = self.tableWidget_4.rowCount()
                        self.tableWidget_4.insertRow(rowPos)

            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        else:
            try:
                self.cur.execute('''select * from booking where booking_date= %s'''
                                 ,(date5,))
                sData = self.cur.fetchall()
                print(sData)
                if sData:
                    self.cur.callproc('bookd', [date5, ])
                    self.tableWidget_4.setRowCount(0)
                    self.tableWidget_4.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        # print(row) gives the no of iterates
                        # print(form) gives point of data at
                        for row2, item in enumerate(form):
                            # print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                # print(col) gives the col count
                                # print(items1) gives the items one ny one
                                self.tableWidget_4.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_4.rowCount()
                            self.tableWidget_4.insertRow(rowPos)
                else:
                    self.tableWidget_4.setRowCount(0)
                    self.tableWidget_4.insertRow(0)
                    self.statusBar().showMessage('No booking exists on the date ', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)

    ###################################################
    ##################Admin_route#####################

    def Route_Search(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        key = self.comboBox_5.currentText()
        feature = self.lineEdit_20.text()
        if feature:
            id = int(feature)
            id1= tuple([id])
        self.lineEdit_20.setText('')
        if key == 'ALL':
            try:
                self.cur.callproc('Route_search')

                self.tableWidget_7.setRowCount(0)
                self.tableWidget_7.insertRow(0)

                for row, form in enumerate(self.cur.stored_results()):
                    #print(row) gives the no of iterates
                    #print(form) gives point of data at
                    for row2, item in enumerate(form):
                        #print (row2) gives the row count
                        # print(item) gives the its start tuple
                        for col, item1 in enumerate(item):
                            #print(col) gives the col count
                            #print(items1) gives the items one ny one
                            self.tableWidget_7.setItem(row2, col, QTableWidgetItem(str(item1)))
                            col += 1

                        rowPos = self.tableWidget_7.rowCount()
                        self.tableWidget_7.insertRow(rowPos)

            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        elif key =='Route ID':
            try:
                self.cur.execute('''select route_id from route''')
                sData = self.cur.fetchall()
                if id1 in sData:
                    self.cur.callproc('Route', [feature, ])
                    self.tableWidget_7.setRowCount(0)
                    self.tableWidget_7.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        #print(row) gives the no of iterates
                        #print(form) gives point of data at
                        for row2, item in enumerate(form):
                            #print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                #print(col) gives the col count
                                #print(items1) gives the items one ny one
                                self.tableWidget_7.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_7.rowCount()
                            self.tableWidget_7.insertRow(rowPos)
                else:
                    self.tableWidget_7.setRowCount(0)
                    self.tableWidget_7.insertRow(0)
                    self.statusBar().showMessage('ID does not Exists', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        else:
            try:
                self.cur.execute('''select airline_id from airline''')
                sData = self.cur.fetchall()
                if id1 in sData:
                    self.cur.callproc('Aroute', [feature, ])
                    self.tableWidget_7.setRowCount(0)
                    self.tableWidget_7.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        #print(row) gives the no of iterates
                        #print(form) gives point of data at
                        for row2, item in enumerate(form):
                            #print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                #print(col) gives the col count
                                #print(items1) gives the items one ny one
                                self.tableWidget_7.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_7.rowCount()
                            self.tableWidget_7.insertRow(rowPos)
                else:
                    self.tableWidget_7.setRowCount(0)
                    self.tableWidget_7.insertRow(0)
                    self.statusBar().showMessage('ID does not Exists', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)

    def Route_add(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        from_place = self.lineEdit_22.text()
        to_place = self.lineEdit_11.text()
        airline_id = self.lineEdit_23.text()
        economy = self.lineEdit_21.text()
        business = self.lineEdit_24.text()
        self.lineEdit_22.setText('')
        self.lineEdit_11.setText('')
        self.lineEdit_23.setText('')
        self.lineEdit_21.setText('')
        self.lineEdit_24.setText('')
        id2 = int(airline_id)
        id1 = tuple([id2])
        try:
            self.cur.execute('''select airline_id from airline ''')
            Data = self.cur.fetchall()
            if id1 in Data:
                self.cur.execute('''select airline_id, rfrom, rto  from route ''')
                Data1 = self.cur.fetchall()
                if (id2, from_place, to_place) not in Data1:
                    self.cur.execute('''insert into route (rfrom,rto,economy_cost,business_cost,airline_id) values (%s,%s, %s, %s, %s)
                    ''', (from_place, to_place, economy, business, airline_id))
                    self.db.commit()
                    self.statusBar().showMessage('Route Added', 3000)
                else:
                    self.statusBar().showMessage('Route Already Exists', 3000)
            else:
                self.statusBar().showMessage('Airline_ID does not exist in Airline', 3000)
        except:
            self.statusBar().showMessage('Route not added Wrong data', 3000)

    def Route_remove(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        route_id = self.lineEdit_23.text()
        if route_id:
            id2 = int(route_id)
            id1 = tuple([id2])
        self.lineEdit_23.setText('')
        try:
            self.cur.execute('''select route_id from route''')
            sData = self.cur.fetchall()
            if id1 in sData:
                self.cur.execute(''' DELETE FROM route WHERE route_id = %s ''', (route_id,))
                self.db.commit()
                self.statusBar().showMessage('Deleted Successfully', 3000)
            else:
                self.statusBar().showMessage('Id does not exist', 3000)
        except:
            self.statusBar().showMessage('Not Deleted  or Enter Credentials', 3000)

    ###################################################
    ##################Admin_User#####################

    def User_Search(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        key = self.comboBox_6.currentText()
        feature = self.lineEdit_25.text()
        self.lineEdit_25.setText('')
        if key == 'ALL':
            try:
                self.cur.callproc('alluser')

                self.tableWidget_8.setRowCount(0)
                self.tableWidget_8.insertRow(0)

                for row, form in enumerate(self.cur.stored_results()):
                    # print(row) gives the no of iterates
                    # print(form) gives point of data at
                    for row2, item in enumerate(form):
                        # print (row2) gives the row count
                        # print(item) gives the its start tuple
                        for col, item1 in enumerate(item):
                            # print(col) gives the col count
                            # print(items1) gives the items one ny one
                            self.tableWidget_8.setItem(row2, col, QTableWidgetItem(str(item1)))
                            col += 1

                        rowPos = self.tableWidget_8.rowCount()
                        self.tableWidget_8.insertRow(rowPos)

            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        elif key == 'User ID':
            try:
                self.cur.execute('''select user_id from user''')
                sData = self.cur.fetchall()
                id = int(feature)
                id1 = tuple([id])
                if id1 in sData:
                    self.cur.callproc('userid', [feature, ])
                    self.tableWidget_8.setRowCount(0)
                    self.tableWidget_8.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        # print(row) gives the no of iterates
                        # print(form) gives point of data at
                        for row2, item in enumerate(form):
                            # print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                # print(col) gives the col count
                                # print(items1) gives the items one ny one
                                self.tableWidget_8.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_8.rowCount()
                            self.tableWidget_8.insertRow(rowPos)
                else:
                    self.tableWidget_8.setRowCount(0)
                    self.tableWidget_8.insertRow(0)
                    self.statusBar().showMessage('ID does not Exists', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        else:
            try:
                self.cur.execute('''select user_name from user''')
                sData = self.cur.fetchall()
                name = (feature,)
                if name in sData:
                    self.cur.callproc('usern', [feature, ])
                    self.tableWidget_8.setRowCount(0)
                    self.tableWidget_8.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        # print(row) gives the no of iterates
                        # print(form) gives point of data at
                        for row2, item in enumerate(form):
                            # print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                # print(col) gives the col count
                                # print(items1) gives the items one ny one
                                self.tableWidget_8.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_8.rowCount()
                            self.tableWidget_8.insertRow(rowPos)
                else:
                    self.tableWidget_8.setRowCount(0)
                    self.tableWidget_8.insertRow(0)
                    self.statusBar().showMessage('USER Name does not Exists', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)

    def User_add(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        name = self.lineEdit_65.text()
        phone = self.lineEdit_67.text()
        mail = self.lineEdit_66.text()
        address = self.lineEdit_68.text()
        age = int(self.lineEdit_63.text())
        gender = self.lineEdit_69.text()
        password = self.lineEdit_94.text()
        self.lineEdit_65.setText('')
        self.lineEdit_67.setText('')
        self.lineEdit_66.setText('')
        self.lineEdit_68.setText('')
        self.lineEdit_63.setText('')
        self.lineEdit_69.setText('')
        self.lineEdit_94.setText('')
        gen = ['male', 'female', 'others', 'Male', 'Female', 'Others']
        valid = 0
        if '@' in mail and '.' in mail:
            j = mail.index('@')
            k = mail.index('.')
            if j > k:
                if '.' in mail[j:]:
                    m = mail[j:].index('.')
                    m = m + j
                    if mail[m + 1:] == 'com' or mail[m + 1:] == 'ac.in' or mail[m + 1:] == 'in':
                        valid = 1
                    else:
                        valid = 0
                else:
                    valid = 0
            elif j < k:
                m = mail[j:].index('.')
                m = m + j
                if mail[m + 1:] == 'com' or mail[m + 1:] == 'ac.in':
                    valid = 1
                else:
                    valid = 0
        else:
            valid = 0
        try:
            if gender in gen:
                if 18 < age < 112:
                    if valid == 1:
                        if len(password) > 4:
                            self.cur.execute(
                                '''insert into user (user_name,phone,email,Address,age,gender,passward) values (%s,%s,%s,%s,%s,%s,%s);''',
                                (name, phone, mail, address, age, gender, password))
                            self.db.commit()
                            self.statusBar().showMessage('User Added', 3000)
                        else:
                            self.statusBar().showMessage('Give password of length > 4', 3000)
                    else:
                        self.statusBar().showMessage('Invalid email', 3000)
                else:
                    self.statusBar().showMessage('age not valid (between 18 and 100) ', 3000)
            else:
                self.statusBar().showMessage('Gender invalid', 3000)
        except:
            self.statusBar().showMessage('User with Same Name exists', 3000)

    def User_remove(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        user_id = self.lineEdit_64.text()
        id2 = int(user_id)
        id1 = tuple([id2])
        self.lineEdit_64.setText('')
        try:
            self.cur.execute('''select user_id from user''')
            sData = self.cur.fetchall()
            if id1 in sData:
                self.cur.execute(''' DELETE FROM user WHERE user_id = %s ''', (id2,))
                self.db.commit()
                self.statusBar().showMessage('Deleted User Successfully', 3000)
            else:
                self.statusBar().showMessage('Id does not exist in User', 3000)
        except:
            self.statusBar().showMessage('Not Deleted ', 3000)

    ############################################################
    ######################Admin_admin##########################

    def Admin_add(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        admin_name = self.lineEdit_72.text()
        admin_password = self.lineEdit_75.text()
        admin_confirm = self.lineEdit_71.text()
        self.lineEdit_72.setText('')
        self.lineEdit_75.setText('')
        self.lineEdit_71.setText('')
        try:
            if admin_password == admin_confirm:
                if len(admin_password) > 4:
                    self.cur.execute('''
                                INSERT INTO admin (admin_name, admin_password) VALUE (%s,%s)
                            ''', (admin_name, admin_password))
                    self.db.commit()
                    self.statusBar().showMessage('Added Admin Successfully', 3000)
                else:
                    self.statusBar().showMessage('Give password of length > 4', 3000)
            else:
                self.statusBar().showMessage('Password does not match', 3000)
        except:
            self.statusBar().showMessage('Admin with same name exists ', 3000)

    def Admin_delete(self):
        admin_name = self.lineEdit_77.text()
        admin_password = self.lineEdit_82.text()
        if admin_name:
            name = (admin_name,)
        self.lineEdit_77.setText('')
        self.lineEdit_82.setText('')
        try:
            self.cur.execute('''select admin_name from admin''')
            sData = self.cur.fetchall()
            if name in sData:
                self.cur.execute('''select admin_password from admin where admin_name = %s''', (admin_name,))
                Data = self.cur.fetchall()
                if (admin_password,) in Data:
                    self.cur.execute('''delete from admin where admin_password =%s and admin_name =%s
                    ''', (admin_password, admin_name,))
                    self.db.commit()
                    self.statusBar().showMessage('Deleted Admin password Successfully', 3000)
                else:
                    self.statusBar().showMessage('Password authentication error', 3000)
            else:
                self.statusBar().showMessage('Admin does not exist', 3000)
        except:
            self.statusBar().showMessage('Admin not Deleted ', 3000)

    def Admin_details(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        key = self.comboBox_15.currentText()
        feature = self.lineEdit_70.text()
        self.lineEdit_70.setText('')
        if key == 'ALL':
            try:
                self.cur.callproc('alladmin')

                self.tableWidget_19.setRowCount(0)
                self.tableWidget_19.insertRow(0)

                for row, form in enumerate(self.cur.stored_results()):
                    # print(row) gives the no of iterates
                    # print(form) gives point of data at
                    for row2, item in enumerate(form):
                        # print (row2) gives the row count
                        # print(item) gives the its start tuple
                        for col, item1 in enumerate(item):
                            # print(col) gives the col count
                            # print(items1) gives the items one ny one
                            self.tableWidget_19.setItem(row2, col, QTableWidgetItem(str(item1)))
                            col += 1

                        rowPos = self.tableWidget_19.rowCount()
                        self.tableWidget_19.insertRow(rowPos)

            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        elif key == 'Admin ID':
            try:
                self.cur.execute('''select admin_id from admin''')
                sData = self.cur.fetchall()
                id = int(feature)
                id1 = tuple([id])
                if id1 in sData:
                    self.cur.callproc('adminid', [feature, ])
                    self.tableWidget_19.setRowCount(0)
                    self.tableWidget_19.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        # print(row) gives the no of iterates
                        # print(form) gives point of data at
                        for row2, item in enumerate(form):
                            # print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                # print(col) gives the col count
                                # print(items1) gives the items one ny one
                                self.tableWidget_19.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_19.rowCount()
                            self.tableWidget_19.insertRow(rowPos)
                else:
                    self.tableWidget_19.setRowCount(0)
                    self.tableWidget_19.insertRow(0)
                    self.statusBar().showMessage('ID does not Exists', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)
        else:
            try:
                self.cur.execute('''select admin_name from admin''')
                sData = self.cur.fetchall()
                name = (feature,)
                if name in sData:
                    self.cur.callproc('adminn', [feature, ])
                    self.tableWidget_19.setRowCount(0)
                    self.tableWidget_19.insertRow(0)

                    for row, form in enumerate(self.cur.stored_results()):
                        # print(row) gives the no of iterates
                        # print(form) gives point of data at
                        for row2, item in enumerate(form):
                            # print (row2) gives the row count
                            # print(item) gives the its start tuple
                            for col, item1 in enumerate(item):
                                # print(col) gives the col count
                                # print(items1) gives the items one ny one
                                self.tableWidget_19.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_19.rowCount()
                            self.tableWidget_19.insertRow(rowPos)
                else:
                    self.tableWidget_19.setRowCount(0)
                    self.tableWidget_19.insertRow(0)
                    self.statusBar().showMessage('admin Name does not Exists', 3000)
            except:
                self.statusBar().showMessage('Error Displaying', 3000)

    def Admin_Update(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        admin_name = self.lineEdit_76.text()
        admin_password = self.lineEdit_73.text()
        admin_new_password = self.lineEdit_74.text()
        name = (admin_name,)
        self.lineEdit_76.setText('')
        self.lineEdit_73.setText('')
        self.lineEdit_74.setText('')
        try:
            self.cur.execute('''select admin_name from admin''')
            sData = self.cur.fetchall()
            if name in sData:
                self.cur.execute('''select admin_password from admin where admin_name = %s''', (admin_name,))
                Data = self.cur.fetchall()
                if (admin_password,) in Data:
                    if admin_password != admin_new_password:
                        if len(admin_new_password) > 4:
                            self.cur.execute('''UPDATE admin SET admin_password =%s WHERE admin_name =%s
                            ''', (admin_new_password, admin_name,))
                            self.db.commit()
                            self.statusBar().showMessage('Updated Admin password Successfully', 3000)
                        else:
                            self.statusBar().showMessage('Give password of length > 4', 3000)
                    else:
                        self.statusBar().showMessage('Password are same no change', 3000)
                else:
                    self.statusBar().showMessage('Password authentication error', 3000)
            else:
                self.statusBar().showMessage('Admin does not exist', 3000)
        except:
            self.statusBar().showMessage('Password not updated ', 3000)

    ###################################################
    ##################User_route#####################

    def User_Route_Search(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        from_key = self.comboBox_16.currentText()
        to_key = self.comboBox_17.currentText()
        try:
            self.cur.execute('''select  rfrom from route''')
            fData = self.cur.fetchall()
            self.cur.execute('''select  rto from  route''')
            tData = self.cur.fetchall()
            self.comboBox_16.clear()
            self.comboBox_16.addItem('--From--')
            self.comboBox_17.clear()
            self.comboBox_17.addItem('--To--')
            ls=[]
            ls1=[]
            for i in fData:
                ls.append(i)
            for i in tData:
                ls1.append(i)
            ls2 = set(ls)
            ls3 = set(ls1)
            for i in ls2:
                self.comboBox_16.addItem(i[0])
            for i in ls3:
                self.comboBox_17.addItem(i[0])
        except:
            self.statusBar().showMessage('Unable to set end station combobox')
        try:
            if from_key != '--From--' and to_key != '--To--':
                if from_key != to_key:
                    self.cur.execute('''select r.route_id, r.rfrom, r.rto, r.economy_cost, r.business_cost, r.airline_id,c.economy_count, c.business_count from route r, count c where rfrom =%s and rto = %s and r.airline_id = c.airline_id'''
                                     ,(from_key, to_key))
                    form1 = self.cur.fetchall()
                    if form1:
                        self.tableWidget_20.setRowCount(0)
                        self.tableWidget_20.insertRow(0)
                        ls =[]
                        for row2, item in enumerate(form1):
                            # print (row2) #gives the row count
                            # print(item) #gives the its start tuple
                            for col, item1 in enumerate(item):
                                # print(col) #gives the col count
                                # print(items1) #gives the items one ny one

                                    self.tableWidget_20.setItem(row2, col, QTableWidgetItem(str(item1)))
                                    col += 1

                            rowPos = self.tableWidget_20.rowCount()
                            self.tableWidget_20.insertRow(rowPos)
                    else:
                        self.tableWidget_20.setRowCount(0)
                        self.tableWidget_20.insertRow(0)
                        self.statusBar().showMessage('No flight on this route', 3000)
                else:
                    self.tableWidget_20.setRowCount(0)
                    self.tableWidget_20.insertRow(0)
                    self.statusBar().showMessage('From and to are same', 3000)
            else:
                self.tableWidget_20.setRowCount(0)
                self.tableWidget_20.insertRow(0)
                self.statusBar().showMessage('route credentials not proper', 3000)
        except:
            self.tableWidget_20.setRowCount(0)
            self.tableWidget_20.insertRow(0)
            self.statusBar().showMessage('Wrong Credentials', 3000)

    ###################################################
    ##################User_Booking#####################

    def User_Booking(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        name = self.lineEdit_101.text()
        global nam
        config.nam = name
        print(config.nam)
        date = self.dateEdit.dateTime()
        print(date)
        date6 = str(date).split('.') #concert tostring and split the pt statement
        print(date6)
        date1 = date6[2].split('(') #select the input in () and split the into 3
        print(date1)
        date2 = date1[1].split(',') #now split the data to y, m, d)
        print(date2)
        date3 = date2[2].split(')') #now d) to d
        print(date3)
        if int(date2[1]) < 10 or int(date3[0]) < 10:
            if int(date2[1]) < 10:
                date12 = '0' + date2[1]
                date12 = date12.replace(" ", "")
                print(date12)
            if int(date3[0]) < 10:
                date30 = '0' + date3[0]
                date30 = date30.replace(" ", "")

            date4 = date2[0] + date12 + date30  # add y m d
            date7 = date2[0] + '-' + date12 + '-' + date30
        else:
            date4 = date2[0] + date2[1] + date3[0]  # add y m d
            date7 = date2[0] + '-' + date2[1] + '-' + date3[0]  # add y m d
        print(date4)
        date5 = date4.replace(" ", "")  # ymd removing spaces
        date8 = date7.replace(" ", "-")  # ymd removing spaces
        print(date5)
        global dt
        config.dt = date5
        seats = self.comboBox_8.currentText()
        route_id = self.lineEdit_86.text()
        global rti
        config.rti =  route_id
        seat_type = self.comboBox_18.currentText()
        card_name = self.lineEdit_78.text()
        card_no = self.lineEdit_81.text()
        global cno
        config.cno =  card_no

        try:
            if seats:
                self.cur.execute('''select route_id from route''')
                sData = self.cur.fetchall()
                print(sData)
                id = int(route_id)
                print('1')
                id2 = tuple([id])
                if id2 in sData:
                    print('2')
                    if len(card_no) <= 16:
                        print('3',date5)
                        if date5 >= '20210201' and date5 <= '20211229':
                            print('4')
                            print('6')
                            print(date5)
                            self.cur.execute(''' Insert INTO booking (booking_date, booking_user_name, route_id, seat_type, card_name,card_no,count) value (%s, %s, %s, %s, %s,%s,%s) '''
                                             , (date5, name, route_id, seat_type, card_name, card_no, seats))
                            self.db.commit()
                            print('7')
                            print('9')
                            self.statusBar().showMessage('booking details saved add passenger details and confirm booking', 10000)
                            self.lineEdit_111.setText('')
                            self.lineEdit_101.setText('')
                            self.lineEdit_86.setText('')
                            self.lineEdit_78.setText('')
                            self.lineEdit_81.setText('')
                            if seats == '1':
                                self.tabWidget_3.setCurrentIndex(4)
                            elif seats == '2':
                                self.tabWidget_3.setCurrentIndex(5)
                            else:
                                self.tabWidget_3.setCurrentIndex(6)
                        else:
                            self.statusBar().showMessage("Can't book tickets one year from now (2020-12-29)  ", 3000)
                    else:
                        self.statusBar().showMessage('Enter a valid Card No with 16 digit ', 3000)
                else:
                    self.statusBar().showMessage('Route_id does not match', 3000)

        except:
            self.statusBar().showMessage('Booking rejected Wrong data entries', 3000)
            self.lineEdit_101.setText('')
            self.lineEdit_86.setText('')
            self.lineEdit_78.setText('')
            self.lineEdit_81.setText('')

    def fun1(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()
        print('hifun1')
        name1 = self.lineEdit_107.text()
        gender1 = self.lineEdit_108.text()
        age1 = self.lineEdit_83.text()
        self.lineEdit_107.setText('')
        self.lineEdit_108.setText('')
        self.lineEdit_83.setText('')
        try:
            print('hi2')
            print(config.rti)
            self.cur.execute(
                ''' select booking_id from booking where route_id =%s and booking_user_name = %s and card_no = %s and booking_date= %s ''',
                (config.rti, config.nam, config.cno, config.dt))
            Data = self.cur.fetchall()
            id3 = Data[0]
            id4 = id3[0]
            print(id4)
            print('811')
            self.cur.execute(
                '''Insert INTO passenger (passenger_name,passenger_gender, age, booking_Id, travel_date) values (%s,%s,%s,%s,%s)'''
                , (name1, gender1, age1, id4, config.dt))
            self.db.commit()
            self.statusBar().showMessage("Booking successful and Confirmed and payment received with %18 GST  ", 5000)
            self.tabWidget_3.setCurrentIndex(1)
        except:
            self.statusBar().showMessage("Booking unsuccessful  ", 5000)

    def fun2(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()
        print('hifun2')
        name21 = self.lineEdit_111.text()
        gender21 = self.lineEdit_110.text()
        age21 = self.lineEdit_109.text()
        name22 = self.lineEdit_114.text()
        gender22 = self.lineEdit_113.text()
        age22 = self.lineEdit_112.text()
        self.lineEdit_111.setText('')
        self.lineEdit_110.setText('')
        self.lineEdit_109.setText('')
        self.lineEdit_114.setText('')
        self.lineEdit_113.setText('')
        self.lineEdit_112.setText('')
        try:
            print('hi2')
            print(config.rti)
            self.cur.execute(
                ''' select booking_id from booking where route_id =%s and booking_user_name = %s and card_no = %s and booking_date= %s ''',
                (config.rti, config.nam, config.cno, config.dt))
            Data = self.cur.fetchall()
            id3 = Data[0]
            id4 = id3[0]
            print(id4)
            print('811')
            print('1')
            self.cur.execute(
                '''Insert INTO passenger (passenger_name,passenger_gender, age, booking_Id, travel_date) values (%s,%s,%s,%s,%s)'''
                , (name21, gender21, age21, id4, config.dt))
            print('2')
            self.cur.execute(
                '''Insert INTO passenger (passenger_name,passenger_gender, age, booking_Id, travel_date) values (%s,%s,%s,%s,%s)'''
                , (name22, gender22, age22, id4, config.dt))
            self.db.commit()
            self.statusBar().showMessage("Booking successful and Confirmed and payment received with %18 GST  ", 5000)
            self.tabWidget_3.setCurrentIndex(1)
        except:
            self.statusBar().showMessage("Booking unsuccessful  ", 5000)

    def fun3(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()
        print('hifun2')
        name31 = self.lineEdit_117.text()
        gender31 = self.lineEdit_116.text()
        age31 = self.lineEdit_115.text()
        name32 = self.lineEdit_120.text()
        gender32 = self.lineEdit_118.text()
        age32 = self.lineEdit_119.text()
        name33 = self.lineEdit_123.text()
        gender33 = self.lineEdit_121.text()
        age33 = self.lineEdit_122.text()
        self.tabWidget_3.setCurrentIndex(1)
        self.lineEdit_117.setText('')
        self.lineEdit_116.setText('')
        self.lineEdit_115.setText('')
        self.lineEdit_120.setText('')
        self.lineEdit_118.setText('')
        self.lineEdit_119.setText('')
        self.lineEdit_123.setText('')
        self.lineEdit_121.setText('')
        self.lineEdit_122.setText('')
        try:
            print('hi2')
            print(config.rti)
            self.cur.execute(
                ''' select booking_id from booking where route_id =%s and booking_user_name = %s and card_no = %s and booking_date= %s ''',
                (config.rti, config.nam, config.cno, config.dt))
            Data = self.cur.fetchall()
            id3 = Data[0]
            id4 = id3[0]
            print(id4)
            print('811')
            print('1')
            self.cur.execute(
                '''Insert INTO passenger (passenger_name,passenger_gender, age, booking_Id, travel_date) values (%s,%s,%s,%s,%s)'''
                , (name31, gender31, age31, id4, config.dt))
            self.db.commit()
            print('2')
            self.cur.execute(
                '''Insert INTO passenger (passenger_name,passenger_gender, age, booking_Id, travel_date) values (%s,%s,%s,%s,%s)'''
                , (name32, gender32, age32, id4, config.dt))
            self.db.commit()
            print('3')
            self.cur.execute(
                '''Insert INTO passenger (passenger_name,passenger_gender, age, booking_Id, travel_date) values (%s,%s,%s,%s,%s)'''
                , (name33, gender33, age33, id4, config.dt))
            self.db.commit()
            self.statusBar().showMessage("Booking successful and Confirmed and payment received with %18 GST  ", 5000)
            self.tabWidget_3.setCurrentIndex(1)
        except:
            self.statusBar().showMessage("Booking unsuccessful  ", 5000)


    def User_Cancel_Booking(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        name = self.lineEdit_103.text()
        date = self.dateEdit_2.dateTime()
        card_no = self.lineEdit_102.text()
        self.lineEdit_103.setText('')
        self.lineEdit_102.setText('')
        print(date)
        date6 = str(date).split('.')  # concert tostring and split the pt statement
        print(date6)
        date1 = date6[2].split('(')  # select the input in () and split the into 3
        print(date1)
        date2 = date1[1].split(',')  # now split the data to y, m, d)
        print(date2)
        date3 = date2[2].split(')')  # now d) to d
        print(date3)
        if int(date2[1]) < 10 or int(date3[0]) < 10:
            if int(date2[1]) < 10:
                date12 = ' 0' + date2[1]
                date12 = date12.replace(" ", "")
                print(date12)
            if int(date3[0]) < 10:
                date30 = ' 0' + date3[0]
                date30 = date30.replace(" ", "")
            date7 = date2[0] + date12 +  date30
            date4 = date2[0] +'-'+date12 +'-'+ date30  # add y m d
            print(date4)
        else:
            date4 = date2[0] +'-' +date2[1] +'-'+date3[0]  # add y m d
            date7 = date2[0] + date2[1] + date3[0]
        print(date4)
        date5 = date4.replace(" ", "-")  # ymd removing spaces
        date8 = date7.replace(" ", "")
        print(date5, date8)
        try:
            if date8 >= '20210201':
                print(date5,name,card_no)
                self.cur.execute('''select * from booking where booking_date = %s and booking_user_name= %s and card_no = %s '''
                                 ,(date5, name, card_no))
                Data = self.cur.fetchall()
                print(Data)
                if Data:
                    print('hi')
                    self.cur.execute('''delete from booking where booking_date = %s and booking_user_name= %s and card_no = %s '''
                                 ,(date8, name, card_no))
                    self.db.commit()
                    self.statusBar().showMessage('Booking Cancelled ',3000)
                else:
                    self.statusBar().showMessage('Booking already cancelled or does not exist ',3000)
            else:
                self.statusBar().showMessage('Booking before current date 29th dec 2020 can not be cancelled  ',5000)
        except:
            self.statusBar().showMessage('Details error can not delete booking',3000)



    ###################################################
    ##################User_Ticket#####################

    def User_generate(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        name = self.lineEdit_105.text()
        date = self.dateEdit_3.dateTime()
        card_no = self.lineEdit_104.text()
        self.lineEdit_105.setText('')
        self.lineEdit_104.setText('')
        print(date)
        date6 = str(date).split('.')  # concert tostring and split the pt statement
        print(date6)
        date1 = date6[2].split('(')  # select the input in () and split the into 3
        print(date1)
        date2 = date1[1].split(',')  # now split the data to y, m, d)
        print(date2)
        date3 = date2[2].split(')')  # now d) to d
        print(date3)
        if int(date2[1]) < 10 or int(date3[0]) < 10:
            if int(date2[1]) < 10:
                date12 = ' 0' + date2[1]
                date12 = date12.replace(" ", "")
                print(date12)
            if int(date3[0]) < 10:
                date30 = ' 0' + date3[0]
                date30 = date30.replace(" ", "")
            date7 = date2[0] + date12 +  date30
            date4 = date2[0] +'-'+date12 +'-'+ date30  # add y m d
            print(date4)
        else:
            date4 = date2[0] +'-' +date2[1] +'-'+date3[0]  # add y m d
            date7 = date2[0] + date2[1] + date3[0]
        print(date4)
        date5 = date4.replace(" ", "-")  # ymd removing spaces
        date8 = date7.replace(" ", "")
        print(date5, date8)
        try:
            if date8 >= '20210201':
                print(date5,name,card_no)
                self.cur.execute('''select * from booking where booking_date = %s and booking_user_name= %s and card_no = %s '''
                                 ,(date5, name, card_no))
                Data = self.cur.fetchall()
                print(Data)
                if Data:
                    print('hi')
                    self.cur.execute('''select B.booking_id, B.booking_user_name, A.airline_name, R.rfrom, R.rto,A.airline_arrival, A.airline_departure, B.seat_type, P.Total_cost from booking B ,route R, payment P, airline A where B.booking_id = P.booking_id and B.route_id = R.route_id and R.airline_id = A.airline_id and B.booking_user_name = %s and B.card_no = %s and B.booking_date= %s '''
                                 ,(name, card_no, date5))
                    tick = self.cur.fetchall()
                    print(tick)
                    self.db.commit()
                    if tick:
                        self.tableWidget_2.setRowCount(0)
                        self.tableWidget_2.insertRow(0)

                        for row2, item in enumerate(tick):
                            # print (row2) #gives the row count
                            # print(item) #gives the its start tuple
                            for col, item1 in enumerate(item):
                                # print(col) #gives the col count
                                # print(items1) #gives the items one ny one
                                self.tableWidget_2.setItem(row2, col, QTableWidgetItem(str(item1)))
                                col += 1

                            rowPos = self.tableWidget_2.rowCount()
                            self.tableWidget_2.insertRow(rowPos)
                    self.statusBar().showMessage('Ticket Generated',3000)
                else:
                    self.statusBar().showMessage('Booking does not exist ',3000)
            else:
                self.statusBar().showMessage('Tickets before current date 29th dec 2020 can not  be generated  ',3000)
        except:
            self.statusBar().showMessage('Details error can not Generate Ticket',3000)

    ###################################################
    ##################User_Setting#####################

    def User_details(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()
        name = self.lineEdit_79.text()
        key = self.comboBox_2.currentText()
        value = self.lineEdit_87.text()
        password = self.lineEdit_85.text()
        self.lineEdit_79.setText('')
        self.lineEdit_85.setText('')
        self.lineEdit_87.setText('')
        try:
            self.cur.execute('''select user_name from user''')
            sData = self.cur.fetchall()
            if (name,) in sData:
                self.cur.execute('''select passward from user where user_name = %s
                ''', (name,))
                Data = self.cur.fetchall()
                if (password,) in Data:
                    if key == 'age':
                        self.cur.execute('''UPDATE user SET age = %s WHERE user_name = %s
                                                ''', (value, name))
                    elif key == 'phone':
                        self.cur.execute('''UPDATE user SET key = %s WHERE user_name = %s
                                                ''', (value, name))
                    elif key == 'address':
                        self.cur.execute('''UPDATE user SET Address = %s WHERE user_name = %s
                                                ''', (value, name))
                    elif key == 'gender':
                        self.cur.execute('''UPDATE user SET gender = %s WHERE user_name = %s
                                                ''', (value, name))
                    self.db.commit()
                    self.statusBar().showMessage('Updated User details Successfully', 3000)
                else:
                    self.statusBar().showMessage('Password authentication error', 3000)
            else:
                self.statusBar().showMessage('User does not exist', 3000)
        except:
            self.statusBar().showMessage('Details not updated', 3000)

    def User_password(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()
        name1 = self.lineEdit_97.text()
        password = self.lineEdit_98.text()
        new_password = self.lineEdit_99.text()
        name = (name1,)
        self.lineEdit_97.setText('')
        self.lineEdit_98.setText('')
        self.lineEdit_99.setText('')
        try:
            self.cur.execute('''select email from user''')
            sData = self.cur.fetchall()
            if name in sData:
                self.cur.execute('''select passward from user where email = %s''', (name1,))
                Data = self.cur.fetchall()
                if (password,) in Data:
                    if password != new_password:
                        if len(new_password) > 4:
                            self.cur.execute('''UPDATE user SET passward =%s WHERE email =%s
                            ''', (new_password, name1,))
                            self.db.commit()
                            self.statusBar().showMessage('Updated user password Successfully', 3000)
                        else:
                            self.statusBar().showMessage('Give password of length > 4', 3000)
                    else:
                        self.statusBar().showMessage('Password are same no change', 3000)
                else:
                    self.statusBar().showMessage('Password authentication error', 3000)
            else:
                self.statusBar().showMessage('user does not exist', 3000)
        except:
            self.statusBar().showMessage('Password not updated ', 3000)

    ###################################################
    ##################New_User#####################

    def Welcome_User_details(self):
        self.db = mysql.connector.connect(host='localhost', user='root', passwd="password", db="airline")
        self.cur = self.db.cursor()

        name = self.lineEdit_89.text()
        phone = self.lineEdit_93.text()
        mail = self.lineEdit_92.text()
        address = self.lineEdit_90.text()
        age = int(self.lineEdit_88.text())
        gender = self.lineEdit_91.text()
        password = self.lineEdit_95.text()
        confirm_password = self.lineEdit_96.text()
        self.lineEdit_89.setText('')
        self.lineEdit_93.setText('')
        self.lineEdit_92.setText('')
        self.lineEdit_90.setText('')
        self.lineEdit_88.setText('')
        self.lineEdit_91.setText('')
        self.lineEdit_95.setText('')
        self.lineEdit_96.setText('')
        gen = ['male', 'female', 'others', 'Male', 'Female', 'Others']
        valid = 0
        if password == confirm_password:
            if '@' in mail and '.' in mail:
                j = mail.index('@')
                k = mail.index('.')
                if j > k:
                    if '.' in mail[j:]:
                        m = mail[j:].index('.')
                        m = m + j
                        if mail[m + 1:] == 'com' or mail[m + 1:] == 'ac.in' or mail[m + 1:] == 'in':
                            valid = 1
                        else:
                            valid = 0
                    else:
                        valid = 0
                elif j < k:
                    m = mail[j:].index('.')
                    m = m + j
                    if mail[m + 1:] == 'com' or mail[m + 1:] == 'ac.in':
                        valid = 1
                    else:
                        valid = 0
            else:
                valid = 0
            try:
                if gender in gen:
                    if 18 < age < 112:
                        if valid == 1:
                            if len(password) > 4:
                                self.cur.execute(
                                    '''insert into user (user_name,phone,email,Address,age,gender,passward) values (%s,%s,%s,%s,%s,%s,%s);''',
                                    (name, phone, mail, address, age, gender, password))
                                self.db.commit()
                                self.statusBar().showMessage('User Added', 3000)
                            else:
                                self.statusBar().showMessage('Give password of length > 4', 3000)
                        else:
                            self.statusBar().showMessage('Invalid email', 3000)
                    else:
                        self.statusBar().showMessage('age not valid (between 18 and 100) ', 3000)
                else:
                    self.statusBar().showMessage('Gender invalid', 3000)
            except:
                self.statusBar().showMessage('User with Same Name exists', 3000)
        else:
            self.statusBar().showMessage('Password does not match', 3000)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
