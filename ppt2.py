import random

puntos_jugador = 0
puntos_maquina = 0 



while puntos_jugador < 2 and puntos_maquina < 2 :
    
    opciones = ["piedra","papel","tijera"]
    
    jugador = None
    
    while jugador not in opciones :
        jugador = input ("elige piedra,papel o tijera:").lower()
        if jugador not in opciones :
            print("opcion no valida")
   
    maquina = random.choice(opciones)
    print("la maquina eligio",maquina)
    if jugador == maquina :
        print("empate")
        print("jugador:",puntos_jugador,"|","maquina:",puntos_maquina)
    elif jugador == "piedra" and maquina == "tijera" :
        print("ganaste")
        puntos_jugador += 1
        print("jugador:",puntos_jugador,"|","maquina:",puntos_maquina)
    elif jugador == "piedra" and maquina == "papel" :
        print("perdiste")
        puntos_maquina += 1
        print("jugador:",puntos_jugador,"|","maquina:",puntos_maquina)
    elif jugador == "papel" and  maquina == "piedra" :
        print("ganaste")
        puntos_jugador += 1
        print("jugador:",puntos_jugador,"|","maquina:",puntos_maquina)
    elif jugador == "papel" and maquina == "tijera" :
        print("perdiste")
        puntos_maquina += 1
        print("jugador:",puntos_jugador,"|","maquina:",puntos_maquina)
    elif jugador == "tijera" and maquina == "papel" :
        print("ganaste")
        puntos_jugador += 1
        print("jugador:",puntos_jugador,"|","maquina:",puntos_maquina)
    elif jugador == "tijera" and maquina == "piedra" :
        print("perdiste")
        puntos_maquina += 1
        print("jugador:",puntos_jugador,"|","maquina:",puntos_maquina)

print("tus puntos son:",puntos_jugador,"|","puntos maquina:",puntos_maquina)

if puntos_jugador == 2 :
    print("Felicidades,Ganaste el juego")
else:
    print("Mala suerte,Perdiste")