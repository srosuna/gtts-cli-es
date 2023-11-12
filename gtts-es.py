import os

input_file = input("Introduce el nombre del archivo de entrada: ")
output_file = input("Introduce el nombre del archivo de salida: ")

os.system(f"gtts-cli -f {input_file} -o {output_file} -l es")


#Realizado por Samuel R Osuna comentarios y donaciones en criptomonedas a @srosuna1 en X.com  paypal.me/srojas1974
