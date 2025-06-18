from PyQt6.QtWidgets import*
from PyQt6.QtGui import*

def shop_window():
    window = QDialog()
    elements = [
        {
           "name": "test1",
            "img": "asteroid (1).png",
            "price": 100
        }
    ]

    elements2 = [
        {
            "name": "test2",
            "img": "rocket (1).png",
            "price": 200
        }
    ]





    main_line = QHBoxLayout()
    for element in elements:
        ver = QVBoxLayout()
        name_lbl = QLabel(element["name"])
        img_pm = QPixmap(element[img])
        img_lbl = QLabel()
        img_lbl.setPixmap(img_pm)
        img_pm = img_pm.scaledToWidth(100)
        price_lbl = QLabel(str(element["price"]))
        buy_btn = QPushButton("Купити")


        ver.addWidget(name_lbl)
        ver.addWidget(img_lbl)
        ver.addWidget(price_lbl)
        ver.addWidget(buy_btn)
        main_line.addLayout(ver)



    for element2 in elements2:
        ver2 = QVBoxLayout()





    window.setLayout(main_line)
    window.show()
    window.exec()