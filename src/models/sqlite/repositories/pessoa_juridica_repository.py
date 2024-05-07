from src.models.sqlite.entities.pessoa_juridica import PessoaJuridica
from src.models.sqlite.interfaeces.cliente_repository import Cliente


class PessoaJuridicaRepository(Cliente):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def criar_pessoa_juridica(
            self,
            faturameno: float,
            idade: int,
            nome_fantasia: str,
            celular: str,
            email: str,
            categoria: str,
            saldo: float,
    ) -> None:
        with self.__db_connection as database:
            try:
                pessoa_fisica = PessoaJuridica(
                    faturameno=faturameno,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(pessoa_fisica)
                database.session.commit()

            except Exception as exception:
                database.session.rollback()

                raise exception

    def consultar_saldo(self, pessoa_juridica):
        with self.__db_connection as database:
            try:

                consulta = database.session.query(PessoaJuridica).filter_by(nome=pessoa_juridica.nome_fantasia).first()
                return consulta.saldo

            except Exception as exception:
                database.session.rollback()

                raise exception

    def sacar_dinheiro(self, quantia, pessoa_juridica):
        limite_saque = 10000

        saldo = self.consultar_saldo(pessoa_juridica)

        if quantia <= limite_saque and quantia <= saldo:

            saldo -= quantia
            return f"Saque de R${quantia} realizado com sucesso. Saldo restante: R${saldo}"

        else:
            return "Erro: Quantia de saque excede o limite ou saldo insuficiente."

    def realizar_extrato(self, pessoa_juridica):
        with self.__db_connection as database:
            try:

                pessoa = database.session.query(PessoaJuridica).filter_by(nome=pessoa_juridica.nome_fantasia).first()
                return {
                    "Nome": pessoa.nome_fantasia,
                    "Saldo": pessoa.saldo,
                    "categoria": pessoa.categoria,
                }

            except Exception as exception:

                raise exception
