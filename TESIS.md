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

A partir del diagnóstico preliminar de operaciones de tecnologías de la información que reporta una demanda asistencial estimada de 1,400 a 1,500 solicitudes por ciclo académico con demoras de resolución de hasta 72 horas en la Universidad Señor de Sipán, la presente investigación tuvo como objetivo desarrollar un chatbot basado en arquitecturas Transformer para optimizar el soporte a las operaciones tecnológicas institucionales. La metodología correspondió a una investigación aplicada con enfoque mixto y diseño cuasi-experimental con post-prueba. La muestra documental estuvo conformada por trece manuales de usuario y reglamentos oficiales vigentes organizados en cinco módulos operativos. A partir de este acervo se sintetizó un corpus balanceado de 400 conversaciones en formato ShareGPT (70% monoturno y 30% multiturno), aplicándose ajuste fino mediante adaptación de bajo rango (LoRA) sobre el modelo razonador Gemma-4-E2B-it cuantizado a GGUF e implementándose paralelamente la arquitectura de generación aumentada por recuperación jerárquica Sipán-STAIR con indexación basada en árbol de contenidos sobre PostgreSQL. La evaluación técnica comparativa sobre un banco de pruebas ciego de 50 casos mediante la metodología de evaluación guiada por referencia (Reference-Guided LLM-as-a-Judge) evidenció que la arquitectura Sipán-STAIR alcanzó un 55.00% de exactitud global fáctica frente al 14.00% obtenido por el modelo con ajuste fino, logrando reducir la tasa de alucinaciones del 78.0% al 34.0%. Asimismo, la inferencia local registró una latencia media de 11.89 segundos frente a 91.76 segundos del flujo con recuperación documental. La evaluación de usabilidad y satisfacción con una muestra de [Z] usuarios finales reportó una puntuación media de [X] puntos en la escala SUS y una satisfacción del [Y]%. Se concluye que la recuperación jerárquica sobre Transformers constituye una solución técnicamente viable y superior para garantizar rigor fáctico en el soporte tecnológico universitario.

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

## 1.1. Síntesis de la situación problemática

En el contexto global contemporáneo, la acelerada transformación digital ha redefinido la operatividad y la gestión de servicios en las instituciones de educación superior. De acuerdo con Banu (2023), la integración estratégica de las tecnologías de la información (TI) en la administración educativa resulta un factor determinante para garantizar la continuidad académica, optimizar la comunicación interdepartamental y simplificar procesos operativos complejos. No obstante, a medida que las universidades incorporan un número creciente de plataformas tecnológicas (como campus virtuales, pasarelas de pagos en línea, módulos de matrícula y repositorios de bibliotecas digitales), la demanda asistencial dirigida a los equipos de soporte técnico experimenta un incremento exponencial (Serrano et al., 2021). Diversas investigaciones evidencian que los métodos tradicionales de atención basados exclusivamente en ventanillas presenciales, bandejas de correo electrónico o sistemas estáticos de tickets resultan insuficientes para absorber la volumetría de solicitudes generada por miles de usuarios simultáneos, generando sobrecarga administrativa y demoras sustanciales (Okonkwo & Ade-Ibijola, 2021).

En el ámbito regional, la Universidad Señor de Sipán (USS), entidad privada de Lambayeque, dispone de múltiples plataformas informáticas descentralizadas para la gestión académica y administrativa (entre las que destacan el aula virtual, el sistema de matrícula en línea, el módulo de pagos virtuales y el catálogo digital de biblioteca). No obstante, la coexistencia de estos diversos aplicativos independientes, sumada a la concurrencia masiva de usuarios en hitos críticos del calendario académico (como los periodos de matrícula, vencimientos de pensiones y evaluaciones finales), genera una concentración sustancial de requerimientos de soporte dirigidos al área técnica.

Esta problemática fue constatada empíricamente a través del diagnóstico situacional preliminar desarrollado mediante una entrevista estructurada aplicada al personal del área de operaciones de TI de la institución (Gómez & Pantaleón, 2024; Anexo 3). A partir de dicho instrumento, se identificó que el equipo de soporte técnico gestiona una carga aproximada de 1,400 a 1,500 solicitudes por ciclo académico. Estas incidencias provienen de manera concurrente de estudiantes de pregrado, posgrado, personal administrativo y docentes de diversas facultades, evidenciando una saturación de los canales asistenciales vigentes.

