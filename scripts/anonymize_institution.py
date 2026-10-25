"""
Script para anonimizar las menciones directas a la institución educativa en la tesis
e incorporar la definición cultural formal de SipánGPT y Sipán-STAIR.
Aplica cambios sincronizados en .docx y .md con compatibilidad multiplataforma.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from platform_utils import (
    get_workspace_path,
    create_backup,
    dual_save,
    DOCUMENT_DEFAULT_NAME,
    MARKDOWN_DEFAULT_NAME
)

try:
    import docx
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    print("Error: python-docx no está instalado. Ejecute: pip install -r requirements.txt")
    sys.exit(1)

cultural_note = (
    "Asimismo, cabe precisar que las denominaciones técnicas «SipánGPT» (asignada a la plataforma conversacional) "
    "y «Sipán-STAIR» (asignada a la arquitectura de recuperación jerárquica) corresponden a nombres clave de desarrollo "
    "asignados en honor y reconocimiento al patrimonio histórico, arqueológico y cultural de la región Lambayeque "
    "(asociado al Señor de Sipán y a la cultura Mochica), desvinculando formalmente dicha designación de cualquier "
    "entidad educativa privada o marca institucional en particular."
)

def anonymize_docx(docx_path: Path) -> None:
    print(f"\n[ANONIMIZACIÓN DOCX] Procesando {docx_path.name}...")
    doc = docx.Document(str(docx_path))
    
    # 1. Actualizar nodos XML en el cuerpo y dentro del SDT (TOC en caché)
    body = doc._body._element
    for t_el in body.iter("{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"):
        if t_el.text and "2.2.1.2. Problemática de atención y demanda asistencial en la USS" in t_el.text:
            t_el.text = t_el.text.replace(
                "2.2.1.2. Problemática de atención y demanda asistencial en la USS",
                "2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada"
            )
            print("  TOC/Heading XML actualizado para 2.2.1.2.")

    # 2. Modificaciones párrafo por párrafo preservando runs y formatos
    inserted_cultural_note = False
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        
        # RESUMEN (P13)
        if "demoras de resolución de hasta 72 horas en la Universidad Señor de Sipán" in t:
            for r in p.runs:
                if "en la Universidad Señor de Sipán, la presente investigación" in r.text:
                    r.text = r.text.replace(
                        "en la Universidad Señor de Sipán, la presente investigación",
                        "en una universidad privada en la región Lambayeque (en adelante, la institución bajo estudio), la presente investigación"
                    )
            print("  RESUMEN anonimizado.")

        # ABSTRACT (P17)
        elif "delays of up to 72 hours at Universidad Señor de Sipán" in t:
            for r in p.runs:
                if "at Universidad Señor de Sipán, this research aimed" in r.text:
                    r.text = r.text.replace(
                        "at Universidad Señor de Sipán, this research aimed",
                        "at a private university in the Lambayeque region (hereinafter, the university under study), this research aimed"
                    )
            print("  ABSTRACT anonimizado.")

        # 1.1 Síntesis problemática - P2 (P29)
        elif "En el ámbito regional, la Universidad Señor de Sipán (USS)" in t:
            p.text = (
                "En el ámbito regional, la universidad privada bajo estudio, ubicada en la región Lambayeque, "
                "dispone de múltiples plataformas informáticas descentralizadas para la gestión académica y administrativa "
                "(entre las que destacan el campus virtual institucional, el sistema de matrícula en línea, el portal de pagos "
                "y el catálogo digital de biblioteca). No obstante, la coexistencia de estos diversos aplicativos independientes, "
                "sumada a la concurrencia masiva de usuarios en hitos críticos del calendario académico (como los periodos de matrícula, "
                "vencimientos de pensiones y evaluaciones finales), genera una concentración sustancial de requerimientos de soporte dirigidos al área técnica."
            )
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            p.paragraph_format.line_spacing = 1.5
            p.paragraph_format.space_after = Pt(6)
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0, 0, 0)
            print("  Párrafo 1.1 regional anonimizado y marcas ocultadas.")

        # Inserción de la nota cultural al final de 1.1
        elif "garantizar la fidelidad fáctica requerida en las operaciones de TI de la universidad." in t:
            if not inserted_cultural_note:
                new_p = doc.add_paragraph()
                new_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                new_p.paragraph_format.line_spacing = 1.5
                new_p.paragraph_format.space_after = Pt(6)
                r = new_p.add_run(cultural_note)
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.color.rgb = RGBColor(0, 0, 0)
                p._p.addnext(new_p._p)
                inserted_cultural_note = True
                print("  Nota de definición cultural de SipánGPT insertada en 1.1.")

        # 1.4 Justificación práctica (P53)
        elif "área de operaciones de TI de la Universidad Señor de Sipán." in t:
            for r in p.runs:
                if "de la Universidad Señor de Sipán." in r.text:
                    r.text = r.text.replace(
                        "de la Universidad Señor de Sipán.",
                        "de la universidad privada bajo estudio."
                    )
            print("  Justificación 1.4 anonimizada.")

        # Encabezado 2.2.1.2 (P97)
        elif t == "2.2.1.2. Problemática de atención y demanda asistencial en la USS":
            p.text = "2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada"
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.keep_with_next = True
            for r in p.runs:
                r.font.name = "Times New Roman"
                r.font.size = Pt(12)
                r.font.bold = True
                r.font.color.rgb = RGBColor(0, 0, 0)
            print("  Encabezado 2.2.1.2 anonimizado.")

        # Párrafo 2.2.1.2 (P98)
        elif "problemática asistencial constatada en la Universidad Señor de Sipán refleja" in t:
            for r in p.runs:
                if "la Universidad Señor de Sipán" in r.text:
                    r.text = r.text.replace(
                        "la Universidad Señor de Sipán",
                        "la universidad privada bajo estudio"
                    )
            print("  Párrafo 2.2.1.2 anonimizado.")

        # Párrafo 2.2.2.7 (P124)
        elif "soporte de TI de la Universidad Señor de Sipán, garantizando" in t:
            for r in p.runs:
                if "de la Universidad Señor de Sipán" in r.text:
                    r.text = r.text.replace(
                        "de la Universidad Señor de Sipán",
                        "de la institución bajo estudio"
                    )
            print("  Párrafo 2.2.2.7 anonimizado.")

        # Referencia Gómez Padilla & Pantaleón Sirlopú (2024)
        elif "Entrevista diagnóstica aplicada al personal de operaciones de tecnologías de la información de la Universidad Señor de Sipán" in t:
            for r in p.runs:
                if "de la Universidad Señor de Sipán" in r.text:
                    r.text = r.text.replace(
                        "de la Universidad Señor de Sipán",
                        "de la universidad privada bajo estudio"
                    )
            print("  Referencia diagnóstica anonimizada.")

    dual_save(doc, docx_path.name)
    print("  Docx guardado y sincronizado con éxito.")

def anonymize_markdown(md_path: Path) -> None:
    print(f"\n[ANONIMIZACIÓN MARKDOWN] Procesando {md_path.name}...")
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Resumen
    content = content.replace(
        "en la Universidad Señor de Sipán, la presente investigación",
        "en una universidad privada en la región Lambayeque (en adelante, la institución bajo estudio), la presente investigación"
    )

    # 2. Abstract
    content = content.replace(
        "at Universidad Señor de Sipán, this research aimed",
        "at a private university in the Lambayeque region (hereinafter, the university under study), this research aimed"
    )

    # 3. Tabla de contenido
    content = content.replace(
        "| 2.2.1.2. Problemática de atención y demanda asistencial en la USS | 13 |",
        "| 2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada | 13 |"
    )

    # 4. 1.1 Síntesis problemática regional
    old_p1_1 = (
        "En el ámbito regional, la Universidad Señor de Sipán (USS), entidad privada de Lambayeque, dispone de múltiples "
        "plataformas informáticas descentralizadas para la gestión académica y administrativa (entre las que destacan el aula virtual, "
        "el sistema de matrícula en línea, el módulo de pagos virtuales y el catálogo digital de biblioteca). No obstante, la coexistencia "
        "de estos diversos aplicativos independientes, sumada a la concurrencia masiva de usuarios en hitos críticos del calendario "
        "académico (como los periodos de matrícula, vencimientos de pensiones y evaluaciones finales), genera una concentración "
        "sustancial de requerimientos de soporte dirigidos al área técnica."
    )
    new_p1_1 = (
        "En el ámbito regional, la universidad privada bajo estudio, ubicada en la región Lambayeque, dispone de múltiples "
        "plataformas informáticas descentralizadas para la gestión académica y administrativa (entre las que destacan el campus virtual "
        "institucional, el sistema de matrícula en línea, el portal de pagos y el catálogo digital de biblioteca). No obstante, la coexistencia "
        "de estos diversos aplicativos independientes, sumada a la concurrencia masiva de usuarios en hitos críticos del calendario "
        "académico (como los periodos de matrícula, vencimientos de pensiones y evaluaciones finales), genera una concentración "
        "sustancial de requerimientos de soporte dirigidos al área técnica."
    )
    content = content.replace(old_p1_1, new_p1_1)

    # 5. Inserción de la nota cultural al final de 1.1
    end_of_1_1 = (
        "Esta convergencia tecnológica se proyecta como una solución viable para automatizar la atención de primer contacto, "
        "reducir sustancialmente los tiempos de resolución y garantizar la fidelidad fáctica requerida en las operaciones de TI de la universidad."
    )
    new_end_of_1_1 = f"{end_of_1_1}\n\n{cultural_note}"
    content = content.replace(end_of_1_1, new_end_of_1_1)

    # 6. 1.4 Justificación práctica
    content = content.replace(
        "área de operaciones de TI de la Universidad Señor de Sipán.",
        "área de operaciones de TI de la universidad privada bajo estudio."
    )

    # 7. Encabezado 2.2.1.2
    content = content.replace(
        "#### 2.2.1.2. Problemática de atención y demanda asistencial en la USS",
        "#### 2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada"
    )

    # 8. Párrafo 2.2.1.2
    content = content.replace(
        "problemática asistencial constatada en la Universidad Señor de Sipán refleja",
        "problemática asistencial constatada en la universidad privada bajo estudio refleja"
    )

    # 9. Párrafo 2.2.2.7
    content = content.replace(
        "soporte de TI de la Universidad Señor de Sipán, garantizando",
        "soporte de TI de la institución bajo estudio, garantizando"
    )

    # 10. Referencia en Sección 8
    content = content.replace(
        "de la Universidad Señor de Sipán* [Instrumento",
        "de la universidad privada bajo estudio* [Instrumento"
    )

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("  Markdown anonimizado y sincronizado con éxito.")

def main():
    docx_file = get_workspace_path(DOCUMENT_DEFAULT_NAME)
    md_file = get_workspace_path(MARKDOWN_DEFAULT_NAME)

    create_backup(docx_file)
    anonymize_docx(docx_file)
    anonymize_markdown(md_file)

if __name__ == "__main__":
    main()
