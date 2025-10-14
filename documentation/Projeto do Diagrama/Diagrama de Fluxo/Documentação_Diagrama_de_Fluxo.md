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
    * Se um voluntário aprovar o cadastro do tutor, o status dele muda para "Apto".
    * O tutor pode então escolher um animal e formalizar a adoção.
    * Após a escolha, é realizado o cadastro de acompanhamento, e o status do animal muda para "Adotado". O processo é finalizado com sucesso.

5.  **Caminho 2: Tutor Não Apto**
    * Se um voluntário reprovar o cadastro, o status do tutor muda para "Não Apto".
    * O sistema pergunta se ele deseja desistir. Se sim, o processo encerra.
    * Se não, o cadastro do tutor é movido para uma lista de "Necessita de Orientação", e um voluntário é notificado para entrar em contato.

### 4. Regras de Negócio e Detalhes Importantes

* **Critério para um tutor ser "Apto":** A aptidão é decidida por um **voluntário**, com base nas respostas de um **formulário de candidatura** preenchido pelo tutor. O voluntário tem as opções "Aprovar" ou "Reprovar" no sistema.

* **Informações Obrigatórias para Animal:** Para cadastrar um animal, é obrigatório preencher: `espécie`, `idade_estimada`, `fotos_iniciais`, `local_resgate`.

* **Status Inicial do Animal:** Todo animal cadastrado recebe o status **"Em Avaliação Veterinária"** por padrão.

* **Regra para Tutor "Não Desiste":** Se um tutor for reprovado mas não desistir, seu status muda para **"Necessita Orientação"**. O sistema deve notificar os administradores/voluntários para que um deles possa entrar em contato com o candidato para dar orientações.

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