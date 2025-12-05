import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout
from data.concepts import CONCEPT_INFO
from views.sidebar import Sidebar
from views.concept_page import ConceptPage
from views.factories.demo_registration import register_demo_models
from views.factories.model_factory import ModelFactory

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Concepts Explorer")
        self.setMinimumSize(1000, 600)
        self.setStyleSheet("background-image: url('images/AI_explorer_background.png');")
        # Create the central container widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        # Horizontal layout: sidebar (left) + content/demo (right)
        layout = QHBoxLayout(central_widget)
        # Sidebar setup
        self.sidebar = Sidebar(default_selection="Concepts Overview")
        self.sidebar.setMaximumWidth(central_widget.width() * 0.5)
        self.sidebar.selection_changed.connect(self.load_module)
        layout.addWidget(self.sidebar, stretch=1)
        # DEFAULT VIEW: Load ConceptPage at startup
        self.visual_area = ConceptPage(CONCEPT_INFO['Concepts Overview'])
        layout.addWidget(self.visual_area)

    def load_module(self, module_name):
        # Load concept page
        concept_page = ConceptPage(CONCEPT_INFO[module_name])
        concept_page.run_demo.connect(self.launch_demo)
        # Replace current widget
        self.visual_area.setParent(None)
        self.visual_area = concept_page
        self.centralWidget().layout().addWidget(self.visual_area)

    def launch_demo(self, module_name):
        try:
            new_widget = ModelFactory.create_model(module_name)
        except ValueError as e:
            print(e)
            return
        self.visual_area.setParent(None)
        self.visual_area = new_widget
        self.centralWidget().layout().addWidget(self.visual_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Register demo models in the factory
    register_demo_models()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
