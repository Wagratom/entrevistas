# ContaBancaria

Este código foi criado com o propósito de resolver o case. O [link]("https://github.com/andersonshindi/ContaBancaria/") já fornece uma boa explicação sobre o que o código deve fazer, então vou compartilhar minhas dificuldades e abordagens.

Embora o código seja relativamente simples, o desafio principal foi o item 4: `aplique code review e refatore conforme as melhores práticas do SOLID, patterns, etc.` Eu já ouvi falar muito sobre SOLID, já estudei, mas às vezes tenho dificuldade em lembrar a aplicação prática de cada princípio.

### mas vamos lar o que ue fiz?
Como tenho experiência em criar APIs, comecei com uma estrutura `CSR (Controller-Service-Repository) / MVT (Model-View-Template)`. Embora o projeto não seja uma API, simulei que a classe ContaBancaria funcionasse como um repositório e criei uma classe separada para executar os comandos de sacar, transferir, e depositar. Para isso, desenvolvi uma interface para a ContaBancaria e implementei essa interface na classe responsável pelas operações. Ficou legal, toda a logica ficou na classe responsavel. Achei que tinha terminado, commitei e fui pra academia.

### Pesadelo
Enquanto estava na academia, fiquei refletindo sobre o código — típico de um programador. Fiquei curioso para saber se haveria algum outro padrão de design que pudesse melhorar a solução além do tradicional que eu uso. Acabei mergulhando no mundo dos padrões de design e descobri mais de 10 diferentes, o que me deixou um pouco confuso sobre qual seria o mais adequado. No final, decidi implementar o padrão `Strategy`, que, se entendi corretamente, e focado em `polimorfismo`. Achei interessante usar porque ja ultilizei conceitos como `polimorfismo / singleton / encapsulamento` e descobrir, agora, que esses são padrões de design me deixou...

### Resumindo
Acabei misturando bastante as coisas e no fim não segui um designer a risca, misturei `Strategy` com `Adapter`. Não sei se teria um problema nisso, mas no fim acho que meu codigo ficou bem desaclopado, escalavel e componentilizado, acho que consigo trocar bastante peças sem precisar mexer em outros componentes. Enfim, alguem mais experiente vai me confirmar se estou certo.
