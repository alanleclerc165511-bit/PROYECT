import random

def generar_pregunta():
    operaciones = ["+", "-", "*", "/"]
    op = random.choice(operaciones)

    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Evitar división entre 0 y hacer divisiones exactas
    if op == "/":
        num1 = num1 * num2

    return num1, num2, op

def calcular_respuesta(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2

def jugar():
    puntaje = 0
    rondas = 5

    print("🎮 Bienvenido al juego de matemáticas")
    print("Resuelve las operaciones:\n")

    for i in range(rondas):
        num1, num2, op = generar_pregunta()
        respuesta_correcta = calcular_respuesta(num1, num2, op)

        print(f"Pregunta {i+1}: {num1} {op} {num2} = ?")
        
        try:
            respuesta_usuario = float(input("Tu respuesta: "))
        except:
            print("Entrada inválida\n")
            continue

        if respuesta_usuario == respuesta_correcta:
            print("✅ Correcto!\n")
            puntaje += 1
        else:
            print(f"❌ Incorrecto. La respuesta era {respuesta_correcta}\n")

    print(f"🏁 Juego terminado. Puntaje: {puntaje}/{rondas}")

# Ejecutar el juego
jugar()
