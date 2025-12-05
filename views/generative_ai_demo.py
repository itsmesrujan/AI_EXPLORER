from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QSpinBox, QHBoxLayout

class GenerativeAIDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.__initUI()

    def __initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("<h1>Generative AI Demo</h1>"))
        layout.addWidget(QLabel("<p>Enter a prompt and watch AI generate content!</p>"))
        self.__prompt_input = QTextEdit()
        layout.addWidget(self.__prompt_input)
        settings_layout = QHBoxLayout()
        self.__temp_box = QSpinBox()
        self.__temp_box.setRange(1, 10)
        self.__temp_box.setValue(7)
        settings_layout.addWidget(QLabel("Creativity (1-10):"))
        settings_layout.addWidget(self.__temp_box)
        layout.addLayout(settings_layout)
        self.__generate_btn = QPushButton("Generate")
        layout.addWidget(self.__generate_btn)
        self.__generate_btn.clicked.connect(self.__run_generation)
        self.__output_area = QTextEdit()
        self.__output_area.setReadOnly(True)
        layout.addWidget(self.__output_area)
        self.setLayout(layout)

    def __run_generation(self):
        try:
            prompt = self.__prompt_input.toPlainText()
            temperature = self.__temp_box.value() / 10
            self.__output_area.setText("⏳ Generating... Please wait.")
            QApplication.processEvents()  # Update UI
            from controllers.generative_ai_controller import GenerativeAIController
            controller_instance = GenerativeAIController()
            text = controller_instance.get_generated_text(prompt, temperature)
            self.__output_area.setText(text)
        except Exception as e:
            self.__output_area.setText(f"⚠️ Error: {str(e)}")