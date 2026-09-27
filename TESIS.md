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

# ÍNDICE GENERAL

| Contenido | Pág. |
| :--- | :--- |
| **DEDICATORIA** | iii |
| **AGRADECIMIENTOS** | iv |
| **RESUMEN** | v |
| **ABSTRACT** | vi |
| **ÍNDICE DE TABLAS** | viii |
| **INTRODUCCIÓN** | 1 |
| **CAPÍTULO I: DISEÑO TEÓRICO** | 2 |
| 1.1. Antecedentes de la Investigación | 2 |
| 1.1.1. Antecedentes Internacionales | 2 |
| 1.1.2. Antecedentes Nacionales | 5 |
| 1.2. Bases Teóricas | 8 |
| 1.2.1. Arquitectura Transformer y Mecanismo de Autoatención | 8 |
| 1.2.2. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento | 12 |
| 1.2.3. Ajuste Fino Eficiente en Parámetros (PEFT) mediante LoRA y Cuantización GGUF | 16 |
| 1.2.4. Generación Aumentada por Recuperación (RAG) y Bases Vectoriales | 20 |
| 1.2.5. Recuperación Guiada por Estructura: Arquitectura Sipán-STAIR y Poda ToC | 25 |
| 1.2.6. Evaluación de Modelos mediante Reference-Guided LLM-as-a-Judge | 29 |
| 1.2.7. Marco de Usabilidad y Experiencia de Usuario: Escala SUS | 33 |
| 1.2.8. Alineación con los Objetivos de Desarrollo Sostenible (ODS 4 y ODS 9) | 36 |
| 1.3. Operacionalización de Variables | 38 |
| 1.3.1. Definición Conceptual | 38 |
| 1.3.2. Definición Operativa | 39 |
| 1.3.3. Matriz de Operacionalización de Variables | 40 |
| **CAPÍTULO II: DISEÑO METODOLÓGICO** | 42 |
| 2.1. Tipo y Enfoque de Investigación | 42 |
| 2.2. Diseño de Contrastación de Hipótesis y Procedimiento Experimental | 44 |
| 2.3. Población y Muestra | 47 |
| 2.3.1. Unidad de Análisis | 47 |
| 2.3.2. Muestra Documental Institucional (Los 13 Documentos Oficiales USS) | 48 |
| 2.3.3. Muestra del Dataset de Instrucción y Banco de Pruebas | 50 |
| 2.3.4. Muestra de Usuarios para la Evaluación Humana | 52 |
| 2.4. Técnicas e Instrumentos de Recolección de Datos | 54 |
| 2.4.1. Análisis Documental y Transcripción Multimodal | 54 |
| 2.4.2. Inferencia Automatizada y Registro de Telemetría | 56 |
| 2.4.3. Instrumento Psicométrico: Cuestionario Estandarizado SUS | 58 |
| 2.5. Aspectos Éticos de la Investigación | 60 |
| **CAPÍTULO III: DESARROLLO DE LA SOLUCIÓN TECNOLÓGICA (INGENIERÍA DEL SISTEMA)** | 62 |
| 3.1. Fase 1: Pipeline de Ingesta y Transcripción Técnica Multimodal | 62 |
| 3.2. Fase 2: Síntesis, Balanceo y Curación del Dataset ShareGPT (400 Diálogos) | 67 |
| 3.3. Fase 3: Modelado y Fine-Tuning de Gemma-4 mediante LoRA | 73 |
| 3.4. Fase 4: Implementación de la Arquitectura RAG Jerárquico Sipán-STAIR | 80 |
| 3.5. Fase 5: Plataforma Web, Panel de Gobernanza y Telemetría en Next.js | 87 |
| **CAPÍTULO IV: RESULTADOS** | 94 |
| 4.1. Resultados del Objetivo Específico 1: Identificación de Fuentes Bibliográficas y Selección Arquitectónica | 94 |
| 4.2. Resultados del Objetivo Específico 2: Construcción y Validación del Dataset Balanceado de Operaciones de TI | 98 |
| 4.3. Resultados del Objetivo Específico 3: Construcción y Convergencia del Modelo Transformer Adaptado (Gemma-4 LoRA) | 104 |
| 4.4. Resultados del Objetivo Específico 4: Desarrollo e Integración de la Plataforma Web Conversacional (SipánGPT) | 110 |
| 4.5. Resultados del Objetivo Específico 5: Evaluación Técnica Comparativa Automatizada y Validación con Usuarios Finales | 117 |
| 4.5.1. Resultados de la Evaluación Técnica Automatizada (50 Casos de Prueba - Benchmark Oficial) | 117 |
| 4.5.2. Resultados de la Evaluación Experimental de Soporte (Decisiones Tipadas System One) | 123 |
| 4.5.3. Resultados de la Evaluación de Usabilidad y Satisfacción con Usuarios Finales (Humana) | 128 |
| **CAPÍTULO V: DISCUSIÓN DE RESULTADOS** | 133 |
| 5.1. Contraste de la Precisión Fáctica y Control de Alucinaciones frente a los Antecedentes | 133 |
| 5.2. El Trade-Off Arquitectónico: Inferencia Paramétrica Local vs. Recuperación Aumentada (RAG) | 137 |
| 5.3. Validez de la Metodología Reference-Guided LLM-as-a-Judge en Entornos Universitarios | 141 |
| 5.4. Percepción de Usabilidad Humana y Cumplimiento de la Hipótesis | 145 |
| **CONCLUSIONES** | 149 |
| **RECOMENDACIONES** | 151 |
| **REFERENCIAS** | 153 |
| **ANEXOS** | 160 |

