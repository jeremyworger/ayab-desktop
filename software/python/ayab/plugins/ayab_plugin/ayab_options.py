# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ayab_options.ui'
#
# Created: Wed Nov 25 21:43:24 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        DockWidget.setObjectName(_fromUtf8("DockWidget"))
        DockWidget.resize(240, 581)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DockWidget.sizePolicy().hasHeightForWidth())
        DockWidget.setSizePolicy(sizePolicy)
        DockWidget.setMinimumSize(QtCore.QSize(240, 581))
        DockWidget.setMaximumSize(QtCore.QSize(240, 581))
        DockWidget.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        DockWidget.setWindowTitle(_fromUtf8(""))
        self.ayab_config = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ayab_config.sizePolicy().hasHeightForWidth())
        self.ayab_config.setSizePolicy(sizePolicy)
        self.ayab_config.setObjectName(_fromUtf8("ayab_config"))
        self.verticalLayout = QtGui.QVBoxLayout(self.ayab_config)
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(self.ayab_config)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(220, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(0, 16777215))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.serial_port_dropdown = QtGui.QComboBox(self.groupBox)
        self.serial_port_dropdown.setObjectName(_fromUtf8("serial_port_dropdown"))
        self.horizontalLayout_3.addWidget(self.serial_port_dropdown)
        self.refresh_ports_button = QtGui.QPushButton(self.groupBox)
        self.refresh_ports_button.setObjectName(_fromUtf8("refresh_ports_button"))
        self.horizontalLayout_3.addWidget(self.refresh_ports_button)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget = QtGui.QTabWidget(self.ayab_config)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(180, 430))
        self.tabWidget.setMaximumSize(QtCore.QSize(1000000, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_knit = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_knit.sizePolicy().hasHeightForWidth())
        self.tab_knit.setSizePolicy(sizePolicy)
        self.tab_knit.setObjectName(_fromUtf8("tab_knit"))
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_knit)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 221, 402))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setMargin(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_6 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout_3.addWidget(self.label_6)
        self.color_edit = QtGui.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.color_edit.sizePolicy().hasHeightForWidth())
        self.color_edit.setSizePolicy(sizePolicy)
        self.color_edit.setMinimum(2)
        self.color_edit.setMaximum(6)
        self.color_edit.setObjectName(_fromUtf8("color_edit"))
        self.verticalLayout_3.addWidget(self.color_edit)
        self.label_5 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout_3.addWidget(self.label_5)
        self.start_line_edit = QtGui.QSpinBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_line_edit.sizePolicy().hasHeightForWidth())
        self.start_line_edit.setSizePolicy(sizePolicy)
        self.start_line_edit.setSuffix(_fromUtf8(""))
        self.start_line_edit.setMinimum(0)
        self.start_line_edit.setMaximum(256)
        self.start_line_edit.setObjectName(_fromUtf8("start_line_edit"))
        self.verticalLayout_3.addWidget(self.start_line_edit)
        self.infRepeat_checkbox = QtGui.QCheckBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infRepeat_checkbox.sizePolicy().hasHeightForWidth())
        self.infRepeat_checkbox.setSizePolicy(sizePolicy)
        self.infRepeat_checkbox.setObjectName(_fromUtf8("infRepeat_checkbox"))
        self.verticalLayout_3.addWidget(self.infRepeat_checkbox)
        self.gbox_startneedle = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.gbox_startneedle.setMinimumSize(QtCore.QSize(0, 60))
        self.gbox_startneedle.setObjectName(_fromUtf8("gbox_startneedle"))
        self.start_needle_color = QtGui.QComboBox(self.gbox_startneedle)
        self.start_needle_color.setGeometry(QtCore.QRect(60, 20, 81, 31))
        self.start_needle_color.setObjectName(_fromUtf8("start_needle_color"))
        self.start_needle_color.addItem(_fromUtf8(""))
        self.start_needle_color.addItem(_fromUtf8(""))
        self.start_needle_edit = QtGui.QSpinBox(self.gbox_startneedle)
        self.start_needle_edit.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.start_needle_edit.setPrefix(_fromUtf8(""))
        self.start_needle_edit.setMinimum(1)
        self.start_needle_edit.setMaximum(100)
        self.start_needle_edit.setProperty("value", 20)
        self.start_needle_edit.setObjectName(_fromUtf8("start_needle_edit"))
        self.verticalLayout_3.addWidget(self.gbox_startneedle)
        self.gbox_stopneedle = QtGui.QGroupBox(self.verticalLayoutWidget)
        self.gbox_stopneedle.setMinimumSize(QtCore.QSize(0, 60))
        self.gbox_stopneedle.setObjectName(_fromUtf8("gbox_stopneedle"))
        self.stop_needle_color = QtGui.QComboBox(self.gbox_stopneedle)
        self.stop_needle_color.setGeometry(QtCore.QRect(60, 20, 81, 31))
        self.stop_needle_color.setObjectName(_fromUtf8("stop_needle_color"))
        self.stop_needle_color.addItem(_fromUtf8(""))
        self.stop_needle_color.addItem(_fromUtf8(""))
        self.stop_needle_edit = QtGui.QSpinBox(self.gbox_stopneedle)
        self.stop_needle_edit.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.stop_needle_edit.setPrefix(_fromUtf8(""))
        self.stop_needle_edit.setMinimum(1)
        self.stop_needle_edit.setMaximum(100)
        self.stop_needle_edit.setProperty("value", 20)
        self.stop_needle_edit.setObjectName(_fromUtf8("stop_needle_edit"))
        self.verticalLayout_3.addWidget(self.gbox_stopneedle)
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout_3.addWidget(self.label_4)
        self.machine_type_box = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.machine_type_box.sizePolicy().hasHeightForWidth())
        self.machine_type_box.setSizePolicy(sizePolicy)
        self.machine_type_box.setObjectName(_fromUtf8("machine_type_box"))
        self.machine_type_box.addItem(_fromUtf8(""))
        self.machine_type_box.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.machine_type_box)
        self.label_3 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.alignment_combo_box = QtGui.QComboBox(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.alignment_combo_box.sizePolicy().hasHeightForWidth())
        self.alignment_combo_box.setSizePolicy(sizePolicy)
        self.alignment_combo_box.setObjectName(_fromUtf8("alignment_combo_box"))
        self.alignment_combo_box.addItem(_fromUtf8(""))
        self.alignment_combo_box.addItem(_fromUtf8(""))
        self.alignment_combo_box.addItem(_fromUtf8(""))
        self.verticalLayout_3.addWidget(self.alignment_combo_box)
        self.tabWidget.addTab(self.tab_knit, _fromUtf8(""))
        self.tab_test = QtGui.QWidget()
        self.tab_test.setObjectName(_fromUtf8("tab_test"))
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.tab_test)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, -1, 211, 184))
        self.verticalLayoutWidget_2.setObjectName(_fromUtf8("verticalLayoutWidget_2"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setMargin(6)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_4.addWidget(self.label)
        self.progress_hall_l = QtGui.QProgressBar(self.verticalLayoutWidget_2)
        self.progress_hall_l.setEnabled(False)
        self.progress_hall_l.setMaximum(1024)
        self.progress_hall_l.setProperty("value", 0)
        self.progress_hall_l.setObjectName(_fromUtf8("progress_hall_l"))
        self.verticalLayout_4.addWidget(self.progress_hall_l)
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_4.addWidget(self.label_2)
        self.progress_hall_r = QtGui.QProgressBar(self.verticalLayoutWidget_2)
        self.progress_hall_r.setEnabled(False)
        self.progress_hall_r.setMaximum(1024)
        self.progress_hall_r.setProperty("value", 0)
        self.progress_hall_r.setObjectName(_fromUtf8("progress_hall_r"))
        self.verticalLayout_4.addWidget(self.progress_hall_r)
        self.label_7 = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout_4.addWidget(self.label_7)
        self.slider_position = QtGui.QSlider(self.verticalLayoutWidget_2)
        self.slider_position.setEnabled(False)
        self.slider_position.setMaximum(199)
        self.slider_position.setOrientation(QtCore.Qt.Horizontal)
        self.slider_position.setObjectName(_fromUtf8("slider_position"))
        self.verticalLayout_4.addWidget(self.slider_position)
        self.label_carriage = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label_carriage.setObjectName(_fromUtf8("label_carriage"))
        self.verticalLayout_4.addWidget(self.label_carriage)
        self.tabWidget.addTab(self.tab_test, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.configure_button = QtGui.QPushButton(self.ayab_config)
        self.configure_button.setObjectName(_fromUtf8("configure_button"))
        self.verticalLayout.addWidget(self.configure_button)
        DockWidget.setWidget(self.ayab_config)

        self.retranslateUi(DockWidget)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DockWidget)

    def retranslateUi(self, DockWidget):
        self.groupBox.setTitle(_translate("DockWidget", "Port Selection", None))
        self.refresh_ports_button.setText(_translate("DockWidget", "Refresh", None))
        self.label_6.setText(_translate("DockWidget", "Colors", None))
        self.label_5.setText(_translate("DockWidget", "Start Line", None))
        self.start_line_edit.setPrefix(_translate("DockWidget", "line ", None))
        self.infRepeat_checkbox.setText(_translate("DockWidget", "Infinite Repeat", None))
        self.gbox_startneedle.setTitle(_translate("DockWidget", "Start Needle", None))
        self.start_needle_color.setItemText(0, _translate("DockWidget", "orange", None))
        self.start_needle_color.setItemText(1, _translate("DockWidget", "green", None))
        self.gbox_stopneedle.setTitle(_translate("DockWidget", "Stop Needle", None))
        self.stop_needle_color.setItemText(0, _translate("DockWidget", "green", None))
        self.stop_needle_color.setItemText(1, _translate("DockWidget", "orange", None))
        self.label_4.setText(_translate("DockWidget", "Machine Type", None))
        self.machine_type_box.setItemText(0, _translate("DockWidget", "single", None))
        self.machine_type_box.setItemText(1, _translate("DockWidget", "ribber", None))
        self.label_3.setText(_translate("DockWidget", "Alignment", None))
        self.alignment_combo_box.setItemText(0, _translate("DockWidget", "center", None))
        self.alignment_combo_box.setItemText(1, _translate("DockWidget", "left", None))
        self.alignment_combo_box.setItemText(2, _translate("DockWidget", "right", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_knit), _translate("DockWidget", "Knit", None))
        self.label.setText(_translate("DockWidget", "Hall Left", None))
        self.progress_hall_l.setFormat(_translate("DockWidget", "%p%", None))
        self.label_2.setText(_translate("DockWidget", "Hall Right", None))
        self.progress_hall_r.setFormat(_translate("DockWidget", "%p%", None))
        self.label_7.setText(_translate("DockWidget", "Position", None))
        self.label_carriage.setText(_translate("DockWidget", "No carriage detected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_test), _translate("DockWidget", "Test", None))
        self.configure_button.setText(_translate("DockWidget", "2. Configure", None))

