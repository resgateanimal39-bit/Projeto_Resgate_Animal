class Pet:
    def __init__(self, id, nome, especie, idade, local_resgate, status, tutor_id=None, tutor="Sem tutor"):
        self.id = id
        self.nome = nome.lower()
        self.especie = especie.lower()
        self.idade = idade
        self.local_resgate = local_resgate.lower()
        self.status = status.lower()
        self.tutor_id = tutor_id
        self.tutor = tutor

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "local_resgate": self.local_resgate,
            "status": self.status,
            "tutor_id": self.tutor_id,
            "tutor": self.tutor
        }
