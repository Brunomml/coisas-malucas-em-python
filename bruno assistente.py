import time
import jogo
import tabuada
import datetime
import androidhelper

droid = androidhelper.Android()

d = datetime.date.today().day
m = datetime.date.today().month
a = datetime.date.today().year

hora = time.strftime('%H:%M')
print(hora)

nome = str(input('digite seu nome:'))
droid.ttsSpeak(f'bem vindo {nome}')

while True:
    r = str(input('digite algo:'))
    
    if r == 'que dia é hoje':
        droid.ttsSpeak(f'dia {d} do mes {m} do ano {a}')
        
    if r == 'oi' or r == 'bom dia':
        droid.ttsSpeak(f'oi {nome}, bom dia')
         
    if r == 'ajuda':
        droid.ttsSpeak('você pode escrever')
        print('oi\nbom dia\nque dia é hoje\njogo\ntabuada')

    if r == 'tabuada':
        droid.ttsSpeak('iniciando tabuada')
        time.sleep(2)
        tabuada.tabu()
        
    if r == 'jogo':
        droid.ttsSpeak('iniciando jogo')
        time.sleep(2)
        jogo.sorte()
    
    if r == 'hora':
        print(hora)
