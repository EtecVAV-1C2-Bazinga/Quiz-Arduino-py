"""
Quiz Interativo sobre Arduino
Curso Técnico em Desenvolvimento de Sistemas - 1ºC2
Atividade Avaliativa - 4º Bimestre
Alunos: Felipe Costa Salino / Filipe Tomaz de Aquino / João Vitor Lopes de Souza / Victor Camargo de Angelo

"""

import random

# ===============================
# Dados do quiz - 50 perguntas
# ===============================

# Banco de Dados com as 50 questões sobre Arduino
quiz_data = [
    {"pergunta": "1. O que é o Arduino?",
     "respostas": ["A) Um tipo de sensor",
                   "B) Um microcontrolador programável de código aberto",
                   "C) Um software de edição de texto",
                   "D) Um sistema operacional",
                   "E) Um tipo de motor"],
     "correta": "B"},

    {"pergunta": "2. Qual linguagem é usada para programar o Arduino?",
     "respostas": ["A) Python", "B) C++", "C) Java", "D) Ruby", "E) Pascal"],
     "correta": "B"},

    {"pergunta": "3. Qual é o microcontrolador do Arduino Uno?",
     "respostas": ["A) ATmega16", "B) ATmega8", "C) ATmega328P", "D) PIC16F877A", "E) ESP32"],
     "correta": "C"},

    {"pergunta": "4. Quantas portas digitais tem o Arduino Uno?",
     "respostas": ["A) 8", "B) 10", "C) 12", "D) 14", "E) 16"],
     "correta": "D"},

    {"pergunta": "5. Quantas portas analógicas o Arduino Uno possui?",
     "respostas": ["A) 4", "B) 5", "C) 6", "D) 8", "E) 10"],
     "correta": "C"},

    {"pergunta": "6. Qual é a tensão de operação do Arduino Uno?",
     "respostas": ["A) 3.3V", "B) 5V", "C) 9V", "D) 12V", "E) 1.5V"],
     "correta": "B"},

    {"pergunta": "7. Qual é a função da porta VIN?",
     "respostas": ["A) Comunicação serial", "B) Entrada de energia externa", "C) Saída PWM",
                   "D) Controle de motores", "E) Leitura de sensores"],
     "correta": "B"},

    {"pergunta": "8. Qual é a função da porta GND?",
     "respostas": ["A) Alimentação positiva", "B) Sinal digital", "C) Terra (referência elétrica)",
                   "D) Saída analógica", "E) Comunicação I2C"],
     "correta": "C"},

    {"pergunta": "9. O que significa PWM?",
     "respostas": ["A) Pulse Width Modulation", "B) Power Wave Mode", "C) Program With Memory",
                   "D) Pulse Wave Method", "E) Power Width Memory"],
     "correta": "A"},

    {"pergunta": "10. Qual pino é usado para comunicação serial TX no Arduino Uno?",
     "respostas": ["A) Pino 0", "B) Pino 1", "C) Pino 2", "D) Pino 3", "E) Pino 13"],
     "correta": "B"},

    {"pergunta": "11. E o pino RX?",
     "respostas": ["A) 0", "B) 1", "C) 2", "D) 3", "E) 13"],
     "correta": "A"},

    {"pergunta": "12. Qual comando é usado para definir o modo de um pino?",
     "respostas": ["A) analogWrite()", "B) pinMode()", "C) digitalRead()", "D) digitalWrite()", "E) setup()"],
     "correta": "B"},

    {"pergunta": "13. Qual comando liga um LED?",
     "respostas": ["A) digitalWrite(pino, LOW);", "B) digitalWrite(pino, HIGH);",
                   "C) pinMode(pino, INPUT);", "D) analogRead(pino);", "E) delay(pino);"],
     "correta": "B"},

    {"pergunta": "14. Qual função pausa o programa por um tempo determinado (em milissegundos)?",
     "respostas": ["A) wait()", "B) delay()", "C) pause()", "D) sleep()", "E) hold()"],
     "correta": "B"},

    {"pergunta": "15. A função setup() é executada:",
     "respostas": ["A) Uma vez no início do programa", "B) Sempre que um botão é pressionado",
                   "C) Repetidamente durante o loop", "D) Apenas quando há erro", "E) Nunca é obrigatória"],
     "correta": "A"},

    {"pergunta": "16. A função loop() é executada:",
     "respostas": ["A) Apenas uma vez", "B) Continuamente", "C) Quando chamada pelo usuário",
                   "D) Apenas com interrupção", "E) Apenas em modo debug"],
     "correta": "B"},

    {"pergunta": "17. Qual comando lê o valor de um sensor analógico?",
     "respostas": ["A) digitalRead()", "B) analogRead()", "C) analogWrite()", "D) readSensor()", "E) pinMode()"],
     "correta": "B"},

    {"pergunta": "18. Qual comando envia dados pela porta serial?",
     "respostas": ["A) Serial.print()", "B) Serial.begin()", "C) Serial.end()", "D) Serial.read()", "E) Serial.available()"],
     "correta": "A"},

    {"pergunta": "19. Qual comando inicia a comunicação serial?",
     "respostas": ["A) Serial.start()", "B) Serial.begin(9600);", "C) Serial.open();", "D) Serial.connect();", "E) Serial.enable();"],
     "correta": "B"},

    {"pergunta": "20. O pino 13 do Arduino Uno geralmente está conectado a:",
     "respostas": ["A) Um botão", "B) Um LED embutido", "C) Um sensor de temperatura", "D) O reset", "E) O GND"],
     "correta": "B"},

    {"pergunta": "21. Qual unidade mede a resistência elétrica?",
     "respostas": ["A) Volt", "B) Ampere", "C) Ohm", "D) Watt", "E) Farad"],
     "correta": "C"},

    {"pergunta": "22. Qual sensor mede a temperatura?",
     "respostas": ["A) LDR", "B) DHT11", "C) HC-SR04", "D) PIR", "E) MPU6050"],
     "correta": "B"},

    {"pergunta": "23. O sensor LDR mede:",
     "respostas": ["A) Temperatura", "B) Luz", "C) Som", "D) Distância", "E) Umidade"],
     "correta": "B"},

    {"pergunta": "24. O sensor ultrassônico HC-SR04 mede:",
     "respostas": ["A) Temperatura", "B) Luz", "C) Distância", "D) Som", "E) Movimento"],
     "correta": "C"},

    {"pergunta": "25. O módulo Bluetooth mais comum usado com Arduino é:",
     "respostas": ["A) HC-05", "B) DHT11", "C) DS18B20", "D) ESP8266", "E) L298N"],
     "correta": "A"},

    {"pergunta": "26. O módulo ESP8266 é usado para:",
     "respostas": ["A) Comunicação Bluetooth", "B) Comunicação Wi-Fi", "C) Comunicação Serial",
                   "D) Controle de motores", "E) Medir temperatura"],
     "correta": "B"},

    {"pergunta": "27. Qual é o software oficial de programação do Arduino?",
     "respostas": ["A) Arduino Maker", "B) Arduino IDE", "C) Arduino Studio", "D) Arduino Lab", "E) Visual Arduino"],
     "correta": "B"},

    {"pergunta": "28. A extensão dos arquivos do Arduino é:",
     "respostas": ["A) .ino", "B) .ard", "C) .cpp", "D) .txt", "E) .exe"],
     "correta": "A"},

    {"pergunta": "29. O que o comando analogWrite() faz?",
     "respostas": ["A) Lê um valor analógico", "B) Gera um sinal PWM", "C) Escreve texto na serial",
                   "D) Configura um pino digital", "E) Reinicia o programa"],
     "correta": "B"},

    {"pergunta": "30. Quantos bits tem a conversão analógica do Arduino Uno?",
     "respostas": ["A) 8 bits", "B) 10 bits", "C) 12 bits", "D) 14 bits", "E) 16 bits"],
     "correta": "B"},

    {"pergunta": "31. O valor máximo retornado por analogRead() é:",
     "respostas": ["A) 255", "B) 512", "C) 1023", "D) 2048", "E) 4096"],
     "correta": "C"},

    {"pergunta": "32. A função map() serve para:",
     "respostas": ["A) Converter intervalos de valores", "B) Medir distância", "C) Enviar dados via Bluetooth",
                   "D) Controlar motores", "E) Calcular médias"],
     "correta": "A"},

    {"pergunta": "33. Qual comando limpa o monitor serial?",
     "respostas": ["A) Serial.clear()", "B) Não existe comando nativo", "C) Serial.reset()", "D) Serial.flush()", "E) Serial.end()"],
     "correta": "B"},

    {"pergunta": "34. O pino A0 é usado para:",
     "respostas": ["A) Comunicação digital", "B) Entrada analógica", "C) Saída PWM", "D) Reset", "E) Alimentação"],
     "correta": "B"},

    {"pergunta": "35. Qual comando configura a taxa de comunicação serial?",
     "respostas": ["A) Serial.config()", "B) Serial.begin(9600)", "C) Serial.start()", "D) Serial.setRate()", "E) Serial.init()"],
     "correta": "B"},

    {"pergunta": "36. O que acontece se conectar 12V direto no pino 5V?",
     "respostas": ["A) Nada", "B) O Arduino funciona normalmente", "C) Queima a placa", "D) O LED pisca", "E) O programa reinicia"],
     "correta": "C"},

    {"pergunta": "37. Qual componente controla a alimentação do Arduino?",
     "respostas": ["A) Microcontrolador", "B) Regulador de tensão", "C) Resistor", "D) Capacitor", "E) Diodo"],
     "correta": "B"},

    {"pergunta": "38. Um resistor serve para:",
     "respostas": ["A) Aumentar corrente", "B) Reduzir corrente", "C) Armazenar carga", "D) Gerar energia", "E) Regular tensão de rede"],
     "correta": "B"},

    {"pergunta": "39. O símbolo Ω representa:",
     "respostas": ["A) Corrente", "B) Resistência", "C) Tensão", "D) Potência", "E) Indutância"],
     "correta": "B"},

    {"pergunta": "40. Qual unidade mede a corrente elétrica?",
     "respostas": ["A) Ohm", "B) Volt", "C) Watt", "D) Ampere", "E) Coulomb"],
     "correta": "D"},

    {"pergunta": "41. O que faz a função Serial.read()?",
     "respostas": ["A) Lê dados recebidos via serial", "B) Envia dados via serial", "C) Fecha a conexão serial",
                   "D) Escreve texto no monitor", "E) Inicia comunicação"],
     "correta": "A"},

    {"pergunta": "42. O módulo L298N é usado para:",
     "respostas": ["A) Ler sensores", "B) Controlar motores DC", "C) Medir distância", "D) Comunicação Wi-Fi", "E) Ligar LEDs"],
     "correta": "B"},

    {"pergunta": "43. O pino RESET serve para:",
     "respostas": ["A) Enviar dados", "B) Reiniciar o microcontrolador", "C) Ligar LEDs",
                   "D) Alimentar sensores", "E) Aumentar tensão"],
     "correta": "B"},

    {"pergunta": "44. Qual biblioteca é usada para o sensor ultrassônico?",
     "respostas": ["A) Wire.h", "B) Servo.h", "C) Ultrasonic.h", "D) LiquidCrystal.h", "E) Stepper.h"],
     "correta": "C"},

    {"pergunta": "45. Qual biblioteca é usada para LCD 16x2?",
     "respostas": ["A) Wire.h", "B) LiquidCrystal.h", "C) LCD.h", "D) Display.h", "E) Print.h"],
     "correta": "B"},

    {"pergunta": "46. O display LCD 16x2 possui:",
     "respostas": ["A) 16 colunas e 2 linhas", "B) 2 colunas e 16 linhas", "C) 8 colunas e 2 linhas",
                   "D) 2 colunas e 8 linhas", "E) 32 caracteres fixos"],
     "correta": "A"},

    {"pergunta": "47. O sensor PIR detecta:",
     "respostas": ["A) Luz", "B) Calor/movimento", "C) Som", "D) Distância", "E) Vibração"],
     "correta": "B"},

    {"pergunta": "48. O que é uma “shield”?",
     "respostas": ["A) Um sensor", "B) Uma placa de expansão", "C) Um motor", "D) Um resistor", "E) Um cabo de comunicação"],
     "correta": "B"},

    {"pergunta": "49. O pino 3, 5, 6, 9, 10 e 11 do Arduino Uno são:",
     "respostas": ["A) Entradas analógicas", "B) Saídas PWM", "C) Portas seriais",
                   "D) Entradas digitais apenas", "E) Pinos GND"],
     "correta": "B"},

    {"pergunta": "50. O que significa IDE?",
     "respostas": ["A) Integrated Design Environment", "B) Integrated Development Environment",
                   "C) Interactive Device Emulator", "D) Internal Debug Environment", "E) Integrated Digital Editor"],
     "correta": "B"}
]

