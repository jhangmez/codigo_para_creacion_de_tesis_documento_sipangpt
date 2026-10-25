# Código para Creación y Gestión Automatizada del Documento de Tesis (SipánGPT)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/Formato-OpenXML%20%2F%20Word%20(.docx)-2b579a.svg" alt="Word docx">
  <img src="https://img.shields.io/badge/Compatibilidad-macOS%20%7C%20Windows-brightgreen.svg" alt="macOS & Windows">
  <img src="https://img.shields.io/badge/Norma-APA%207ma%20Edici%C3%B3n-orange.svg" alt="APA 7">
  <img src="https://img.shields.io/badge/Instituci%C3%B3n-UNPRG-darkred.svg" alt="UNPRG">
</p>

Repositorio oficial de ingeniería documental, automatización y sincronización de contenidos para la elaboración del informe final de tesis de titulación profesional en **Ingeniería de Sistemas** de la **Universidad Nacional Pedro Ruiz Gallo (UNPRG)**, desarrollado en el marco del proyecto de investigación asistencial para una universidad privada en la región Lambayeque:

> **«Chatbot basado en Transformers como asistente en las operaciones de TI en una universidad privada en la región Lambayeque»**

---

## 📋 Descripción del Proyecto

Este repositorio aloja la infraestructura computacional en Python y OpenXML diseñada para estructurar, auditar, sincronizar y editar de manera quirúrgica el documento de tesis en formato Microsoft Word (`.docx`) y Markdown (`TESIS.md`). 

El sistema resuelve las limitaciones de edición remota en Word Online y provee una arquitectura de sincronización bidireccional (*Dual Mirror*) compatible de forma nativa tanto con **macOS** como con **Windows**.

---

## 🏛️ Características Principales

1. **Protocolo Espejo Dual (*Dual Mirror*):**
   - Mantiene una paridad absoluta del 100% entre el documento binario Word ([TESIS_FINAL_IS_V_2024_025_GOMEZ_PANTALEON.docx](TESIS_FINAL_IS_V_2024_025_GOMEZ_PANTALEON.docx)) y el archivo Markdown legible por máquina ([TESIS.md](TESIS.md)).
2. **Sincronización Multiplataforma con OneDrive:**
   - **macOS:** Integración con la API Apple File Provider (`~/Library/CloudStorage/OneDrive-Personal/...`) y validación de estado mediante `fileproviderctl`.
   - **Windows:** Detección automática de rutas sincronizadas vía `%OneDrive%`, `%OneDriveConsumer%` y Registro de Windows.
3. **Paginación Dinámica y Partición de Secciones OpenXML:**
   - Partición formal en secciones independientes: preliminares con pie vacío (sin foliación visible en portada) y cuerpo capitular desvinculado (`is_linked_to_previous = False`) con campo dinámico nativo `PAGE` reiniciando en página 1 desde la Introducción.
4. **Tabla de Contenidos (TOC) Automatizada:**
   - Contenedor Structured Document Tag (`<w:sdt>`) con instrucción de campo `TOC \o "1-3" \h \z \u` y tabulación derecha con puntos guía fijada a 15,0 cm (`8504 dxa`), erradicando desbordes de línea en títulos largos.
5. **Auditoría Estricta de Normas Académicas y Estilo en Español:**
   - **0 comas de Oxford:** Erradicación del vicio anglosajón de coma previa a conjunción copulativa (`", y"` / `", e"`).
   - **0 guiones largos o em-dashes (`—`):** Normalización a paréntesis o comas explicativas para evitar inconsistencias tipográficas.
   - **0 citas numéricas entre corchetes:** Adhesión estricta al sistema autor-año de las normas APA 7ma edición.
6. **Gestión Dinámica de Referencias:**
   - Compilación y ordenamiento alfabético automatizado (con normalización Unicode de tildes) de 33 fuentes bibliográficas en el Capítulo 8, aplicando sangría francesa de 1,27 cm (0,5 pulg.) e interlineado 1.5.

---

## 📂 Estructura del Repositorio

```text
codigo_para_creacion_de_tesis_documento_sipangpt/
├── .gitattributes             # Normalización de saltos de línea LF y declaración binaria de .docx
├── .gitignore                # Reglas estrictas de exclusión (secretos, temporales de Word, SO)
├── README.md                 # Documentación técnica principal del repositorio
├── requirements.txt          # Dependencias de Python requeridas (python-docx, lxml)
├── agents.md                 # Guía de operación, lecciones aprendidas y bitácora técnica para agentes IA
├── TESIS.md                  # Versión completa del documento de tesis en formato Markdown
├── TESIS_FINAL_IS_V_2024_025_GOMEZ_PANTALEON.docx # Documento oficial de tesis en formato Word
└── scripts/                  # Scripts de automatización y auditoría multiplataforma
    ├── __init__.py
    ├── platform_utils.py     # Detección de rutas OneDrive, backup y guardado dual (macOS/Windows)
    ├── audit_style_grammar.py# Validador regex de directivas académicas y ortográficas
    ├── apply_page_numbering.py # Inyección de foliación automática OpenXML en pie derecho
    ├── apply_bases_teoricas.py # Aplicación de bases teóricas aprobadas y 33 referencias APA 7
    ├── update_resumen_benchmark.py # Actualización de métricas oficiales del benchmark en Resumen/Abstract
    └── evidence_tools/       # Utilidades de procesamiento de evidencia científica bibliográfica
        ├── __init__.py
        ├── scan_topics.py
        ├── extract_approved_evidence.py
        └── dump_all_evidence.py
```

