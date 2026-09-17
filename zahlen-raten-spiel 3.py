import random
# Spieler begrüßen
print('Wilkommen beim Zahlen-Raten-Spiel😊')
# Spieler nach Name fragen und das Spiel wird vorgestellt
spieler_name = input('Wie heißt du?')
print(f'Hallo {spieler_name}! Ich bin Dino 🦕.')
# Spieler wählt die höchste Zahl aus
max_zahl = int(input('Bis zu welcher Zahl möchtest du raten?'))
print(f'Super! Ich denke mir eine Zahl zwischen 1 bis {max_zahl} aus. ')
secret = random.randint(1, max_zahl)
attempts = 0
while True:
     guess = int(input('Deine Vermutung: '))
     attempts += 1
     if guess < secret:
         print('📉Zu niedrig! Versuche es nochmal. ')
     elif guess > secret:
         print('📈Zu hoch! Versuche es nochmal. ')
     else:
         print(f'richtig! Du hast das GeheimZahl in {attempts} Versuchen erraten.')
         break
# Runde 2: Der computer rät die Zahl.
print('\n' + '=' * 40)
print('Jetzt drehen wie den Spiel um.')
print(f'Denk dir eine Zahl zwische 1 und {max_zahl} aus, aber sag sie mir nicht.')
input('Drücke Enter wenn du bereit bist...')
min_grenze = 1
max_grenze = max_zahl
computer_versuche = 0
while True:
    tip = (min_grenze + max_grenze) //2
    computer_versuche += 1
    print(f'\nMein {computer_versuche}. Vermutung ist: {tip}')
    Feedback = input('Ist meine Zahl zu [h]och, zu [n]iedrig oder [r]ichtig?').lower()
    if Feedback == 'h':
        max_grenze = tip - 1
    elif Feedback == 'n':
        min_grenze =  tip +1
    elif Feedback == 'r':
        print(f'Wow! Ich habe deine Zahl in {computer_versuche} Versuchen erratten.')

        break
# Sterne-Feedback (1-5 Sterne)
print(f'Vielen Dank fürs Spielen, {spieler_name}!')
sterne = input('Wie sehr hattest du Spaß dabei? (1-5 Sterne⭐️):')
print(f'{sterne} Sterne ⭐️WOW! Danke für dein Feedback {spieler_name}.')


















# Willkommen sagen
# spieler nach name fragen
# zahlen raten spiel 1-100(spieler kann auswählen wwelche number range) 
# wie sehr hat es spieler spass gemacht