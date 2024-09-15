Trabalho da faculdade em PYTHON envolvendo o Mapeamento direto da Cache n funcional

Especificações
Capacidade da memória principal: 4096 palavras*

Capacidade total da memória cache: 128 palavras*

Tamanho da cache line: 16 palavras* (isto é, K = 16)

* 1 palavra = 1 número inteiro
  

Funcionamento Básico da Memória Cache (por Mapeamento Direto)
Endereços x gerados pela CPU são divididos internamente nos seguintes blocos de bits:


w — especifica uma das K palavras de uma cache line ou bloco de memória;

r — especifica o índice do cache line;

t — é a etiqueta (tag) que corresponde aos bits restantes do endereço e serve para identificar qual o bloco que memória principal que se encontra atualmente na cache line;

s — corresponde à concatenação dos bits de t e r e representa o número do bloco de memória principal onde está a palavra à qual se deseja acessar.
Algoritmo

Ao receber a solicitação de uma palavra de memória localizada em um endereço x, extrai-se r e t de x e faz-se então a verificação se t é igual ao tag t' contido na linha r da cache line (passo 2 na figura acima). Se forem iguais, houve um "cache hit" (isto é, a palavra solicitada está na cache) e então utiliza-se w para retornar à CPU a palavra na posição w dos dados da cache line (passo 3 na figura).


Se houver um "cache miss", a cache line r corresponde a um outro bloco de memória. Se esta cache line tiver sido alterada, ela é copiada para a memória principal (a partir do endereço formado pela concatenação de t' | r | 000000) (passo 4a na figura). Em todo caso, o bloco s da memória principal é trazido para a cache line e a palavra no endereço solicitado é retornada à CPU (passo 4b na figura). Assim, a cache é atualizada e próximos acessos a endereços próximos produzirão um cache hit.
