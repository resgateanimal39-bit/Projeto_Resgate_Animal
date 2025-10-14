class Tutor:
    def __init__(self, id, nome, telefone, email, endereco, status_aptidao):
        self.id = id
        self.nome = nome.lower()
        self.telefone = telefone
        self.email = email.lower()
        self.endereco = endereco.lower()
        self.status_aptidao = status_aptidao.lower()

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "telefone": self.telefone,
            "email": self.email,
            "endereco": self.endereco,
            "status_aptidao": self.status_aptidao,
        }