---

# ÍNDICE DE TABLAS

---

# INTRODUCCIÓN

[Redacción correspondiente a INTRODUCCIÓN]

---

# CAPÍTULO I: DISEÑO TEÓRICO

[Redacción correspondiente a CAPÍTULO I: DISEÑO TEÓRICO]

## 1.1. Antecedentes de la Investigación

[Redacción correspondiente a 1.1. Antecedentes de la Investigación]

### 1.1.1. Antecedentes Internacionales

[Redacción correspondiente a 1.1.1. Antecedentes Internacionales]

### 1.1.2. Antecedentes Nacionales

[Redacción correspondiente a 1.1.2. Antecedentes Nacionales]

## 1.2. Bases Teóricas

[Redacción correspondiente a 1.2. Bases Teóricas]

### 1.2.1. Arquitectura Transformer y Mecanismo de Autoatención

[Redacción correspondiente a 1.2.1. Arquitectura Transformer y Mecanismo de Autoatención]

### 1.2.2. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento

[Redacción correspondiente a 1.2.2. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento]

### 1.2.3. Ajuste Fino Eficiente en Parámetros (PEFT) mediante LoRA y Cuantización GGUF

[Redacción correspondiente a 1.2.3. Ajuste Fino Eficiente en Parámetros (PEFT) mediante LoRA y Cuantización GGUF]

### 1.2.4. Generación Aumentada por Recuperación (RAG) y Bases Vectoriales

[Redacción correspondiente a 1.2.4. Generación Aumentada por Recuperación (RAG) y Bases Vectoriales]

### 1.2.5. Recuperación Guiada por Estructura: Arquitectura Sipán-STAIR y Poda ToC

[Redacción correspondiente a 1.2.5. Recuperación Guiada por Estructura: Arquitectura Sipán-STAIR y Poda ToC]

### 1.2.6. Evaluación de Modelos mediante Reference-Guided LLM-as-a-Judge

[Redacción correspondiente a 1.2.6. Evaluación de Modelos mediante Reference-Guided LLM-as-a-Judge]

### 1.2.7. Marco de Usabilidad y Experiencia de Usuario: Escala SUS

[Redacción correspondiente a 1.2.7. Marco de Usabilidad y Experiencia de Usuario: Escala SUS]

### 1.2.8. Alineación con los Objetivos de Desarrollo Sostenible (ODS 4 y ODS 9)

[Redacción correspondiente a 1.2.8. Alineación con los Objetivos de Desarrollo Sostenible (ODS 4 y ODS 9)]

