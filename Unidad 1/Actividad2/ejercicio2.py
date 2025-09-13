# Programa que convierta una calificación numérica en letra (ej. 90–100 → A, 80–89 → B, etc.).
calif = int(input("Ingrese su calificación: "))

if calif <= 100 and calif >= 91:
    print ("Tienes una A.")
elif calif <= 90 and calif >= 81:
    print ("Tienes una B.")
elif calif <= 80 and calif >= 71:
    print ("Tienes una C.")
elif calif <= 70 and calif >= 61:
    print ("Tienes una D.")
elif calif <= 60 and calif >= 51:
    print ("Tienes una E.")
else:
    print ("Tienes una F.")