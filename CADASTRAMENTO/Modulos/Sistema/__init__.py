def RODA_SISTEMA():
    from Modulos import Chrome
    import time
    #IMPORTAÇÕES - PRONTO
    time.sleep(1)
    Chrome.acessar_site()
    # ACESSAR SITE - PRONTO
    time.sleep(5)
    Chrome.senha_e_email()
    # LOGIN - PRONTO
    Chrome.cadastrar_produtos()
    # CADASTRAMENTO - PRONTO