## 1.3. Operacionalización de Variables

[Redacción correspondiente a 1.3. Operacionalización de Variables]

### 1.3.1. Definición Conceptual

[Redacción correspondiente a 1.3.1. Definición Conceptual]

### 1.3.2. Definición Operativa

[Redacción correspondiente a 1.3.2. Definición Operativa]

### 1.3.3. Matriz de Operacionalización de Variables

[Redacción correspondiente a 1.3.3. Matriz de Operacionalización de Variables]

---

# CAPÍTULO II: DISEÑO METODOLÓGICO

[Redacción correspondiente a CAPÍTULO II: DISEÑO METODOLÓGICO]

## 2.1. Tipo y Enfoque de Investigación

[Redacción correspondiente a 2.1. Tipo y Enfoque de Investigación]

## 2.2. Diseño de Contrastación de Hipótesis y Procedimiento Experimental

[Redacción correspondiente a 2.2. Diseño de Contrastación de Hipótesis y Procedimiento Experimental]

## 2.3. Población y Muestra

[Redacción correspondiente a 2.3. Población y Muestra]

### 2.3.1. Unidad de Análisis

[Redacción correspondiente a 2.3.1. Unidad de Análisis]

### 2.3.2. Muestra Documental Institucional (Los 13 Documentos Oficiales USS)

[Redacción correspondiente a 2.3.2. Muestra Documental Institucional (Los 13 Documentos Oficiales USS)]

### 2.3.3. Muestra del Dataset de Instrucción y Banco de Pruebas

[Redacción correspondiente a 2.3.3. Muestra del Dataset de Instrucción y Banco de Pruebas]

### 2.3.4. Muestra de Usuarios para la Evaluación Humana

[Redacción correspondiente a 2.3.4. Muestra de Usuarios para la Evaluación Humana]

## 2.4. Técnicas e Instrumentos de Recolección de Datos

[Redacción correspondiente a 2.4. Técnicas e Instrumentos de Recolección de Datos]

### 2.4.1. Análisis Documental y Transcripción Multimodal

[Redacción correspondiente a 2.4.1. Análisis Documental y Transcripción Multimodal]

### 2.4.2. Inferencia Automatizada y Registro de Telemetría

[Redacción correspondiente a 2.4.2. Inferencia Automatizada y Registro de Telemetría]

### 2.4.3. Instrumento Psicométrico: Cuestionario Estandarizado SUS

[Redacción correspondiente a 2.4.3. Instrumento Psicométrico: Cuestionario Estandarizado SUS]

## 2.5. Aspectos Éticos de la Investigación

[Redacción correspondiente a 2.5. Aspectos Éticos de la Investigación]

---

# CAPÍTULO III: DESARROLLO DE LA SOLUCIÓN TECNOLÓGICA (INGENIERÍA DEL SISTEMA)

[Redacción correspondiente a CAPÍTULO III: DESARROLLO DE LA SOLUCIÓN TECNOLÓGICA (INGENIERÍA DEL SISTEMA)]

## 3.1. Fase 1: Pipeline de Ingesta y Transcripción Técnica Multimodal

[Redacción correspondiente a 3.1. Fase 1: Pipeline de Ingesta y Transcripción Técnica Multimodal]

## 3.2. Fase 2: Síntesis, Balanceo y Curación del Dataset ShareGPT (400 Diálogos)

[Redacción correspondiente a 3.2. Fase 2: Síntesis, Balanceo y Curación del Dataset ShareGPT (400 Diálogos)]

## 3.3. Fase 3: Modelado y Fine-Tuning de Gemma-4 mediante LoRA

[Redacción correspondiente a 3.3. Fase 3: Modelado y Fine-Tuning de Gemma-4 mediante LoRA]

## 3.4. Fase 4: Implementación de la Arquitectura RAG Jerárquico Sipán-STAIR

[Redacción correspondiente a 3.4. Fase 4: Implementación de la Arquitectura RAG Jerárquico Sipán-STAIR]

## 3.5. Fase 5: Plataforma Web, Panel de Gobernanza y Telemetría en Next.js

