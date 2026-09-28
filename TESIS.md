# UNIVERSIDAD NACIONAL PEDRO RUIZ GALLO
## FACULTAD DE INGENIERÍA CIVIL, DE SISTEMAS Y DE ARQUITECTURA
### ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS

---

# "Chatbot basado en Transformers como asistente de soporte en operaciones de TI en una universidad privada en la región Lambayeque"

**TESIS PARA OPTAR EL TÍTULO PROFESIONAL DE INGENIERO DE SISTEMAS**

**Autores:**  
Bach. Jhan Carlos Gómez Padilla  
Bach. Anthony Guillermo Pantaleón Sirlopú  

**Asesor:**  
Dr. Ing. Juan Elías Villegas Cubas  

**Lambayeque – Perú**  
**2026**

---

# APROBACIÓN DEL JURADO

---

# DEDICATORIA

---

# AGRADECIMIENTOS

---

# RESUMEN

A partir del diagnóstico preliminar de operaciones de tecnologías de la información que reporta una demanda asistencial estimada de 1,400 a 1,500 solicitudes por ciclo académico con demoras de resolución de hasta 72 horas en la Universidad Señor de Sipán, la presente investigación tuvo como objetivo desarrollar un chatbot basado en arquitecturas Transformer para optimizar el soporte a las operaciones tecnológicas institucionales. La metodología correspondió a una investigación aplicada con enfoque mixto y diseño cuasi-experimental con post-prueba. La muestra documental estuvo conformada por trece manuales de usuario y reglamentos oficiales vigentes organizados en cinco módulos operativos. A partir de este acervo se sintetizó un corpus balanceado de 400 conversaciones en formato ShareGPT (70% monoturno y 30% multiturno), aplicándose ajuste fino mediante adaptación de bajo rango (LoRA) sobre el modelo razonador Gemma-4-E2B-it cuantizado a GGUF, e implementándose paralelamente la arquitectura de generación aumentada por recuperación jerárquica Sipán-STAIR con indexación basada en árbol de contenidos sobre PostgreSQL. La evaluación técnica comparativa sobre un banco de pruebas ciego de 50 casos mediante la metodología de evaluación guiada por referencia (Reference-Guided LLM-as-a-Judge) evidenció que la arquitectura Sipán-STAIR alcanzó un 55.00% de exactitud global fáctica frente al 14.00% obtenido por el modelo con ajuste fino, logrando reducir la tasa de alucinaciones del 78.0% al 34.0%. Asimismo, la inferencia local registró una latencia media de 11.89 segundos frente a 91.76 segundos del flujo con recuperación documental. La evaluación de usabilidad y satisfacción con una muestra de [Z] usuarios finales reportó una puntuación media de [X] puntos en la escala SUS y una satisfacción del [Y]%. Se concluye que la recuperación jerárquica sobre Transformers constituye una solución técnicamente viable y superior para garantizar rigor fáctico en el soporte tecnológico universitario.

***Palabras claves:*** *Chatbot, Arquitectura Transformers, Operaciones de TI, Fine-Tuning LoRA, Retrieval-Augmented Generation, Sipán-STAIR, LLM-as-a-Judge.*

---

# ABSTRACT

