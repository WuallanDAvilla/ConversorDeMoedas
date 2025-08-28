import customtkinter
import requests
import xmltodict
import os

URL_NOMES_MOEDAS = "https://economia.awesomeapi.com.br/xml/available/uniq"
URL_CONVERSOES = "https://economia.awesomeapi.com.br/xml/available"

def tentar_atualizar_arquivos_xml():
    """Tenta baixar as listas mais recentes da API e salvar nos arquivos XML."""
    print("Tentando atualizar listas de moedas e conversões...")
    try:
        resposta_moedas = requests.get(URL_NOMES_MOEDAS, timeout=5)
        resposta_moedas.raise_for_status()
        with open("moedas.xml", "wb") as f:
            f.write(resposta_moedas.content)
        print("Arquivo 'moedas.xml' atualizado com sucesso.")

        resposta_conversoes = requests.get(URL_CONVERSOES, timeout=5)
        resposta_conversoes.raise_for_status()
        with open("conversoes.xml", "wb") as f:
            f.write(resposta_conversoes.content)
        print("Arquivo 'conversoes.xml' atualizado com sucesso.")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Não foi possível atualizar os arquivos. Erro de conexão: {e}")
        print("Usando os arquivos locais existentes.")
        return False

def carregar_dados_locais():
    """Carrega os dados dos arquivos XML locais."""
    try:
        with open("moedas.xml", "rb") as f:
            dic_moedas = xmltodict.parse(f.read()).get("xml", {})

        with open("conversoes.xml", "rb") as f:
            conversoes_raw = xmltodict.parse(f.read()).get("xml", {})
        
        dic_conversoes = {}
        for par in conversoes_raw:
            origem, destino = par.split("-")
            if origem in dic_conversoes:
                dic_conversoes[origem].append(destino)
            else:
                dic_conversoes[origem] = [destino]
        
        return dic_moedas, dic_conversoes
    except FileNotFoundError as e:
        print(f"ERRO CRÍTICO: Arquivo não encontrado: {e.filename}")
        return None, None
    except Exception as e:
        print(f"ERRO CRÍTICO ao ler arquivos XML: {e}")
        return None, None

