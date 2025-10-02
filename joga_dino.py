import os
import pyautogui as auto

# as = como
# os = é um sistema operacional
# getcwd = pega o caminho da pasta (pega o nome da pasta)

# PEGA O CAMINHO QUE O PYTHON ESTÁ EXECUTANDO O PROGRAMA.
CAMINHO_PASTA = os.getcwd()
print("Caminho da pasta:",CAMINHO_PASTA)


CAMINHO_PASTA_IMAGENS = os.path.join(CAMINHO_PASTA,".\\automacao\\img")
print("Caminho da pasta imagens:",CAMINHO_PASTA_IMAGENS)

# os.path.join monta caminhos | 

lista_fotos = os.listdir(CAMINHO_PASTA_IMAGENS)
print("Conteúdos da lista de fotos:",lista_fotos)


# listdir lista tudo que estiver na pasta img

caminho_dino = os.path.join(CAMINHO_PASTA,".\\automacao\\dino.png")

while True:
    for foto in lista_fotos:
        caminho_da_foto = os.path.join(CAMINHO_PASTA_IMAGENS,foto)
     
        try:# Verificar se a imagem está na tela
            posicao_cacto = auto.locateOnScreen(caminho_da_foto, confidence=0.65)
            posicao_dino = auto.locateOnScreen(caminho_dino, confidence=0.6)
            #Captura o erro se a imagem não estiver na tela
        except:
            posicao_cacto = None
        
        else:
            #Se encontrar a imagem sem erros, pula.
            print("Imagem localizada:", foto)
            print("posição do dino:",posicao_dino.left)


            if posicao_cacto.left -  posicao_dino.left <= 220:
                auto.press("space")
                auto.keyDown("space")


                                    




# O QUE ESSE PROGRAMA FAZ:
# 1. VERIFICA ONDE ESTÁ RODANDO
# 2. PEGA O CAMINHO DA PASTA DE IMAGENS
# 3. PEGA UMA LISTA DE TODAS AS FOTOS DENTRO DE IMAGENS
# 4. PERCORRE A LISTA DE IMAGENS PEGANDO O CAMINHO DAS IMAGENS

# O QUE ESE PROGRAMA TEM QUE FAZER:
# 5. VERIFICAR SE A IMAGEM EXISTE NA TELA
# 6. PULAR SE A IMAGEM ESTIVER NA TELA


