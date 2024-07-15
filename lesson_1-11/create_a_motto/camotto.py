fiat = open("motto.txt", "w")

fiat.write("Fiat Lux! \n")
fiat.close()

fiat = open("motto.txt", "a")
fiat.write("Let there be Light!")