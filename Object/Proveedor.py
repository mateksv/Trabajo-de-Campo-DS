from Object import EmpresaDeTransporte

class Proveedor():
    def __init__(self, cuil: int, razonSocial: str, empresasDeTransporte: list[EmpresaDeTransporte]):
        self.cuil = cuil
        self.razonSocial = razonSocial
        self.empresasDeTransporte = empresasDeTransporte