Asimismo, los hallazgos de campo revelaron una marcada variabilidad en los tiempos de resolución de las consultas, oscilando desde casos simples que demandan entre 5 y 10 minutos hasta solicitudes complejas que tardan hasta 72 horas en completarse (Gómez & Pantaleón, 2024). Esta dispersión temporal responde a factores como la dispersión de la información institucional en múltiples manuales y reglamentos, la necesidad de coordinación manual entre distintas dependencias (como Registros Académicos y Tesorería) y la recurrencia de solicitudes formuladas con información incompleta por parte de los usuarios. Tal como sostienen Noguchi et al. (2016), en los servicios tecnológicos educativos la longitud indeterminada del tiempo de respuesta degrada significativamente la percepción del usuario, pues la celeridad y la consistencia informativa son los determinantes principales de la satisfacción del servicio.

Adicionalmente, el área de operaciones de TI carece de un canal centralizado de autoservicio disponible las 24 horas del día que permita resolver autónomamente las dudas técnicas y reglamentarias recurrentes (Gómez & Pantaleón, 2024). La atención fragmentada genera que el personal especializado dedique un porcentaje sustancial de sus horas laborales a responder preguntas repetitivas (como pasos para el restablecimiento de contraseñas del aula virtual, medios de pago autorizados o fechas límite de reserva de matrícula), en lugar de priorizar incidencias de infraestructura crítica.

Frente a este escenario, las alternativas convencionales de atención presentan claras limitaciones operativas: incrementar el personal humano de soporte resulta insostenible en términos de costos para una cobertura continua de 24 horas, mientras que los chatbots tradicionales basados en árboles de decisión o palabras clave rígidas carecen de la flexibilidad semántica requerida para interpretar la diversidad y variabilidad del lenguaje natural estudiantil (Adamopoulou & Moussiades, 2020; Okonkwo & Ade-Ibijola, 2021).

Asimismo, el empleo de modelos generativos de inteligencia artificial de forma aislada conlleva el riesgo de alucinación fáctica, emitiendo respuestas verosímiles pero normativamente erróneas, lo cual resulta crítico en trámites y pagos universitarios (Lewis et al., 2020).

Por consiguiente, la naturaleza del problema demanda una arquitectura dual: por un lado, modelos basados en Transformers capaces de comprender dependencias contextuales complejas y resolver diálogos en lenguaje natural; y, por otro, mecanismos de Generación Aumentada por Recuperación (RAG) que restrinjan la generación del modelo a la evidencia textual de los manuales y reglamentos oficiales de la institución. Esta convergencia tecnológica se proyecta como una solución viable para automatizar la atención de primer contacto, reducir sustancialmente los tiempos de resolución y garantizar la fidelidad fáctica requerida en las operaciones de TI de la universidad.

## 1.2. Formulación del problema de investigación

A partir de la realidad problemática descrita y de las limitaciones operativas identificadas en la gestión de soporte tecnológico institucional, se plantea la siguiente interrogante general de investigación:

> **¿Cómo puede un Chatbot basado en Transformers mejorar la eficiencia y calidad de la atención en las operaciones de TI de una universidad privada, específicamente en la región Lambayeque, al automatizar la respuesta a las consultas más frecuentes de los usuarios?**

## 1.3. Objetivos

### 1.3.1. Objetivo General
Desarrollar un Chatbot basado en Transformers como asistente en las operaciones de TI en una universidad privada en la región Lambayeque.

### 1.3.2. Objetivos específicos
1. Identificar fuentes bibliográficas sobre Chatbots basados en Transformers.
2. Generar el Dataset según las preguntas más frecuentes de operaciones de TI.
3. Construir un modelo de Transformers adaptado al dominio institucional.
4. Desarrollar una interfaz gráfica para la interacción con el modelo.
5. Evaluar el modelo con el usuario final y contrastar su desempeño operativo.

---

## 1.4. Justificación de la investigación

La presente investigación se fundamenta en dimensiones teóricas, operativas y de responsabilidad socioambiental, respondiendo a la necesidad de optimizar los servicios tecnológicos en la educación superior mediante soluciones computacionales eficientes.

