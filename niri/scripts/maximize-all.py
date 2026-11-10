#!/usr/bin/env python3
import json, subprocess, sys
from pathlib import Path

def query(name):
    return json.loads(subprocess.check_output(['niri', 'msg', '-j', name]))

config = Path(__file__).resolve().parents[1] / 'config.kdl'
text = config.read_text()
marker = 'open-maximized-to-edges true'
enabled = marker in text
if '--apply' not in sys.argv:
    text = text.replace('open-maximized-to-edges ' + str(enabled).lower(),
                        'open-maximized-to-edges ' + str(not enabled).lower())
    config.write_text(text)
    enabled = not enabled
outputs = query('outputs')
widths = [o['logical']['width'] for o in outputs.values() if o.get('logical')]
for window in query('windows'):
    if window['is_floating'] or window.get('app_id') == 'wofi':
        continue
    width = window['layout']['tile_size'][0]
    maximized = any(abs(width - w) < 1 for w in widths)
    if maximized != enabled:
        subprocess.run(['niri', 'msg', 'action', 'maximize-window-to-edges',
                        '--id', str(window['id'])], check=True)
