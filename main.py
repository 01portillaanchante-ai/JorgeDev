meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "Algo aterradador o escalofriante",
            "POV": "Es como decir un porque o una opinion",
            "67": "Es un meme que se refiere a un jugador de basquetbol"
            }

respuesta = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if respuesta in meme_dict.keys():
    print(meme_dict[respuesta])

else:
    print("No existe esta palabra en la lista")
