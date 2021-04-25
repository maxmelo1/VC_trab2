# VC_trab2

Segundo trabalho de visão computacional.

## Organização

### Exercício 1 - Convolução

- 1.1 Método implementado dentro do arquivo [main.py](/ex1-convolucao/main.py).
- 1.2.a: Filtro de média aplicado por kernel 3x3 e 5x5. A imagem alvo é mostrada abaixo.
![Imagem Original](/ex1-convolucao/imgs/noisy.jpg)

  - O resultado da convolução com kernel 3x3 é mostrado abaixo.
  ![Imagem Original](/ex1-convolucao/out/a_3_3.png)

  - O resultado da convolução com kernel 5x5 é mostrado abaixo.
  ![Imagem Original](/ex1-convolucao/out/a_5_5.png)

- 1.2.b: O método para geração de kernel gaussiano, dado valor do desvio padrão é implementado no método getGaussianKernel, no arquivo [main.py](/ex1-convolucao/main.py). As imagens resultantes da convolução de kernel com $\sigma= 1,2,3$ seguem abaixo.
![Imagem Original](/ex1-convolucao/out/b_sigma_1.png)
![Imagem Original](/ex1-convolucao/out/b_sigma_2.png)
![Imagem Original](/ex1-convolucao/out/b_sigma_3.png)

As imagens de resultado possuem a mesma dimensão que a imagem de entrada visto aplicação de padding adequado ao tamanho do kernel (padding=floor(kernel size/2)).

### Exercício 2 - Segmentação com K-Means

### Exercício 3 - Subtração de fundo

## Referências
