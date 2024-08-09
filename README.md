# ContaBancaria

Este código foi criado com o propósito de resolver o case. O [link](https://github.com/andersonshindi/ContaBancaria/) já fornece uma boa explicação sobre o que o código deve fazer, então vou compartilhar minhas dificuldades e abordagens.

Embora o código seja relativamente simples, o desafio principal foi o item 4: `aplique code review e refatore conforme as melhores práticas do SOLID, patterns, etc.` Eu já ouvi falar muito sobre SOLID, já estudei, mas às vezes tenho dificuldade em lembrar a aplicação prática de cada princípio.

### mas vamos lar o que ue fiz?
Como tenho experiência em criar APIs, comecei com uma estrutura `CSR (Controller-Service-Repository) / MVT (Model-View-Template)`. Embora o projeto não seja uma API, simulei que a classe ContaBancaria funcionasse como um repositório e criei uma classe separada para executar os comandos de sacar, transferir, e depositar. Para isso, desenvolvi uma interface para a ContaBancaria e implementei essa interface na classe responsável pelas operações. Ficou legal, toda a logica ficou na classe responsavel. Achei que tinha terminado, commitei e fui pra academia.

### Pesadelo
Enquanto estava na academia, fiquei refletindo sobre o código — típico de um programador. Fiquei curioso para saber se haveria algum outro padrão de design que pudesse melhorar a solução além do tradicional que eu uso. Acabei mergulhando no mundo dos padrões de design e descobri mais de 10 diferentes, o que me deixou um pouco confuso sobre qual seria o mais adequado. No final, decidi implementar o padrão `Strategy`, que, se entendi corretamente, e focado em `polimorfismo`. Achei interessante usar porque ja ultilizei conceitos como `polimorfismo / singleton / encapsulamento` e descobrir, agora, que esses são padrões de design me deixou...

### Resumindo
Acabei misturando bastante as coisas e no fim não segui um designer a risca, misturei `Strategy` com `Adapter`. Não sei se teria um problema nisso, mas no fim acho que meu codigo ficou bem desaclopado, escalavel e componentilizado, acho que consigo trocar bastante peças sem precisar mexer em outros componentes. Enfim, alguem mais experiente vai me confirmar se estou certo.


### Programa

Aqui está um resumo rápido para clonar e testar o código localmente.

## ⚙️ instaling

Clone o repositório e navegue até o diretório do projeto:

```
git clone git@github.com:Wagratom/entrevistas.git
cd entrevistas
```

### Start
Para iniciar o código, estando dentro do diretório do projeto, execute:

```
make
```

### Tests
Para rodar todos os testes automatizados, utilize:

```
make tests
```

Se precisar rodar um teste específico, passe o nome do teste como parâmetro:

```
make test t=<name>
```

### Help
Para visualizar todos os comandos disponíveis e obter mais informações, execute:

```
make help
```

#### obs 🤓
Se você não conseguir usar o `make/Makefile` no seu ambiente, você pode simplesmente replicar os comandos manualmente através da linha de comando.


# Case 2

O case 2 era sobre projetar uma arquiterua de PIX segundo as seguintes regras

 - O Sistema deverá ser capaz de receber a ordem de transferência e efetivar o debito(-) na conta do solicitante antes de
creditar(+) a conta do cliente destinatário
 - O Sistema deverá guardar um histórico de todas as transações por 5 anos
 - Ser compatível com Android e IOS
 - Início com 100 transações diárias, com perspectiva de crescimento para 20 milhões por dia em até 1 ano
 - Ter uma solução com resiliência entre as peças, garantindo assim uma disponibilidade(uptime) superior a 99%
 - Possuir Logs e Métricas de uso

OBS:
Requisitos de segurança não são obrigatórios, mas podem haver perguntas relacionadas
FrontEnd e Apps não fazem parte do escopo do desenho, mas sua sinalização é importante
Utilize a ferramenta Drawio para construção do arquitetura
Não existe resposta certa ou errada. O Objetivo é avaliar a linha de raciocínio do colaborador

### Resultado
Pensei em contar um pouco também de como cheguei nesse resultado, mas resulvi explicar na hora da review

logs em 5 anos: https://docs.aws.amazon.com/pt_br/AmazonS3/latest/userguide/lifecycle-configuration-examples.html


![um diagrama mostrando os diferentes componentes de um sistema de computação em nuvem e como eles funcionam juntos, mecanismo de fluxo de trabalho empresarial, lambda, visualização dinâmica, diagrama legível, diagrama de conceito arquitetônico, diagrama, mix com arquitetura rivendell, colaboração infinita com ia, arquitetura complexa, diagramas detalhados, arquitetura cibernética, arquitetura limpa, gráfico de cena de jogo, aplicativo, interoperabilidade de lentes, arquitetura warcraft, data center extremamente detalhado, um diagrama de wireframe, esquemático, redshift. micro detalhes](./plataformaPix.drawio.png)
