# Função para simular a ideia de locais de doações próximos 
def locaisDoacoes():
    try:
        cep = int(input("Informe o seu CEP (somente números): "))
        print(f"Os locais de doações próximos ao CEP {cep} são:")
        # Apenas para simular, nesse sentido. Poderá ser feito de maneira mais trabalhada com API e geolocalizações posteriormente!
        print("\n • ONG Banco de alimentos; \n • Lar das crianças \n • Anjos da noite \n • Conab \n") 
    except ValueError:
        print("Por favor, informe somente números e não envie informações vazias! A SFOME agradece!")

locaisDoacoes()