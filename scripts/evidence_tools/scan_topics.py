import os
import json

base_dir = "/Users/jhan/Documents/Proyectos/codigo_para_buscar_papers_sobre_tema_en_especifico/outputs"
folders = sorted([f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f))])

results = []
for folder in folders:
    fpath = os.path.join(base_dir, folder)
    ev_path = os.path.join(fpath, "evidencia.json")
    
    num_conservadas = 0
    approved_info = []
    question = ""
    seccion = ""
    
    if os.path.exists(ev_path):
        try:
            with open(ev_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                question = data.get("tema_investigacion", "") or data.get("pregunta_investigacion", "")
                seccion = data.get("seccion_tesis", "")
                conservadas = data.get("evidencias_conservadas", [])
                num_conservadas = len(conservadas)
                for art in conservadas:
                    cita = art.get("cita_narrativa", "") or art.get("autor_ano", "") or art.get("titulo", "")
                    approved_info.append(cita)
        except Exception as e:
            approved_info.append(f"Error: {e}")
            
    results.append({
        "folder": folder,
        "seccion": seccion,
        "question": question,
        "num": num_conservadas,
        "approved": approved_info
    })

print(f"Total folders: {len(results)}\n")
approved_count = 0
empty_count = 0

for r in results:
    n = r["num"]
    sec = r["seccion"]
    folder = r["folder"]
    if n > 0:
        approved_count += 1
        print(f"✅ [{sec}] ({n} papers) | {folder}")
        for a in r["approved"]:
            print(f"     -> {a}")
    else:
        empty_count += 1
        print(f"❌ [{sec}] (0 papers) | {folder}")

print(f"\nSummary: {approved_count} folders WITH approved papers, {empty_count} folders EMPTY (below threshold).")