Based on the preliminary information technology operations diagnosis reporting an estimated service demand of 1,400 to 1,500 support requests per academic semester with resolution delays of up to 72 hours at Universidad Señor de Sipán, this research aimed to develop an artificial intelligence chatbot based on Transformer architectures to optimize institutional technological operations support. The methodological design corresponded to applied research with a mixed approach and quasi-experimental post-test design. The documentary sample comprised thirteen active official user manuals and university regulations organized into five operational modules. From this institutional corpus, a balanced dataset of 400 conversations was synthesized in ShareGPT format (70% single-turn and 30% multi-turn), applying fine-tuning via Low-Rank Adaptation (LoRA) on the quantized Gemma-4-E2B-it reasoning model in GGUF format, and concurrently implementing the Sipán-STAIR hierarchical retrieval-augmented generation architecture with table-of-contents tree indexing on PostgreSQL. Technical comparative evaluation across an independent 50-case benchmark using the Reference-Guided LLM-as-a-Judge methodology revealed that the Sipán-STAIR architecture achieved 55.00% overall factual accuracy compared to 14.00% attained by the fine-tuned model, reducing the hallucination rate from 78.0% to 34.0%. Furthermore, local edge inference recorded an average latency of 11.89 seconds versus 91.76 seconds for the document retrieval pipeline. Usability and satisfaction assessment conducted with a sample of [Z] end users reported an average score of [X] points on the System Usability Scale (SUS) and a user satisfaction level of [Y]%. It is concluded that structure-aware hierarchical retrieval over Transformers constitutes a technically viable, robust, and superior solution for ensuring factual correctness and operational efficiency in higher education technological support.

***Keywords:*** *Chatbot, Transformer Architecture, IT Operations, LoRA Fine-Tuning, Retrieval-Augmented Generation, Sipán-STAIR, LLM-as-a-Judge.*

---

# Tabla de contenido

