class PessoaJuridicaController:
    def __init__(self, pessoa_juridica_repository):
        self.pessoa_juridica_repository = pessoa_juridica_repository

    def criar_pessoa_juridica(self, faturamento, idade, nome_fantasia, celular, email, categoria, saldo):
        try:
            self.pessoa_juridica_repository.criar_pessoa_juridica(
                faturamento=faturamento,
                idade=idade,
                nome_fantasia=nome_fantasia,
                celular=celular,
                email=email,
                categoria=categoria,
                saldo=saldo
            )
        except Exception as exception:
            raise exception

    def consultar_saldo(self, nome_pessoa_juridica):
        try:
            saldo = self.pessoa_juridica_repository.consultar_saldo(nome_pessoa_juridica)
            return saldo
        except Exception as exception:
            raise exception

    def sacar_dinheiro(self, quantia, nome_pessoa_juridica):
        try:
            mensagem = self.pessoa_juridica_repository.sacar_dinheiro(quantia, nome_pessoa_juridica)
            return mensagem
        except Exception as exception:
            raise exception

    def realizar_extrato(self, nome_pessoa_juridica):
        try:
            extrato = self.pessoa_juridica_repository.realizar_extrato(nome_pessoa_juridica)
            return extrato
        except Exception as exception:
            raise exception
