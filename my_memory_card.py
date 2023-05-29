from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
from random import *
app = QApplication([])

window=QWidget()

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основана Москва?')

RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('1147')
rbtn_2 = QRadioButton('1242')
rbtn_3 = QRadioButton('1861')
rbtn_4 = QRadioButton('1943')
RadioGroup= QButtonGroup()
RadioGroup.addButton = rbtn_1
RadioGroup.addButton = rbtn_2
RadioGroup.addButton = rbtn_3
RadioGroup.addButton = rbtn_4
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

TextGroupBox = QGroupBox('Результаты')
lb_Result = QLabel('да')
lb_Correct = QLabel('ответы здесь')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignRight))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)

TextGroupBox.setLayout(layout_res)
layot_line1 = QHBoxLayout()
layot_line2 = QHBoxLayout()
layot_line3 = QHBoxLayout()


layot_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layot_line2.addWidget(RadioGroupBox)
layot_line2.addWidget(TextGroupBox)
TextGroupBox.hide()


layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(TextGroupBox)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
window.setLayout(layout_card)


def show_question():
    RadioGroupBox.show()
    TextGroupBox.hide()
    btn_OK.setText('Атвечаать..')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_result():
    RadioGroupBox.hide()
    TextGroupBox.show()
    btn_OK.setText('Давай дальше')


def check_answer():
    if answers[0].isChecked():
        lb_Result.setText('ХАРОШ ПРОСТО')
        window.score += 1 
        show_result()
        print('Статистика \n-Всего вопросов:', window.total, '\n')
        print('Рейтинг', window.score/window.total*100,'%')
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        lb_Result.setText('F')
        show_result()
        print('Статистика \n-Всего вопросов:', window.total, '\n')
        print('Рейтинг', window.score/window.total*100,'%')

def next_question():
    window.total += 1
    cur_question=randint(0,len(questions_list)-1)
    v = questions_list[cur_question]
    print('Статистика \n-Всего вопросов:', window.total, '\n')
    ask(v)



class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('после какой минуты к покупке доступен aganim`s shard???','15','2','0','30'))
questions_list.append(Question('сколько персонажей в DOTA2???','129','99','42','10'))
questions_list.append(Question('Сколько линий в DOTA2',"3",'1','0','вопрос плохой(('))
questions_list.append(Question('у какого героя наибольший стартовый урпон???','Treant Protector','Chaos Knight','Lina','Pudge)))'))
#questions_list.append(Question('кто саппорт?',''))

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    lb_Question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    show_question()

def cl():
    if btn_OK.text()== 'ответить':
        check_answer()
    else:
        next_question()


window.setLayout(layout_card)
window.setWindowTitle('ХАХАХАХАХА')

btn_OK.clicked.connect(cl)
window.score=0
window.total = 0
next_question()



window.show()
app.exec()