| Contenido | Pág. |
| :--- | :---: |
| **RESUMEN** | i |
| **ABSTRACT** | ii |
| **Tabla de contenido** | iii |
| **Índice de figuras** | vi |
| **Índice de tablas** | ix |
| **1. INTRODUCCIÓN** | 1 |
| 1.1. Síntesis de la situación problemática | 1 |
| 1.2. Formulación del problema de investigación | 2 |
| 1.3. Objetivos | 2 |
| 1.3.1. Objetivo General | 2 |
| 1.3.2. Objetivos específicos | 2 |
| 1.4. Justificación de la investigación | 2 |
| 1.5. Estructura del informe | 3 |
| **2. DISEÑO TEÓRICO** | 4 |
| 2.1. Antecedentes de la investigación | 4 |
| 2.2. Bases teóricas | 12 |
| 2.2.1. Bases teóricas de Operaciones de TI en Educación Superior | 12 |
| 2.2.1.1. Gestión de servicios e incidencias de TI (ITSM / Help Desk) | 12 |
| 2.2.1.2. Problemática de atención y demanda asistencial en la USS | 13 |
| 2.2.1.3. Canales digitales de autoservicio estudiantil | 14 |
| 2.2.1.4. Calidad del servicio de soporte y tiempos de respuesta | 15 |
| 2.2.2. Bases teóricas de Inteligencia Artificial y Procesamiento de Lenguaje Natural | 17 |
| 2.2.2.1. Inteligencia Artificial y Machine Learning | 17 |
| 2.2.2.2. Métricas de Evaluación de Modelos de Lenguaje | 18 |
| a. Matriz de confusión y Exactitud Fáctica (C / P / I) | 18 |
| b. Métricas de Generación y Tasa de Alucinación | 19 |
| c. Métricas de Recuperación de Información (Recall@K y Precisión) | 20 |
| 2.2.2.3. Arquitectura Transformer y Mecanismo de Autoatención | 21 |
| 2.2.2.4. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento | 22 |
| 2.2.2.5. Ajuste Fino Eficiente (PEFT) mediante LoRA y Cuantización GGUF | 24 |
| 2.2.2.6. Generación Aumentada por Recuperación (RAG) | 25 |
| 2.2.2.7. Arquitectura STAIR (Structure-Aware Information Retriever) | 26 |
| 2.2.2.8. Metodología Reference-Guided LLM-as-a-Judge | 27 |
| 2.2.3. Bases teóricas de Hardware y Entorno de Inferencia | 28 |
| 2.2.3.1. Unidad de cómputo local: Apple Silicon M4 y Memoria Unificada | 28 |
| 2.2.3.2. Motor de inferencia local: Ollama y Llama.cpp | 29 |
| 2.2.3.3. Plataforma de Fine-Tuning: Unsloth | 30 |
| 2.2.4. Bases teóricas de desarrollo de software | 31 |
| 2.2.4.1. Arquitectura de Software y Clean Architecture | 31 |
| 2.2.4.2. API REST y Protocolo SSE (Server-Sent Events) | 32 |
| 2.2.4.3. Control de Acceso Basado en Roles (RBAC) | 32 |
| 2.2.4.4. Next.js y React | 33 |
| 2.2.4.5. PostgreSQL y Extensión pgvector | 33 |
| 2.2.4.6. Prisma ORM | 34 |
| 2.2.4.7. Integración y Despliegue Continuos (CI/CD con Vercel y Neon) | 34 |
| 2.3. Operacionalización de variable | 35 |
| 2.3.1. Definición conceptual | 35 |
| 2.3.2. Definición operativa | 35 |
| Tabla 2: Operacional de variables del proyecto | 36 |
| **3. DISEÑO METODOLÓGICO** | 37 |
| 3.1. Tipo de investigación | 37 |
| 3.2. Metodología empleada: CRISP-DM adaptada a IA Conversacional | 37 |
| 3.3. Flujo de Trabajo del Sistema | 38 |
| 3.4. Metodología de Trabajo (Kanban) | 41 |
| 3.4.1. Principios de Kanban aplicados al proyecto | 41 |
| 3.4.2. Estructura del tablero Kanban | 42 |
| 3.5. Población y muestra | 42 |
| 3.5.1. Población | 42 |
| 3.5.2. Muestra | 42 |
| a. Muestra documental institucional (Los 13 documentos de operaciones de TI) | 42 |
| b. Muestra del dataset sintético (400 conversaciones ShareGPT) | 42 |
| c. Muestra del banco de pruebas (50 casos Ground Truth independientes) | 42 |
| d. Muestra de usuarios para la validación humana | 43 |
| 3.6. Técnicas, instrumentos, equipos y materiales | 43 |
| 3.6.1. Técnicas | 43 |
| 3.6.2. Instrumentos | 44 |
| 3.6.3. Equipos | 44 |
| 3.6.4. Materiales | 44 |
| 3.6.5. Aspectos éticos de la investigación | 44 |
| **4. RESULTADOS** | 46 |
| 4.1. Construcción del dataset de soporte en operaciones de TI | 46 |
| 4.1.1. Proceso de ingesta y transcripción técnica de los 13 manuales oficiales | 46 |
| 4.1.2. Segmentación semántica atómica y matriz de cuotas (400 diálogos) | 48 |
| 4.1.3. Distribución del dataset por subconjunto (Train 350 / Test 50) | 51 |
| 4.2. Entrenamiento y comparación de modelos Transformers | 54 |
| 4.2.1. Condiciones de entrenamiento en Apple Silicon M4 con Unsloth | 54 |
| 4.2.2. Selección del modelo base: Gemma-4-E2B-it (Reasoning LLM) | 55 |
| 4.2.3. Entrenamiento del modelo con LoRA y evolución de curvas de pérdida | 56 |
| 4.2.4. Estabilidad del gradiente y convergencia asintótica | 65 |
| 4.2.5. Exportación, cuantización GGUF Q4_K_M y despliegue local | 70 |
| 4.3. Diseño, construcción e implementación de la arquitectura Sipán-STAIR | 80 |
| 4.3.1. Extracción y persistencia del árbol ToC canónico (Document.tocTree) | 80 |
| 4.3.2. Poda de árbol en memoria (routeQueryToToCBranches) | 85 |
| 4.3.3. Segmentación estructural por artículos con inyección de breadcrumbs | 90 |
| 4.3.4. Indexación vectorial en PostgreSQL con pgvector y gemini-embedding-2 | 95 |
| 4.4. Desarrollo de la plataforma web conversacional (SipánGPT) | 115 |
| 4.4.1. Selección y justificación del stack tecnológico (Next.js 16 + Vercel AI SDK) | 115 |
| 4.4.2. Arquitectura general del sistema SipánGPT | 116 |
| 4.4.3. Desarrollo del sistema web y API REST con streaming SSE | 119 |
| 4.4.4. Funcionamiento del sistema en tiempo real y capturas de la plataforma | 127 |
| 4.5. Validación y evaluación comparativa del sistema | 130 |
| 4.5.1. Protocolo experimental con Reference-Guided LLM-as-a-Judge | 130 |
| 4.5.2. Resultados comparativos: Gemma-4 Fine-Tuned vs. Sipán-STAIR RAG | 131 |
| 4.5.3. Validación experimental de apoyo mediante decisiones tipadas (Jev) | 134 |
| 4.5.4. Validación de usabilidad y satisfacción con usuarios finales (Escala SUS) | 136 |
| 4.5.5. Análisis comparativo de los resultados frente a los antecedentes | 138 |
| **5. DISCUSIÓN DE RESULTADOS** | 140 |
| **6. CONCLUSIONES** | 143 |
| **7. RECOMENDACIONES** | 145 |
| **8. REFERENCIAS** | 146 |
| **9. ANEXOS** | 153 |
| Anexo A. Repositorios de código fuente del proyecto en GitHub | 153 |
| A.1. Módulo de Ingesta y Transcripción Técnica Multimodal | 153 |
| A.2. Fábrica de Datos Sintéticos ShareGPT para Fine-Tuning | 153 |
| A.3. Plataforma Web SipánGPT (Next.js + RAG Sipán-STAIR) | 153 |
| A.4. Suite de Evaluación Automatizada y Benchmark Científico | 153 |
| Anexo B. Plataforma Web SipánGPT en Producción (Acceso y URLs) | 154 |
| Anexo C. Diccionario de Base de Datos y Esquemas Prisma / PostgreSQL | 155 |
| Anexo D. Manual de Usuario y Guía de Operación de SipánGPT | 156 |
| Anexo E. Dataset Consolidado de 400 Diálogos en Hugging Face Hub | 157 |
| Anexo F. Registro Completo de Inferencia y Calificación del Benchmark (50 Casos) | 158 |
| Anexo G. Instrumento de Evaluación de Usabilidad (Cuestionario SUS) | 159 |

