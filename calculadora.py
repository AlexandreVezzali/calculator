command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("> Iniciando calculadora...")
        num_one = input("> Digite um número: ")
        symbol = input("> (+) para uma soma; (-) para uma subtração; (*) para uma multiplicação; (/) para uma divisão: ")
        if symbol == "+":
            num_two = input(f"> Digite outro número que irá somar à {num_one}: ")
            result = float(num_one) + float(num_two)
        elif symbol == "-":
            num_two = input(f"> Digite outro número que irá subtrair {num_one}: ")
            result = float(num_one) - float(num_two)
        elif symbol == "*":
            num_two = input(f"> Digite outro número que irá multiplicar {num_one}: ")
            result = float(num_one) * float(num_two)
        elif symbol == "/":
            num_two = input(f"> Digite outro número que irá dividir {num_one}: ")
            result = float(num_one) / float(num_two)
    elif command == "=":
        print(result)
    elif command == "help":
        print("""        
Start - para iniciar a calculadora
=     - para obter o resultado
quit  - para sair da calculadora        
        """)
    elif command == "quit":
        print("Até mais!")
        break
    else:
        print("Não entendi... se está com dificuldade digite o comando 'help' ")