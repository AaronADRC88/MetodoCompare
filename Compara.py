__author__ = 'aferreiradominguez'


class Hotel(object):
    """ Hotel: os seus atributos son: nome, ubicacion, puntuaci?n e prezo."""

    def __init__(self, nome='*', ubicacion='*',
                 puntuacion=0, prezo=float("inf")):
        """ nome e ubicacion deben ser cadeas non valeiras,
            puntuaci?n e prezo son n?meros.
            Si o precio ? 0 se reemplaza por infinito. """

        if self.e_cadea_non_valeira(nome):
            self.nome = nome
        else:
            raise TypeError("O nome debe ser unha cadea non valeira")

        if self.e_cadea_non_valeira(ubicacion):
            self.ubicacion = ubicacion
        else:
            raise TypeError("A ubicaci?n debe ser unha cadea non valeira")

        if self.e_numero(puntuacion):
            self.puntuacion = puntuacion
        else:
            raise TypeError("A puntuaci?n debe ser un n?mero")

        if self.e_numero(prezo):
            if prezo != 0:
                self.prezo = prezo
            else:
                self.prezo = float("inf")
        else:
            raise TypeError("O prezo debe ser un n?mero")

    def e_cadea_non_valeira(self, cadea):
        return len(cadea) > 0

    def e_numero(self, valor):
        return isinstance(valor, (int, float, complex))

    def __str__(self):
        """ Mostra o hotel segundo o requerido. """
        return self.nome + " de " + self.ubicacion + \
               " - Puntuaci?n: " + str(self.puntuacion) + " - Prezo: " + \
               str(self.prezo) + " euros."

    def calidadPrecio(self):
        return (self.puntuacion * 20) / self.prezo

    def __cmp__(self, other):
        diferencia = self.calidadPrecio() - other.calidadPrecio()
        if diferencia < 0:
            return -1
        elif diferencia > 0:
            return 1
        else:
            return 0


h = Hotel("aa", "bb", 5, 15)
h2=Hotel("cc","dd",3,20)
print(h)

print(h.__cmp__(h2))