# Documentação do Diagrama de Fluxo - Projeto Resgate Animal

**Versão:** 1.0
**Autoras:** Guinevere Cavalcanti e Andreza Gomes de Santana
**Tarefa Relacionada:** #4

---

### 1. Visão Geral e Objetivo

O objetivo deste documento é detalhar o fluxo de processos do sistema "Resgate Animal", desde o resgate inicial de um animal até a finalização do processo de adoção. Este documento serve como guia técnico para a equipe de desenvolvimento implementar as classes, funções e regras de negócio.

### 2. Atores Envolvidos

* **Administrador/Voluntário:** Responsável por resgatar animais, cadastrá-los no sistema e aprovar a aptidão de tutores.
* **Tutor em Potencial:** Pessoa interessada em adotar um animal.

### 3. O Fluxo Passo a Passo

1.  **Coleta e Cadastro Inicial:** O processo começa com o resgate de um animal. Um voluntário, em campo ou na base, preenche os dados iniciais do animal (fotos, espécie, local de resgate) no sistema. O animal recebe o status inicial de "Em Avaliação Veterinária".

2.  **Disponibilidade para Adoção:** Após a liberação veterinária, um voluntário atualiza o status do animal para "Disponível para Adoção", tornando-o visível na plataforma.

3.  **Verificação de Aptidão do Tutor:** Um tutor interessado preenche um formulário de candidatura. O sistema então entra em estado de espera pela aprovação de um voluntário/administrador.

4.  **Caminho 1: Tutor Apto (Fluxo Feliz)**
    * Após um voluntário aprovar o cadastro do tutor, o status dele no sistema muda para "Apto".
    * O tutor então escolhe um animal e formaliza a intenção de adoção.
    * Com a adoção confirmada, o sistema apresenta uma tela de sucesso e próximos passos com o título **"PARABÉNS!"**.
    * A tela informa ao usuário: **"Se perfil foi aprovado! O próximo passo é agendar a visitar para buscar o seu novo amigo!"**.
    * A ação final esperada do usuário é clicar no botão **"Agendar Visita"** para organizar a retirada do pet.
    * Neste ponto do fluxo, o status do animal no sistema é alterado para "Adotado", e o ID do tutor é permanentemente vinculado ao animal.

5.  **Caminho 2: Tutor Não Apto (Fluxo de Orientação)**
    * Se um voluntário reprovar o cadastro, o status do tutor no sistema é alterado para "Não Apto".
    * O sistema então apresenta ao usuário uma tela de feedback empática, com o título **"É UMA PENA"**.
    * A tela informa que "No momento seu perfil não atende a todos os critérios" e gerencia a expectativa do usuário dizendo que **"Um dos nossos voluntários entrará em contato para dar as orientações!"**.
    * O usuário tem duas opções claras de ação na tela:
        * **Opção 1 (Ação Principal): "Aguardar Orientações"**. Ao selecionar esta opção, o status do tutor é atualizado para "Necessita Orientação" no sistema, e um alerta é gerado para a equipe de voluntários. O fluxo para o tutor é pausado, aguardando o contato.
        * **Opção 2 (Ação Secundária): "Deseja desistir?"**. Ao selecionar esta opção, o processo de adoção é formalmente encerrado para este candidato.
        
* **Arrecadação de Fundos:** Este é um processo **externo** ao sistema principal e **não precisa** ser implementado no escopo de código deste projeto.

### 5. Dados Envolvidos (Classes e Atributos)

* **Classe `Animal`:**
    * `id` (gerado automaticamente)
    * `nome_provisorio`
    * `especie`
    * `idade_estimada`
    * `fotos` (uma lista de links ou arquivos)
    * `local_resgate`
    * `status` (os valores podem ser: "Em Avaliação Veterinária", "Disponível para Adoção", "Em Processo de Adoção", "Adotado")
    * `tutor_responsavel_id` (preenchido após adoção)

* **Classe `Tutor`:**
    * `id` (gerado automaticamente)
    * `nome_completo`
    * `endereco`
    * `contato` (telefone/email)
    * `respostas_formulario` (um campo para guardar as respostas do formulário)
    * `status_aptidao` (os valores podem ser: "Em Análise", "Apto", "Não Apto", "Necessita Orientação")