---

# Índice de figuras

---

# Índice de tablas

---

# 1. INTRODUCCIÓN

[Redacción correspondiente a 1. INTRODUCCIÓN]

## 1.1. Síntesis de la situación problemática

[Redacción correspondiente a 1.1. Síntesis de la situación problemática]

## 1.2. Formulación del problema de investigación

[Redacción correspondiente a 1.2. Formulación del problema de investigación]

## 1.3. Objetivos

[Redacción correspondiente a 1.3. Objetivos]

### 1.3.1. Objetivo General

[Redacción correspondiente a 1.3.1. Objetivo General]

### 1.3.2. Objetivos específicos

[Redacción correspondiente a 1.3.2. Objetivos específicos]

## 1.4. Justificación de la investigación

[Redacción correspondiente a 1.4. Justificación de la investigación]

## 1.5. Estructura del informe

[Redacción correspondiente a 1.5. Estructura del informe]

---

# 2. DISEÑO TEÓRICO

[Redacción correspondiente a 2. DISEÑO TEÓRICO]

## 2.1. Antecedentes de la investigación

[Redacción correspondiente a 2.1. Antecedentes de la investigación]

## 2.2. Bases teóricas

[Redacción correspondiente a 2.2. Bases teóricas]

### 2.2.1. Bases teóricas de Operaciones de TI en Educación Superior

[Redacción correspondiente a 2.2.1. Bases teóricas de Operaciones de TI en Educación Superior]

#### 2.2.1.1. Gestión de servicios e incidencias de TI (ITSM / Help Desk)

[Redacción correspondiente a 2.2.1.1. Gestión de servicios e incidencias de TI (ITSM / Help Desk)]

#### 2.2.1.2. Problemática de atención y demanda asistencial en la USS

[Redacción correspondiente a 2.2.1.2. Problemática de atención y demanda asistencial en la USS]

#### 2.2.1.3. Canales digitales de autoservicio estudiantil

