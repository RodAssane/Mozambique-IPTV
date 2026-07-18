from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
from datetime import datetime


def criar_xml(programas):

    tv = Element("tv")

    channel = SubElement(tv, "channel", id="TVM")
    display = SubElement(channel, "display-name")
    display.text = "TVM"

    hoje = datetime.now().strftime("%Y%m%d")

    for i, programa in enumerate(programas):

        hora_inicio = programa["hora"].replace(":", "")

        if i < len(programas) - 1:
            hora_fim = programas[i + 1]["hora"].replace(":", "")
        else:
            hora_fim = "235900"

        p = SubElement(
            tv,
            "programme",
            start=f"{hoje}{hora_inicio}00 +0200",
            stop=f"{hoje}{hora_fim}00 +0200",
            channel="TVM"
        )

        titulo = SubElement(p, "title", lang="pt")
        titulo.text = programa["titulo"]

    xml = minidom.parseString(
        tostring(tv)
    ).toprettyxml(indent="    ")

    with open(
        "epg/mozambique.xml",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(xml)

    print("XMLTV criado.")