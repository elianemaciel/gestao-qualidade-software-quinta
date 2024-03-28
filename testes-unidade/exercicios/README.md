- 1 - Suponha uma função fib(n), que retorna o n-ésimo termo da sequência de Fibonacci, isto é, fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3, etc. Escreva um teste de unidade para essa função.


6. Seja a seguinte função. Observe que ela possui quatro comandos, sendo dois deles if. Logo, esses dois ifs geram quatro branches:

void f(int x, int y) {
  if (x > 0) {
     x = 2 * x;
     if (y > 0) {
        y = 2 * y;
     }
  }
}
Supondo o código acima, preencha a próxima tabela, com os valores da cobertura de comandos e cobertura de branches obtidos com os testes especificados na primeira coluna (ou seja, a primeira coluna define as chamadas da função f que o teste realiza).