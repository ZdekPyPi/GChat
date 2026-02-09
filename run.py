# TEST FILE
from dotenv import load_dotenv
import sys
import os

sys.path.append("./gchatUts")
from gchatUts import GChat

load_dotenv()

whook = os.getenv("WEBHOOK_URL")
g = GChat(webhook=whook)


# EXEMPLO TE CODIGO PARA GERAR ETAPAS
from gchatUts.sections import SectionEtapa, Etapa, ItemEtapa
from gchatUts.uikit import UiSection, UiDecoratedText, UiColumn, UiColumns, UiButton, UiCard
from gchatUts.sections import SectionResumo, SectionSuccess, SectionError, SectionWarn, SectionText

# CRIA O RESUMO
sectionResumo = SectionResumo(
    data_start="23/12/1991",  # DATA DE EXECUCAO
    hora_start="18:43:02",  # HORA DE INICIO
    hora_end="19:20:45",  # HORA DE TERMINO
    duracao="00:37:57",  # TEMPO DE EXECUCAO
    target="5 / 10",  # QUANTOS ITENS CONCLUIDOS
    maquina=True,
)

successSection = SectionSuccess(
    title="A tarefa foi concluída com sucesso.",
    text="Todos os processos foram validados.",
)

errorSection = SectionError(
    title="A tarefa foi concluída com erro.",
    text="""Message: no such element: Unable to locate element: {"method":"xpath","selector":"//input[@type="email"]"}[0x0x7ff65c5c6b55+79621]\n\t\t\tGet""",
)

warnSection = SectionWarn(title="A tarefa foi com alertas.", text="Atençao....")
textSection = SectionText(
    title="Texto Simples", text="Texto de exemplo\nOutro texto\nFim"  # OPCIONAL
)
textSection2 = SectionText(text="Texto sem titulo")
textSection3 = SectionText(
    title="Texto Simples",  # OPCIONAL
    text="Texto de exemplo com Icone",
    icon_url="https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u1f916.png",
)

textSection4 = SectionText(
    title="Texto Simples",  # OPCIONAL
    text="Texto de exemplo com Botoes a direita",
    icon_url="https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u1f916.png",
    right_button=UiButton(text="Google", url="https://www.google.com"),
)

textSection5 = SectionText(
    title="Texto Simples",  # OPCIONAL
    text="Texto de exemplo com Botoes a baixo",
    icon_url="https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u1f916.png",
    bottom_buttons=[
        UiButton(text="Google", url="https://www.google.com"),
        UiButton(text="Youtube", url="https://www.youtube.com"),
    ],
)


# CRIA O OBJETO DAS ETAPAS COM A COLUNA DE CADA ETAPA E ATRIBUI UM ID PARA CADA
sectionEtapa = SectionEtapa(
    [
        Etapa(titulo="step1", icone="✈️", id_etapa="1"),
        Etapa(titulo="step2", icone="➕", id_etapa="2"),
        Etapa(titulo="step3", icone="🛡️", id_etapa="3"),
        Etapa(titulo="step4", icone="⬆️", id_etapa="4"),
        Etapa(titulo="step5", icone="⚖️", id_etapa="5"),
    ]
)

# ADCIONA UM ITEM NA LISTA
sectionEtapa.add_job(
    descricao="NOME DO PROCESSO",
    etapas=[
        ItemEtapa(id_etapa="1", status=ItemEtapa.STS_SUCC),
        ItemEtapa(id_etapa="2", status=ItemEtapa.STS_WARN),
        ItemEtapa(id_etapa="3", status=ItemEtapa.STS_DANG),
        ItemEtapa(id_etapa="4", status=ItemEtapa.STS_BLUE),
        ItemEtapa(id_etapa="5", status=ItemEtapa.STS_BLCK),
    ],
)


custom_sec = UiSection(
    widgets=[
        UiColumns(
            columns=[
                UiColumn(
                    widgets=[
                        UiDecoratedText(
                            top_label="<b>HOSTNAME</b>", text="SRV-PROD-01"
                        ),
                        UiDecoratedText(top_label="<b>USUÁRIO</b>", text="admin_bot"),
                    ]
                ),
                UiColumn(
                    widgets=[
                        UiDecoratedText(top_label="<b>ROBÔ</b>", text="Worker_Alpha"),
                        UiDecoratedText(
                            top_label="<b>STATUS</b>",
                            text='<b><font color="#2ecc71">● DEPLOY</font></b>',
                        ),
                    ]
                ),
            ]
        )
    ]
)

card = UiCard(
    title="NOME DO ROBO",
    subtitle="hehehehe",
    image_url="https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/assets/Sport utility vehicle/3D/sport_utility_vehicle_3d.png",  # ICONE TDO TITULO
    sections=[
        sectionResumo,
        sectionEtapa,
        successSection,
        errorSection,
        warnSection,
        textSection,
        textSection2,
        textSection3,
        textSection4,
        textSection5,
        custom_sec,
    ],  # SECOES EXTRAS
    # sections        = [custom_sec] #SECOES EXTRAS
)

g.send_card(card=card)


pass
