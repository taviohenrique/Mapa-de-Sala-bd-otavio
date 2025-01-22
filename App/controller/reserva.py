from datetime import datetime, timedelta
from App.model.reserva import Reserva
from App.controller.utils import modificarDataReserva, listas_intervalo_dias


def fazendoReserva(idLogin, dados, diasValidos):
    diaInicio = modificarDataReserva(dados['diaInicio'])
    diaFim = modificarDataReserva(dados['diaFim'])
    lista_de_dias = listas_intervalo_dias(diaInicio, diaFim, diasValidos)
    for diaAtual in lista_de_dias:
        Reserva(idLogin, dados['idDocente'], dados['idCurso'], dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'], 0, dados['observações']).fazer_reserva()
    return True

        
def validarCadastro(dados, diasValidos):
    diaInicio = modificarDataReserva(dados['diaInicio'])
    diaInicio = datetime.strptime(diaInicio, "%d/%m/%Y")
    diaFim = modificarDataReserva(dados['diaFim'])
    diaFim = datetime.strptime(diaFim, "%d/%m/%Y")
    diaAtual = diaInicio
    listaDias = []
    
    while diaAtual <= diaFim:
        diaSemana = diaAtual.weekday()
        validar = Reserva.validar_periodo(dados['idSala'], diaAtual, dados['inicioCurso'], dados['fimCurso'])
        if diasValidos[diaSemana]:
            if validar:
                listaDias.append(validar[0])
        diaAtual += timedelta(days=1)
    return listaDias

def trocar_reserva(dados1, dados2):
    if Reserva.atualizar(dados1['idLogin'], dados1['idPessoa'], dados1['idcurso'], dados1['idSala'], dados1['dia'], dados1['inicioCurso'], dados1['fimCurso'], dados1['observações'],  dados1['idReserva']):
        Reserva.atualizar(dados2['idLogin'], dados2['idPessoa'], dados2['idcurso'], dados2['idSala'], dados2['dia'], dados2['inicioCurso'], dados2['fimCurso'], dados2['observações'],  dados2['idReserva'])

# def deletarReserva(oferta):
#     if Reserva.
#     if Reserva.deletar(idReserva):
#         return True
#     return False

def atualizarReserva(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
    if Reserva.atualizar(idLogin, idPessoa, idCurso, idSala, dia, hrInicio, hrFim, observacao, idReserva):
        return True
    return False

def validarDiaSemana(dia, diaSemana):
    formatoDia = modificarDataReserva(dia)
    formatoDia = datetime.strptime(formatoDia, "%d/%m/%Y")
    dia = datetime.weekday(formatoDia)
    if diaSemana[dia]:
        return True
    print('Selecione o dia da semana certo!')
    return False

