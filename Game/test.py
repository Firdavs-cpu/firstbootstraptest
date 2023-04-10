from browser import document,html,timer
import random

# Construction de la calculatrice

calc = html.TABLE(id='con')
lines = ['камень','ножница','бумага']

calc <= (html.DIV('DISPLAY',id='div'))
calc <= (html.DIV(100,id='balans'))
calc <= (html.DIV(html.TD(line,id='result') for line in lines))

document <= calc

result = document["result"] # direct acces to an element by its id
div = document["div"]
balans = document['balans']
def action(event):
    if balans.text == '0':
        div.text = 'Ты шо, как ты проиграл???'
        return 

    element = event.target
    value = element.text
    robot = random.choice(lines)
    if value==robot:
        div.text='Ничея'
    elif value in "камень":
        if robot == 'бумага':
            div.text = 'Вы проиграли'
            balans.text = int(balans.text)-10
        elif robot == 'ножница':
            div.text = "Вы выиграли"
            balans.text = int(balans.text)-10
    elif value == "ножница":
        if robot == 'камень':
            div.text = 'Вы проиграли'
            balans.text = int(balans.text)-10
        elif robot == 'бумага':
            div.text = "Вы выиграли"
            balans.text = int(balans.text)-10
    elif value == "бумага":
        if robot == 'ножница':
            div.text = 'Вы проиграли'
            balans.text = int(balans.text)-10
        elif robot == 'камень':
            div.text = "Вы выиграли"
            balans.text = int(balans.text)-10


def timering(ev):
    for i in range(10):
        div.text='-'*i
    timer.set_timeout(action, 1000,ev)
    
# Associate function action() to the event "click" on all buttons
for button in document.select("td"):
    button.bind("click", timering)