### Justificación teórica y tecnológica
Desde el punto de vista teórico, el estudio aporta al campo del Procesamiento de Lenguaje Natural (PLN) aplicado a la gestión de servicios de tecnologías de la información (ITSM). Aborda el problema de la pérdida de fidelidad fáctica (*alucinación*) que manifiestan los Modelos de Lenguaje de Gran Escala (LLMs) cuando dependen exclusivamente de su memoria paramétrica (Lewis et al., 2020). La investigación fundamenta la articulación entre técnicas de Ajuste Fino Eficiente en Parámetros (*PEFT / LoRA*) para la adaptación de estilo conversacional (Hu et al., 2021) y la arquitectura de Generación Aumentada por Recuperación (*RAG*) guiada por estructura jerárquica (*Sipán-STAIR*), sustentada en la metodología de Kumar et al. (2026). Esta combinación permite demostrar que la delimitación semántica de documentos oficiales preserva la coherencia normativa y el rigor fáctico en las respuestas del sistema.

### Justificación práctica y operativa
En el plano práctico, la investigación resuelve un cuello de botella asistencial constatado en el área de operaciones de TI de la Universidad Señor de Sipán. El diagnóstico situacional evidenció una carga semestral de 1,400 a 1,500 requerimientos de soporte técnico, con tiempos de atención que se extienden hasta por 72 horas debido a la fragmentación de canales y a la gestión manual de consultas repetitivas (Gómez & Pantaleón, 2024; Anexo 3; Serrano et al., 2021). La implementación del asistente conversacional automatiza la resolución de incidencias de primer contacto con disponibilidad continua (24/7), disminuyendo los tiempos de espera a escasos segundos y reduciendo la frustración del usuario en periodos críticos como matrículas y evaluaciones (Banu, 2023; Noguchi et al., 2016).

### Justificación social y alineación con los Objetivos de Desarrollo Sostenible (ODS)
El proyecto se alinea de manera explícita con la Agenda 2030 de la Organización de las Naciones Unidas (2015, 2023) a través de dos objetivos estratégicos:

1. **ODS 4: Educación de Calidad (Meta 4.3):** La meta 4.3 establece la necesidad de garantizar el acceso igualitario de todos los estudiantes a una formación superior y técnica de calidad. En los entornos universitarios modernos, las trabas operativas en plataformas virtuales (como bloqueos de cuenta en campus virtual, confusión en pasarelas de pago o desinformación en trámites de matrícula) representan factores de exclusión que perjudican la continuidad del estudiante. El desarrollo del chatbot democratiza el acceso a la información técnica oficial, garantizando un autoservicio asistencial oportuno y transparente que reduce la brecha operativa en la comunidad académica.
2. **ODS 9: Industria, Innovación e Infraestructura (Metas 9.5 y 9.c):** La investigación fomenta la modernización de la infraestructura digital universitaria mediante la adopción de tecnologías de información emergentes (Meta 9.c) y el fortalecimiento de la innovación científica aplicada (Meta 9.5). En lugar de sostener mesas de ayuda tradicionales de baja eficiencia, se despliega una infraestructura de software inteligente y escalable.

### Justificación ambiental y computacional: Principios de Green AI
De manera complementaria, la investigación incorpora el paradigma de **Green AI** (Schwartz et al., 2020), el cual postula que el progreso en inteligencia artificial no debe medirse únicamente por la precisión del modelo, sino también por su eficiencia energética y costo computacional. Frente a la tendencia contemporánea de desplegar modelos masivos en clústeres de servidores que generan una alta huella de carbono, este proyecto implementó la cuantización a 4 bits en formato GGUF (`Q4_K_M`) y el ajuste fino mediante adaptadores LoRA sobre hardware de arquitectura unificada (*Apple Silicon M4*).

Esta decisión de ingeniería se sustenta en los lineamientos internacionales de sostenibilidad tecnológica, tales como el marco del **Artículo 40 del Reglamento de Inteligencia Artificial de la Unión Europea (EU AI Act)** (Unión Europea, 2024), que promueve normas armonizadas para medir y mitigar el consumo de recursos y energía de los modelos de propósito general y las directrices del Comité de Green AI de la **Green Software Foundation (2024)**. La ejecución local del modelo cuantizado con un consumo eléctrico de solo 14.6 W demuestra la viabilidad de implementar soluciones de IA institucionales de alto rendimiento bajo estándares de bajo impacto ambiental y sostenibilidad económica.

---

## 1.5. Estructura del informe

