from PyQt5.QtWidgets import QWidget, QDateEdit
from PyQt5.QtCore import QDate, pyqtSlot
from PyQt5.uic import loadUi
from App.model.reserva import Reserva
from App.controller.pessoa import buscarPessoas
from App.controller.curso import listarCursos
from App.controller.sala import listarSala
from App.controller.utils import modificarData


class EditarReserva(QWidget):
    def __init__(self):
        super().__init__()
        loadUi('App/view/ui/editarReserva.ui',self)
        
        #btn editar reserva = btnEditarReserva

        self.diaInicio = self.findChild(QDateEdit, 'diaInicio') 
        self.diaFim = self.findChild(QDateEdit, 'diaFim')

        self.diaInicio.setCalendarPopup(True)
        self.diaInicio.setDisplayFormat('dd/MM/yyyy')
        self.diaInicio.setDate(QDate.currentDate())
        self.setDataMinima()
        self.setMinimoFim()
        self.diaInicio.dateChanged.connect(self.setDataMinima)
        self.inicioCurso.timeChanged.connect(self.setMinimoFim)

        self.diaFim.setCalendarPopup(True)
        self.diaFim.setDisplayFormat('dd/MM/yyyy')
        self.diaFim.setDate(QDate.currentDate()) 

        self.dicionarioCurso = listarCursos()
        self.popularCurso()
        # self.cursoReserva.currentIndexChanged.connect(self.popularReserva)

    @pyqtSlot()
    def on_btnEditarReserva_clicked(self):
        # print(self.diaInicio.text().strip())
        # print(self.inicioCurso.time().toString('HH:mm'))
        print(Reserva.teste('19:00','2025-01-21', 1))

    def setDataMinima(self):
        """Define a data mínima de término da reserva"""
        primeiroDia = self.diaInicio.date()
        self.diaFim.setMinimumDate(primeiroDia)
    
    def setMinimoFim(self):
        """Define o horário mínimo para acabar a reserva"""
        horarioComeco = self.inicioCurso.time()
        self.fimCurso.setMinimumTime(horarioComeco)

    def popularCurso(self):
        curso = self.dicionarioCurso.keys()
        self.cursoReserva.addItems(curso)
    
    # def getIdReserva(self):
    #     reservaSelecionada = Reserva.teste()

    # def popularReserva(self):
    #     idReservaComboBox = self.getIdReserva()

    def getDados(self)->dict:
        """Pegando o dados na interface e retornando os valores"""
        pessoas = buscarPessoas()
        sala = listarSala()
        curso = listarCursos() 
        nomeDocenteResponsavel = self.nomeDocente.currentText().strip()
        idDocente = pessoas[nomeDocenteResponsavel]
        nomeSala = self.salaReserva.currentText().strip()
        idSala = sala[nomeSala]
        nomeCurso = self.cursoReserva.currentText().strip()
        idCurso = curso[nomeCurso]
        
        
        equipamentos = self.equipamentosReserva.text().strip() 
        diaInicio = modificarData(self.diaInicio.text().strip() )
        diaFim = modificarData(self.diaFim.text().strip() )
        observacao = self.observacaoReserva.text().strip() 
        cursoInicio = self.inicioCurso.time().toString('HH:mm')
        cursoFim = self.fimCurso.time().toString('HH:mm')
        segunda = self.segCheck.isChecked()        
        terca = self.terCheck.isChecked()
        quarta = self.quaCheck.isChecked()
        quinta = self.quiCheck.isChecked()
        sexta = self.sextaCheck.isChecked()
        sabado = self.sabCheck.isChecked()

        dados = {"idDocente":idDocente, 
                 "idSala":idSala, 
                 "idCurso":idCurso,
                 "equipamentos":equipamentos,
                 "diaInicio":diaInicio,
                 "diaFim":diaFim,
                 "observações":observacao,
                 "inicioCurso":cursoInicio,
                 "fimCurso":cursoFim,
                 "seg":segunda,
                 "ter":terca,
                 "qua":quarta,
                 "qui":quinta,
                 "sexta":sexta,
                 "sab":sabado}
        return dados