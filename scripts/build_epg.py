from fetch_tvm import obter_programacao
from xmltv import criar_xml


def main():
    programas = obter_programacao()
    criar_xml(programas)


if __name__ == "__main__":
    main()