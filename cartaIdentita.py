# compilare una carta di identità usando il dizionario
persona = {}

name = input("Come ti chiami? ")
persona["name"] = name
print(persona)

age = input("Quanti anni hai? ")
persona["age"] = age
print(persona)

job = input("Cosa fai nella vita? ")
persona["job"] = job
print(persona)

key = input("Che altro vuoi aggiungere? ")
value = input(f"qual è il tuo {key}")
persona[key] = value
print(persona)