[Redacción correspondiente a 2.2.1.3. Canales digitales de autoservicio estudiantil]

#### 2.2.1.4. Calidad del servicio de soporte y tiempos de respuesta

[Redacción correspondiente a 2.2.1.4. Calidad del servicio de soporte y tiempos de respuesta]

### 2.2.2. Bases teóricas de Inteligencia Artificial y Procesamiento de Lenguaje Natural

[Redacción correspondiente a 2.2.2. Bases teóricas de Inteligencia Artificial y Procesamiento de Lenguaje Natural]

#### 2.2.2.1. Inteligencia Artificial y Machine Learning

[Redacción correspondiente a 2.2.2.1. Inteligencia Artificial y Machine Learning]

#### 2.2.2.2. Métricas de Evaluación de Modelos de Lenguaje

[Redacción correspondiente a 2.2.2.2. Métricas de Evaluación de Modelos de Lenguaje]

##### a. Matriz de confusión y Exactitud Fáctica (C / P / I)

[Redacción correspondiente a a. Matriz de confusión y Exactitud Fáctica (C / P / I)]

##### b. Métricas de Generación y Tasa de Alucinación

[Redacción correspondiente a b. Métricas de Generación y Tasa de Alucinación]

##### c. Métricas de Recuperación de Información (Recall@K y Precisión)

[Redacción correspondiente a c. Métricas de Recuperación de Información (Recall@K y Precisión)]

#### 2.2.2.3. Arquitectura Transformer y Mecanismo de Autoatención

[Redacción correspondiente a 2.2.2.3. Arquitectura Transformer y Mecanismo de Autoatención]

#### 2.2.2.4. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento

[Redacción correspondiente a 2.2.2.4. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento]

#### 2.2.2.5. Ajuste Fino Eficiente (PEFT) mediante LoRA y Cuantización GGUF

[Redacción correspondiente a 2.2.2.5. Ajuste Fino Eficiente (PEFT) mediante LoRA y Cuantización GGUF]

#### 2.2.2.6. Generación Aumentada por Recuperación (RAG)

[Redacción correspondiente a 2.2.2.6. Generación Aumentada por Recuperación (RAG)]

#### 2.2.2.7. Arquitectura STAIR (Structure-Aware Information Retriever)

[Redacción correspondiente a 2.2.2.7. Arquitectura STAIR (Structure-Aware Information Retriever)]

#### 2.2.2.8. Metodología Reference-Guided LLM-as-a-Judge

[Redacción correspondiente a 2.2.2.8. Metodología Reference-Guided LLM-as-a-Judge]

### 2.2.3. Bases teóricas de Hardware y Entorno de Inferencia

[Redacción correspondiente a 2.2.3. Bases teóricas de Hardware y Entorno de Inferencia]

#### 2.2.3.1. Unidad de cómputo local: Apple Silicon M4 y Memoria Unificada

[Redacción correspondiente a 2.2.3.1. Unidad de cómputo local: Apple Silicon M4 y Memoria Unificada]

#### 2.2.3.2. Motor de inferencia local: Ollama y Llama.cpp

[Redacción correspondiente a 2.2.3.2. Motor de inferencia local: Ollama y Llama.cpp]

#### 2.2.3.3. Plataforma de Fine-Tuning: Unsloth

[Redacción correspondiente a 2.2.3.3. Plataforma de Fine-Tuning: Unsloth]

### 2.2.4. Bases teóricas de desarrollo de software

[Redacción correspondiente a 2.2.4. Bases teóricas de desarrollo de software]

#### 2.2.4.1. Arquitectura de Software y Clean Architecture

[Redacción correspondiente a 2.2.4.1. Arquitectura de Software y Clean Architecture]

#### 2.2.4.2. API REST y Protocolo SSE (Server-Sent Events)

[Redacción correspondiente a 2.2.4.2. API REST y Protocolo SSE (Server-Sent Events)]

#### 2.2.4.3. Control de Acceso Basado en Roles (RBAC)

