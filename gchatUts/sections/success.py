import json,os
from gchatUts.uikit import Uikit



class SectionSuccess:

    def __init__(self,title=None,text=None):
        self.title = title
        self.text  = text
    

    def section(self):
        text = self.text.replace("\n",'<br>') if self.text else None
        dec_text = Uikit.decoratedText(
            text         = f"<b>{self.title}</b>" if self.title else None,
            bottom_label = text,
            icon_url     = "https://raw.githubusercontent.com/googlefonts/noto-emoji/main/png/128/emoji_u2705.png"
            )
        base = Uikit.section(widgets=[dec_text])

        return base


