import json,os
from gchat.uikit import *



class SectionText:

    def __init__(self,title=None,text=None,icon_url=None,right_button:UiButton=None,bottom_buttons:list[UiButton]=None):
        self.title          = title
        self.text           = text
        self.icon_url       = icon_url
        self.right_button   = right_button
        self.bottom_buttons = bottom_buttons
    

    def render(self):
        widgets = []
        text = self.text.replace("\n",'<br>') if self.text else None
        widgets.append(UiDecoratedText(
            text         = self.title,
            bottom_label = text,
            icon_url     = self.icon_url,
            right_button = self.right_button
            )
        )
        if self.bottom_buttons:
            widgets.append(UiButtonList(buttons = self.bottom_buttons))

        base = UiSection(widgets=widgets).render()

        return base