[Redacción correspondiente a 2.2.4.3. Control de Acceso Basado en Roles (RBAC)]

#### 2.2.4.4. Next.js y React

[Redacción correspondiente a 2.2.4.4. Next.js y React]

#### 2.2.4.5. PostgreSQL y Extensión pgvector

[Redacción correspondiente a 2.2.4.5. PostgreSQL y Extensión pgvector]

#### 2.2.4.6. Prisma ORM

[Redacción correspondiente a 2.2.4.6. Prisma ORM]

#### 2.2.4.7. Integración y Despliegue Continuos (CI/CD con Vercel y Neon)

[Redacción correspondiente a 2.2.4.7. Integración y Despliegue Continuos (CI/CD con Vercel y Neon)]

## 2.3. Operacionalización de variable

[Redacción correspondiente a 2.3. Operacionalización de variable]

### 2.3.1. Definición conceptual

[Redacción correspondiente a 2.3.1. Definición conceptual]

### 2.3.2. Definición operativa

[Redacción correspondiente a 2.3.2. Definición operativa]

### Tabla 2: Operacional de variables del proyecto

[Redacción correspondiente a Tabla 2: Operacional de variables del proyecto]

---

# 3. DISEÑO METODOLÓGICO

[Redacción correspondiente a 3. DISEÑO METODOLÓGICO]

## 3.1. Tipo de investigación

[Redacción correspondiente a 3.1. Tipo de investigación]

## 3.2. Metodología empleada: CRISP-DM adaptada a IA Conversacional

[Redacción correspondiente a 3.2. Metodología empleada: CRISP-DM adaptada a IA Conversacional]

## 3.3. Flujo de Trabajo del Sistema

[Redacción correspondiente a 3.3. Flujo de Trabajo del Sistema]

## 3.4. Metodología de Trabajo (Kanban)

[Redacción correspondiente a 3.4. Metodología de Trabajo (Kanban)]

### 3.4.1. Principios de Kanban aplicados al proyecto

[Redacción correspondiente a 3.4.1. Principios de Kanban aplicados al proyecto]

### 3.4.2. Estructura del tablero Kanban

[Redacción correspondiente a 3.4.2. Estructura del tablero Kanban]

## 3.5. Población y muestra

[Redacción correspondiente a 3.5. Población y muestra]

### 3.5.1. Población

[Redacción correspondiente a 3.5.1. Población]

### 3.5.2. Muestra

[Redacción correspondiente a 3.5.2. Muestra]

#### a. Muestra documental institucional (Los 13 documentos de operaciones de TI)

[Redacción correspondiente a a. Muestra documental institucional (Los 13 documentos de operaciones de TI)]

#### b. Muestra del dataset sintético (400 conversaciones ShareGPT)

[Redacción correspondiente a b. Muestra del dataset sintético (400 conversaciones ShareGPT)]

#### c. Muestra del banco de pruebas (50 casos Ground Truth independientes)

[Redacción correspondiente a c. Muestra del banco de pruebas (50 casos Ground Truth independientes)]

#### d. Muestra de usuarios para la validación humana

[Redacción correspondiente a d. Muestra de usuarios para la validación humana]

## 3.6. Técnicas, instrumentos, equipos y materiales

[Redacción correspondiente a 3.6. Técnicas, instrumentos, equipos y materiales]

### 3.6.1. Técnicas

[Redacción correspondiente a 3.6.1. Técnicas]

### 3.6.2. Instrumentos

[Redacción correspondiente a 3.6.2. Instrumentos]

### 3.6.3. Equipos

[Redacción correspondiente a 3.6.3. Equipos]

### 3.6.4. Materiales

[Redacción correspondiente a 3.6.4. Materiales]

### 3.6.5. Aspectos éticos de la investigación

[Redacción correspondiente a 3.6.5. Aspectos éticos de la investigación]

---

# 4. RESULTADOS

[Redacción correspondiente a 4. RESULTADOS]

## 4.1. Construcción del dataset de soporte en operaciones de TI

