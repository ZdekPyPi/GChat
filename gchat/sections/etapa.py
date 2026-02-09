import json,os
from dataclasses import dataclass
from gchat.uikit import *

@dataclass
class Etapa:
    titulo    :str= None
    icone     :str= None
    id_etapa  :str= None

@dataclass
class ItemEtapa:
    STS_SUCC = "🟩"
    STS_WARN = "🟨"
    STS_DANG = "🟥"
    STS_BLUE = "🟦"
    STS_WHIT = "⬜"
    STS_BLCK = "⬛"
    STS_NOIC = "⠀"

    id_etapa: str
    status   : str

class SectionEtapa:
    etapas = None
    jobs = None

    def __init__(self,etapas:list[Etapa],title="<b>📁 Processo</b>",job_icon="📑"):
        self.etapas   = etapas
        self.jobs     = {}
        self.title    = title
        self.job_icon = job_icon
    
    def add_job(self,descricao,etapas=list[ItemEtapa]):
        self.jobs[descricao] = etapas
    
    def render_legendas(self):
        return UiSection(header="Legenda",widgets=[
            UiDecoratedText(
                text=" ".join([f"{x.icone}{x.titulo}" for x in self.etapas])
            )
        ]).render()


    def render_etapas(self):

        col_1 = UiColumn(widgets=[
            UiDecoratedText(text=self.title)
        ])
        col_2 = UiColumn(widgets=[
            UiDecoratedText(text=" ".join([x.icone for x in self.etapas]))
        ])
        
        #ITEMS
        for desc,job_etapas in self.jobs.items():
            col_1.widgets.append(UiDecoratedText(text=f"{self.job_icon} {desc}"))
            
            icn_etapas = []
            for etapa in self.etapas:
                icn = [x.status for x in job_etapas if x.id_etapa == etapa.id_etapa] or [ItemEtapa.STS_NOIC]
                icn_etapas.append(icn[0])

            col_2.widgets.append(UiDecoratedText(text=" ".join(icn_etapas)))

        return UiSection(header="Status por Etapa",widgets=[UiColumns(columns=[col_1,col_2])]).render()


    def render(self):
        return [self.render_legendas(),self.render_etapas()]
