import os
import json

base_dir = "/Users/jhan/Documents/Proyectos/codigo_para_buscar_papers_sobre_tema_en_especifico/outputs"

folders = [
    ("2.2.1. Bases teóricas de Operaciones de TI en Educación Superior", "tema_what-is-the-role-and-operational-impact-of-in"),
    ("2.2.1.1. Gestión de servicios e incidencias de TI (ITSM / Help Desk)", "tema_how-is-it-service-management-itsm-or-itil-imp"),
    ("2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada", "tema_what-are-the-challenges-ticket-volume-overloa"),
    ("2.2.2.3. Arquitectura Transformer y Mecanismo de Autoatención", "tema_how-does-the-scaled-dot-product-and-multi-hea"),
    ("b. Métricas de Generación y Tasa de Alucinación", "tema_how-are-hallucination-rates-factual-consisten"),
    ("2.2.2.5. Ajuste Fino Eficiente (PEFT) mediante LoRA y Cuantización GGUF", "tema_how-do-low-rank-adaptation-lora-qlora-and-ggu"),
    ("2.2.2.6. Generación Aumentada por Recuperación (RAG)", "tema_how-does-retrieval-augmented-generation-rag-i"),
    ("2.2.2.7. Arquitectura STAIR (Structure-Aware Information Retriever)", "tema_how-does-structure-aware-document-retrieval-u"),
    ("2.2.2.8. Metodología Reference-Guided LLM-as-a-Judge", "tema_how-does-reference-guided-llm-as-a-judge-eval"),
    ("2.2.3. Bases teóricas de Hardware y Entorno de Inferencia", "tema_what-are-the-architectural-paradigms-of-edge")
]

for section_name, folder in folders:
    fpath = os.path.join(base_dir, folder)
    ev_path = os.path.join(fpath, "evidencia.json")
    
    print(f"\n{'='*80}")
    print(f"SECCIÓN: {section_name}")
    print(f"FOLDER: {folder}")
    print(f"{'='*80}")
    
    if not os.path.exists(ev_path):
        continue
        
    with open(ev_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    for art in data.get("evidencias_conservadas", []):
        print("\n-----------------------------------------")
        print("Título:", art.get("titulo"))
        print("Cita narrativa:", art.get("cita_narrativa_apa7"))
        print("Cita parentética:", art.get("cita_parentetica_apa7"))
        print("Referencia APA:", art.get("referencia_bibliografica_apa7"))
        print("Cita textual literal:", art.get("cita_textual_literal"))
        print("Abstract:", art.get("abstract_completo", "")[:350], "...\n")
