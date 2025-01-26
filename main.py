import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

login = os.getenv('login')
password = os.getenv('password')

letter_text = ("""Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.""")

friend_name = 'Антон'
web_site = 'https://dvmn.org/profession-ref-program/leon.fissenko/Lw7mi/'
sender_name = 'Лев'

personal_letter = letter_text.replace('%friend_name%', friend_name)
personal_letter = personal_letter.replace('%website%', web_site)
personal_letter = personal_letter.replace('%my_name%', sender_name)

sender_mail = 'LeonardoMcLucky@yandex.ru'
recipient_mail = 'LeoMcLucky@yandex.ru'
email_subject = 'Приглашение!'

letter = """\
From: {Адрес_отправителя}
To: {Адрес_получателя}
Subject: {Заголовок_письма}
Content-Type: text/plain; charset="UTF-8";

{Текст}""".format(Адрес_отправителя=sender_mail, Адрес_получателя=recipient_mail,\
Заголовок_письма=email_subject, Текст=personal_letter)

letter = letter.encode("UTF-8")

email_from = sender_mail
email_to = recipient_mail
message = letter

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(email_from, email_to, message)
server.quit()