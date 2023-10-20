print('hello word')
#game animal secreto 2
animal_secreto = "elefante"
palpite = ""
dicas = [
    'é grande',
    'tem tromba',
    'aparece no filme dumbo']
tentativa = 0
while palpite != animal_secreto:
  print(f"Dica nº{tentativa} o animal {dicas[tentativa]}")
  palpite = input("adivinhe o aninal que estou pensando  ")
  tentativa += 1
  if tentativa == 3:
    print('acabouuu, game ouver!')

  print("parabens você acertouu!")