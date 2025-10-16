# Documentação do Fluxo de Casos de Uso - Projeto Resgate Animal

**Versão:** 1.0
**Autoras:** Guinevere Cavalcanti e Andreza Gomes de Santana


---

### 1. Visão Geral e Objetivo

O objetivo deste documento é detalhar o **fluxo completo e os Casos de Uso (UCs)** do sistema "Resgate Animal". Ele abrange desde o registro inicial de um animal resgatado (UC1) até a finalização do processo de adoção (UC5), além dos processos de suporte essenciais (UC7 a UC17). Este documento serve como guia técnico para a equipe de desenvolvimento implementar as classes, funções e regras de negócio.

### 2. Atores Envolvidos

Os atores foram consolidados para simplificar o fluxo de desenvolvimento:

| Ator | Papéis e UCs Principais |
| :--- | :--- |
| **Administrador / Funcionário ONG** | Gerencia usuários (UC16), Parcerias (UC12) e registra/edita animais (UC2). |
| **Voluntário (Resgate e Geral)** | Recolhe animais, registra resgates (UC1) e gerencia escalas (UC15). |
| **Tutor em Potencial (Adotante)** | Cadastra-se (UC3), solicita adoção (UC5) e busca serviços (UC9, UC10, UC11). |
| **Equipe Veterinária (Vet)** | Agenda (UC7) e registra castração/atendimento (UC8). |
| **Sistema** | Responsável por notificações (UC17), geolocalização (UC13) e avaliação automatizada de tutores (UC4). |

### 3. O Fluxo Passo a Passo (Caminho Crítico)

#### 3.1. Coleta e Cadastro Inicial (UC1 & UC2)
1. O processo começa com o resgate de um animal. O **Encontrante** ou **Voluntário** registra o animal (UC1).
2. São preenchidos dados iniciais: localização (GPS ou endereço), fotos e condição do animal.
3. O **Funcionário ONG/Administrador** abre a ficha para completar o registro (UC2), inserindo nome, microchip e histórico médico.
4. O animal recebe o status inicial de **"Em Avaliação Veterinária"**.

#### 3.2. Disponibilidade e Candidatura (UC2 & UC3)
1. Após a liberação veterinária, o **Funcionário ONG** atualiza o status do animal (UC2) para **"Disponível para Adoção"**.
2. O **Adotante** (Tutor em Potencial) cria sua conta (UC3), preenchendo dados pessoais, tipo de residência e informações sobre sua experiência com animais.
3. O **Adotante** submete a candidatura (UC3).

#### 3.3. Verificação de Aptidão do Tutor (UC4)
1. O **Sistema** apresenta o questionário de avaliação de aptidão ao **Adotante** (UC4).
2. O **Sistema** aplica regras e heurísticas (pontos) para gerar um *score* inicial.
3. O status do Adotante é movido para **"Em Análise"** (implícito, estado entre registro e aprovação).

#### 3.4. Caminho 1: Tutor Apto (Fluxo Feliz)
* **Aprovação:** Caso o *score* seja satisfatório ou após a visita domiciliar opcional (UC4), o **Funcionário ONG** muda o status do Tutor para **"Aprovado"**.
* **Formalização da Adoção (UC5):** O Tutor seleciona o pet e solicita a adoção.
* **Finalização:** Assinam o termo de adoção digital. O sistema atualiza o status do animal para **"Adotado"** (UC5), finalizando o processo com sucesso.

#### 3.5. Caminho 2: Tutor Não Apto
* **Reprovação:** Se o **Funcionário ONG** reprovar a candidatura (UC4) com base em regras de negócio (por exemplo, histórico de maus-tratos ou incompatibilidade de residência), o status do Tutor muda para **"Reprovado"** ou **"Condicional"**.
* **Recorrência:**
    * Se o Adotante aceitar a reprovação, o processo encerra.
    * Se o Adotante não aceitar e precisar de orientação (status **"Necessita Orientação"**), o **Administrador** ou **Voluntário** é notificado (UC17) para entrar em contato e dar orientações (implícito no fluxo alternativo de reprovação).

### 4. Regras de Negócio e Detalhes Importantes

| Regra | Descrição e UC Relacionada |
| :--- | :--- |
| **Critério de Aptidão** | Aptidão decidida por um **Funcionário ONG/Administrador** após a aplicação de *score* inicial do sistema (UC4). Regras incluem: checagem de histórico de maus-tratos e idade mínima. |
| **Informações Obrigatórias (UC1)** | **Fotos** são obrigatórias em casos de ferimentos. Os campos mínimos para o registro são: localização, fotos e condições do animal. |
| **Status Inicial do Animal** | Após o registro, o animal está pendente no painel e o status é atualizado para inclusão completa (UC2). |
| **Período Probatório** | Criação de um período probatório (ex.: 30 dias) com direito a devolução do animal (UC5). |
| **Devolução** | A **ONG** avalia o motivo e aceita/recusa a devolução conforme política (UC6). Se a devolução for por maus-tratos, deve-se registrar ocorrência e notificar autoridades. |
| **Doações/Convênios** | O sistema deve garantir a **transparência fiscal**, emissão de recibos, e proteção de dados do doador (UC14). Disponibiliza convênios para usuários elegíveis (UC12). |

### 5. Dados Envolvidos (Entidades Centrais)

As entidades centrais do sistema são: Pet, Adotante, Adoção, Devolução, Clínicas, Parcerias, Agendamento, Voluntário, Doação, Histórico Médico.

| Entidade | Atributos Chave e Status (Exemplos) |
| :--- | :--- |
| **`Pet`** | `id` (gerado automaticamente), `nome_provisorio`, `especie`, `idade_estimada`, `fotos`, `local_resgate`. |
| **`Status do Pet`** | "Em Avaliação Veterinária" (implícito), "Disponível para Adoção", "Adotado". |
| **`Adotante`** | `id` (gerado automaticamente), `nome_completo`, `endereco`, `contato` (telefone/email), `respostas_formulario`. |
| **`Status de Aptidão`** | "Em Análise" (pendente), "Aprovado", "Reprovado", "Condicional". |
| **`Adoção`** | Vínculo **Pet ↔ Adotante**, data de registro, documentos assinados, período probatório. |
| **`Histórico Médico`** | Vacinas, status (castrado/não castrado), observações do procedimento (UC8). |

**Segurança de Dados:** Os dados sensíveis do adotante e doador devem ser protegidos, em conformidade com a **LGPD** (Lei Geral de Proteção de Dados).