---

## 🚀 Guía de Instalación y Uso

### Prerrequisitos
- **Python 3.10** o superior instalado en el sistema.
- Cliente de **Microsoft OneDrive** configurado (opcional si solo se desea editar en local).

---

### En Windows (PowerShell)

```powershell
# 1. Clonar el repositorio
git clone https://github.com/jhangmez/codigo_para_creacion_de_tesis_documento_sipangpt.git
cd codigo_para_creacion_de_tesis_documento_sipangpt

# 2. Crear y activar entorno virtual
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar auditoría de estilo y calidad
python scripts\audit_style_grammar.py

# 5. Ejecutar actualización o sincronización
python scripts\update_resumen_benchmark.py
```

> ⚠️ **Importante en Windows:** Antes de ejecutar cualquier script que modifique el archivo `.docx`, asegúrese de **cerrar Microsoft Word de escritorio** y **cerrar la pestaña de Word Online en el navegador** para evitar errores de bloqueo de archivo (`[WinError 32] Sharing violation`).

---

### En macOS (Zsh / Terminal)

```bash
# 1. Clonar el repositorio
git clone https://github.com/jhangmez/codigo_para_creacion_de_tesis_documento_sipangpt.git
cd codigo_para_creacion_de_tesis_documento_sipangpt

# 2. Crear y activar entorno virtual
python3 -m venv .venv
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar auditoría de estilo
python3 scripts/audit_style_grammar.py

# 5. Ejecutar actualización o sincronización
python3 scripts/update_resumen_benchmark.py
```

---

## 📊 Estado Actual de Avance del Documento

| Sección de la Tesis | Estado | Contenido Incorporado |
| :--- | :---: | :--- |
| **Páginas Preliminares** | ✅ Completo | Portada institucional UNPRG, Aprobación, Dedicatoria, Agradecimientos, Resumen, Abstract e Índices automáticos. |
| **Capítulo 1: Introducción** | ✅ Completo | 1.1 Problemática objetiva, 1.2 Formulación del problema, 1.3 Objetivos (general y 5 específicos), 1.4 Justificación tridimensional y 1.5 Estructura del informe. |
| **Capítulo 2: Antecedentes (2.1)** | ✅ Completo | 25 estudios empíricos cuantitativos (10 internacionales y 15 nacionales de los últimos 5 años) con métricas estadísticas y aportes. |
| **Capítulo 2: Bases Teóricas (2.2)** | 🔄 En curso | 10 subsecciones temáticas aprobadas con evidencia científica formal; 19 subsecciones preservadas como borradores bajo el principio *Strict Boundary*. |
| **Capítulo 3: Metodología** | ⏳ Borrador | Estructura definida con marcadores para CRISP-DM, Kanban, población, muestra de 13 manuales y 400 diálogos ShareGPT. |
| **Capítulo 4: Resultados** | ⏳ Borrador | Estructura definida con marcadores para ingesta, entrenamiento LoRA de Gemma-4, RAG Sipán-STAIR, plataforma web y benchmark. |
| **Capítulo 5: Discusión** | ⏳ Borrador | Estructura lista para contrastación. |
| **Capítulo 6: Conclusiones** | ⏳ Borrador | Estructura lista para síntesis de objetivos. |
| **Capítulo 7: Recomendaciones** | ⏳ Borrador | Estructura lista para directivas de trabajo futuro. |
| **Capítulo 8: Referencias** | ✅ Actualizado | 33 fuentes bibliográficas rigurosamente formateadas en APA 7ma edición con sangría francesa y orden alfabético. |
| **Capítulo 9: Anexos** | ⏳ Borrador | Estructura definida para repositorios, capturas, esquemas Prisma y diccionario de datos. |

---

## 🔒 Seguridad y Manejo de Secretos

- El repositorio cuenta con una política de exclusión estricta en [.gitignore](.gitignore) que bloquea cualquier archivo `.env`, llaves privadas (`*.pem`, `*.key`), tokens de autenticación y credenciales JSON.
- Todo desarrollo posterior que requiera credenciales externas deberá documentarse mediante un archivo de plantilla `.env.example` con valores ficticios.

---

## 📖 Guía para Agentes de Inteligencia Artificial

Para instrucciones detalladas sobre arquitectura de código, OpenXML twips, directivas de redacción académica y lecciones aprendidas, consulte el archivo [agents.md](agents.md).