El presente informe se organiza en cuatro capítulos. El Capítulo I presenta el marco lógico de la investigación, incluyendo la síntesis de la situación problemática en las operaciones de TI, la formulación del problema, los objetivos general y específicos, así como la justificación teórica, práctica y social del estudio. El Capítulo II desarrolla el marco teórico, abarcando los antecedentes de la investigación, las bases teóricas relacionadas con la gestión de operaciones de TI en educación superior, la arquitectura Transformer, el ajuste fino eficiente con LoRA, la generación aumentada por recuperación jerárquica (Sipán-STAIR), la evaluación mediante LLM-as-a-judge y la operacionalización de las variables del estudio. El Capítulo III describe el marco metodológico empleado, incluyendo el tipo y diseño de investigación, la metodología de desarrollo de software y gestión ágil, la población y muestra documental institucional, el dataset de instrucción y las técnicas e instrumentos utilizados. El Capítulo IV presenta los resultados obtenidos, correspondientes a la ingesta documental y síntesis del dataset de soporte de TI, el entrenamiento y convergencia del modelo Transformer con LoRA en hardware local, la implementación de la arquitectura RAG jerárquica con árbol ToC, el desarrollo de la plataforma web conversacional (SipánGPT) y la validación experimental mediante el benchmark automatizado y las pruebas con usuarios finales. Finalmente, se presentan la discusión de resultados, las conclusiones, las recomendaciones, las referencias bibliográficas y los anexos correspondientes.

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

Adamopoulou, E., & Moussiades, L. (2020). Chatbots: History, technology, and applications. *Machine Learning with Applications*, 2, Artículo 100006. https://doi.org/10.1016/j.mlwa.2020.100006

Banu, A. (2023). The impact of technology integration in educational management and administration. *International Journal for Multidisciplinary Research (IJFMR)*, 5(6), 1–8. https://doi.org/10.36948/ijfmr.2023.v05i06.10858

Gómez Padilla, J. C., & Pantaleón Sirlopú, A. G. (2024). *Entrevista diagnóstica aplicada al personal de operaciones de tecnologías de la información de la Universidad Señor de Sipán* [Instrumento de recolección de datos preliminar no publicado]. Escuela Profesional de Ingeniería de Sistemas, Universidad Nacional Pedro Ruiz Gallo, Lambayeque, Perú. (Ver Anexo 3).

Green Software Foundation. (2024, 17 de octubre). *The EU AI Act: Insights from the Green AI Committee*. https://greensoftware.foundation/articles/the-eu-ai-act-insights-from-the-green-ai-committee/

Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2021). LoRA: Low-rank adaptation of large language models. *arXiv preprint arXiv:2106.09685*. https://doi.org/10.48550/arXiv.2106.09685

Kumar, V., Pulivarthi, M., Kumar, V., Sen, J., Bhat, R. A., & Joshi, S. (2026). STAIR (Structure-Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation. *arXiv preprint arXiv:2609.03874*. https://doi.org/10.48550/arXiv.2609.03874

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems (NeurIPS 2020)*, 33, 9459–9474. https://doi.org/10.48550/arXiv.2005.11401

Noguchi, O., Munechika, M., & Kajihara, C. (2016). A study on user satisfaction with an entire operation including indefinite-length response time. *Total Quality Science*, 2(2), 70–79. https://doi.org/10.17929/tqs.2.70

Okonkwo, C. W., & Ade-Ibijola, A. (2021). Chatbots applications in education: A systematic review. *Computers and Education: Artificial Intelligence*, 2, Artículo 100033. https://doi.org/10.1016/j.caeai.2021.100033

Organización de las Naciones Unidas. (2015). *Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible* (Resolución A/RES/70/1). Naciones Unidas. https://undocs.org/es/A/RES/70/1

Organización de las Naciones Unidas. (2023). *Informe sobre los Objetivos de Desarrollo Sostenible 2023: Edición especial*. Naciones Unidas. https://unstats.un.org/sdgs/report/2023/

Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O. (2020). Green AI. *Communications of the ACM*, 63(12), 54–63. https://doi.org/10.1145/3381831

Serrano, J., Faustino, J., Adriano, D., Pereira, R., & da Silva, M. M. (2021). An IT service management literature review: Challenges, benefits, opportunities and implementation practices. *Information*, 12(3), Artículo 111. https://doi.org/10.3390/info12030111

Unión Europea. (2024). Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial (Reglamento de Inteligencia Artificial). *Diario Oficial de la Unión Europea*, L 2024/1689. https://data.europa.eu/eli/reg/2024/1689/oj

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30, 5998–6008.

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., & Stoica, I. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *Advances in Neural Information Processing Systems (NeurIPS 2023)*, 36, 46595–46623. https://doi.org/10.48550/arXiv.2306.05685

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
