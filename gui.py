from aqt.qt import *
from aqt.utils import show_warning

from .flashcard_topology import TopologyDialog

class TosetViewDialog(TopologyDialog):
    def build_interface(self, layout: QBoxLayout) -> None:
        degree = self.topo.measure_order(self.fields)
        self.field_editors = {}
        self.field_layout = QVBoxLayout()
        layout.addLayout(self.field_layout)
        for name in self.fields:
            field_editor = QLineEdit()
            field_editor.setText(self.fields[name])
            self.field_editors[name] = field_editor
            if name.startswith("Item"):
                self.field_layout.addWidget(field_editor)
            else:
                container = QWidget()
                row = QHBoxLayout(container)
                row.addWidget(QLabel(f"{name}:"))
                row.addWidget(field_editor)
                self.field_layout.addWidget(container)
        plus_button = QPushButton("+ longer")
        plus_button.clicked.connect(self.enlarge)
        layout.addWidget(plus_button)

    def capture_fields(self) -> None:
        for field_name, editor in self.field_editors.items():
            self.fields[field_name] = editor.text()

    def enlarge(self) -> None:
        old_order = self.topo.measure_order(self.fields)
        new_order = self.topo.next_order(old_order)
        if new_order >= 12:
            show_warning(
                "Long sequences hurt performance.\n"
                f"Expanding to {new_order} items."
            )
        for i in range(old_order + 1, new_order + 1):
            field_name = f"Item {i}"
            edit = QLineEdit()
            self.field_editors[field_name] = edit
            self.field_layout.addWidget(edit)
            self.fields[field_name] = ""
