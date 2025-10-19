Documentação do Diagrama de Requisitos - Projeto “Resgate de Animais” 

Autoras: Maria Eunice Cantalice e Thais Adryene

1. Introdução 

Este documento descreve o Diagrama de Requisitos do sistema Resgate de Animais, desenvolvido com o objetivo de representar o processo de registo, adoção e suporte de animais resgatados. 
 	O diagrama ilustra o fluxo principal do sistema, incluindo a análise do perfil do adotante, os processos de adoção, devolução e parcerias associadas ao cuidado animal. 

 

2. Descrição Geral do Sistema 

O sistema Resgate de Animais visa registrar animais encontrados em pontos de resgate mapeados, permitindo que sejam disponibilizados para adoção responsável. 
 	Além disso, o sistema oferece suporte para pós-adoção, gestão de devoluções e integração com clínicas para vacinas, consultas e castração, além de adestradores e pet sitters. 

Principais utilizadores: 

Voluntários e protetores de animais 

Clínicas veterinárias e abrigos 

Adotantes 

Administradores do sistema 

 

3. Descrição do Diagrama de Requisitos 

O diagrama de requisito representa o fluxo lógico do processo de resgate e adoção, desde o momento em que o animal é encontrado até ao acompanhamento pós-adoção. 

 

Principais etapas identificadas: 

Animal Resgatado – início do processo. 

Registrar Pet – registo dos dados do animal resgatado. 

Mapear Pontos de Resgate – localização e gestão dos pontos de resgate de onde está localizado este animal. 

Perfil do Adotante ok? – verificação do perfil do potencial adotante. 

Não: aplicar Questionário/Avaliação. 

Sim: seguir para Registrar Adoção. 

Registrar Adoção – registo formal da adoção do animal. 

Parcerias/Convênios – ligação com entidades parceiras. 

Proibida Venda de Animais – regra ética do sistema. 

Devolveu? – verificação se o animal foi devolvido. 

Sim: executar Registrar Devolução. 

Não: realizar Suporte ao Animal. 

Registrar Devolução – novo registo do animal no sistema. 

Suporte ao Animal – acompanhamento do animal adotado, incluindo: 

Clínicas por localização 

Agendar/registrar castração 

Adestradores/Pet Sitters 

Proibida eutanásia 


### Tabela de Requisitos Identificados

#### Requisitos Funcionais

* **Requisito Funcional 01: Registrar pet**
    * Permite o registro de animais resgatados com dados como: espécie, nome, idade, condições de saúde e local de resgate.
* **Requisito Funcional 02: Mapear local de resgate**
    * Fazer o mapeamento da localidade via Google Maps antes do resgate para ter conhecimento sobre a região e acessibilidade do local, assim, efetuando o resgate.
* **Requisito Funcional 03: Avaliar perfil do adotante**
    * Visa avaliar se o adotante é apto ou não para prosseguir com a adoção: se o ambiente que o animal vai ficar é adequado, se o adotante tem condições financeiras para arcar com as necessidades do pet, se o adotante tem uma boa convivência com a sociedade sendo apto psicologicamente para cuidar do pet.
* **Requisito Funcional 04: Aplicar questionário**
    * Inclui perguntas pessoais para que assim possamos analisar o adotante e torna-lo apto.
* **Requisito Funcional 05: Registrar a adoção**
    * Vincular o pet a um adotante incluindo os dados do adotante e do pet.
* **Requisito Funcional 06: Registrar devolução**
    * Registrar devolução do pet: deve conter os motivos da devolução, e a data da devolução.
* **Requisito Funcional 07: Suporte ao animal**
    * Disponibilizar informações de suporte pós adoção: alimentação adequada, estado de saúde, se é adestrado ou não, temperamento do pet etc...
* **Requisito Funcional 08: Parcerias/Convênio**
    * Gerenciar parcerias com clinicas veterinárias, ONG’S, adestradores e pet shops.
* **Requisito Funcional 09: Clínicas por localização**
    * Exibe uma lista de clinicas veterinárias próximas ao adotante.
* **Requisito Funcional 10: Agendamento de castração**
    * Permite que o adotante agende a castração do seu pet com clinicas parceiras.
* **Requisito Funcional 11: Adestradores/Pet sitters**
    * Exibe lista de profissionais parceiros disponíveis.

#### Regras de Negócio

* **Regra de Negócio 01: Proibida venda de animais**
    * Nenhuma transação comercial pode ser registrada no sistema apenas adoção e doação.
* **Regra de Negócio 02: Proibida eutanásia**
    * O sistema não pode registrar casos de eutanásia (política ética da ONG).
* **Regra de Negócio 03: Histórico completo do animal**
    * Cada animal deve ter histórico de resgate, adoção e devoluções como uma linha do tempo.
* **Regra de Negócio 04: Adoção responsável**
    * Apenas adotantes aprovados podem concluir o processo de adoção.
* **Regra de Negócio 05: Parcerias verificadas**
    * Somente parcerias validadas podem ser exibidas ao público.
* **Regra de Negócio 06: Transparência e rastreabilidade**
    * Todos os registros devem ser auditáveis, necessário para a prestação de contas.

#### Requisitos Não Funcionais

* **Requisito não Funcional 01: Usabilidade**
    * Interface intuitiva, acessível e adaptada a dispositivos móveis.
* **Requisito não Funcional 02: Segurança de dados**
    * Garantir proteção dos dados dos adotantes e dos animais (Lei Geral de Proteção de Dados).
* **Requisito não Funcional 03: Disponibilidade**
    * O sistema deve estar disponível 24h por dia.
* **Requisito não Funcional 04: Performance**
    * O carregamento de páginas deve ser inferior a 3 segundos.

### Relações e Dependências

**Conclusão:** O levantamento dos requisitos e dependências mostra que o sistema proposto organiza de forma eficiente todo o ciclo de resgate, avaliação, adoção e acompanhamento de animais.

Ele se estrutura em três núcleos principais:
* **Gestão Animal** — registro e histórico completo dos pets resgatados.
* **Adoção e Avaliação** — controle ético da adoção com base em perfis e questionários.
* **Suporte e Parcerias** — acompanhamento pós-adoção com clínicas e adestradores.

As dependências críticas garantem integridade e rastreabilidade (adoção só após aprovação, auditoria completa e histórico inalterável). Já os requisitos não funcionais asseguram usabilidade, segurança de dados e conformidade com a LGPD.

Conclui-se que o projeto é socialmente responsável, tecnicamente viável e escalável, com potencial de automatizar e dar transparência ao processo de adoção responsável de animais.
