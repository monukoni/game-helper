import json

from PyQt5.QtCore import pyqtSignal, QObject

from dataclasses import dataclass, asdict


@dataclass
class SteppySettings:
    delay: int = 10
    speech_buble_font_size: int = 15

    @classmethod
    def from_file(cls, file_name: str):
        with open(file_name, "r") as f:
            contents = f.read()
            contents_dict = json.loads(contents)
            return cls(**contents_dict)

    def save_to_file(self, file_name: str):
        with open(file_name, "w") as f:
            f.write(json.dumps(asdict(self)))


class SettingsOnUpdate(QObject):
    on_updated_signal = pyqtSignal(SteppySettings)

    def on_update(self, settings: SteppySettings):
        self.on_updated_signal.emit(settings)
