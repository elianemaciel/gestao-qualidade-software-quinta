## Exercícios:

___________________________________________________________________________________________________________________________________________________________________________________________________

**Exercício: Testando uma Função de Fatorial**

Você foi encarregado de escrever testes unitários para uma função de cálculo de fatorial em Python. Sua tarefa é escrever testes para garantir que a função fatorial(n) esteja implementada corretamente.

A função fatorial(n) deve retornar o fatorial de um número inteiro não negativo n. O fatorial de um número n é o produto de todos os inteiros positivos menores ou iguais a n.

Por exemplo:

-  O fatorial de 0 é 1.
-  O fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.

Instruções:

Escreva testes para a função fatorial(n) para verificar se ela retorna o resultado correto para diferentes valores de n.
Certifique-se de testar os seguintes casos:
- n igual a 0.
- n igual a 1.
- n igual a um número positivo maior que 1.
- n igual a um número negativo (nesse caso, a função deve lançar uma exceção).
Use a biblioteca de testes padrão do Python, como unittest ou pytest, para escrever e executar os testes.
- Crie um PR com o código gerado (Nesse repositório) e peça a um colega para que faça a revisão.

________________________________________________________________________________________________________________________________________________________________________________________________

**Exercício: Testando uma Função de Fibonacci**

Suponha uma função fib(n), que retorna o n-ésimo termo da sequência de Fibonacci, isto é, fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3, etc. Escreva um teste de unidade para essa função.
- Crie um PR com o código gerado (Nesse repositório) e peça a um colega para que faça a revisão.
_____________________________________________________________________________________________________________________________________________________________________________________________________

**Exercício: Testando uma Função de Fibonacci**

Seja a seguinte função. Observe que ela possui quatro comandos, sendo dois deles if. Logo, esses dois ifs geram quatro branches:

```void f(int x, int y) {
  if (x > 0) {
     x = 2 * x;
     if (y > 0) {
        y = 2 * y;
     }
  }
}
```

Supondo o código acima, crie os testes necessários e preencha uma tabela com os valores da cobertura de comandos e cobertura de branches obtidos com os testes especificados.
