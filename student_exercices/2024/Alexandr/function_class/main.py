from livre import Livre

if __name__ == '__main__':
    livre1 = Livre('Blanche Neige')
    livre2 = Livre('LOTR')
    print(Livre.get_nombre_livres())
    livre1.set_titre("The shining")
    print(livre1.titre)
