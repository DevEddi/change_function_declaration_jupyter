# Change Function Declaration

🎓 College: [Faculdade Metodista Granbery](http://granbery.edu.br/)

👨‍🏫 Teacher: [Marco Antônio - Github](https://github.com/marcoaparaujo) | [Linkedin](https://www.linkedin.com/in/marco-ant%C3%B4nio-ara%C3%BAjo/)

📗 Book: [Refatoração - Aperfeiçoando o design de códigos existentes - Martin Fowler](https://www.amazon.com/-/pt/dp/B087N8LKYB/ref=sr_1_1?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=M4T29CCKD30E&keywords=refatora%C3%A7%C3%A3o&qid=1651322207&sprefix=refatora%C3%A7%C3%A3o%2Caps%2C203&sr=8-1)

## Code

O método change function Declaration tem objetivo de substituir o nome da função para algo que possa ser melhor compreendido, além de favorecer compreensão de manutenções futuras. O procedimento que escolhido foi o simples como no livro orienta para execução da refatoração.

O código que escolhi foi uma atividade dado em aula pelo Professor [Ricardo Silva Campos](https://www.linkedin.com/in/ricardo-campos-505220237/). Essa função recebe um parâmetro de nomes de coluna do dataset, os dados são verificados pela sua severidade e depois ocorre sua substituição dos valores ausentes de acordo com o seu tipo.

O código pode ser encontrado na plataforma [Kaggle](https://www.kaggle.com/code/edmilsoneddi/data-mining-discipline-exercise)

The change function Declaration method is intended to replace the function name with something that can be better understood, in addition to favoring understanding of future maintenance. The procedure chosen was the simple one as in the book guides for performing the refactoring.

The code I chose was an activity given in class by [Ricardo Silva Campos](https://www.linkedin.com/in/ricardo-campos-505220237/). This function takes a parameter of column names from the dataset, the data is checked for its severity, and then the missing values are replaced according to their type.

The code can be found on the platform [Kaggle](https://www.kaggle.com/code/edmilsoneddi/data-mining-discipline-exercise)

## Simple Method - Change Function Declaration

Nesse código utilizei o procedimento simples. De acordo com livro, que está referenciado logo acima, você deve seguir esse passos:

- Se você estiver removendo um parâmetro, certifique-se de que ele não seja referenciado no corpo da função.
- Altere a declaração do método para a declaração desejada.
- Encontre todas as referências à declaração antiga do método e atualize-as  com a nova chamada.
- Teste.

In this code I used the simple procedure. According to the book, which is referenced just above, you must follow these steps:

- If you are removing a parameter, make sure it is not referenced in the function body.
- Change the method declaration to the desired declaration.
- Find all references to the old method declaration and update them with the new call.
- Test.



## Tools
### pytest
```sh
    pip install ipytest
```
### testbook
```sh
    pip install testbook
```
### jupyter notebook
```sh
    pip install jupyter
```
### pandas
```sh
    pip install pandas
```
