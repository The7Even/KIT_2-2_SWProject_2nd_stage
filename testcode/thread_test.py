import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel
)
from PyQt6.QtCore import QTimer, Qt


class ProgressDemo(QWidget):
    def __init__(self):
        super().__init__()
        # 진행 상태를 기억할 변수 (0 ~ 100)
        self.progress = 0

        # 주기적 반복을 처리할 QTimer 준비
        self.timer = QTimer(self)
        self.timer.setInterval(100)  # 100ms 간격
        self.timer.timeout.connect(self.advance_one_step)

        self.init_ui()

    def init_ui(self):
        # 1. 위젯 생성
        self.status_label = QLabel(f"현재 진행 상태: {self.progress}%", self)
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setStyleSheet("font-size: 16px; font-weight: bold; margin: 15px;")

        self.step_btn = QPushButton("1 Step 진행", self)
        self.auto_btn = QPushButton("자동 진행 시작", self)

        # 2. 버튼 클릭 이벤트 연결
        self.step_btn.clicked.connect(self.on_step_clicked)
        self.auto_btn.clicked.connect(self.toggle_auto)

        # 3. 레이아웃 배치
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.step_btn)
        btn_layout.addWidget(self.auto_btn)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.status_label)
        main_layout.addLayout(btn_layout)

        self.setLayout(main_layout)
        self.setWindowTitle("PyQt6 진행 단계 제어 예제")
        self.resize(320, 160)

    def update_display(self):
        # 화면의 라벨 텍스트를 현재 상태값으로 갱신
        self.status_label.setText(f"현재 진행 상태: {self.progress}%")

    def advance_one_step(self):
        # 1%씩 전진시키는 공통 로직
        if self.progress < 100:
            self.progress += 1
            self.update_display()
        else:
            # 100% 도달 시 타이머 자동 중지
            self.stop_timer()

    def on_step_clicked(self):
        # 1 step 버튼을 눌렀을 때
        if self.progress < 100:
            self.advance_one_step()

    def toggle_auto(self):
        # 자동 버튼을 누르면 시작/정지 토글
        if self.timer.isActive():
            self.stop_timer()
        else:
            if self.progress < 100:
                self.timer.start()
                self.auto_btn.setText("자동 진행 일시정지")

    def stop_timer(self):
        # 타이머 정지 및 버튼 라벨 초기화
        self.timer.stop()
        self.auto_btn.setText("자동 진행 시작")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProgressDemo()
    window.show()
    sys.exit(app.exec())