[Redacción correspondiente a 3.5. Fase 5: Plataforma Web, Panel de Gobernanza y Telemetría en Next.js]

---

# CAPÍTULO IV: RESULTADOS

[Redacción correspondiente a CAPÍTULO IV: RESULTADOS]

## 4.1. Resultados del Objetivo Específico 1: Identificación de Fuentes Bibliográficas y Selección Arquitectónica

[Redacción correspondiente a 4.1. Resultados del Objetivo Específico 1: Identificación de Fuentes Bibliográficas y Selección Arquitectónica]

## 4.2. Resultados del Objetivo Específico 2: Construcción y Validación del Dataset Balanceado de Operaciones de TI

[Redacción correspondiente a 4.2. Resultados del Objetivo Específico 2: Construcción y Validación del Dataset Balanceado de Operaciones de TI]

## 4.3. Resultados del Objetivo Específico 3: Construcción y Convergencia del Modelo Transformer Adaptado (Gemma-4 LoRA)

[Redacción correspondiente a 4.3. Resultados del Objetivo Específico 3: Construcción y Convergencia del Modelo Transformer Adaptado (Gemma-4 LoRA)]

## 4.4. Resultados del Objetivo Específico 4: Desarrollo e Integración de la Plataforma Web Conversacional (SipánGPT)

[Redacción correspondiente a 4.4. Resultados del Objetivo Específico 4: Desarrollo e Integración de la Plataforma Web Conversacional (SipánGPT)]

## 4.5. Resultados del Objetivo Específico 5: Evaluación Técnica Comparativa Automatizada y Validación con Usuarios Finales

[Redacción correspondiente a 4.5. Resultados del Objetivo Específico 5: Evaluación Técnica Comparativa Automatizada y Validación con Usuarios Finales]

### 4.5.1. Resultados de la Evaluación Técnica Automatizada (50 Casos de Prueba - Benchmark Oficial)

[Redacción correspondiente a 4.5.1. Resultados de la Evaluación Técnica Automatizada (50 Casos de Prueba - Benchmark Oficial)]

### 4.5.2. Resultados de la Evaluación Experimental de Soporte (Decisiones Tipadas System One)

[Redacción correspondiente a 4.5.2. Resultados de la Evaluación Experimental de Soporte (Decisiones Tipadas System One)]

### 4.5.3. Resultados de la Evaluación de Usabilidad y Satisfacción con Usuarios Finales (Humana)

[Redacción correspondiente a 4.5.3. Resultados de la Evaluación de Usabilidad y Satisfacción con Usuarios Finales (Humana)]

---

# CAPÍTULO V: DISCUSIÓN DE RESULTADOS

[Redacción correspondiente a CAPÍTULO V: DISCUSIÓN DE RESULTADOS]

## 5.1. Contraste de la Precisión Fáctica y Control de Alucinaciones frente a los Antecedentes

[Redacción correspondiente a 5.1. Contraste de la Precisión Fáctica y Control de Alucinaciones frente a los Antecedentes]

## 5.2. El Trade-Off Arquitectónico: Inferencia Paramétrica Local vs. Recuperación Aumentada (RAG)

[Redacción correspondiente a 5.2. El Trade-Off Arquitectónico: Inferencia Paramétrica Local vs. Recuperación Aumentada (RAG)]

## 5.3. Validez de la Metodología Reference-Guided LLM-as-a-Judge en Entornos Universitarios

[Redacción correspondiente a 5.3. Validez de la Metodología Reference-Guided LLM-as-a-Judge en Entornos Universitarios]

## 5.4. Percepción de Usabilidad Humana y Cumplimiento de la Hipótesis

[Redacción correspondiente a 5.4. Percepción de Usabilidad Humana y Cumplimiento de la Hipótesis]

---

# CONCLUSIONES

[Redacción correspondiente a CONCLUSIONES]

---

# RECOMENDACIONES

[Redacción correspondiente a RECOMENDACIONES]

---

# REFERENCIAS

[Redacción correspondiente a REFERENCIAS]

---

# ANEXOS

[Redacción correspondiente a ANEXOS]