[Redacción correspondiente a 4.1. Construcción del dataset de soporte en operaciones de TI]

### 4.1.1. Proceso de ingesta y transcripción técnica de los 13 manuales oficiales

[Redacción correspondiente a 4.1.1. Proceso de ingesta y transcripción técnica de los 13 manuales oficiales]

### 4.1.2. Segmentación semántica atómica y matriz de cuotas (400 diálogos)

[Redacción correspondiente a 4.1.2. Segmentación semántica atómica y matriz de cuotas (400 diálogos)]

### 4.1.3. Distribución del dataset por subconjunto (Train 350 / Test 50)

[Redacción correspondiente a 4.1.3. Distribución del dataset por subconjunto (Train 350 / Test 50)]

## 4.2. Entrenamiento y comparación de modelos Transformers

[Redacción correspondiente a 4.2. Entrenamiento y comparación de modelos Transformers]

### 4.2.1. Condiciones de entrenamiento en Apple Silicon M4 con Unsloth

[Redacción correspondiente a 4.2.1. Condiciones de entrenamiento en Apple Silicon M4 con Unsloth]

### 4.2.2. Selección del modelo base: Gemma-4-E2B-it (Reasoning LLM)

[Redacción correspondiente a 4.2.2. Selección del modelo base: Gemma-4-E2B-it (Reasoning LLM)]

### 4.2.3. Entrenamiento del modelo con LoRA y evolución de curvas de pérdida

[Redacción correspondiente a 4.2.3. Entrenamiento del modelo con LoRA y evolución de curvas de pérdida]

### 4.2.4. Estabilidad del gradiente y convergencia asintótica

[Redacción correspondiente a 4.2.4. Estabilidad del gradiente y convergencia asintótica]

### 4.2.5. Exportación, cuantización GGUF Q4_K_M y despliegue local

[Redacción correspondiente a 4.2.5. Exportación, cuantización GGUF Q4_K_M y despliegue local]

## 4.3. Diseño, construcción e implementación de la arquitectura Sipán-STAIR

[Redacción correspondiente a 4.3. Diseño, construcción e implementación de la arquitectura Sipán-STAIR]

### 4.3.1. Extracción y persistencia del árbol ToC canónico (Document.tocTree)

[Redacción correspondiente a 4.3.1. Extracción y persistencia del árbol ToC canónico (Document.tocTree)]

### 4.3.2. Poda de árbol en memoria (routeQueryToToCBranches)

[Redacción correspondiente a 4.3.2. Poda de árbol en memoria (routeQueryToToCBranches)]

### 4.3.3. Segmentación estructural por artículos con inyección de breadcrumbs

[Redacción correspondiente a 4.3.3. Segmentación estructural por artículos con inyección de breadcrumbs]

### 4.3.4. Indexación vectorial en PostgreSQL con pgvector y gemini-embedding-2

[Redacción correspondiente a 4.3.4. Indexación vectorial en PostgreSQL con pgvector y gemini-embedding-2]

## 4.4. Desarrollo de la plataforma web conversacional (SipánGPT)

[Redacción correspondiente a 4.4. Desarrollo de la plataforma web conversacional (SipánGPT)]

### 4.4.1. Selección y justificación del stack tecnológico (Next.js 16 + Vercel AI SDK)

[Redacción correspondiente a 4.4.1. Selección y justificación del stack tecnológico (Next.js 16 + Vercel AI SDK)]

### 4.4.2. Arquitectura general del sistema SipánGPT

[Redacción correspondiente a 4.4.2. Arquitectura general del sistema SipánGPT]

### 4.4.3. Desarrollo del sistema web y API REST con streaming SSE

[Redacción correspondiente a 4.4.3. Desarrollo del sistema web y API REST con streaming SSE]

### 4.4.4. Funcionamiento del sistema en tiempo real y capturas de la plataforma

[Redacción correspondiente a 4.4.4. Funcionamiento del sistema en tiempo real y capturas de la plataforma]

