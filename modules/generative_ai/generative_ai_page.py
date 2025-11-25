from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QSpinBox, QHBoxLayout
from modules.generative_ai.generative_ai_demo import GenerativeAIDemo

class GenerativeAIPage(QWidget):
    def __init__(self):
        super().__init__()
        self.demo = GenerativeAIDemo()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h1>Generative AI Demo</h1>"))
        layout.addWidget(QLabel("<p>Enter a prompt and watch AI generate content!</p>"))
        self.prompt_input = QTextEdit()
        layout.addWidget(self.prompt_input)
        settings_layout = QHBoxLayout()
        self.temp_box = QSpinBox()
        self.temp_box.setRange(1, 10)
        self.temp_box.setValue(7)
        settings_layout.addWidget(QLabel("Creativity (1-10):"))
        settings_layout.addWidget(self.temp_box)
        layout.addLayout(settings_layout)
        self.generate_btn = QPushButton("Generate")
        layout.addWidget(self.generate_btn)
        self.generate_btn.clicked.connect(self.run_generation)
        self.output_area = QTextEdit()
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)
        self.setLayout(layout)

    def run_generation(self):
        prompt = self.prompt_input.toPlainText()
        temperature = self.temp_box.value() / 10
        self.output_area.setText("⏳ Generating... Please wait.")
        QApplication.processEvents()  # Update UI
        try:
            output = self.demo.generate_text(prompt, temperature=temperature, max_tokens=200)
            self.output_area.setText(output)
        except Exception as e:
            self.output_area.setText(f"⚠️ Error: {str(e)}")