import os

# Função que limpa a tela, usada quando necessário. Para deixar melhor visualmente!!
def limpar_tela():
    """Limpa a tela do console"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Função de mostrar o menu "Principal"
def mostrar_menu():
    """Exibe o menu principal do programa"""

    print("=" * 50) # Usado para dar aquela impressão de uma linha / Separação

    print("          QUIZ INTERATIVO - ARDUINO")
    print("=" * 50)

    # Opções de 1 a 3, para escolher onde ir no menu
    print("1 - Responder Quiz")
    print("2 - Exibir Regras")
    print("3 - Encerrar Programa")
    print("=" * 50)


# Função de mostrar as regras do quiz
def mostrar_regras():
    """Exibe as regras do jogo"""

    # Usando a função de limpar tela, aqui
    limpar_tela()

    print("=" * 50)
    print("              REGRAS DO QUIZ")
    print("=" * 50)

    # Regras em "ul", demonstrando cada regra do quiz / jogo
    print("• O quiz contém 20 perguntas sobre Arduino")
    print("• Cada pergunta vale 0,5 ponto")
    print("• Nota máxima: 10,0 pontos")
    print("• As perguntas são de múltipla escolha (A-E)")
    print("• Digite apenas a letra da alternativa")
    print("• Perguntas e alternativas são embaralhadas")
    print("• Boa sorte!")

    print("=" * 50)
    input("Pressione Enter para voltar ao menu...")

# Função que sorteia 20 questões do banco de dados a cima
def sortear_questoes():
    """Seleciona aleatoriamente 20 perguntas do banco de dados"""
    return random.sample(quiz_data, 20)

# Função que embaralha a sequencia das alternativas - mantendo a resposta certa
def embaralhar_alternativas(questao):

    """Embaralha o conteúdo das alternativas mas mantém A, B, C, D, E na ordem"""

    # Cria uma cópia das alternativas
    alternativas = questao["respostas"].copy()
    
    # Extrai apenas o conteúdo (remove "A) ", "B) ", etc.)

    conteudos = []
    for alt in alternativas:
        # Pega tudo depois do ") " - o conteúdo da alternativa
        
        conteudo = alt.split(") ", 1)[1]
        conteudos.append(conteudo)
    
    # Embaralha apenas os conteúdos
    random.shuffle(conteudos)
    
    # Reconstrói as alternativas com as letras na ordem correta
    alternativas_embaralhadas = []
    letras = ["A", "B", "C", "D", "E"]
    
    for i, letra in enumerate(letras):
        alternativas_embaralhadas.append(f"{letra}) {conteudos[i]}")
    
    # Encontra qual é a nova posição da resposta correta
    resposta_original_correta = None
    for alt in questao["respostas"]:
        if alt.startswith(questao["correta"] + ")"):
            resposta_original_correta = alt.split(") ", 1)[1]
            break
    
    # Encontra em qual posição (letra) está a resposta correta agora
    for i, conteudo in enumerate(conteudos):
        if conteudo == resposta_original_correta:
            nova_letra_correta = letras[i]
            break
    
    return alternativas_embaralhadas, nova_letra_correta

# Função que exibe as questões e alternativas de forma aleatorias
def exibir_questao(numero, questao, alternativas_embaralhadas):
    """Exibe uma questão com suas alternativas embaralhadas"""

    print(f"\nQuestão {numero}: {questao['pergunta']}") # Exibe a questão e seu numero

    print("-" * 60) # Linha criada para o espaçamento
    
    for alternativa in alternativas_embaralhadas:
        print(alternativa) # Exibe as Alternativas agora embaralhadas
    
    print("-" * 60)

# Função que verifica se a reposta do Usuario está correta
def verificar_resposta(resposta_usuario, resposta_correta):

    """Verifica se a resposta do usuário está correta"""

    return resposta_usuario.upper() == resposta_correta # Se a resposta do usuario for iguala a certa, transformando ela em MAIUSCULA


