import pygame
from src.config import FERRAMENTAS, DEBUG

class CursorPersonalizado:
    def __init__(self):
        # Carregar todos os cursores das ferramentas (apenas as que têm cursor)
        self.cursores = {}
        
        # Encontrar o primeiro cursor disponível como padrão
        primeiro_cursor = None
        
        for ferramenta_info in FERRAMENTAS.values():
            nome = ferramenta_info["nome"]
            
            # Só processar se a ferramenta tem cursor definido
            if "cursor" in ferramenta_info:
                imagem = pygame.image.load(ferramenta_info["cursor"]).convert_alpha()
                imagem = pygame.transform.scale(imagem, (120, 120))
                imagem.set_colorkey((255, 255, 255))
                self.cursores[nome] = imagem
                
                # Guardar o primeiro cursor encontrado
                if primeiro_cursor is None:
                    primeiro_cursor = nome
        
        # Cursor atual (usar o primeiro encontrado)
        self.ferramenta_atual = primeiro_cursor if primeiro_cursor else "foice"
        
        # Propriedades baseadas no cursor atual
        self.largura = 120
        self.altura = 120
        self.hitbox = pygame.Rect(0, 0, 40, 40)

    def mudar_ferramenta(self, ferramenta):
        """Muda o cursor baseado na ferramenta selecionada"""
        if ferramenta in self.cursores:
            self.ferramenta_atual = ferramenta
        # Se a ferramenta não tem cursor, mantém o atual

    def desenhar(self, screen, posicao):
        # Desenha o cursor atual
        screen.blit(self.cursores[self.ferramenta_atual], posicao)

        # Atualiza hitbox baseada na posição do mouse
        self.hitbox.topleft = (posicao[0] + 30, posicao[1] + 10)

        if DEBUG:
            pygame.draw.rect(screen, (255, 0, 0), self.hitbox, 2)

    def get_hitbox(self):
        return self.hitbox