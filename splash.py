# Eseguire prima di tutto "pip install Pillow"
from PIL import Image

# Carica l'immagine matrice, di dimensione 1285x724
matrice = Image.open("matrice.png")

# Estrai la parte sinistra 1024x724 dell'immagine matrice
parte_sinistra = matrice.crop((0, 0, 1024, 724))

# Estrai la parte destra 261x724 dell'immagine matrice
parte_destra = matrice.crop((1024, 0, 1285, 724))

# Ruota la parte destra di 90 gradi a destra
parte_destra = parte_destra.transpose(Image.ROTATE_270)

# Trasla la parte destra di 2 pixel a sinistra
parte_destra = parte_destra.crop((2, 0, 724, 261))

# Crea una nuova immagine 1024x1024 con sfondo nero
nuova_immagine = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))

# Incolla la parte sinistra nella parte superiore della nuova immagine
nuova_immagine.paste(parte_sinistra, (0, 0))

# Incolla la parte destra traslata a sinistra nella parte inferiore sinistra della nuova immagine
nuova_immagine.paste(parte_destra, (0, 724))

# Salva l'immagine risultante
nuova_immagine.save("immagine_risultante.png", format="PNG", depth=32)

# Lanciare lo script con "py .\splash.py"
