from collections import namedtuple

from mqtt_panel.web.component import Component

Action = namedtuple("Action", "name id")


class TitleBar(Component):
    def __init__(self):
        super().__init__(4)
        self._actions = []

    def _body(self, fh):
        self._write_render(fh, '''\
        <div class="titlebar noselect">
          <img class="titlebar-icon" src="icon-192x192.png"/>
          <span class="titlebar-title">MQTT Panel</span>
          <span class="titlebar-toggle-menubar material-icons">menu</span>
        </div>
        ''', indent=self._indent)
