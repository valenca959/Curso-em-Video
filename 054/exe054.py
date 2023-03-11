from datetime import date
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f"Em que ano a {pess}° pessoa nasceu? "))
    idade = date.today().year - nasc
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print(f"Ao todo tivemos {totmaior} pessoas maiores de idade"
      f"\nE também tivemos {totmenor} pessoas menores de idade")
