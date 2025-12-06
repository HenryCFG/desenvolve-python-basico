import emoji

print("Emojis disponíveis:")
print("❤️ - :red_heart:")
print("👍 - :thumbs_up:")
print("🤔 - :thinking_face:")
print("🥳 - :partying_face:")
print()

frase_codificada = input("Digite uma frase e ela será emojizada: ")

frase_emojizada = emoji.emojize(frase_codificada, language='en')

print("Frase emojizada:")
print(frase_emojizada)