## 4.5. Validación y evaluación comparativa del sistema

[Redacción correspondiente a 4.5. Validación y evaluación comparativa del sistema]

### 4.5.1. Protocolo experimental con Reference-Guided LLM-as-a-Judge

[Redacción correspondiente a 4.5.1. Protocolo experimental con Reference-Guided LLM-as-a-Judge]

### 4.5.2. Resultados comparativos: Gemma-4 Fine-Tuned vs. Sipán-STAIR RAG

[Redacción correspondiente a 4.5.2. Resultados comparativos: Gemma-4 Fine-Tuned vs. Sipán-STAIR RAG]

### 4.5.3. Validación experimental de apoyo mediante decisiones tipadas (Jev)

[Redacción correspondiente a 4.5.3. Validación experimental de apoyo mediante decisiones tipadas (Jev)]

### 4.5.4. Validación de usabilidad y satisfacción con usuarios finales (Escala SUS)

[Redacción correspondiente a 4.5.4. Validación de usabilidad y satisfacción con usuarios finales (Escala SUS)]

### 4.5.5. Análisis comparativo de los resultados frente a los antecedentes

[Redacción correspondiente a 4.5.5. Análisis comparativo de los resultados frente a los antecedentes]

---

# 5. DISCUSIÓN DE RESULTADOS

[Redacción correspondiente a 5. DISCUSIÓN DE RESULTADOS]

---

# 6. CONCLUSIONES

[Redacción correspondiente a 6. CONCLUSIONES]

---

# 7. RECOMENDACIONES

[Redacción correspondiente a 7. RECOMENDACIONES]

---

# 8. REFERENCIAS

[Redacción correspondiente a 8. REFERENCIAS]

---

# 9. ANEXOS

[Redacción correspondiente a 9. ANEXOS]

## Anexo A. Repositorios de código fuente del proyecto en GitHub

[Redacción correspondiente a Anexo A. Repositorios de código fuente del proyecto en GitHub]

### A.1. Módulo de Ingesta y Transcripción Técnica Multimodal

[Redacción correspondiente a A.1. Módulo de Ingesta y Transcripción Técnica Multimodal]

### A.2. Fábrica de Datos Sintéticos ShareGPT para Fine-Tuning

[Redacción correspondiente a A.2. Fábrica de Datos Sintéticos ShareGPT para Fine-Tuning]

### A.3. Plataforma Web SipánGPT (Next.js + RAG Sipán-STAIR)

[Redacción correspondiente a A.3. Plataforma Web SipánGPT (Next.js + RAG Sipán-STAIR)]

### A.4. Suite de Evaluación Automatizada y Benchmark Científico

[Redacción correspondiente a A.4. Suite de Evaluación Automatizada y Benchmark Científico]

## Anexo B. Plataforma Web SipánGPT en Producción (Acceso y URLs)

[Redacción correspondiente a Anexo B. Plataforma Web SipánGPT en Producción (Acceso y URLs)]

## Anexo C. Diccionario de Base de Datos y Esquemas Prisma / PostgreSQL

[Redacción correspondiente a Anexo C. Diccionario de Base de Datos y Esquemas Prisma / PostgreSQL]

## Anexo D. Manual de Usuario y Guía de Operación de SipánGPT

[Redacción correspondiente a Anexo D. Manual de Usuario y Guía de Operación de SipánGPT]

## Anexo E. Dataset Consolidado de 400 Diálogos en Hugging Face Hub

[Redacción correspondiente a Anexo E. Dataset Consolidado de 400 Diálogos en Hugging Face Hub]

## Anexo F. Registro Completo de Inferencia y Calificación del Benchmark (50 Casos)

[Redacción correspondiente a Anexo F. Registro Completo de Inferencia y Calificación del Benchmark (50 Casos)]

## Anexo G. Instrumento de Evaluación de Usabilidad (Cuestionario SUS)

[Redacción correspondiente a Anexo G. Instrumento de Evaluación de Usabilidad (Cuestionario SUS)]
