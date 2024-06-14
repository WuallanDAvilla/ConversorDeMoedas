#janela
#título
#campos para selecionar as moedas de origem e destino
#botões para converter
#lista de exibição com os nomes das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter
 
#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

janela = customtkinter.CTk()
janela.geometry("300x400")


#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text="Conversor de moedas", font=("arial", 22))

texto_moeda_origem = customtkinter.CTkLabel(janela, text="Selecione a moeda de origem")
campo_moeda_origem1 = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])
texto_moeda_destino = customtkinter.CTkLabel(janela, text="Selecione a moeda de destino")
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values= ["USD", "EUR", "BRL", "BTC"])

def converter_moeda():
    print("Converter Moeda")
botao_converter = customtkinter.CTkButton(janela, text="Converter", command=converter_moeda)

lista_moedas = customtkinter.CTkScrollableFrame(janela)
moeda1 = customtkinter.CTkLabel(lista_moedas, text="USD: Dólar Americano")
moeda2 = customtkinter.CTkLabel(lista_moedas, text="EUR: Euro")
moeda3 = customtkinter.CTkLabel(lista_moedas, text="BRL: Real Brasileiro")
moeda4 = customtkinter.CTkLabel(lista_moedas, text="BTC: BitCoin")


moedas_disponiveis = ["USD: Dólar americano", "EUR: Euro", "BRL: Real Brasileiro", "BTC: BitCoin"]
for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text=moeda)
    texto_moeda.pack()

#colocar os elementos criados na tela
titulo.pack(padx=10, pady=10)
texto_moeda_origem.pack(padx=10, pady=0)
campo_moeda_origem1.pack(padx=10, pady=10)
texto_moeda_destino.pack(padx=10, pady=0)
campo_moeda_origem.pack(padx=10, pady=10)
botao_converter.pack(padx=10, pady=10)
lista_moedas.pack()

#rodar a janela
janela.mainloop()

