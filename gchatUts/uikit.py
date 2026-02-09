from urllib.parse import quote


class UiButton:
    def __init__(self, text, url):
        self.text = text
        self.url = url

    def render(self):
        return {"text": self.text, "onClick": {"openLink": {"url": self.url}}}


class UiDecoratedText:
    def __init__(
        self,
        top_label=None,
        text=None,
        bottom_label=None,
        icon_url=None,
        right_button: UiButton = None,
    ):
        self.top_label = top_label
        self.text = text
        self.bottom_label = bottom_label
        self.icon_url = icon_url
        self.right_button = right_button

    def render(self):
        base = {
            "decoratedText": {
                "topLabel": self.top_label,
                "text": self.text,
                "bottomLabel": self.bottom_label,
            }
        }
        if self.icon_url:
            base["decoratedText"]["startIcon"] = {"iconUrl": self.icon_url}

        if self.right_button:
            base["decoratedText"]["button"] = self.right_button.render()

        return base


class UiSection:
    def __init__(self, widgets: list, header: str = None):
        self.widgets = widgets
        self.header = header

    def render(self):
        return {"header": self.header, "widgets": [x.render() for x in self.widgets]}


class UiButtonList:
    def __init__(self, buttons: list[UiButton]):
        self.buttons = buttons

    def render(self):
        return {"buttonList": {"buttons": [btn.render() for btn in self.buttons]}}


class UiColumn:
    def __init__(self, widgets: list, horizontal_alignment="START"):
        self.widgets = widgets
        self.horizontal_alignment = horizontal_alignment

    def render(self):
        base = {
            "horizontalAlignment": self.horizontal_alignment,
            "widgets": [x.render() for x in self.widgets],
        }
        return base


class UiColumns:
    def __init__(self, columns: list[UiColumn]):
        self.columns = columns

    def render(self):
        base = {"columns": {"columnItems": [x.render() for x in self.columns]}}
        return base


class UiCard:
    def __init__(
        self, title=None, subtitle=None, image_url=None, sections: list[UiSection] = []
    ):
        self.title = title
        self.subtitle = subtitle
        self.image_url = image_url
        self.sections = sections

    def render(self):
        sections = []
        for s in self.sections:
            rendered = s.render()
            sections += rendered if isinstance(rendered, list) else [rendered]

        encoded_image_url = (
            quote(self.image_url, safe=":/?#[]@!$&'()*+,;=") if self.image_url else None
        )
        return {
            "card": {
                "header": {
                    "title": self.title,
                    "subtitle": self.subtitle,
                    "imageUrl": encoded_image_url,
                },
                "sections": sections,
            }
        }
