## Desafio 1

Sua primeira tarefa como estagiário será implementar a criação de contas de e-mail para alunos da UFF. Para isso,
será necessário ler o [arquivo csv](alunos.csv) que contém os dados dos alunos e, de acordo com o nome e o status do aluno oferecer um conjunto de
opções de e-mail para ele escolher. Ao final do processo, o aluno recebe uma mensagem informando que sua conta será criada
nos próximos minutos.

**Regras:**
* Apenas alunos ativos podem criar um UFFMail
* As opções de UFFMail devem ser geradas de acordo com o nome do aluno
* Um aluno só pode ter um UFFMail
* Utilizar Orientação a Objetos para resolver o problema
* Livre escolha para a linguagem a ser utilizada

 
**Exemplo**
```bash
Digite sua matrícula:
105457

Laura, por favor escolha uma das opções abaixo para o seu UFFMail
1 - laura_azevedo@id.uff.br
2 - lauraac@id.uff.br
3 - lauracunha@id.uff.br
4 - lcunha@id.uff.br
5 - lazevedocunha@id.uff.br

1

A criação de seu e-mail (laura_azevedo@id.uff.br) será feita nos próximos minutos.
Um SMS foi enviado para 99999-9971 com a sua senha de acesso.
```


**Executando**
- Instalar corretamente o Python27 no computador onde será executado.
- Iniciar o prompt de comando 
- Comando: cd (local dos arquivos)
- Comando: python emailGen.py
