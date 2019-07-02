from PyQt5 import QtWidgets, QtGui, QtCore

import View.MainWindowView
import Model.Call

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = View.MainWindowView()
        self.ui.setupUi(self)
        self.__retrieveCalls()

    def __retrieveCalls(self):
        for call in Model.Call.select().dicts():
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            itemCount = 0
            for key in call:
                self.ui.tableWidget.setItem(rowPosition, itemCount, QtWidgets.QTableWidgetItem(str(call[key])))
                itemCount += 1

    def createCalls(self):
        # data = ,
        # nomeUsuario = peewee.CharField(),
        # documento = peewee.CharField(),
        # laboratorio = peewee.CharField(),
        # equipamento = peewee.CharField(),
        # numeroAmostras = peewee.CharField(),
        # atividade = peewee.IntegerField(),
        # tipoUsuario = peewee.IntegerField(),
        # origemUsuario,
        data = [
            ('2019-07-02', 'Leonardo', '302060', 'LAM', 'VSM', 12, 1, 1, 1),
            ('2019-07-03', 'Maria', '202060', 'LAMEF', 'VSM', 12, 1, 1, 1),
            ('2019-07-04', 'Joana', '702060', 'LEME', 'VSM', 12, 1, 1, 1),
            ('2019-07-05', 'Creusa', '002060', 'LABIOMAT', 'VSM', 12, 1, 1, 1),
        ]
        fields = [
            Model.Call.data,
            Model.Call.nomeUsuario,
            Model.Call.documento,
            Model.Call.laboratorio,
            Model.Call.equipamento,
            Model.Call.numeroAmostras,
            Model.Call.atividade,
            Model.Call.tipoUsuario,
            Model.Call.origemUsuario
        ]
        Model.Call.insert_many(data, fields = fields).execute()