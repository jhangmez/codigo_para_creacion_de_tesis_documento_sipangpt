"""
Configuración automatizada de la numeración de páginas en pie de página derecho nativo de Word (OpenXML).
Desvincula la Sección 0 (Páginas Preliminares) para que no muestre foliación visible
e inyecta el campo dinámico PAGE en la Sección 1 iniciando en 1 desde la Introducción.
Compatible con macOS y Windows.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from platform_utils import get_workspace_path, find_onedrive_path, dual_save, DOCUMENT_DEFAULT_NAME

try:
    import docx
    from docx.oxml import parse_xml
    from docx.oxml.ns import nsdecls, qn
except ImportError:
    print("Error: python-docx no está instalado. Ejecute: pip install -r requirements.txt")
    sys.exit(1)

def apply_page_numbering(file_path: Path) -> None:
    print(f"\n[PAGINACIÓN] Configurando secciones y pie de página en: {file_path}")
    doc = docx.Document(str(file_path))
    
    if len(doc.sections) < 2:
        raise ValueError(f"Se esperaban al menos 2 secciones en el documento, se encontraron {len(doc.sections)}")
        
    s0 = doc.sections[0]
    s1 = doc.sections[1]
    
    # 1. Asegurar que la Sección 0 (páginas preliminares) no tenga numeración visible
    for p in list(s0.footer.paragraphs):
        p.text = ""
        
    # 2. Desvincular el pie de página de la Sección 1 respecto a la Sección 0
    s1.footer.is_linked_to_previous = False
    footer1 = s1.footer
    
    # Limpiar párrafos existentes en el pie de página de la Sección 1
    for p in list(footer1.paragraphs):
        p._p.getparent().remove(p._p)
        
    # 3. Construir el párrafo de pie de página alineado a la derecha con el campo nativo dinámico PAGE
    ns_w = nsdecls("w")
    footer_xml = f"""
    <w:p {ns_w}>
      <w:pPr>
        <w:pStyle w:val="Footer"/>
        <w:jc w:val="right"/>
        <w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>
      </w:pPr>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
          <w:sz w:val="24"/>
          <w:szCs w:val="24"/>
        </w:rPr>
        <w:fldChar w:fldCharType="begin"/>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
          <w:sz w:val="24"/>
          <w:szCs w:val="24"/>
        </w:rPr>
        <w:instrText xml:space="preserve"> PAGE </w:instrText>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
          <w:sz w:val="24"/>
          <w:szCs w:val="24"/>
        </w:rPr>
        <w:fldChar w:fldCharType="separate"/>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
          <w:sz w:val="24"/>
          <w:szCs w:val="24"/>
        </w:rPr>
        <w:t>1</w:t>
      </w:r>
      <w:r>
        <w:rPr>
          <w:rFonts w:ascii="Times New Roman" w:hAnsi="Times New Roman"/>
          <w:sz w:val="24"/>
          <w:szCs w:val="24"/>
        </w:rPr>
        <w:fldChar w:fldCharType="end"/>
      </w:r>
    </w:p>
    """
    footer1._element.append(parse_xml(footer_xml))
    
    # 4. Asegurar que las propiedades de sección inicien en 1 con formato decimal
    sectPr1 = s1._sectPr
    pgNumType = sectPr1.find(qn("w:pgNumType"))
    if pgNumType is None:
        sectPr1.append(parse_xml(f'<w:pgNumType {ns_w} w:fmt="decimal" w:start="1"/>'))
    else:
        pgNumType.set(qn("w:fmt"), "decimal")
        pgNumType.set(qn("w:start"), "1")
        
    doc.save(str(file_path))
    print(f"  Paginación aplicada correctamente en: {file_path}")

def main():
    ws_path = get_workspace_path(DOCUMENT_DEFAULT_NAME)
    od_path = find_onedrive_path(DOCUMENT_DEFAULT_NAME)
    
    apply_page_numbering(ws_path)
    if od_path:
        apply_page_numbering(od_path)

if __name__ == "__main__":
    main()
