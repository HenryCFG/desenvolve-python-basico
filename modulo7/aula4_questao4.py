import random
import os

def imprime_enforcado(erros, estagios):
    """Imprime o estágio do enforcado correspondente ao número de erros."""
    if erros >= 0 and erros < len(estagios):
        print(estagios[erros])
    else:
        print(estagios[-1])

def jogar_forca():
    nome_gabarito_forca = "gabarito_forca.txt"
    nome_gabarito_enforcado = "gabarito_enforcado.txt"
    
    try:
        with open(nome_gabarito_forca, 'r', encoding='utf-8') as f:
            palavras = [p.strip().upper() for p in f if p.strip()]
        
        with open(nome_gabarito_enforcado, 'r', encoding='utf-8') as f:
            estagios_raw = f.read()
            estagios = [s.strip() for s in estagios_raw.split("=========")]
            estagios = [e for e in estagios if e]
            
    except FileNotFoundError:
        print(f"Erro: Certifique-se de que os arquivos '{nome_gabarito_forca}' e '{nome_gabarito_enforcado}' existam.")
        return

    if not palavras:
        print("Erro: O arquivo de palavras está vazio.")
        return
        
    palavra_secreta = random.choice(palavras)
    letras_adivinhadas = set()
    erros = 0
    max_erros = 6 
    
    print("\n--- Jogo da Forca ---\n")

    while erros < max_erros:
        palavra_mascarada = ""
        vitoria = True
        for letra in palavra_secreta:
            if letra in letras_adivinhadas:
                palavra_mascarada += letra + " "
            else:
                palavra_mascarada += "_ "
                vitoria = False

        print(f"Palavra: {palavra_mascarada}")
        
        if vitoria:
            print(f"\n🏆 Parabéns! Você acertou a palavra: {palavra_secreta} 🏆")
            return

        print(f"Erros: {erros}/{max_erros}")
        print(f"Letras usadas: {sorted(list(letras_adivinhadas - set(palavra_secreta)))}")
        imprime_enforcado(erros, estagios)

        while True:
            tentativa = input("Digite uma letra: ").upper().strip()
            if len(tentativa) == 1 and tentativa.isalpha():
                if tentativa in letras_adivinhadas:
                    print("Você já tentou essa letra. Tente outra.")
                else:
                    letras_adivinhadas.add(tentativa)
                    break
            else:
                print("Entrada inválida. Digite apenas uma letra.")

        if tentativa not in palavra_secreta:
            erros += 1
            print("❌ Erro! Essa letra não está na palavra.")
        else:
            print("✅ Acerto!")

    imprime_enforcado(erros, estagios)
    print("\n💀 Você foi enforcado!")
    print(f"A palavra era: {palavra_secreta}")
