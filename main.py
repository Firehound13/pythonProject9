from config import PAIS
from helpers import top_notícias

if __name__ == '__main__':
    notícias = top_notícias(PAIS)

    print(f"**** Listando as top notícias do país {PAIS.upper()} ****")

    for numero in range(len(notícias)):
        print(f"{numero + 1} - {notícias[numero]}")



