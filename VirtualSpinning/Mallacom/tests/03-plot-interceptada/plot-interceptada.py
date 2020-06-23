from matplotlib import pyplot as plt
from pathlib import Path
from VirtualSpinning.Mallacom.Mallacom import Mallacom


CWD = Path.cwd()
FILE = Path(__file__)
DIR = FILE.parent


def main():
    print('testing: Mallacom -> read-plot')
    print('CWD: ', CWD)
    print('DIR: ', DIR)
    print('__file__: ', FILE)
    mc = Mallacom.leer_de_archivo(DIR / 'temp' / 'malla.txt')
    mc_i = Mallacom.leer_de_archivo(DIR / 'temp' / 'malla_i.txt')
    fig, ax = plt.subplots()
    mc.marco.graficar(fig, ax)
    mc.pre_graficar_interfibras(fig, ax, color_por="random")
    fig, ax = plt.subplots()
    mc_i.marco.graficar(fig, ax)
    mc_i.pre_graficar_interfibras(fig, ax, color_por="random")
    plt.show()


if __name__ == '__main__':
    main()