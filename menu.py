from PyQt6.QtWidgets import*

app = QApplication([])
window = QWidget()
knopka1 = QPushButton("start")
knopka2 = QPushButton("shop")
knopka3 = QPushButton("setting")
knopka4 = QPushButton("exit")

main_lain = QVBoxLayout()
main_lain.addWidget(knopka1)
main_lain.addWidget(knopka2)
main_lain.addWidget(knopka3)
main_lain.addWidget(knopka4)


window.setLayout(main_lain)
knopka1.clicked.connect(start_game)
knopka2.clicked.connect(shop_window)

window.show()
app.exec()