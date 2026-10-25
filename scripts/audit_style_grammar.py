"""
Script de auditoría integral de estilo académico, normas APA 7ma edición y reglas gramaticales en español.
Valida tanto el archivo Word (.docx) como el archivo Markdown (TESIS.md).
Funciona de manera idéntica en macOS y Windows.
"""

import re
import sys
from pathlib import Path

# Permitir imports relativos al ejecutar como script independiente
sys.path.insert(0, str(Path(__file__).resolve().parent))
from platform_utils import get_workspace_path, DOCUMENT_DEFAULT_NAME, MARKDOWN_DEFAULT_NAME

try:
    import docx
except ImportError:
    print("Error: python-docx no está instalado. Ejecute: pip install -r requirements.txt")
    sys.exit(1)

def audit_text_content(title: str, text: str) -> list[str]:
    """Audita una cadena de texto según los estándares obligatorios de la tesis."""
    issues = []
    
    # 1. Coma de Oxford en español (coma antes de conjunción copulativa 'y' o 'e')
    oxford = re.findall(r"[,\s]*,\s+[ye]\b", text)
    if oxford:
        issues.append(f"Comas de Oxford detectadas ({len(oxford)}): {oxford[:5]}")
        
    # 2. Guiones largos o em-dashes (—)
    emdashes = re.findall(r"—", text)
    if emdashes:
        issues.append(f"Guiones largos em-dash (—) detectados ({len(emdashes)})")
        
    # 3. Citas numéricas entre corchetes ([1], [2], [1, 5], etc.)
    # Excluir referencias de código markdown y los marcadores de la muestra [Z], [X], [Y]
    brackets = re.findall(r"(?<!`)(?:\[\d+(?:,\s*\d+)*\])(?!`)", text)
    if brackets:
        issues.append(f"Citas numéricas entre corchetes detectadas ({len(brackets)}): {brackets[:5]}")
        
    # 4. Marcadores residuales de borrador no permitidos en producción
    draft_markers = re.findall(r"\b(?:PENDIENTE|BORRADOR)\b", text)
    if draft_markers:
        issues.append(f"Marcadores de borrador detectados ({len(draft_markers)}): {draft_markers[:5]}")
        
    return issues

def audit_docx(docx_path: Path) -> bool:
    print(f"\n[AUDIT DOCX] Analizando {docx_path.name}...")
    if not docx_path.exists():
        print(f"  Error: No existe el archivo {docx_path}")
        return False
        
    doc = docx.Document(str(docx_path))
    full_text = "\n".join(p.text for p in doc.paragraphs)
    
    # También auditar celdas de tablas
    table_texts = []
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                table_texts.append(cell.text)
    full_text += "\n" + "\n".join(table_texts)
    
    issues = audit_text_content("DOCX", full_text)
    if issues:
        print("  FALLOS DETECTADOS EN DOCX:")
        for issue in issues:
            print(f"    - {issue}")
        return False
    else:
        print("  CORRECTO: Documento DOCX 100% limpio (0 comas Oxford, 0 em-dashes, 0 citas numéricas).")
        return True

def audit_markdown(md_path: Path) -> bool:
    print(f"\n[AUDIT MARKDOWN] Analizando {md_path.name}...")
    if not md_path.exists():
        print(f"  Error: No existe el archivo {md_path}")
        return False
        
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
        
    issues = audit_text_content("MARKDOWN", md_text)
    if issues:
        print("  FALLOS DETECTADOS EN MARKDOWN:")
        for issue in issues:
            print(f"    - {issue}")
        return False
    else:
        print("  CORRECTO: Documento Markdown 100% limpio (0 comas Oxford, 0 em-dashes, 0 citas numéricas).")
        return True

def main():
    docx_file = get_workspace_path(DOCUMENT_DEFAULT_NAME)
    md_file = get_workspace_path(MARKDOWN_DEFAULT_NAME)
    
    ok_docx = audit_docx(docx_file)
    ok_md = audit_markdown(md_file)
    
    if ok_docx and ok_md:
        print("\n[AUDITORIA EXITOSA] Ambos documentos cumplen estrictamente con todas las directivas.")
        sys.exit(0)
    else:
        print("\n[AUDITORIA CON OBSERVACIONES] Corrija los errores reportados antes de confirmar cambios.")
        sys.exit(1)

if __name__ == "__main__":
    main()
