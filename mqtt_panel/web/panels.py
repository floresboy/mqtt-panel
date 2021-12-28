from mqtt_panel.web.component import Component
from mqtt_panel.util import blob_hash


class Panels(Component):
    def __init__(self):
        super().__init__(4)
        self._panel_map = {}
        self._panels = []

    def add_panel(self, panel):
        self._panels.append(panel)
        self._panel_map[panel.name] = panel

    def _body(self, fh):
        for panel in self._panels:
            panel.body(fh)

    def open(self):
        for panel in self._panels:
            panel.open()
        self._identity = blob_hash([p.identity for p in self._panels])
