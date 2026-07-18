from fetch_tvm import obter_programacao as obter_tvm
from fetch_tvmi import obter_programacao as obter_tvmi
from xmltv import criar_xml


def main():

    canais = {
        "TVM": obter_tvm(),
        "TVMINT": obter_tvmi()
    }

    criar_xml(canais)


if __name__ == "__main__":
    main()