from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit
from PySide6.QtCore import Signal

class ConceptPage(QWidget):
    run_demo = Signal(str)
    def __init__(self, concept_data):
        super().__init__()
        self.data = concept_data
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Title
        title = QLabel(concept_data["title"])
        title.setStyleSheet("font-size: 22px; font-weight: bold;")
        layout.addWidget(title)
        # Description
        desc = QLabel(concept_data["description"])
        desc.setWordWrap(True)
        layout.addWidget(desc)
        # How-it-works
        how_label = QLabel("\nHow It Works:")
        how_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(how_label)
        for step in concept_data["how_it_works"]:
            step_label = QLabel(f"• {step}")
            layout.addWidget(step_label)
        # Examples
        ex_label = QLabel("\nExamples:")
        ex_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(ex_label)
        for ex in concept_data["examples"]:
            ex_item = QLabel(f"• {ex}")
            layout.addWidget(ex_item)
        # Run Demo Button
        run_btn = QPushButton("Run Demo")
        run_btn.setStyleSheet("font-size: 16px; padding: 10px;")
        run_btn.clicked.connect(lambda: self.run_demo.emit(concept_data["title"]))
        layout.addWidget(run_btn)
