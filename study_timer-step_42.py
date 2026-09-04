# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: StudyTimer
class ColorFormatter:
    """Простой форматтер ANSI-цветов с поддержкой отключения."""
    def __init__(self, enabled=True):
        self.enabled = enabled
        self._codes = {
            'reset': '\033[0m',
            'bold': '\033[1m',
            'dim': '\033[2m',
            'red': '\033[31m',
            'green': '\033[32m',
            'yellow': '\033[33m',
            'blue': '\033[34m',
            'magenta': '\033[35m',
            'cyan': '\033[36m',
            'white': '\033[37m',
            'bg_red': '\033[41m',
            'bg_green': '\033[42m',
            'bg_yellow': '\033[43m',
            'bg_blue': '\033[44m',
            'bg_magenta': '\033[45m',
            'bg_cyan': '\033[46m',
            'bg_white': '\033[47m',
        }

    def color(self, text, color):
        if not self.enabled:
            return text
        return self._codes.get(color, '') + text + self._codes['reset']

    def bg(self, text, color):
        if not self.enabled:
            return text
        return self._codes.get(color, '') + text + self._codes['reset']

    def bold(self, text):
        if not self.enabled:
            return text
        return self._codes['bold'] + text + self._codes['reset']

    def dim(self, text):
        if not self.enabled:
            return text
        return self._codes['dim'] + text + self._codes['reset']
