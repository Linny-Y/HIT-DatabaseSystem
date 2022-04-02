# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'administrator.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

import sys
import pymysql


class Ui_administrator(object):
    def connect(self):
        con = pymysql.connect(host= 'localhost', port= 3306, charset='utf8',
                            user= 'root', password= '1234567890', 
                            database= 'teaching_management_system')
        return con
    def studentInsert(self):
        con = self.connect()
        cur = con.cursor()
        sno,sname,classno,sage,ssex = self.lineEdit_sno.text(),self.lineEdit_sname.text(),self.lineEdit_cno.text(),self.lineEdit_sage.text(),self.comboBox_sex.currentText()
        if not sno or not sname or not classno or not sage:
            QMessageBox.warning(self, '警告', '不能为空')
        elif not cur.execute('select * from class where cno=%s',[classno]):
            QMessageBox.warning(self, '警告', '班级不存在')
        elif cur.execute('select * from student where sno=%s',[sno]):
            QMessageBox.warning(self, '警告', '该学生已存在')
        else:
            cur.execute("insert into student VALUES(%s,%s,%s,%s,%s)",[sno,sname,ssex,classno,sage])
            con.commit()
            QMessageBox.information(self, '成功', '学生信息已录入')
        self.lineEdit_sname.clear()

        
    def studentDelete(self):
        con = self.connect()
        cur = con.cursor()
        sno = self.lineEdit_sno.text()
        if not sno :
            QMessageBox.warning(self, '警告', '不能为空')
        elif not cur.execute('select * from student where sno=%s',[sno]):
            QMessageBox.warning(self, '警告', '该学生不存在')
        else:
            cur.execute("delete from student where sno=%s",[sno])
            con.commit()
            QMessageBox.information(self, '成功', '学生信息已删除')

    def InsertSchedule(self):
        con = self.connect()
        cur = con.cursor()
        courseno,teacherno = self.lineEdit_courseno.text(),self.lineEdit_tno.text()
        year,semester = self.comboBox_year.currentText(),self.comboBox_semester.currentText()
        if not courseno or not teacherno:
            QMessageBox.warning(self, '警告', '不能为空')
        elif not cur.execute('select * from course where course.courseno=%s',[courseno]):
            QMessageBox.warning(self, '警告', '该课程不存在')
        elif not cur.execute('select * from teacher where teacher.tno=%s',[teacherno]):
            QMessageBox.warning(self, '警告', '该教师不存在')
        elif cur.execute('select * from schedule where schedule.teacherno=%s and schedule.courseno=%s and schedule.year=%s and schedule.semester=%s',[teacherno,courseno,year,semester]):
            QMessageBox.warning(self, '警告', '该排课已存在')
        else:
            cur.execute('insert into schedule values(%s,NULL,%s,%s,%s)',[courseno,teacherno,year,semester])
            con.commit()
            QMessageBox.information(self, '成功', '排课信息已录入')



    def course2student(self):
        con = self.connect()
        cur = con.cursor()
        coursename = self.lineEdit_coursename.text()
        if not coursename:
            QMessageBox.warning(self, '警告', '不能为空')
        else:
            cur.execute('select studentno,sname,courseno,scheduleno from student_courses where coursename=%s',[coursename])
            res = []
            res.append('studentno \t sname \t courseno \t scheduleno')
            for item in cur.fetchall():
                res.append(str(item[0])+'\t'+str(item[1])+'\t'+str(item[2])+'\t'+str(item[3]))
            QMessageBox.information(self, '成功', '\n'.join(res) if len(res) > 0 else '无结果')


    def score(self):
        con = self.connect()
        cur = con.cursor()
        sno = self.lineEdit_sno2.text()
        query = 'select studentno,count(*),avg(score) from choose group by studentno '
        if not sno:
            cur.execute(query)
            res = []
            res.append('studentno \t count \t avg')
            for item in cur.fetchall():
                res.append(str(item[0])+'\t'+str(item[1])+'\t'+str(item[2]))
            QMessageBox.information(self, '成功', '\n'.join(res) if len(res) > 0 else '无结果')
        elif not cur.execute('select * from choose where studentno=%s',[sno]):
            QMessageBox.warning(self, '警告', '该学号无结果')
        else:
            cur.execute(query+'having studentno=%s',[sno])
            res = []
            res.append('studentno \t count \t avg')
            for item in cur.fetchall():
                res.append(str(item[0])+'\t'+str(item[1])+'\t'+str(item[2]))
            QMessageBox.information(self, '成功', '\n'.join(res) if len(res) > 0 else '无结果')


    def setupUi(self, administrator):
        administrator.setObjectName("administrator")
        administrator.resize(979, 625)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        administrator.setFont(font)
        self.centralwidget = QtWidgets.QWidget(administrator)
        self.centralwidget.setObjectName("centralwidget")
        self.backbutton = QtWidgets.QPushButton(self.centralwidget)
        self.backbutton.setGeometry(QtCore.QRect(10, 10, 93, 32))
        self.backbutton.setObjectName("backbutton")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(60, 70, 391, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_sno = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_sno.setText("")
        self.lineEdit_sno.setObjectName("lineEdit_sno")
        self.gridLayout_3.addWidget(self.lineEdit_sno, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_sname = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_sname.setText("")
        self.lineEdit_sname.setObjectName("lineEdit_sname")
        self.gridLayout_2.addWidget(self.lineEdit_sname, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_13 = QtWidgets.QGridLayout()
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.lineEdit_cno = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_cno.setText("")
        self.lineEdit_cno.setObjectName("lineEdit_cno")
        self.gridLayout_13.addWidget(self.lineEdit_cno, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout_13.addWidget(self.label_16, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_13)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.comboBox_sex = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_sex.setObjectName("comboBox_sex")
        self.comboBox_sex.addItem("")
        self.comboBox_sex.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_sex)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.gridLayout_4.addLayout(self.formLayout, 1, 3, 1, 1)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_sage = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_sage.setText("")
        self.lineEdit_sage.setObjectName("lineEdit_sage")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sage)
        self.gridLayout_4.addLayout(self.formLayout_4, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.studentInsertButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.studentInsertButton.setObjectName("studentInsertButton")
        self.horizontalLayout.addWidget(self.studentInsertButton)
        self.studentDeletepushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.studentDeletepushButton.setObjectName("studentDeletepushButton")
        self.horizontalLayout.addWidget(self.studentDeletepushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 41, 171))
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(560, 70, 356, 231))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.lineEdit_courseno = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_courseno.setText("")
        self.lineEdit_courseno.setObjectName("lineEdit_courseno")
        self.gridLayout_7.addWidget(self.lineEdit_courseno, 1, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_7)
        self.gridLayout_11 = QtWidgets.QGridLayout()
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.lineEdit_tno = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_tno.setText("")
        self.lineEdit_tno.setObjectName("lineEdit_tno")
        self.gridLayout_11.addWidget(self.lineEdit_tno, 1, 1, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_11)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.formLayout_6 = QtWidgets.QFormLayout()
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.comboBox_semester = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_semester.setObjectName("comboBox_semester")
        self.comboBox_semester.addItem("")
        self.comboBox_semester.addItem("")
        self.comboBox_semester.addItem("")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_semester)
        self.gridLayout_5.addLayout(self.formLayout_6, 1, 5, 1, 1)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.comboBox_year = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_year.setObjectName("comboBox_year")
        self.comboBox_year.addItem("")
        self.comboBox_year.addItem("")
        self.comboBox_year.addItem("")
        self.comboBox_year.addItem("")
        self.comboBox_year.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_year)
        self.gridLayout_5.addLayout(self.formLayout_3, 1, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_5)
        # self.gridLayout_10 = QtWidgets.QGridLayout()
        # self.gridLayout_10.setObjectName("gridLayout_10")
        # self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        # self.label_13.setObjectName("label_13")
        # self.gridLayout_10.addWidget(self.label_13, 1, 0, 1, 1)
        # self.lineEdit_capacity = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        # self.lineEdit_capacity.setText("")
        # self.lineEdit_capacity.setObjectName("lineEdit_capacity")
        # self.gridLayout_10.addWidget(self.lineEdit_capacity, 1, 1, 1, 1)
        # self.verticalLayout_2.addLayout(self.gridLayout_10)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.InsertSchedulepushButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.InsertSchedulepushButton.setObjectName("InsertSchedulepushButton")
        self.horizontalLayout_2.addWidget(self.InsertSchedulepushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(20, 400, 51, 51))
        self.label_25.setObjectName("label_25")
        self.verticalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setGeometry(QtCore.QRect(100, 340, 361, 141))
        self.verticalLayoutWidget_5.setObjectName("verticalLayoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_6.addWidget(self.label_27)
        self.gridLayout_15 = QtWidgets.QGridLayout()
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.lineEdit_coursename = QtWidgets.QLineEdit(self.verticalLayoutWidget_5)
        self.lineEdit_coursename.setText("")
        self.lineEdit_coursename.setObjectName("lineEdit_coursename")
        self.gridLayout_15.addWidget(self.lineEdit_coursename, 1, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.verticalLayoutWidget_5)
        self.label_28.setObjectName("label_28")
        self.gridLayout_15.addWidget(self.label_28, 1, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_15)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.course2studentButton = QtWidgets.QPushButton(self.verticalLayoutWidget_5)
        self.course2studentButton.setObjectName("course2studentButton")
        self.horizontalLayout_6.addWidget(self.course2studentButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(560, 340, 351, 141))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_7.addWidget(self.label_29)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.lineEdit_sno2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_6)
        self.lineEdit_sno2.setText("")
        self.lineEdit_sno2.setObjectName("lineEdit_sno2")
        self.gridLayout_17.addWidget(self.lineEdit_sno2, 1, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.label_30.setObjectName("label_30")
        self.gridLayout_17.addWidget(self.label_30, 1, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_17)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.scoreButton = QtWidgets.QPushButton(self.verticalLayoutWidget_6)
        self.scoreButton.setObjectName("scoreButton")
        self.horizontalLayout_7.addWidget(self.scoreButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(530, 50, 20, 500))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 320, 910, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(60, 50, 20, 500))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        administrator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(administrator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 979, 29))
        self.menubar.setObjectName("menubar")
        administrator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(administrator)
        self.statusbar.setObjectName("statusbar")
        administrator.setStatusBar(self.statusbar)

        self.retranslateUi(administrator)
        QtCore.QMetaObject.connectSlotsByName(administrator)

        # operation
        self.studentInsertButton.clicked.connect(self.studentInsert)
        self.studentDeletepushButton.clicked.connect(self.studentDelete)
        self.InsertSchedulepushButton.clicked.connect(self.InsertSchedule)
        self.course2studentButton.clicked.connect(self.course2student)
        self.scoreButton.clicked.connect(self.score)


    def retranslateUi(self, administrator):
        _translate = QtCore.QCoreApplication.translate
        administrator.setWindowTitle(_translate("administrator", "管理员"))
        self.backbutton.setText(_translate("administrator", "返回"))
        self.label.setText(_translate("administrator", "     学生信息（删除操作仅需学号）"))
        self.label_5.setText(_translate("administrator", "   学号   "))
        self.label_3.setText(_translate("administrator", "   姓名   "))
        self.label_16.setText(_translate("administrator", "   班号   "))
        self.comboBox_sex.setItemText(0, _translate("administrator", "female"))
        self.comboBox_sex.setItemText(1, _translate("administrator", "male"))
        self.label_2.setText(_translate("administrator", "   性别   "))
        self.label_6.setText(_translate("administrator", "   年龄   "))
        self.studentInsertButton.setText(_translate("administrator", "插入"))
        self.studentDeletepushButton.setText(_translate("administrator", "删除"))
        self.label_4.setText(_translate("administrator", "插入\n"
" 与\n"
"删除"))
        self.label_9.setText(_translate("administrator", "课程安排"))
        self.label_10.setText(_translate("administrator", " 课程号  "))
        self.label_17.setText(_translate("administrator", "教师工号"))
        self.label_8.setText(_translate("administrator", "   学期   "))
        self.comboBox_semester.setItemText(0, _translate("administrator", "spring"))
        self.comboBox_semester.setItemText(1, _translate("administrator", "summer"))
        self.comboBox_semester.setItemText(2, _translate("administrator", "autumn"))
        self.label_7.setText(_translate("administrator", "   年份   "))
        self.comboBox_year.setItemText(0, _translate("administrator", "2019"))
        self.comboBox_year.setItemText(1, _translate("administrator", "2020"))
        self.comboBox_year.setItemText(2, _translate("administrator", "2021"))
        self.comboBox_year.setItemText(3, _translate("administrator", "2022"))
        self.comboBox_year.setItemText(4, _translate("administrator", "2023"))
        # self.label_13.setText(_translate("administrator", "选课容量"))
        self.InsertSchedulepushButton.setText(_translate("administrator", "插入"))
        self.label_25.setText(_translate("administrator", "查询"))
        self.label_27.setText(_translate("administrator", "查询选修某课程学生"))
        self.label_28.setText(_translate("administrator", "课程名称"))
        self.course2studentButton.setText(_translate("administrator", "查询"))
        self.label_29.setText(_translate("administrator", "查询学生选课数和平均成绩\n(若学号为空则输出所有学生)"))
        self.label_30.setText(_translate("administrator", "学号"))
        self.scoreButton.setText(_translate("administrator", "查询"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    administrator = QtWidgets.QMainWindow()
    ui = Ui_administrator()
    ui.setupUi(administrator)
    administrator.show()
    sys.exit(app.exec_())
