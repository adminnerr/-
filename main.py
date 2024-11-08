import sys
import math
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt

class EntropyCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("程序熵值计算器")
        self.setGeometry(100, 100, 400, 200)

        # 创建标签并设置对齐
        self.label = QLabel("拖放文件计算熵值", self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 18px; padding: 10px;")

        # 设置布局
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

        # 设置支持拖放文件
        self.setAcceptDrops(True)

    def calculate_entropy(self, file_path):
        """计算文件的熵值"""
        with open(file_path, 'rb') as file:
            byte_data = file.read()
            entropy = 0.0
            for b in range(256):
                freq = byte_data.count(b)
                if freq > 0:
                    prob = freq / len(byte_data)
                    entropy += prob * math.log(prob, 2)
            entropy = -entropy
            return entropy

    def update_label_color(self, entropy_value):
        """根据熵值设置标签的颜色"""
        if entropy_value < 3.0:
            self.label.setStyleSheet("font-size: 18px; padding: 10px; background-color: lightgreen;")
        elif 3.0 <= entropy_value < 4.0:
            self.label.setStyleSheet("font-size: 18px; padding: 10px; background-color: green;")
        elif 4.0 <= entropy_value < 5.0:
            self.label.setStyleSheet("font-size: 18px; padding: 10px; background-color: yellow;")
        elif 5.0 <= entropy_value < 6.0:
            self.label.setStyleSheet("font-size: 18px; padding: 10px; background-color: orange;")
        elif 6.0 <= entropy_value < 7.0:
            self.label.setStyleSheet("font-size: 18px; padding: 10px; background-color: red;")
        else:
            self.label.setStyleSheet("font-size: 18px; padding: 10px; background-color: darkred;")

    def dragEnterEvent(self, event):
        """判断拖入的文件是否有效"""
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        """处理文件拖放事件"""
        file_path = event.mimeData().urls()[0].toLocalFile()
        if file_path:
            entropy_value = self.calculate_entropy(file_path)
            self.label.setText(f"文件熵值: {entropy_value:.4f}")
            self.update_label_color(entropy_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EntropyCalculator()
    window.show()
    sys.exit(app.exec_())