def pegar_cotacao_online(moeda_origem, moeda_destino):
    """Obtém a cotação atual para um par de moedas pela internet."""
    link = f"https://economia.awesomeapi.com.br/last/{moeda_origem}-{moeda_destino}"
    try:
        response = requests.get(link, timeout=5)
        response.raise_for_status()
        dados = response.json()
        cotacao = dados[f"{moeda_origem}{moeda_destino}"]["bid"]
        return float(cotacao)
    except requests.exceptions.RequestException:
        return None
    except (KeyError, ValueError):
        return None

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Conversor de Moedas")
        self.geometry("750x550")
        
        tentar_atualizar_arquivos_xml()
        self.dic_moedas, self.dic_conversoes = carregar_dados_locais()

   
        if not self.dic_moedas or not self.dic_conversoes:
            self.mostrar_erro_critico("Erro ao carregar arquivos 'moedas.xml' ou 'conversoes.xml'.\nVerifique se eles estão na pasta do projeto.")
        else:
            self.setup_ui()

    def setup_ui(self):
        """Configura a interface gráfica principal."""
     
        self.font_titulo = ("Arial", 24, "bold")
        self.font_label = ("Arial", 16)
        self.font_resultado = ("Arial", 20, "bold")
        self.font_botao = ("Arial", 18)

       
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1) 

        self.create_widgets()

    def create_widgets(self):
        """Cria todos os elementos visuais da aplicação."""

        customtkinter.CTkLabel(self, text="Conversor de Moedas", font=self.font_titulo).grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        frame_entrada = customtkinter.CTkFrame(self)
        frame_entrada.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        frame_entrada.grid_columnconfigure((0, 2), weight=3)
        frame_entrada.grid_columnconfigure(1, weight=1)

        customtkinter.CTkLabel(frame_entrada, text="De:", font=self.font_label).grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.campo_moeda_origem = customtkinter.CTkOptionMenu(frame_entrada, values=sorted(list(self.dic_conversoes.keys())), command=self.carregar_moedas_destino)
        self.campo_moeda_origem.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.botao_inverter = customtkinter.CTkButton(frame_entrada, text="⇄", font=("", 24), width=50, command=self.inverter_moedas)
        self.botao_inverter.grid(row=1, column=1, padx=5, pady=5, sticky="s")

        customtkinter.CTkLabel(frame_entrada, text="Para:", font=self.font_label).grid(row=0, column=2, padx=10, pady=5, sticky="w")
        self.campo_moeda_destino = customtkinter.CTkOptionMenu(frame_entrada, values=["Selecione uma moeda"])
        self.campo_moeda_destino.grid(row=1, column=2, padx=10, pady=5, sticky="ew")
        self.carregar_moedas_destino(self.campo_moeda_origem.get())

        customtkinter.CTkLabel(frame_entrada, text="Valor:", font=self.font_label).grid(row=2, column=0, padx=10, pady=(15, 5), sticky="w")
        self.campo_valor = customtkinter.CTkEntry(frame_entrada, placeholder_text="1,00", font=self.font_label)
        self.campo_valor.grid(row=3, column=0, columnspan=3, padx=10, pady=5, sticky="ew")
        
        frame_acoes = customtkinter.CTkFrame(self)
        frame_acoes.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        frame_acoes.grid_columnconfigure((0, 1), weight=1)
        
        self.botao_converter = customtkinter.CTkButton(frame_acoes, text="Converter", font=self.font_botao, command=self.converter_moeda)
        self.botao_converter.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        self.botao_limpar = customtkinter.CTkButton(frame_acoes, text="Limpar", font=self.font_botao, command=self.limpar_campos, fg_color="#D32F2F", hover_color="#B71C1C")
        self.botao_limpar.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        self.texto_resultado = customtkinter.CTkLabel(frame_acoes, text="", font=self.font_resultado)
        self.texto_resultado.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

        lista_moedas_frame = customtkinter.CTkScrollableFrame(self, label_text="Moedas Disponíveis para Consulta")
        lista_moedas_frame.grid(row=3, column=0, padx=20, pady=10, sticky="nsew")

        for codigo_moeda in sorted(self.dic_moedas.keys()):
            nome_moeda = self.dic_moedas[codigo_moeda]
            texto_moeda = customtkinter.CTkLabel(lista_moedas_frame, text=f"{codigo_moeda}: {nome_moeda}", font=("", 14), anchor="w")
            texto_moeda.pack(fill="x", padx=10)

    def carregar_moedas_destino(self, moeda_selecionada):
        """Atualiza a lista de moedas de destino quando a de origem muda."""
        lista_moedas_destino = sorted(self.dic_conversoes.get(moeda_selecionada, []))
        self.campo_moeda_destino.configure(values=lista_moedas_destino)
        if lista_moedas_destino:
            self.campo_moeda_destino.set(lista_moedas_destino[0])
        else:
            self.campo_moeda_destino.set("Nenhuma conversão")

    def converter_moeda(self):
        """Executa a conversão quando o botão é clicado."""
        moeda_origem = self.campo_moeda_origem.get()
        moeda_destino = self.campo_moeda_destino.get()
        
        valor_str = self.campo_valor.get().replace(",", ".") or "1.0"
        try:
            valor = float(valor_str)
        except ValueError:
            self.texto_resultado.configure(text="Erro: Valor digitado é inválido.", text_color="orange")
            return

        self.texto_resultado.configure(text="Buscando cotação online...", text_color="gray")
        self.update_idletasks()
        
        cotacao = pegar_cotacao_online(moeda_origem, moeda_destino)
        
        if cotacao:
            resultado = valor * cotacao
            self.texto_resultado.configure(text=f"{valor:,.2f} {moeda_origem} = {resultado:,.2f} {moeda_destino}", text_color="cyan")
        else:
            self.texto_resultado.configure(text="Erro de conexão ao buscar a cotação.", text_color="red")

    def inverter_moedas(self):
        """Inverte as moedas de origem e destino."""
        origem = self.campo_moeda_origem.get()
        destino = self.campo_moeda_destino.get()

        if destino in self.dic_conversoes and origem in self.dic_conversoes[destino]:
            self.campo_moeda_origem.set(destino)
            self.carregar_moedas_destino(destino)
            self.campo_moeda_destino.set(origem)
            self.limpar_campos()

    def limpar_campos(self):
        """Limpa o campo de valor e o resultado."""
        self.campo_valor.delete(0, "end")
        self.texto_resultado.configure(text="")
    
    def mostrar_erro_critico(self, mensagem):
        """Mostra uma mensagem de erro que impede o programa de continuar."""
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        error_label = customtkinter.CTkLabel(self, text=mensagem, font=self.font_titulo, text_color="red", wraplength=500)
        error_label.grid(row=0, column=0)

if __name__ == "__main__":
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    app = App()
    app.mainloop()