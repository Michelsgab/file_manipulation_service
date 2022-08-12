class Projeto:
    def __init__(self, id=None, nome=None, descricao=None, cargo=None, empresa=None, email=None, github=None,
                 linkedin=None, telefone=None, curriculo=None, foto=None):
        self._id = id,
        self._nome = nome
        self._descricao = descricao
        self._cargo = cargo
        self._empresa = empresa
        self._email = email
        self._github = github
        self._linkedin = linkedin
        self._telefone = telefone
        self._curriculo = curriculo
        self._foto = foto

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def empresa(self):
        return self._empresa

    @empresa.setter
    def empresa(self, empresa):
        self._empresa = empresa

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def github(self):
        return self._github

    @github.setter
    def github(self, github):
        self._github = github

    @property
    def linkedin(self):
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        self._linkedin = linkedin

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def curriculo(self):
        return self._curriculo

    @curriculo.setter
    def curriculo(self, curriculo):
        self._curriculo = curriculo

    @property
    def foto(self):
        return self._foto

    @foto.setter
    def foto(self, foto):
        self._foto = foto

    def __iter__(self):
        for key in self.__dict__:
            yield key.replace('_', ''), self.__getattribute__(key)
