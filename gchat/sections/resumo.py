import json,os
from gchat.uikit import *
import socket


class SectionResumo:

    def __init__(self,data_start:str,hora_start:str,hora_end:str,duracao:str,maquina:bool,target=None):
        self.data_start = data_start
        self.hora_start = hora_start
        self.hora_end   = hora_end
        self.duracao    = duracao
        self.target     = target
        self.maquina    = maquina

    
    def get_local_ip(self):
        # Cria um socket temporário para "tentar" uma conexão externa 
        # (isso ajuda a identificar qual interface de rede está ativa)
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # Não precisa ser um IP real/alcançável, apenas um formato válido
            s.connect(('8.8.8.8', 1))
            ip_local = s.getsockname()[0]
        except Exception:
            ip_local = '127.0.0.1'
        finally:
            s.close()
        return ip_local

    def render(self):

        periodo = UiDecoratedText(
            top_label    = "Período",
            text         = "📅" + self.data_start,
            bottom_label = "Início: {} | Fim: {}".format(self.hora_start,self.hora_end)
            )
        
        duracao = UiDecoratedText(
            top_label    = "Duração",
            text         = "⏱️" + self.duracao,
            )
        sucesso = UiDecoratedText(
            top_label    = "Sucesso",
            text         = "🎯" + self.target,
            ) if self.target else None
        
        maquina = UiDecoratedText(
            top_label    = "Máquina",
            text         = "💻" + socket.gethostname(),
            bottom_label = self.get_local_ip()
            ) if self.maquina else None
        
        return UiSection(
            header="Resumo da Operação",
            widgets=[
                UiColumns(columns=[
                    UiColumn(widgets=[x for x in [periodo, maquina] if x]),
                    UiColumn(widgets=[x for x in [duracao,sucesso] if x]),
                ])
        ]).render()


