import pyautogui
import time
import pandas
# IMPORTAÇÕES - PRONTO

email = str(input("\033[33mDigite o E-mail que você usar para acessar o site: \033[0m"))
print("\033[36m" + "=" * 100)
print("E-mail - Pronto")
print("=" * 100 + "\033[0m")
# E-MAIL INFORMADO - PRONTO
senha = str(input("\033[33mDgite a Senha que você usar para acessar o site: \033[0m"))
print("\033[36m" + "=" * 100)
print("Senha - Pronto")
print("=" * 100 + "\033[0m")
# SENHA INFORMADA - PRONTO

def acessar_site():
    print("\033[32m" + "=" * 100)
    print("Abrindo o Chrome...")
    print("=" * 100 + "\033[0m")
    # TEXTO INCIAL - PRONTO
    time.sleep(1)
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("Chrome")
    time.sleep(1)
    pyautogui.press("enter")
    # ABRIU CHROME - PRONTO
    time.sleep(5)
    link_do_site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
    # LINK PARA ACESSAR O SITE - PRONTO
    pyautogui.write(link_do_site)
    time.sleep(1)
    pyautogui.press("enter")


def senha_e_email():
    time.sleep(5)
    pyautogui.click(x=314, y=434)
    time.sleep(1)
    pyautogui.write(email)
    time.sleep(1)
    pyautogui.press("tab")
    # E-MAIL - PRONTO
    time.sleep(1)
    pyautogui.write(senha)
    time.sleep(1)
    pyautogui.press("enter")
    # SENHA - PRONTO


def cadastrar_produtos():
    tabela = pandas.read_csv("CADASTRAMENTO/Modulos/Banco de Dados/Produtos.csv")
    # TABELA IMPORTADA - PRONTO
    for linha in tabela.index:
        time.sleep(1)
        pyautogui.click(x=260, y=301)
        # INICIAR - PRONTO
        time.sleep(1)
        codigo = tabela.loc[linha, "Código do produto"]
        pyautogui.write(codigo)
        time.sleep(1)
        pyautogui.press("tab")
        # CÓDIGO DO PRODUTO - PRONTO
        time.sleep(1)
        marca = tabela.loc[linha, "Marca do Produto"]
        pyautogui.write(marca)
        time.sleep(1)
        pyautogui.press("tab")
        # MARCA DO PRODUTO - PRONTO
        time.sleep(1)
        tipo = tabela.loc[linha, "Tipo do Produto"]
        pyautogui.write(tipo)
        time.sleep(1)
        pyautogui.press("tab")
        # TIPO DO PRODUTO - PRONTO
        time.sleep(1)
        categoria = tabela.loc[linha, "Categoria do Produto"]
        pyautogui.write(categoria)
        time.sleep(1)
        pyautogui("tab")
        # CATEGORIA DO PRODUTO - PRONTO
        time.sleep(1)
        preço = tabela.loc[linha, "Preço Unitário do Produto"]
        pyautogui.write(preço)
        time.sleep(1)
        pyautogui.press("tab")
        # PREÇO DO PRODUTO - PRONTO
        time.sleep(1)
        custo = tabela.loc[linha, "Custo do Produto"]
        pyautogui.write(custo)
        time.sleep(1)
        pyautogui.press("tab")
        # CUSTO DO PRODUTO - PRONTO
        time.sleep(1)
        obs = tabela.loc[linha, "OBS"]
        if not pandas.isna(obs):
            pyautogui.write(obs)
        pyautogui.press("tab")
        # OBS - PRONTO
        pyautogui.press("enter")
        pyautogui.scroll(5000)
        # VOLTAR PRO COMEÇO - PRONTO
