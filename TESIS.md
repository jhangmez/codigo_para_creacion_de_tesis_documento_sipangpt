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

A partir del diagnóstico preliminar de operaciones de tecnologías de la información que reporta una demanda asistencial estimada de 1,400 a 1,500 solicitudes por ciclo académico con demoras de resolución de hasta 72 horas en una universidad privada en la región Lambayeque (en adelante, la institución bajo estudio), la presente investigación tuvo como objetivo desarrollar un chatbot basado en arquitecturas Transformer para optimizar el soporte a las operaciones tecnológicas institucionales. La metodología correspondió a una investigación aplicada con enfoque mixto y diseño cuasi-experimental con post-prueba. La muestra documental estuvo conformada por trece manuales de usuario y reglamentos oficiales vigentes organizados en cinco módulos operativos. A partir de este acervo se sintetizó un corpus balanceado de 400 conversaciones en formato ShareGPT (70% monoturno y 30% multiturno), aplicándose ajuste fino mediante adaptación de bajo rango (LoRA) sobre el modelo razonador Gemma-4-E2B-it cuantizado a GGUF e implementándose paralelamente la arquitectura de generación aumentada por recuperación jerárquica Sipán-STAIR con indexación basada en árbol de contenidos sobre PostgreSQL. La evaluación técnica comparativa sobre un banco de pruebas ciego de 50 casos mediante la metodología de evaluación guiada por referencia (Reference-Guided LLM-as-a-Judge) evidenció que la arquitectura Sipán-STAIR alcanzó un 45,00% de exactitud global fáctica frente al 6,00% obtenido por el modelo con ajuste fino, logrando reducir la tasa de alucinaciones del 90,0% al 48,0%. Asimismo, la arquitectura Sipán-STAIR registró una latencia media de 7,47 segundos por consulta frente a 12,15 segundos de la inferencia local con el modelo adaptado, demostrando una mayor eficiencia temporal en el flujo de recuperación documental. La evaluación de usabilidad y satisfacción con una muestra de [Z] usuarios finales reportó una puntuación media de [X] puntos en la escala SUS y una satisfacción del [Y]%. Se concluye que la recuperación jerárquica sobre Transformers constituye una solución técnicamente viable y superior para garantizar rigor fáctico en el soporte tecnológico universitario.

***Palabras claves:*** *Chatbot, Arquitectura Transformers, Operaciones de TI, Fine-Tuning LoRA, Retrieval-Augmented Generation, Sipán-STAIR, LLM-as-a-Judge.*

---

# ABSTRACT

Based on the preliminary information technology operations diagnosis reporting an estimated service demand of 1,400 to 1,500 support requests per academic semester with resolution delays of up to 72 hours at a private university in the Lambayeque region (hereinafter, the university under study), this research aimed to develop an artificial intelligence chatbot based on Transformer architectures to optimize institutional technological operations support. The methodological design corresponded to applied research with a mixed approach and quasi-experimental post-test design. The documentary sample comprised thirteen active official user manuals and university regulations organized into five operational modules. From this institutional corpus, a balanced dataset of 400 conversations was synthesized in ShareGPT format (70% single-turn and 30% multi-turn), applying fine-tuning via Low-Rank Adaptation (LoRA) on the quantized Gemma-4-E2B-it reasoning model in GGUF format, and concurrently implementing the Sipán-STAIR hierarchical retrieval-augmented generation architecture with table-of-contents tree indexing on PostgreSQL. Technical comparative evaluation across an independent 50-case benchmark using the Reference-Guided LLM-as-a-Judge methodology revealed that the Sipán-STAIR architecture achieved 45.00% overall factual accuracy compared to 6.00% attained by the fine-tuned model, reducing the hallucination rate from 90.0% to 48.0%. Furthermore, the Sipán-STAIR architecture recorded an average query latency of 7.47 seconds versus 12.15 seconds for local edge inference with the adapted model, demonstrating higher temporal efficiency in the document retrieval pipeline. Usability and satisfaction assessment conducted with a sample of [Z] end users reported an average score of [X] points on the System Usability Scale (SUS) and a user satisfaction level of [Y]%. It is concluded that structure-aware hierarchical retrieval over Transformers constitutes a technically viable, robust, and superior solution for ensuring factual correctness and operational efficiency in higher education technological support.

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
| 2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada | 13 |
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

En el ámbito regional, la universidad privada bajo estudio, ubicada en la región Lambayeque, dispone de múltiples plataformas informáticas descentralizadas para la gestión académica y administrativa (entre las que destacan el campus virtual institucional, el sistema de matrícula en línea, el portal de pagos y el catálogo digital de biblioteca). No obstante, la coexistencia de estos diversos aplicativos independientes, sumada a la concurrencia masiva de usuarios en hitos críticos del calendario académico (como los periodos de matrícula, vencimientos de pensiones y evaluaciones finales), genera una concentración sustancial de requerimientos de soporte dirigidos al área técnica.

Esta problemática fue constatada empíricamente a través del diagnóstico situacional preliminar desarrollado mediante una entrevista estructurada aplicada al personal del área de operaciones de TI de la institución (Gómez & Pantaleón, 2024; Anexo 3). A partir de dicho instrumento, se identificó que el equipo de soporte técnico gestiona una carga aproximada de 1,400 a 1,500 solicitudes por ciclo académico. Estas incidencias provienen de manera concurrente de estudiantes de pregrado, posgrado, personal administrativo y docentes de diversas facultades, evidenciando una saturación de los canales asistenciales vigentes.

Asimismo, los hallazgos de campo revelaron una marcada variabilidad en los tiempos de resolución de las consultas, oscilando desde casos simples que demandan entre 5 y 10 minutos hasta solicitudes complejas que tardan hasta 72 horas en completarse (Gómez & Pantaleón, 2024). Esta dispersión temporal responde a factores como la dispersión de la información institucional en múltiples manuales y reglamentos, la necesidad de coordinación manual entre distintas dependencias (como Registros Académicos y Tesorería) y la recurrencia de solicitudes formuladas con información incompleta por parte de los usuarios. Tal como sostienen Noguchi et al. (2016), en los servicios tecnológicos educativos la longitud indeterminada del tiempo de respuesta degrada significativamente la percepción del usuario, pues la celeridad y la consistencia informativa son los determinantes principales de la satisfacción del servicio.

Adicionalmente, el área de operaciones de TI carece de un canal centralizado de autoservicio disponible las 24 horas del día que permita resolver autónomamente las dudas técnicas y reglamentarias recurrentes (Gómez & Pantaleón, 2024). La atención fragmentada genera que el personal especializado dedique un porcentaje sustancial de sus horas laborales a responder preguntas repetitivas (como pasos para el restablecimiento de contraseñas del aula virtual, medios de pago autorizados o fechas límite de reserva de matrícula), en lugar de priorizar incidencias de infraestructura crítica.

Frente a este escenario, las alternativas convencionales de atención presentan claras limitaciones operativas: incrementar el personal humano de soporte resulta insostenible en términos de costos para una cobertura continua de 24 horas, mientras que los chatbots tradicionales basados en árboles de decisión o palabras clave rígidas carecen de la flexibilidad semántica requerida para interpretar la diversidad y variabilidad del lenguaje natural estudiantil (Adamopoulou & Moussiades, 2020; Okonkwo & Ade-Ibijola, 2021).

Asimismo, el empleo de modelos generativos de inteligencia artificial de forma aislada conlleva el riesgo de alucinación fáctica, emitiendo respuestas verosímiles pero normativamente erróneas, lo cual resulta crítico en trámites y pagos universitarios (Lewis et al., 2020).

Por consiguiente, la naturaleza del problema demanda una arquitectura dual: por un lado, modelos basados en Transformers capaces de comprender dependencias contextuales complejas y resolver diálogos en lenguaje natural; y, por otro, mecanismos de Generación Aumentada por Recuperación (RAG) que restrinjan la generación del modelo a la evidencia textual de los manuales y reglamentos oficiales de la institución. Esta convergencia tecnológica se proyecta como una solución viable para automatizar la atención de primer contacto, reducir sustancialmente los tiempos de resolución y garantizar la fidelidad fáctica requerida en las operaciones de TI de la universidad.

Asimismo, cabe precisar que las denominaciones técnicas «SipánGPT» (asignada a la plataforma conversacional) y «Sipán-STAIR» (asignada a la arquitectura de recuperación jerárquica) corresponden a nombres clave de desarrollo asignados en honor y reconocimiento al patrimonio histórico, arqueológico y cultural de la región Lambayeque (asociado al Señor de Sipán y a la cultura Mochica), desvinculando formalmente dicha designación de cualquier entidad educativa privada o marca institucional en particular.

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
En el plano práctico, la investigación resuelve un cuello de botella asistencial constatado en el área de operaciones de TI de la universidad privada bajo estudio. El diagnóstico situacional evidenció una carga semestral de 1,400 a 1,500 requerimientos de soporte técnico, con tiempos de atención que se extienden hasta por 72 horas debido a la fragmentación de canales y a la gestión manual de consultas repetitivas (Gómez & Pantaleón, 2024; Anexo 3; Serrano et al., 2021). La implementación del asistente conversacional automatiza la resolución de incidencias de primer contacto con disponibilidad continua (24/7), disminuyendo los tiempos de espera a escasos segundos y reduciendo la frustración del usuario en periodos críticos como matrículas y evaluaciones (Banu, 2023; Noguchi et al., 2016).

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

## 2.1. Antecedentes de la investigación

Espinosa-Luna et al. (2023) desarrollaron y evaluaron la usabilidad de un chatbot conversacional basado en el modelo de lenguaje GPT-3.5-Turbo para la atención de preguntas frecuentes de estudiantes de primer ciclo de Ingeniería de Sistemas en la Universidad Nacional de Trujillo. La arquitectura del sistema fue implementada bajo un esquema *serverless* en la nube mediante la plataforma Render, empleando una API REST construida con Node.js y Express, una base de datos en MongoDB Atlas para el repositorio de información académica y la API de WhatsApp Cloud configurada mediante *webhooks*, aplicando técnicas de ingeniería de peticiones (*prompt engineering*) para delimitar el contexto de las respuestas. Mediante un diseño preexperimental con enfoque cuantitativo, la solución se evaluó con una muestra de 41 estudiantes que interactuaron con el asistente durante cinco días y completaron el instrumento CUQ (*Chatbot Usability Questionnaire*). Como resultado, el chatbot obtuvo una usabilidad media de 73,40 puntos (DE = 10,10), situándose en un nivel aceptable (grado B-) y estadísticamente superior al umbral estándar de referencia de 68 puntos mediante la prueba T de Student ($t = 3,396$; $p = 0,002$); asimismo, el 93% de los participantes calificó las respuestas como útiles, destacando puntuaciones altas en facilidad de uso (4,29/5) y navegación (4,22/5). La investigación concluyó que los modelos LLM integrados a servicios de mensajería instantánea optimizan la atención y disponibilidad de soporte al estudiante, recomendando incorporar técnicas de ajuste fino (*fine-tuning*) para reducir patrones de respuesta robóticos e incrementar la naturalidad conversacional.

Anaya y Rodríguez (2026) desarrollaron e implementaron un chatbot conversacional basado en inteligencia artificial para el Área de Admisión de la Universidad Nacional Pedro Ruiz Gallo, con el propósito de optimizar la eficiencia operativa y la calidad de las respuestas ante las consultas frecuentes de los postulantes. La investigación siguió un diseño cuasiexperimental de enfoque aplicado y alcance exploratorio, integrando el modelo de lenguaje GPT-3.5 Turbo mediante la API de Asistentes de OpenAI bajo un esquema de generación aumentada por recuperación (RAG) con indexación vectorial (*vector store*). El componente del backend se construyó como una API REST en Node.js y Express desplegada en la nube sobre Render, interconectada en tiempo real con la API de WhatsApp Cloud de Meta a través de *webhooks*, empleando como base de conocimiento el prospecto de admisión y el banco de preguntas institucionales debidamente depurados y normalizados. La solución fue evaluada mediante una validación comparativa frente a la documentación oficial bajo criterios de exactitud, relevancia y claridad, alcanzando una precisión del 75% en respuestas correctas (15 de 20 consultas temáticas evaluadas) y reduciendo el tiempo de atención a escasos segundos sin intervención humana; asimismo, se constató que el modelo procesó con mayor fidelidad los datos presentados en texto plano en comparación con los extraídos de tablas o imágenes. Los autores concluyeron que el chatbot constituye una alternativa funcional, escalable y de bajo costo para agilizar la atención preuniversitaria, recomendando estructurar la información institucional en formatos planos para maximizar la efectividad de la recuperación semántica.

Veliz y Velásquez (2024) implementaron un asistente virtual conversacional mediante un chatbot interactivo integrado a WhatsApp con el objetivo de optimizar la atención de consultas sobre los procesos de gestión académica para estudiantes y egresados de la Universidad Nacional Pedro Ruiz Gallo (UNPRG). La investigación se desarrolló bajo un enfoque cuantitativo-descriptivo de tipo aplicado y diseño preexperimental con mediciones diagnósticas previas y posteriores a la intervención tecnológica, gestionando el ciclo de desarrollo de software a través del marco de trabajo ágil Scrum (estructurado en cuatro Sprints, seis historias de usuario y 29 tareas monitoreadas con tableros Kanban y gráficos de *Burndown*). A nivel arquitectónico, la solución se programó en lenguaje Python utilizando librerías como Flask y Pandas, estructurando una base de conocimiento en hojas de cálculo (Microsoft Excel) organizada en árboles temáticos sobre planes de estudio, convalidaciones, matrículas, actas, exámenes y expedición de grados y títulos; asimismo, el entorno operativo integró los servicios en la nube de Twilio para la mensajería de WhatsApp, conectándose al servidor local mediante un túnel de proxy inverso seguro con Ngrok para el procesamiento de peticiones vía *webhooks*. La evaluación se contrastó aplicando una encuesta diagnóstica inicial a 300 alumnos y una encuesta post-implementación a una muestra de 307 estudiantes de la Facultad de Ciencias Físicas y Matemáticas que utilizaron el sistema, evaluando las dimensiones de usabilidad (eficacia, eficiencia y satisfacción) y experiencia de usuario (facilidad de aprendizaje y nivel de aceptación) bajo escala Likert. Como resultados cuantitativos principales, la satisfacción estudiantil con el acceso a la información académica aumentó de un 48,70% inicial en los canales tradicionales a un 89,45% tras la puesta en marcha del asistente virtual; a nivel dimensional, la usabilidad alcanzó un promedio general del 86,80% (con 84,85% en eficacia, 89,40% en eficiencia y 86,15% en satisfacción), destacando que el 90,50% de los encuestados afirmó haber obtenido respuesta de forma inmediata y el 86,00% logró resolver sus dudas con éxito. Paralelamente, la dimensión de experiencia registró un 89,45% favorable (87,00% en facilidad de aprendizaje y 91,80% en aceptación), con un 91,20% de disposición a recomendar el uso de la herramienta. Los autores concluyeron que la automatización de consultas mediante mensajería instantánea descongestiona significativamente los módulos de atención presencial y estandariza la orientación universitaria, recomendando migrar el asistente a servidores dedicados de la universidad y designar personal técnico permanente para actualizar periódicamente el repositorio normativo institucional.

Carrizales y Ramirez (2019) diseñaron e implementaron una arquitectura tecnológica basada en un chatbot cognitivo con la finalidad de optimizar el acceso y la búsqueda de información institucional en el Sistema Integrado de la Calidad (SICA) de la Universidad Peruana de Ciencias Aplicadas. El desarrollo metodológico se estructuró a partir del marco de referencia CCRA V4.0 (*Cloud Computing Reference Architecture*) complementado con buenas prácticas del PMBOK, seleccionando a IBM Cloud como proveedor principal tras un análisis comparativo de plataformas. La solución integró servicios cognitivos de IBM Watson (Watson Assistant para la gestión del diálogo y Watson Discovery para la indización y recuperación de documentos normativos, reglamentos y políticas), incorporando además capacidades de voz con *Speech to Text* y *Text to Speech* sobre una interfaz web con intercambio de mensajes bajo el formato JSON. Tras una fase de diagnóstico donde más del 80% de los usuarios manifestó demoras superiores a los 3 minutos en el portal tradicional, el prototipo se evaluó durante un mes en el que registró 278 conversaciones y 1325 mensajes (con un promedio de 4,77 mensajes por sesión). La validación mediante encuesta aplicada a personal administrativo y auditores internos evidenció que el 89,5% consideró óptimo el tiempo de respuesta, el 89,4% destacó su facilidad de uso, el 63,2% valoró positivamente su interactividad y eficacia, alcanzando un 63,1% de satisfacción general; asimismo, se constató un incremento del 65% en la confianza del sistema y un aumento del 85,4% en la experiencia de usuario. La investigación concluyó que una arquitectura en la nube fundamentada en servicios cognitivos optimiza sustancialmente la gestión documental académica en contraste con los motores de búsqueda tradicionales, recomendando una adecuada gestión de incidentes bajo ITIL y la previsión de costos de licenciamiento para garantizar la disponibilidad continua del servicio.

Choque (2018) implementó un modelo de tecnología cognitiva complementado con patrones de experiencia del cliente (*Customer Experience* - CX) para optimizar los servicios de soporte académico mediante un chatbot en el área de Canales de Contacto de la Universidad Peruana de Ciencias Aplicadas. La propuesta se estructuró a partir de un flujo metodológico de cinco fases (captura, comprensión de lenguaje natural, gestión del diálogo, generación de respuesta y consumo), gestionado bajo los lineamientos del PMBOK e integrado conceptualmente con ITIL v3 para el soporte operativo. A nivel técnico, la solución se desplegó sobre la plataforma en la nube IBM Cloud, utilizando JavaScript para el desarrollo del aplicativo web y conectándose con la API Watson Conversation para el procesamiento de lenguaje natural, en cuyo entorno se modelaron intenciones, entidades y flujos de diálogo gobernados por reglas de negocio y patrones CX (marca, emoción y función). La validación se llevó a cabo mediante una prueba de concepto con una muestra de 50 estudiantes universitarios de diversas carreras y a través del juicio de expertos con analistas y directivos del área de Calidad y Servicios. Como resultados principales, el asistente redujo en más del 99,9% el tiempo de espera por consulta (pasando del estándar institucional de hasta 48 horas a menos de medio segundo de respuesta inmediata) y alcanzó un 80% de aprobación estudiantil para su adopción como canal oficial de atención; asimismo, evaluaciones previas de usabilidad situaron a la herramienta en 81,875 puntos en la escala SUS (*System Usability Scale*). La investigación concluyó que la combinación de computación cognitiva y patrones de interacción centrados en la experiencia del usuario mitiga la frialdad y las demoras de las plataformas universitarias tradicionales, demostrando viabilidad técnica y aceptabilidad institucional para la atención de procesos críticos como la matrícula.

Musayón (2023) determinó el impacto de un agente conversacional basado en inteligencia artificial en el proceso de atención de los estudiantes de la Universidad Nacional Toribio Rodríguez de Mendoza de Amazonas (filial Bagua). La investigación se desarrolló bajo un enfoque cuantitativo, de tipo aplicado y diseño preexperimental con mediciones de pretest y postest en un solo grupo, aplicándose a una muestra probabilística de 132 alumnos matriculados en la Facultad de Ingeniería de Sistemas y Mecánica Eléctrica. A nivel tecnológico, la solución integró un modelo de lenguaje de gran escala (LLM) de OpenAI (ChatGPT) interconectado con el portal web institucional mediante una arquitectura compuesta por módulos de procesamiento y generación de lenguaje natural (NLP/NLG), un gestor de diálogo y una base de conocimientos alimentada con el corpus de preguntas frecuentes y reglamentos normativos de la entidad. Para la recolección de datos se emplearon fichas de observación validadas por juicio de expertos, analizando tres dimensiones operativas: expectativa del usuario, interacción y calidad del servicio. Tras el análisis inferencial mediante la prueba de rangos con signo de Wilcoxon ($p = 0,000$), se demostraron diferencias estadísticamente significativas: el primer tiempo promedio de respuesta descendió de 626,72 minutos a 0,0909 minutos (con una mediana reducida de 15 minutos a escasos 0,09 minutos, equivalentes a ~5,4 segundos), el tiempo de resolución cayó de una media de 850,67 minutos a 2,363 minutos (mediana disminuida de 30 a 2 minutos) y el índice de satisfacción global del estudiante aumentó de 68,13% a 86,65% (mediana incrementada del 75% al 90%). La investigación concluyó que los chatbots basados en IA transforman favorablemente los canales de atención universitaria al suprimir los tiempos de espera y brindar resolución casi inmediata a consultas académicas críticas, recomendando la delimitación y mantenimiento continuo de la base de datos documental para conservar la precisión del agente.

Lopez y Segura (2023) desarrollaron un chatbot con inteligencia artificial orientado a optimizar la calidad en la atención de consultas sobre grados académicos y títulos para estudiantes y egresados del Instituto para la Calidad de la Educación de la Universidad de San Martín de Porres (USMP-ICED). La investigación correspondió a un estudio de tipo aplicado bajo un enfoque cuantitativo, gestionando el ciclo de desarrollo del proyecto mediante el marco de trabajo Kanban. En el aspecto tecnológico, el asistente se construyó con Node.js y JavaScript, incorporando técnicas de Procesamiento de Lenguaje Natural (NLP) a través de la herramienta Google Dialogflow para asegurar la identificación precisa de intenciones, entidades y el contexto de las consultas a partir de un banco estructurado de preguntas frecuentes. La validación del sistema contempló pruebas funcionales y una evaluación de usabilidad fundamentada en la norma ISO/IEC 25010, complementada con el análisis de la calidad de servicio mediante el modelo multidimensional SERVQUAL, el cual examinó las brechas en capacidad de respuesta (tiempo de respuesta), confiabilidad (precisión y eficiencia conversacional) y empatía. Como resultados principales, el aplicativo obtuvo una puntuación de usabilidad de 8,89 sobre 10 bajo el estándar ISO 25010 y mejoró la calidad del servicio de atención en un 83,52% de acuerdo con la escala SERVQUAL; asimismo, la solución optimizó la experiencia del usuario al resolver las dudas académicas en lapsos inmediatos de 1 a 2 minutos. Los autores concluyeron que la integración de servicios cognitivos en plataformas de mensajería automatizada agiliza de forma sustantiva la gestión y el acceso a la información administrativa universitaria, recomendando el monitoreo constante de intenciones para alinear las respuestas a futuras modificaciones en las directivas de graduación.

Quispe (2024) implementó un chatbot conversacional denominado «Upcito» orientado a optimizar la calidad del servicio de atención al egresado en los trámites de obtención de grados académicos y títulos profesionales en la Universidad Peruana de Ciencias e Informática. El estudio se enmarcó en una investigación de tipo aplicada con diseño preexperimental de pretest y postest sobre un único grupo, evaluando a una muestra no probabilística de 54 egresados que realizaron gestiones administrativas durante el año 2024. En el plano tecnológico, el asistente se integró directamente en el portal web institucional mediante la plataforma conversacional Chatling, estructurando árboles de decisión y flujos guiados para la consulta interactiva de requisitos según el nivel académico solicitado (bachiller, título profesional o maestría). La medición de datos se realizó a través de un cuestionario de satisfacción de 26 ítems estructurado bajo las dimensiones de fiabilidad, capacidad de respuesta y seguridad adaptadas del modelo SERVQUAL, validado por juicio de expertos y con una alta confiabilidad mediante el coeficiente Alfa de Cronbach ($\alpha = 0,850$ en el pretest y $\alpha = 0,834$ en el postest). Tras aplicar la prueba no paramétrica de rangos con signo de Wilcoxon, se comprobaron diferencias estadísticamente significativas en todas las variables ($p = 0,000$): la media de la calidad general del servicio aumentó de 2,0370 a 3,7963 puntos sobre 5 ($Z = -6,394$), reduciendo la insatisfacción inicial del 81,5% al 1,9% y logrando un 74,1% de valoraciones positivas; asimismo, la fiabilidad se elevó de 2,0556 a 3,8333 ($Z = -6,219$), la capacidad de respuesta se incrementó de 2,0370 a 3,8148 ($Z = -6,397$) alcanzando un 72,3% de aprobación y la seguridad subió de 2,1667 a 3,7037 ($Z = -6,339$). La investigación concluyó que la automatización de la atención mitiga la saturación en ventanilla y estandariza la orientación institucional en horarios ininterrumpidos (24/7), sugiriendo la incorporación de algoritmos de inteligencia artificial más complejos y protocolos de escalamiento hacia agentes humanos para la atención de casos no previstos.

De La Cruz y Mere (2023) implementaron un chatbot interactivo con inteligencia artificial con el propósito de mejorar el aprendizaje significativo del curso de Algoritmos en los estudiantes del tercer ciclo de la Facultad de Ingeniería de Sistemas de la Universidad Nacional San Luis Gonzaga de Ica. La investigación se desarrolló bajo un enfoque cuantitativo de tipo aplicado y diseño preexperimental con mediciones de pretest y postest en un solo grupo, aplicándose a una muestra no probabilística intencional de 32 alumnos. En el apartado arquitectónico, el asistente conversacional se construyó sobre la plataforma de procesamiento de lenguaje natural Dialogflow de Google, estructurando páginas de diálogo, entidades y entrenamiento de intenciones (*intents*) enlazadas a servicios en la nube de Google Cloud Platform para ofrecer explicaciones teóricas y resolución contextual de dudas de programación. La recolección de datos se llevó a cabo mediante un cuestionario de 35 ítems formulado a partir de la teoría del aprendizaje significativo de Ausubel (evaluando las dimensiones de aprendizaje representacional, de conceptos y proposicional), complementado con una escala de evaluación de percepción de la herramienta. Tras el procesamiento inferencial mediante la prueba no paramétrica de rangos con signo de Wilcoxon, se comprobaron incrementos estadísticamente significativos en todos los niveles evaluados ($p = 0,000$): la media global del aprendizaje significativo se elevó de 1,13 puntos (DE = 0,336) en el pretest a 4,41 puntos (DE = 0,498) en el postest (estadístico de Wilcoxon = 528,00), transformando un 88% de respuestas en fuerte desacuerdo inicial a un 100% de aprobación estudiantil (59% de acuerdo y 41% muy de acuerdo); paralelamente, el aprendizaje representacional incrementó su promedio de 1,34 a 4,44 puntos, el aprendizaje de conceptos ascendió de 1,47 a 4,44 y el proposicional aumentó de 1,25 a 4,47 ($p = 0,000$). Los autores concluyeron que los asistentes conversacionales basados en IA actúan como un canal complementario idóneo para suplir la falta de retroalimentación personalizada en aulas con alta carga estudiantil, facilitando la asimilación autodirigida de estructuras algorítmicas y recomendando la articulación formal del agente dentro de las guías de práctica de la asignatura.

Vallejos (2023) determinó la influencia del uso de un chatbot en el servicio de atención al cliente a través de redes sociales en la empresa deportiva Master GOL en la ciudad de Tarapoto. La investigación adoptó un enfoque cuantitativo de tipo aplicado y diseño cuasiexperimental, evaluando a una muestra no probabilística de 60 clientes divididos en un grupo de control (30 atendidos por el personal) y un grupo experimental (30 atendidos mediante el asistente virtual). El ciclo de desarrollo de software se guio por la metodología ágil Programación Extrema (XP) en sus cuatro fases, construyendo una solución conversacional integrada a la API de WhatsApp Cloud a través de *webhooks*, respaldada por una plataforma web de administración desarrollada con Ruby on Rails (v6) en el backend, Vue.js en el frontend y MariaDB como motor de base de datos relacional para gestionar la disponibilidad de horarios, reservas y enlaces de localización con Google Maps. Para la evaluación se diseñó un cuestionario de 15 ítems en escala Likert basado en el modelo SERVQUAL, analizando las dimensiones de calidad del servicio y satisfacción del cliente. Tras corroborar la distribución normal de los datos mediante la prueba de Shapiro-Wilk, el contraste inferencial mediante la prueba T de Student para muestras independientes ($t = -75,509$; $gl = 58$; $p = 0,000$) demostró mejoras estadísticamente significativas: el nivel general de atención favorable aumentó del 33,87% en el pretest al 94,53% en el postest; a escala dimensional, la calidad de servicio se incrementó del 32,87% al 95,53% y la satisfacción del cliente ascendió del 35,87% al 92,53%, destacando puntuaciones de total acuerdo en resolución de problemas (96,7%), atención personalizada (93,3%) y capacidad de respuesta inmediata (90,0%). El estudio concluyó que la automatización de la atención por canales de mensajería social optimiza sustancialmente la interacción comercial al suprimir los tiempos muertos y la saturación de los canales telefónicos tradicionales, recomendando formalizar los requerimientos de verificación de Meta para evitar interrupciones en la disponibilidad del servicio.

Hartono et al. (2025) diseñaron y evaluaron un asistente virtual de preguntas y respuestas basado en el modelo de lenguaje de código abierto Gemma-2-2b-it con el propósito de optimizar el acceso a la información académica, operativa y de admisión para postulantes y estudiantes en el Institut Sains dan Teknologi Terpadu Surabaya (Indonesia). La metodología combinó y contrastó empíricamente dos enfoques de optimización: Generación Aumentada por Recuperación (RAG) y ajuste fino (*finetuning*) mediante QLoRA (cuantización a 4 bits, tasa de aprendizaje de $1\text{e-}3$ por dos épocas). El corpus documental se conformó a partir de 1078 transcripciones de conversaciones de WhatsApp, el contenido extraído del portal web universitario y cuatro reglamentos institucionales en formato PDF, procesados mediante segmentación recursiva (*chunk size* de 1000 caracteres y *overlap* de 100) y aumentación sintética de datos. La arquitectura RAG integró la base de datos vectorial ChromaDB comparando dos modelos de incrustación: el multilingüe PMM (`paraphrase-multilingual-mpnet-base-v2`) y el modelo nativo en indonesio LZR (`all-indo-e5-small-v4`). A través del marco de evaluación estandarizado RAGAS (*Retrieval Augmented Generation Assessment*), los resultados demostraron que el RAG implementado sobre el modelo base no ajustado (Escenario 2) alcanzó el mejor desempeño global con una puntuación RAGAS de 0,72 (fidelidad de 0,78, precisión de contexto de 0,81, cobertura de contexto de 0,69 y relevancia de respuesta de 0,65); por el contrario, los modelos RAG sometidos a ajuste fino previo sufrieron una pérdida drástica de fidelidad (puntuaciones entre 0,04 y 0,11), originada por el sobreajuste (*overfitting*) a las expresiones informales del chat. Asimismo, en una prueba de 300 consultas de prueba, el modelo con ajuste fino exclusivo (Escenario 1) obtuvo mayores niveles de precisión (0,43), exhaustividad (0,43) y ROUGE-1 (0,36) en preguntas cerradas del dominio entrenado, registrando una similitud de coseno equivalente (0,51 frente a 0,59 del RAG base). Los autores concluyeron que el paradigma RAG sobre modelos base garantiza una mayor capacidad de generalización y anclaje factual ante información académica cambiante, recomendando incorporar mecanismos de reclasificación (*reranking*) y ajuste fino específico sobre el modelo de *embeddings* para perfeccionar la recuperación de contexto.

Sánchez (2023) desarrolló un asistente virtual en Telegram enfocado en optimizar el proceso de integración, orientación y resolución de dudas de los alumnos de nuevo ingreso en el marco del Proyecto Mentor de la Escuela Técnica Superior de Ingenieros Informáticos de la Universidad Politécnica de Madrid (España). La metodología de desarrollo de software comprendió el análisis de necesidades estudiantiles, el diseño de la persistencia de datos y la codificación del sistema en el lenguaje Python utilizando el entorno PyCharm y la librería `pyTelegramBotAPI` (`telebot`), implementando concurrencia mediante hilos de ejecución (*threading*) para gestionar la recepción de mensajes en segundo plano sin bloquear el hilo principal. La arquitectura tecnológica se sustentó en una base de datos relacional MySQL integrada mediante `mysql.connector`, la cual articuló tablas dinámicas para el registro de estudiantes a través de su identificador de chat de Telegram y tablas estáticas con información de las 10 asignaturas obligatorias de primer curso, horarios, aulas, correos de docentes y datos históricos de rendimiento (tasas de rendimiento, éxito y absentismo correspondientes a tres periodos académicos entre 2019 y 2022). A nivel de interfaz, el bot incorporó teclados interactivos con los módulos `ReplyKeyboardMarkup`, `ReplyKeyboardRemove` y `ForceReply`, implementando comandos funcionales (`/alta`, `/mis_asignaturas`, `/tasas_asignatura`, `/tasas_curso`, `/faq`) para la consulta rápida de profesores, comparativas de dificultad académica y redirección a enlaces oficiales de trámites y reservas universitarias. La validación del prototipo evidenció que la restricción de interacciones a menús de botones estructurados previene errores de sintaxis en el ingreso de datos y acorta drásticamente el tiempo de localización de recursos frente a la navegación tradicional en el portal web institucional. La autora concluyó que la integración de chatbots en plataformas de mensajería masiva constituye un soporte complementario de alto valor para mitigar el estrés informativo de los ingresantes, recomendando incorporar en etapas futuras modelos de lenguaje natural con inteligencia artificial para habilitar diálogos más humanos e interfaces de voz accesibles.

Santacruz (2022) implementó un chatbot interactivo basado en inteligencia artificial orientado a automatizar los procesos de difusión de información y comunicación en la Unidad de Titulación de la carrera de Pedagogía de las Ciencias Experimentales Informática de la Universidad Central del Ecuador. La investigación se desarrolló bajo un enfoque cualitativo de alcance exploratorio-descriptivo con diseño no experimental de corte transversal bajo la modalidad de propuesta tecnológica, estructurando el ciclo de desarrollo del asistente mediante la metodología de diseño instruccional ADDIE *Rapid Prototyping* en sus cinco fases cíclicas (análisis, diseño, desarrollo, implementación y evaluación). En la fase diagnóstica inicial, se aplicaron entrevistas semiestructuradas a una muestra de ocho docentes de la carrera, cuyos testimonios fueron analizados mediante codificación y redes semánticas con el software ATLAS.ti para determinar los requerimientos informativos críticos. A nivel arquitectónico, la solución se configuró sobre la plataforma de procesamiento de lenguaje natural Google Dialogflow, diseñando un árbol de intenciones (*intents*) y frases de entrenamiento orientadas a absolver consultas sobre requisitos documentales, instructivos, modalidades de grado (proyectos o examen complexivo) y canales de contacto institucional. La articulación técnica se gestionó a través de la consola de Google Cloud Platform mediante credenciales de cuenta de servicio exportadas en formato JSON, integrándose con el aplicativo móvil Autorespondedor de WhatsApp para gobernar las respuestas automáticas e interactuar con los usuarios desde la plataforma WhatsApp Business, vinculando además enlaces directos a carpetas documentales en Google Drive. La evaluación final de la herramienta se llevó a cabo mediante una matriz técnica de 16 ítems distribuida en cuatro dimensiones (sencillez de uso, visualización, formas de interacción e innovación) calificada por docentes especialistas en tecnologías educativas, alcanzando una puntuación media global de 8,9 sobre 10 puntos (con calificaciones individuales de 8,8 y 9,0). El autor concluyó que la implementación de agentes conversacionales integrados a servicios de mensajería masiva elimina la saturación burocrática y reduce los tiempos de espera del alumnado frente al uso exclusivo del correo electrónico institucional, recomendando mantener la actualización continua de las intenciones de diálogo conforme varíen los reglamentos de titulación y replicar el modelo en otras áreas académicas de la facultad.

Garibay (2020) diseñó e implementó un asistente virtual inteligente denominado «CP-Bot» con el propósito de optimizar los canales de atención y agilizar el registro de socios en el programa de recompensas Club Premier de Grupo Aeroméxico. La propuesta se desarrolló bajo la modalidad de proyecto laboral estructurado en un plan de seis fases operativas (planeación y *kick-off*, entrenamiento, pruebas, lanzamiento, ajustes y autogestión), complementado con un esquema de mantenimiento técnico continuo. En el ámbito arquitectónico, la solución se construyó sobre la plataforma cognitiva Agentbot provista por Aivo, la cual incorporó algoritmos de Procesamiento de Lenguaje Natural y aprendizaje automático (*Machine Learning*) para interpretar intenciones, tolerar errores ortográficos y contextualizar el diálogo; asimismo, la herramienta se integró de forma omnicanal con WhatsApp Business API, Facebook Messenger y Chat Web bajo las normativas de seguridad de datos GDPR y Zendesk Sunshine, contemplando un protocolo de enrutamiento hacia operadores humanos del centro de contacto (Teleperformance) para gestiones de alta complejidad. La evaluación del sistema se realizó mediante encuestas automatizadas de satisfacción y seguimiento métrico sobre un volumen superior a las 10 000 interacciones. Como resultados destacados, WhatsApp se consolidó como el canal preferencial con 1295 interacciones mensuales, donde el 83,33% correspondió a usuarios nuevos que gestionaron principalmente su inscripción (*enrollment*) y consulta de millas; en el plano operativo, el soporte virtual redujo en un 50% el tiempo promedio de atención humana ante consultas complejas de empresas aliadas (disminuyendo de 30 a 15 minutos), alcanzando una valoración media de 4,67 sobre 5 estrellas, un índice de satisfacción del cliente (C-Sat) del 93,33% y una efectividad resolutiva directa del 50,00%. El estudio concluyó que la incorporación de asistentes virtuales en plataformas de mensajería instantánea descongestiona significativamente los conmutadores telefónicos y democratiza el autoservicio 24/7 en empresas de servicios masivos, recomendando simplificar las secuencias de captura de datos para mitigar la tasa de deserción estudiada durante el llenado de formularios extensos.

Winkler et al. (2020) desarrollaron y evaluaron experimentalmente a «Sara», un agente conversacional inteligente dotado de andamiaje pedagógico (*scaffolding*) e interacción multimodal (voz y texto), diseñado para intervenir activamente durante lecciones en video y potenciar el aprendizaje de programación en Python. La investigación se sustentó en los postulados de la teoría sociocultural del andamiaje y la teoría cognitiva del aprendizaje multimedia, implementando un diseño experimental de laboratorio factorial $2 \times 2$ con medidas repetidas sobre una muestra de 182 estudiantes universitarios de pregrado y posgrado distribuidos en cuatro tratamientos y un grupo de control. En el ámbito arquitectónico, el asistente se integró sobre un reproductor web articulando tres principios de diseño: un esquema jerárquico de diálogo principal y subdiálogos correctivos calibrados a la Zona de Desarrollo Próximo (ZPD) del aprendiz; un clasificador de intenciones sustentado en la librería de código abierto NLP.js desplegada en infraestructura propia por motivos de privacidad y entrenada con un corpus de 800 enunciados, conectado a la Web Speech API de HTML5 para la transcripción del habla del estudiante; y un motor de salida multicanal basado en la Speech Synthesis API de HTML5 que emitía explicaciones auditivas acompañadas de texto en pantalla. Mediante análisis de covarianza (ANCOVA) controlando el conocimiento previo, la carga cognitiva y la preferencia perceptual, los resultados confirmaron efectos principales altamente significativos: el grupo que interactuó con Sara obtuvo los mayores promedios normalizados tanto en retención de información con 77,8 puntos ($F(4,359) = 29,9$; $p < 0,0001$; $\eta_p^2 = 0,08$) como en capacidad de transferencia para resolver nuevos problemas de código con 65,4 puntos ($F(4,359) = 22,3$; $p < 0,0001$; $\eta_p^2 = 0,06$), superando ampliamente al grupo de control pasivo (60,9 y 44,0 puntos respectivamente); paralelamente, se comprobó un efecto de interacción positivo entre el andamiaje y la modalidad por voz ($p = 0,0001$ en retención y $p = 0,009$ en transferencia), registrando una precisión en la selección de intervenciones (*ISA*) del 95,48%. Los investigadores concluyeron que incorporar agentes conversacionales con voz y andamiaje dinámico en videos educativos emula con eficacia la tutoría humana presencial y supera las limitaciones del e-learning estático, recomendando desarrollar herramientas de autoría accesibles para facilitar la configuración de estos asistentes a docentes sin experiencia en programación.

Okonkwo y Ade-Ibijola (2021) desarrollaron una revisión sistemática de literatura orientada a examinar el estado del arte, los beneficios operacionales y los principales desafíos técnicos vinculados a la implementación de chatbots en el ámbito educativo. La investigación siguió las directrices metodológicas de revisión sistemática para ingeniería de software establecidas por Kitchenham y Wohlin, estructuradas en tres fases formales (planificación, ejecución y reporte). La exploración documental se llevó a cabo en seis bases de datos científicas de referencia (IEEE Digital Library, ScienceDirect, SpringerLink, Scopus, Taylor & Francis y ERIC) abarcando la producción académica en inglés entre 2015 y mayo de 2021 mediante ecuaciones booleanas combinadas de agentes conversacionales y educación. De un universo inicial de 2048 registros identificados, los autores seleccionaron una muestra final de 53 artículos tras superar un protocolo de inclusión, exclusión y un control de calidad metodológica compuesto por cinco criterios evaluados por pares con un umbral mínimo aprobatorio de 7,5 sobre 15 puntos. Como hallazgos cuantitativos, el mapeo evidenció que la mayor concentración de aplicaciones correspondió a la enseñanza y el aprendizaje con un 66%, seguido por el desarrollo e investigación académica con un 19%, la evaluación del rendimiento estudiantil con un 6%, las tareas de gestión y soporte administrativo con un 5% y la asesoría vocacional con un 4%. Entre los beneficios esenciales se identificaron la capacidad de atención concurrente a múltiples usuarios sin saturación, el acceso inmediato a la información (24/7) y la centralización de contenidos formativos; paralelamente, se catalogaron como desafíos críticos las deficiencias del procesamiento de lenguaje natural (NLP) ante expresiones coloquiales no entrenadas, la escasez de evaluaciones empíricas con muestras muestrales representativas y la dificultad logística para supervisar y actualizar continuamente los bancos de conocimiento. Los autores concluyeron que los asistentes conversacionales son piezas clave para la modernización institucional, recomendando formular protocolos rigurosos de pruebas de usabilidad y establecer directrices éticas claras sobre la privacidad y el resguardo de los datos del alumnado.

Parrales-Bravo et al. (2024) desarrollaron y evaluaron «CSM» (*Chatbot Solution to Manage Student Questions*), un sistema conversacional de código abierto basado en aprendizaje automático y procesamiento de lenguaje natural integrado en Telegram, orientado a resolver dudas sobre aranceles, pagos y matrícula de los estudiantes del Curso de Nivelación de Carrera en Ingeniería de Software de la Universidad de Guayaquil (Ecuador). La arquitectura del agente se estructuró a partir de un perceptrón multicapa (MLP) con regularización L2 (0,01) y optimizador Adam, evaluando tres variantes estructurales mediante validación cruzada de 5 pliegues (*k-fold cross-validation*); se seleccionó la segunda versión (tres capas densas de 128, 64 y capa de salida Softmax, con capas intermedias *Dropout* al 50% y activación ReLU, entrenada por 250 épocas con *batch size* de 5), la cual alcanzó una exactitud del 83,20% en validación sin incurrir en el sobreajuste detectado en modelos más complejos. El pipeline de procesamiento lingüístico empleó tokenización, lematización con WordNetLemmatizer (NLTK Python) y un modelo de bolsa de palabras binaria (BoW), alojando el backend en la nube sobre Render conectado a una base de datos relacional PostgreSQL para el control de sesiones y cuotas de uso (30 consultas diarias por estudiante), implementando validación de acceso mediante contraseñas de un solo uso (OTP vía PyOTP) a correos institucionales. La evaluación cuantitativa con seis estudiantes midió los tiempos de realización de tres tareas operativas: registro inicial (media de 3,50 minutos), ejecución de cinco consultas (media de 3,16 minutos; DE = 0,75) y desuscripción (media de 3,33 minutos), confirmando la prueba de Kruskal-Wallis la ausencia de diferencias significativas entre tareas ($p = 0,2623 > 0,05$) y evidenciando una notable reducción temporal frente a la atención presencial en secretaría. Paralelamente, una encuesta de percepción aplicada a 60 estudiantes universitarios bajo escala Likert (1 a 5) en cinco atributos (facilidad de uso, velocidad, comportamiento del sistema, confianza de reutilización y calidad de respuesta) arrojó puntuaciones aprobatorias superiores a 3 en todas las dimensiones, con una alta concentración en calificaciones de 4 y 5. Los investigadores concluyeron que el despliegue de chatbots en plataformas de mensajería social agiliza sustancialmente la gestión de procesos académicos recurrentes, recomendando investigar la integración con modelos de lenguaje masivos para flexibilizar la comprensión semántica.

Wang et al. (2022) examinaron de manera empírica cómo el uso de chatbots basados en inteligencia artificial genera agilidad empresarial (distinguiendo entre agilidad interna y externa) y cómo dicha agilidad optimiza el desempeño en el servicio de atención al cliente, contrastando el impacto del uso rutinario frente al uso innovador de la tecnología. La fundamentación teórica se estructuró a partir de la Teoría de Capacidades Dinámicas (*Dynamic Capabilities View* - DCV), implementando un diseño de investigación cuantitativo transversal evaluado mediante modelos de ecuaciones estructurales por mínimos cuadrados parciales (PLS-SEM) con el software SmartPLS (v3.2.8) y *bootstrapping* de 5000 remuestreos, complementado con análisis de mediación mediante el macro PROCESS de Hayes. La muestra estuvo constituida por 294 profesionales y empleados del área de marketing y soporte al cliente en Estados Unidos, vinculados a organizaciones que operan con plataformas conversacionales como SnatchBot y Bold360 en diversos sectores (banca y finanzas 15,0%, manufactura 13,3%, comercio minorista 11,9% y salud 9,9%). Los resultados demostraron que el uso de chatbots explicó el 49,37% de la varianza en la agilidad interna y el 48,79% en la externa, las cuales a su vez explicaron el 66,68% de la varianza del desempeño en el servicio al cliente ($R^2 = 0,6668$); asimismo, aunque el uso rutinario influyó positivamente en la agilidad interna ($\beta = 0,23$; $p < 0,001$) y externa ($\beta = 0,22$; $p < 0,001$), el uso innovador desplegó un efecto predictivo sustancialmente superior en ambas dimensiones ($\beta = 0,53$; $p < 0,001$). Paralelamente, se comprobó que la agilidad externa ejerció el mayor impacto sobre la calidad del servicio ($\beta = 0,65$; $p < 0,001$) en contraste con la agilidad interna ($\beta = 0,20$; $p < 0,05$), evidenciando el análisis *post-hoc* que el uso innovador es especialmente determinante en organizaciones grandes ($\beta = 0,58$). La investigación concluyó que los agentes conversacionales con IA trascienden la simple automatización de tareas operativas y actúan como inductores estratégicos de adaptación y flexibilidad institucional, recomendando que las organizaciones promuevan la exploración activa y el descubrimiento de nuevos casos de uso del chatbot más allá de la atención rutinaria de preguntas frecuentes.

León-Granizo y León-Granizo (2021) desarrollaron un asistente virtual conversacional integrado a una aplicación móvil con el objetivo de mejorar y agilizar el acceso a la información recurrente sobre los procesos de matrícula y titulación en la Facultad de Ciencias Físicas y Matemáticas de la Universidad de Guayaquil. La investigación se sustentó en una metodología descriptiva para diagnosticar la problemática de atención en periodos de alta concurrencia y adoptó el marco de trabajo ágil Scrum para la gestión iterativa del desarrollo de software. Para la determinación de requisitos se aplicó un muestreo probabilístico aleatorio sobre una población de 1143 estudiantes de la carrera de Ingeniería en Sistemas Computacionales, consolidando una muestra de 278 encuestados (con un margen de error del 5,21% y un nivel de confianza del 95%), complementada con entrevistas semiestructuradas aplicadas a las analistas de Secretaría General y de la Unidad de Integración Curricular. En el apartado tecnológico, los autores seleccionaron el motor de Procesamiento de Lenguaje Natural Google Dialogflow tras una evaluación comparativa frente a IBM Watson Assistant y Amazon Lex, conectándolo mediante *webhooks* con un servidor en Linode que gestionó la base de datos y un panel web de administración de sesiones; a nivel de interfaz de usuario, se construyó una aplicación móvil con estética de mensajería instantánea utilizando el *framework* híbrido Ionic. Los hallazgos del diagnóstico inicial evidenciaron que el 52,88% de los estudiantes dependía de ventanillas físicas secuenciales y que las cualidades más demandadas para un chatbot eran la precisión en las respuestas (34,17%) y la disponibilidad continua 24/7 (31,65%); posteriormente, la validación del asistente a través de encuestas de satisfacción integradas al cierre de cada interacción demostró que el 75% de las conversaciones proporcionó información plenamente útil y resolutiva para los requerimientos académicos del alumnado. La investigación concluyó que la automatización conversacional móvil descongestiona eficazmente la carga laboral de las dependencias académicas durante los picos de inscripción, recomendando ampliar el entrenamiento de las intenciones de diálogo hacia los servicios y dependencias de toda la universidad para unificar la atención estudiantil.

Kuhail et al. (2023) desarrollaron una revisión sistemática de literatura orientada a clasificar, comparar y reflexionar sobre las técnicas de diseño instruccional y los estilos de interacción humano-computadora implementados en chatbots educativos. La investigación siguió los lineamientos metodológicos para revisiones sistemáticas en ingeniería de software propuestos por Keele, estructurando el protocolo de búsqueda, extracción y síntesis documental con el soporte de la herramienta colaborativa Rayyan. La exploración se efectuó en cuatro bases de datos digitales indexadas (ACM Digital Library, Scopus, IEEE Xplore y SpringerLink) para el decenio comprendido entre 2011 y 2021 mediante ecuaciones booleanas especializadas en agentes conversacionales pedagógicos. A partir de un total inicial de 1208 artículos identificados, un proceso de revisión y descarte por pares bajo criterios de inclusión, exclusión y verificación de rigor empírico consolidó una muestra definitiva de 36 investigaciones primarias (63,88% correspondientes a actas de congresos y 36,11% a artículos de revistas Q1/Q2). Como hallazgos cuantitativos en sus siete dimensiones de análisis, los resultados revelaron que la informática y ciencias de la computación constituyó el área temática más abordada con un 33,33% (enseñanza de lenguajes como Python y Java, bases de datos y redes), seguida por educación general con un 27,77% y aprendizaje de idiomas extranjeros con un 16,66%; a nivel de despliegue, el 69,44% de los chatbots se implementó sobre entornos web, frente a un 16,66% en aplicaciones móviles y un 13,88% en sistemas de escritorio. En cuanto a su rol formativo, el 55,55% operó como agentes de enseñanza directa y el 36,11% como agentes pares de apoyo, predominando una interacción gobernada por el asistente (*chatbot-driven*) en el 88,88% de los casos (52,77% guiados por flujos predeterminados y 36,11% basados en intenciones con herramientas como Dialogflow). Asimismo, el 36,11% de los estudios recurrió a diseños experimentales con grupos de control que evidenciaron mejoras estadísticamente significativas en el aprendizaje y la satisfacción del usuario ($p < 0,05$), identificando como principales debilidades la escasez de datos para el entrenamiento de los modelos y la falta de aplicación explícita de heurísticas de usabilidad. Los investigadores concluyeron que los agentes conversacionales en entornos web potencian notablemente el aprendizaje personalizado y la retención conceptual, recomendando adoptar marcos de diseño centrado en el usuario y explorar herramientas de desarrollo orientadas al usuario final (*End-User Development*) para agilizar su adopción institucional.

Neumann et al. (2025) diseñaron, implementaron y evaluaron «MoodleBot», un agente conversacional de código abierto impulsado por modelos de lenguaje de gran escala (LLM) y Generación Aumentada por Recuperación (RAG), integrado de forma nativa en la plataforma Moodle para apoyar el aprendizaje autorregulado (SRL) y la resolución de dudas en el curso de Bases de Datos y Sistemas de Información de la Universidad RWTH Aachen (Alemania). La solución tecnológica se construyó utilizando el framework LangChain (`BaseMultiActionAgent`) y LlamaIndex sobre el modelo GPT-4 (calibrado a temperatura cero), vinculando una base de datos vectorial Weaviate con incrustaciones generadas por `text-embedding-ada-002` a partir de diapositivas, notas de clase y ejercicios, además de emplear una base de datos MongoDB para la auditoría de costos e historiales de conversación; asimismo, el agente incorporó una cadena `create-stuff-documents-chain` restringida a los cinco fragmentos documentales más relevantes para controlar el gasto computacional. La validación del sistema se sustentó en el Modelo de Aceptación Tecnológica (TAM) mediante un cuestionario en escala Likert (1 a 5) aplicado a una muestra de 46 estudiantes (30 completaron el instrumento en su totalidad), analizado con análisis factorial exploratorio (PCA, varianza explicada del 67%, KMO = 0,7041, esfericidad de Bartlett con $p = 0,000$ y coeficientes Alfa de Cronbach entre 0,688 y 0,802) y regresión múltiple; paralelamente, la precisión técnica se examinó mediante contraste manual por asistentes docentes (TA) y una cadena automatizada de verificación de hechos (`LLMSummarization-CheckerChain`). Como resultados primordiales, los estudiantes reportaron puntuaciones favorables en facilidad de operación (PEOU3 = 4,60) y utilidad para el estudio de contenidos (PU7 = 4,46), evidenciando que la actitud hacia el bot predijo significativamente la intención de uso continuado ($R^2 = 1,0699$; $p = 0,000$); no obstante, la preferencia por el chatbot sobre un tutor humano obtuvo un promedio moderado (BI1 = 2,70), ratificando su función como complemento pedagógico y no como sustituto docente. En el plano técnico, MoodleBot alcanzó una exactitud del 88% en 100 respuestas validadas por el TA, mientras que el fact-checking automático registró una exactitud del 82% pero una baja especificidad (8%), denotando la insuficiencia de emplear el propio LLM como único filtro verificador; finalmente, el costo promedio de las consultas fue de 1,65 USD por estudiante. La investigación concluyó que los agentes RAG embebidos en entornos virtuales de aprendizaje potencian el estudio autónomo y descongestionan los foros de dudas, recomendando explorar modelos de lenguaje de código abierto autoalojados para mitigar la dependencia económica de APIs propietarias.

Neupane et al. (2024) desarrollaron y evaluaron empíricamente BARKPLUG v.2, un sistema integral de chatbot basado en modelos de lenguaje masivos y pipelines de Generación Aumentada por Recuperación (RAG), concebido para centralizar y democratizar el acceso a la información académica, administrativa y de servicios en la Mississippi State University (Estados Unidos). La arquitectura del asistente se alimentó mediante un rastreador web multihilo desarrollado con la librería Scrapy que recopiló y normalizó contenidos provenientes de 42 dependencias universitarias (incluyendo departamentos de ingeniería, admisiones, becas, ayuda financiera, alojamiento, biblioteca y seguridad del campus); la información depurada se estructuró a través del divisor `RecursiveCharacterTextSplitter` con fragmentos de 8000 caracteres y un solapamiento de 1200 caracteres, vectorizándose con el modelo `text-embedding-3-large` de OpenAI y almacenándose en la base de datos vectorial ChromaDB bajo una búsqueda por umbral de similitud mínima. La generación de respuestas se implementó mediante la API de GPT-3.5-Turbo de OpenAI orquestada con LangChain, desplegando la aplicación sobre el framework web Django (Python) con capacidades de autenticación, gestión de historiales y envío de consultas por correo electrónico. La eficacia del sistema se midió mediante una doble aproximación: cuantitativa, aplicando el framework RAGAS sobre preguntas de prueba con respuestas de referencia y de usabilidad subjetiva mediante el cuestionario System Usability Scale (SUS) suministrado a 50 estudiantes de posgrado y pregrado. Como hallazgos cuantitativos más relevantes, BARKPLUG v.2 alcanzó una media armónica global RAGAS de 0,96 sobre 1,0 punto (con valores consistentes de 0,96 a 0,97 entre categorías temáticas), registrando una precisión de contexto entre 0,95 y 0,98, cobertura contextual de 0,96 a 0,99, fidelidad de respuesta de 0,96 a 0,99 y relevancia entre 0,96 y 0,99; en la evaluación de extremo a extremo, el sistema obtuvo un 0,8923 en exactitud de respuesta (*answer correctness*) para recursos universitarios y un 0,8434 en similitud semántica para programas de ingeniería, mientras que la usabilidad percibida arrojó un puntaje medio SUS de 67,75 puntos, confirmando un nivel de usabilidad práctico y satisfactorio. Los autores concluyeron que la articulación de RAG multidepartamental elimina los fallos de desactualización y alucinación característicos de los modelos LLM estándar aislados, recomendando para etapas posteriores incorporar reconocimiento automático de voz (ASR), soporte multilingüe y técnicas de compresión de contexto *map-reduce*.

Kumar et al. (2026) desarrollaron y evaluaron STAIR (*STructure Aware Information Retriever*), un sistema avanzado de recuperación de información basado en modelos de lenguaje de gran escala (LLM) que indexa y recupera secciones documentales aprovechando la estructura global y jerárquica de la tabla de contenidos (ToC) de textos extensos, abordando las limitaciones de pérdida de contexto (*lost in the middle*) y fragmentación arbitraria de las arquitecturas tradicionales de Generación Aumentada por Recuperación (RAG). Para validar la propuesta, los investigadores construyeron el benchmark multidominio SearchTome a partir de 18 libros extensos pertenecientes a seis áreas del conocimiento (Educación, Finanzas, Derecho, Medicina, Ciencias Naturales y Ciencias Sociales), extrayendo sus índices temáticos mediante PyMuPDF y generando consultas sintéticas pareadas con el modelo Mixtral 8x7B. El flujo de STAIR se implementó adaptando el modelo Mistral Instruct v0.2 mediante ajuste fino supervisado con adaptadores LoRA ($r = 16$, $\alpha = 32$) sobre ventanas de contexto de hasta 14 000 tokens (concatenando el ToC completo con la consulta, $q + ToC_D$), aplicando durante la inferencia una técnica de decodificación restringida que limita la salida exclusivamente a los nodos hoja válidos de la estructura. En la evaluación sobre SearchTome, STAIR alcanzó un Recall@1 de 82,6%, un Recall@3 de 90,8% y un nDCG@3 de 87,5%, superando de forma estadísticamente significativa ($p < 0,05$ en pruebas de aleatorización en los seis dominios evaluados) al modelo base de índice diferenciable DSI (76,9% en Recall@1, logrando una ganancia del +7,4%), así como a DPR con NV-Embed-v2 (68,7%), BM25 en ElasticSearch (59,5%) y Mistral sin entrenar (13,8%). Asimismo, los estudios de ablación revelaron que el anclaje estructural del ToC redujo la tasa de error a 18,67% con una proporción de alucinación de secciones inexistentes inferior al 0,05% (frente a 3,25% en DSI y 23,86% en Mistral base), demostrando un rendimiento robusto incluso en nodos con escasos ejemplos de entrenamiento. Los autores concluyeron que el uso de estructuras de contenido globales como unidades de recuperación supera las deficiencias del particionado ciego por longitud de texto (*chunking* plano), garantizando una recuperación semántica de alta precisión para sistemas de diálogo y agentes de consulta sobre literatura técnica extensa.

Zheng et al. (2023) desarrollaron y validaron empíricamente el paradigma *LLM-as-a-Judge*, una metodología automatizada que emplea modelos de lenguaje de gran escala (LLM) de frontera como evaluadores sustitutos del juicio humano para medir la calidad conversacional y la capacidad de seguimiento de instrucciones en asistentes virtuales, abordando la desconexión de los benchmarks tradicionales de preguntas cerradas (como MMLU y HELM) respecto a las preferencias reales de los usuarios. Para fundamentar el marco de evaluación, los autores crearon dos nuevos entornos de prueba: MT-bench, una batería de 80 preguntas complejas de múltiples turnos articulada en ocho categorías temáticas (redacción, *roleplay*, extracción, razonamiento, matemáticas, código, ciencias STEM y humanidades); y Chatbot Arena, una plataforma comunitaria de evaluación anónima a ciegas (*crowdsourced*) en la cual los usuarios interactúan en paralelo con dos modelos y votan por la mejor respuesta. En el plano metodológico, se formalizaron tres modalidades de arbitraje (comparación por pares, asignación directa de puntuación en escala del 1 al 10 y evaluación guiada por respuestas de referencia), diseñando técnicas de mitigación frente a sesgos recurrentes: permutación de respuestas para corregir el sesgo de posición (*swapping positions*), pruebas contra el sesgo de verbosidad excesiva y el uso de prompting con cadena de pensamiento (*Chain-of-Thought*) que redujo los fallos de calificación en problemas lógicos y matemáticos del 70% al 15%. La validación del sistema se contrastó analizando 3000 votos emitidos por 58 evaluadores humanos de nivel experto en MT-bench y una muestra representativa de 3000 juicios sobre un repositorio superior a los 30 000 enfrentamientos en Chatbot Arena. Como hallazgos cuantitativos primordiales, GPT-4 demostró una concordancia del 85% frente a los evaluadores humanos en decisiones sin empate, superando la concordancia interna registrada entre los propios humanos (81%) y alcanzando un 87% de correlación en las votaciones del Arena; adicionalmente, en las discrepancias entre humanos y el modelo, los evaluadores consideraron razonables las justificaciones explicativas de GPT-4 en el 75% de los casos y modificaron su postura inicial en un 34%. En las pruebas de resistencia a la longitud artificial, GPT-4 exhibió una tasa de error de solo 8,7% (frente a 91,3% en GPT-3.5 y Claude-v1), liderando la clasificación de MT-bench con un promedio de 8,99 sobre 10 puntos en contraste con GPT-3.5 (7,94) y modelos abiertos como Vicuna-13B (6,39). Los autores concluyeron que el uso de LLMs avanzados como jueces proporciona una alternativa rigurosa, explicable y altamente escalable para aproximar la evaluación humana en interacciones abiertas, validando su implementación como un estándar robusto para medir la efectividad y alineación de los chatbots conversacionales.

Sarthi et al. (2024) desarrollaron y evaluaron experimentalmente RAPTOR (*Recursive Abstractive Processing for Tree-Organized Retrieval*), un novedoso sistema de indexación y recuperación jerárquico diseñado para potenciar modelos de lenguaje en arquitecturas de Generación Aumentada por Recuperación (RAG) sobre documentos extensos, resolviendo la pérdida de comprensión holística y la incapacidad de razonamiento multietapa de las técnicas convencionales basadas en fragmentación corta y contigua (*chunking* plano). La propuesta metodológica consistió en construir una estructura de árbol ascendente (*bottom-up*) a partir de fragmentos base de 100 tokens que preservan la coherencia oracional, vectorizados mediante el codificador SBERT (`multi-qa-mpnet-base-cos-v1`); dichos segmentos fueron agrupados mediante un algoritmo de agrupamiento suave (*soft clustering*) basado en Modelos de Mezcla Gaussiana (GMM) con reducción de dimensionalidad por UMAP y selección óptima por el Criterio de Información Bayesiano (BIC), para luego generar resúmenes abstractivos de cada clúster empleando GPT-3.5-Turbo (con una tasa de compresión media del 72%) y repetir recursivamente el proceso de re-incrustación hasta alcanzar la raíz. Para la recuperación en inferencia, los autores implementaron el método de árbol colapsado (*collapsed tree*), el cual aplana la jerarquía y compara la consulta simultáneamente contra todos los nodos y resúmenes mediante similitud de coseno y búsqueda vectorial rápida con FAISS hasta un umbral de 2000 tokens. La solución se evaluó en tres exigentes conjuntos de datos para textos voluminosos (QuALITY, QASPER y NarrativeQA) acoplada a tres modelos lectores (UnifiedQA 3B, GPT-3 y GPT-4). Como resultados sobresalientes, RAPTOR junto a GPT-4 fijó un nuevo récord en el benchmark QuALITY al alcanzar una precisión global del 82,6% (superando en 20,3 puntos porcentuales absolutos al mejor registro previo de 62,3%) y un 76,2% en el subconjunto desafiante *QuALITY-HARD* (superando por 21,5% al estado del arte CoLISA); en QASPER, logró una puntuación F1 líder de 55,7%, batiendo a recuperadores densos (DPR) y léxicos (BM25) por márgenes de hasta 4,5 y 10,2 puntos; asimismo, en NarrativeQA obtuvo un récord METEOR de 19,10%. Los estudios de ablación constataron que entre el 18,5% y el 57,36% de los nodos recuperados correspondieron a resúmenes de capas no hojas, demostrando además un escalado estrictamente lineal en tiempo y consumo de tokens para textos de hasta 78 000 tokens procesados en hardware de consumo. Los investigadores concluyeron que articular representaciones recursivas a distintos niveles de abstracción semántica permite a los asistentes virtuales responder con precisión tanto a dudas temáticas complejas como a detalles puntuales, consolidando a RAPTOR como un referente esencial para optimizar la recuperación contextual en chatbots institucionales y educativos.

## 2.2. Bases teóricas

[Redacción correspondiente a 2.2. Bases teóricas]

### 2.2.1. Bases teóricas de Operaciones de TI en Educación Superior

La Gestión de Servicios de Tecnologías de la Información (ITSM, por sus siglas en inglés *Information Technology Service Management*) constituye el marco estratégico y operativo que alinea la provisión de infraestructura tecnológica con los objetivos institucionales y académicos de las organizaciones de educación superior. En los entornos universitarios contemporáneos, la creciente dependencia de sistemas de información académica, plataformas de matrícula y aulas virtuales exige una gestión formal de las operaciones de TI orientada a garantizar la disponibilidad continua, la integridad operativa y la satisfacción de la comunidad universitaria. Como demuestran Palilingan y Batmetan (2018), la ausencia de procesos sistemáticos de gestión operativa en sistemas de información académica desencadena la acumulación de incidencias no resueltas que degradan la calidad del servicio educativo. Al adoptar las directrices operativas del marco ITIL (*Information Technology Infrastructure Library*), los autores evidenciaron que el 84,5% de las incidencias operativas en sistemas académicos pueden resolverse con rapidez y pertinencia mediante flujos estandarizados, mientras que el 15,5% restante se canaliza hacia niveles especializados de escalamiento para evitar fallos sistémicos mayores. En consecuencia, la fundamentación teórica de las operaciones de TI en la educación superior demanda transitar de esquemas reactivos de soporte hacia modelos gobernados por procesos rigurosos que optimicen la asignación de recursos y aseguren la continuidad del servicio frente a picos de demanda.

#### 2.2.1.1. Gestión de servicios e incidencias de TI (ITSM / Help Desk)

La gestión de incidencias representa uno de los procesos nucleares dentro del ciclo de vida de las operaciones de servicios de TI, cuyo propósito primordial es restaurar la operatividad normal del servicio en el menor tiempo posible y minimizar el impacto adverso en las actividades institucionales. De acuerdo con Ibrahim y Hamarash (2025), el marco ITSM se define formalmente como un conjunto articulado de procesos, documentación técnica y mejores prácticas requeridas para gobernar los servicios de tecnologías de la información de manera eficaz y medible. En los centros de soporte universitario (*Service Desks* o mesas de ayuda), la implementación de este marco se estructura sobre las fases normativas de ITIL: registro inicial del incidente, categorización temática, priorización basada en urgencia e impacto, diagnóstico preliminar, resolución técnica y cierre documentado (Palilingan y Batmetan, 2018). Asimismo, evaluaciones de madurez en la adopción de ITIL v3 en instituciones de educación superior revelan que la falta de estandarización en la recepción de solicitudes genera demoras críticas y sobrecarga en el personal técnico (Rahmana, 2025). La literatura especializada coincide en que la formalización de mesas de ayuda mediante flujos estandarizados de gestión de incidencias no solo reduce la tasa de reincidencia de problemas operativos, sino que incrementa significativamente la transparencia y trazabilidad del soporte brindado a estudiantes y docentes.

#### 2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada

Las mesas de ayuda y dependencias de soporte técnico en instituciones universitarias enfrentan cuellos de botella operativos agudos originados por la volumetría masiva de consultas durante hitos clave del calendario académico, tales como los periodos de matrícula, el registro de asignaturas, los vencimientos de pensiones y las evaluaciones finales. La experiencia del usuario (UX) se posiciona como el criterio central de evaluación de la eficacia de los servicios de soporte de TI, viéndose severamente menoscabada cuando los canales de atención tradicionales (ventanillas presenciales, teléfonos o correos electrónicos) colapsan ante solicitudes concurrentes (Babar et al., 2025). En su revisión sistemática sobre la colaboración entre humanos e inteligencia artificial en servicios de soporte de TI, Babar et al. (2025) señalan que la saturación de los canales asistenciales genera tiempos excesivos de primera respuesta, fatiga cognitiva en el personal técnico de soporte y demoras prolongadas en la resolución de incidencias. En este contexto, la problemática asistencial constatada en la universidad privada bajo estudio refleja este fenómeno estructural, donde el personal técnico debe destinar un porcentaje sustancial de su jornada laboral a absolver consultas repetitivas de primer nivel (*Tier-1*), restando capacidad operativa para atender incidentes críticos de infraestructura de red o fallos de servidores. Por ende, la literatura fundamenta que la automatización conversacional y la colaboración sinérgica entre modelos inteligentes y operadores humanos representa la solución idónea para descongestionar el flujo de tickets y optimizar la experiencia asistencial universitaria.

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

En los sistemas conversacionales y modelos de lenguaje de gran escala aplicados a dominios cerrados, la evaluación de la calidad generativa no puede limitarse a métricas léxicas tradicionales (como BLEU o ROUGE), resultando indispensable cuantificar rigurosamente la fidelidad fáctica y la tasa de alucinación (*hallucination rate*). La alucinación se define formalmente como la generación de información verosímil y gramaticalmente correcta pero fácticamente errónea, desactualizada o carente de sustento en las fuentes documentales de referencia. En un estudio sistemático sobre el comportamiento de modelos generativos avanzados en dominios reglamentarios, Dahl et al. (2024) demostraron que los LLMs sin anclaje documental presentan alucinaciones en al menos el 58% de las interacciones, exhiben dificultades severas para anticipar o predecir sus propios errores y tienden a aceptar de forma acrítica premisas incorrectas formuladas por los usuarios. Para abordar esta vulnerabilidad en entornos normativos y de misión crítica, Asgari et al. (2025) formalizaron un marco integral de auditoría y evaluación de seguridad fáctica para modelos de lenguaje, el cual mide la tasa de alucinación mediante la clasificación y ponderación de inconsistencias intrínsecas (contradicciones directas con el texto base) e inconsistencias extrínsecas (inserción de hechos o directivas no respaldadas por la fuente oficial). La aplicación de estas métricas en sistemas de soporte universitario resulta imperativa, dado que la emisión de respuestas alucinadas respecto a normativas de matrícula, montos de trámites o plazos reglamentarios acarrea perjuicios administrativos directos para el estudiante y compromete la confiabilidad institucional del asistente virtual.

##### c. Métricas de Recuperación de Información (Recall@K y Precisión)

[Redacción correspondiente a c. Métricas de Recuperación de Información (Recall@K y Precisión)]

#### 2.2.2.3. Arquitectura Transformer y Mecanismo de Autoatención

La arquitectura Transformer, introducida por Vaswani et al. (2017), revolucionó el campo del Procesamiento de Lenguaje Natural al prescindir totalmente de estructuras recurrentes y convolucionales, fundamentando su capacidad de representación exclusivamente en mecanismos de autoatención (*self-attention*). El componente central de esta formulación es la atención por producto escalar escalado (*Scaled Dot-Product Attention*), la cual calcula la compatibilidad entre una consulta (*Query*, Q), un conjunto de claves (*Key*, K) y valores (*Value*, V) escalados mediante la raíz cuadrada de su dimensión para prevenir la saturación del gradiente. La extensión a autoatención multicabezal (*Multi-Head Attention*) proyecta linealmente las consultas, claves y valores en múltiples subespacios de representación independientes, permitiendo que el modelo atienda conjuntamente a información contextual proveniente de distintas posiciones y relaciones sintáctico-semánticas. En un análisis empírico riguroso sobre el funcionamiento interno de la autoatención multicabezal, Voita et al. (2019) demostraron que los diferentes cabezales de atención se especializan funcionalmente en tareas lingüísticas concretas (tales como dependencias sintácticas directas o seguimiento de palabras adyacentes), mientras que una proporción sustancial de cabezales redundantes puede ser podada sin degradar el rendimiento del modelo (por ejemplo, podando 38 de 48 cabezales en el codificador con una pérdida marginal de solo 0,15 puntos BLEU). Complementariamente, investigaciones arquitectónicas avanzadas como Transformer in Transformer (Han et al., 2021) evidencian que el principio de autoatención anidada y multicabezal puede extenderse a representaciones atómicas jerárquicas con alta eficiencia computacional, validando la solidez matemática y la versatilidad de la autoatención para capturar dependencias de largo alcance en corpus documentales extensos.

#### 2.2.2.4. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento

[Redacción correspondiente a 2.2.2.4. Modelos de Lenguaje de Gran Escala (LLMs) y Modo de Razonamiento]

#### 2.2.2.5. Ajuste Fino Eficiente (PEFT) mediante LoRA y Cuantización GGUF

El despliegue práctico de modelos de lenguaje de gran escala en infraestructura computacional local y de consumo enfrenta severas restricciones de memoria de acceso aleatorio (RAM/VRAM) y capacidad de procesamiento. Para viabilizar la adaptación de dominio sin incurrir en los exorbitantes costos computacionales del reentrenamiento completo (*full fine-tuning*), surgieron las técnicas de Ajuste Fino Eficiente en Parámetros (PEFT, por sus siglas en inglés *Parameter-Efficient Fine-Tuning*), entre las cuales destaca la Adaptación de Bajo Rango (LoRA, *Low-Rank Adaptation*) formulada por Hu et al. (2021). LoRA congela los pesos preentrenados originales del modelo e introduce matrices de descomposición de bajo rango en las proyecciones lineales de las capas de atención, reduciendo los parámetros entrenables en más del 99% sin menoscabar la calidad representacional del modelo adaptado. En un exhaustivo estado del arte sobre modelos ligeros y eficientes, Chavan et al. (2024) destacan que la combinación de PEFT con cuantización post-entrenamiento a 4 bits (QLoRA) y formatos de compresión binaria como GGUF (*GPT-Generated Unified Format*) optimiza drásticamente la latencia y la huella de memoria durante la inferencia en entornos de computación en el borde (*edge computing*). Asimismo, Wang et al. (2025) fundamentan que el co-diseño coordinado entre algoritmos de bajo rango, entornos de ejecución optimizados y arquitecturas de hardware con memoria unificada permite ejecutar agentes cognitivos inteligentes de forma autosuficiente, confiable y con preservación estricta de la privacidad de los datos, demostrando la viabilidad técnica de alojar asistentes institucionales avanzados directamente en hardware local sin depender de clústeres de servidores externos.

#### 2.2.2.6. Generación Aumentada por Recuperación (RAG)

La Generación Aumentada por Recuperación (RAG, por sus siglas en inglés *Retrieval-Augmented Generation*) constituye uno de los paradigmas más sólidos y extendidos para mitigar las alucinaciones y resolver el desfase temporal de los modelos de lenguaje de gran escala, combinando la memoria paramétrica del modelo generador con repositorios de conocimiento externo no paramétricos. De acuerdo con las revisiones integrales de Gao et al. (2023) y Zhao et al. (2024), el ecosistema RAG ha evolucionado desde formulaciones iniciales ingenuas (*Naive RAG*) (basadas en indexación plana y búsqueda semántica directa) hacia arquitecturas avanzadas y modulares (*Advanced & Modular RAG*) que incorporan preprocesamiento jerárquico, técnicas de filtrado dinámico, enrutamiento semántico y reordenamiento (*reranking*) de pasajes documentales. A nivel teórico, Mialon et al. (2023) catalogan a los sistemas aumentados como modelos dotados de habilidades de razonamiento y uso de herramientas externas para descomponer tareas complejas en subprocesos verificables. Asimismo, en una revisión sistemática de literatura, Brown et al. (2025) evidencian que los enfoques RAG estructurados y conscientes del contexto superan ampliamente a las arquitecturas generativas aisladas al anclar las respuestas en evidencias documentales explícitas. En este sentido, Farahani y Johansson (2024) descifran la interacción entre la memoria paramétrica del modelo y la memoria no paramétrica recuperada, demostrando experimentalmente que el suministro oportuno de fragmentos relevantes inhibe la generación de información ficticia y prioriza la verdad factual del contexto provisto. En consecuencia, la arquitectura RAG se consolida como el pilar fundamental para asistentes universitarios de soporte de TI, garantizando que cada directiva o respuesta técnica derive exclusivamente de los reglamentos institucionales oficiales.

#### 2.2.2.7. Arquitectura STAIR (Structure-Aware Information Retriever)

A pesar de las ventajas intrínsecas de RAG, los sistemas convencionales suelen fallar ante textos institucionales extensos debido a dos deficiencias estructurales: el problema de la aguja en el pajar (*needle in a haystack*), donde la fragmentación arbitraria en trozos planos (*flat chunking*) despoja a las oraciones del contexto circundante necesario para su correcta interpretación y la pérdida de la visión global del documento, que impide sintetizar respuestas multietapa (Majri, 2026). Para superar estas limitaciones, surge la recuperación guiada por estructura jerárquica, materializada en arquitecturas que aprovechan la tabla de contenidos (ToC) del documento como un mapa semántico de navegación previa a la recuperación detallada (Majri, 2026; Kumar et al., 2026). En este paradigma se fundamenta STAIR (*STructure-Aware Information Retriever*), desarrollado por Kumar et al. (2026), el cual indexa y recupera secciones documentales completas mediante un esquema de enrutamiento en dos etapas guiado por el árbol ToC. Bajo esta arquitectura, el modelo recibe la consulta articulada con la estructura del índice institucional (q + ToC_D) y ejecuta una poda de ramas irrelevantes en memoria antes de descender hacia los nodos hoja pertinentes. Como demuestran empíricamente Kumar et al. (2026), la navegación estructurada eleva el Recall@1 al 82,6% y reduce la tasa de alucinación a valores inferiores al 0,05%, superando ampliamente a los índices densos convencionales (DPR) y a los motores léxicos basados en BM25. En la presente tesis, la arquitectura adoptada (denominada Sipán-STAIR) adapta este principio al ecosistema documental de soporte de TI de la institución bajo estudio, garantizando que el asistente conversacional localice con precisión milimétrica los reglamentos y guías oficiales sin extraviarse en pasajes inconexos.

#### 2.2.2.8. Metodología Reference-Guided LLM-as-a-Judge

La evaluación de la calidad de respuesta en asistentes conversacionales orientados a tareas institucionales representa un desafío metodológico complejo, puesto que los benchmarks tradicionales sustentados en preguntas cerradas de opción múltiple (tales como MMLU o HELM) resultan incapaces de medir la coherencia contextual, el tono asistencial y la alineación con las preferencias humanas en diálogos abiertos. Frente a esta limitación, Zheng et al. (2023) introdujeron y validaron el paradigma *LLM-as-a-Judge*, una metodología sistemática que emplea modelos de lenguaje de última generación como árbitros automatizados para evaluar la precisión y exhaustividad de las respuestas generadas por otros modelos. Entre las modalidades formuladas por Zheng et al. (2023), la evaluación guiada por referencias (*Reference-Guided Grading*) destaca como el enfoque de mayor rigor para dominios cerrados, proveyendo al modelo evaluador una respuesta canónica certificada (*ground truth*) elaborada por expertos, acompañada de rúbricas multidimensionales para juzgar corrección fáctica, claridad y ausencia de omisiones. Esta modalidad mitiga de forma contundente los sesgos habituales del arbitraje automático (tales como el sesgo de verbosidad excesiva y el sesgo posicional de orden de presentación), alcanzando una concordancia del 85% frente a juicios emitidos por evaluadores humanos de nivel experto. De este modo, el paradigma *Reference-Guided LLM-as-a-Judge* se fundamenta como un estándar robusto, reproducible y escalable para auditar cuantitativamente la efectividad de asistentes de TI universitarios, permitiendo certificar la fidelidad fáctica del chatbot frente al banco institucional de preguntas y respuestas oficiales.

### 2.2.3. Bases teóricas de Hardware y Entorno de Inferencia

La proliferación de modelos de inteligencia artificial y su creciente demanda de recursos de cómputo han impulsado una transformación de los paradigmas de despliegue, evolucionando desde la dependencia exclusiva de macrocentros de datos en la nube hacia esquemas de Inteligencia en el Borde (*Edge Intelligence*). De acuerdo con la formulación teórica de Zhou et al. (2019), la inteligencia en el borde fusiona las capacidades del aprendizaje automático con la computación cercana al usuario final, resolviendo los desafíos críticos de latencia en la transmisión de datos, congestión de ancho de banda en la red institucional, costos recurrentes de licenciamiento y la vulnerabilidad en la privacidad de la información. En los entornos organizacionales y universitarios contemporáneos, la adopción de esquemas de inferencia y procesamiento local en el borde (*Edge Inference*) asegura que las consultas institucionales, historiales de estudiantes y credenciales de acceso se procesen de manera autónoma sin salir de la infraestructura física de la entidad (Zhou et al., 2019). Este marco arquitectónico respalda la soberanía tecnológica y la disponibilidad operativa continua (24/7), garantizando que el asistente de soporte de TI continúe operando con baja latencia incluso ante caídas de la conexión externa a internet o políticas restrictivas de protección de datos personales.

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

Asgari, E., Montaña-Brown, N., Dubois, M., Khalil, S., Balloch, J., Yeung, J. A., & Pimenta, D. (2025). A framework to assess clinical safety and hallucination rates of llms for medical text summarisation. *npj Digital Medicine*, 8(1), Artículo 274. https://doi.org/10.1038/s41746-025-01670-7

Babar, Z., Paul, R., Rahman, M. A., & Barua, T. (2025). A systematic review of human-ai collaboration in IT support services: Enhancing user experience and workflow automation. *Journal of Artificial Intelligence and Cloud Computing*, 4(1), 1–12. https://doi.org/10.63125/grqtf978

Banu, A. (2023). The impact of technology integration in educational management and administration. *International Journal for Multidisciplinary Research (IJFMR)*, 5(6), 1–8. https://doi.org/10.36948/ijfmr.2023.v05i06.10858

Brown, A., Roman, M., & Devereux, B. (2025). A systematic literature review of retrieval-augmented generation: Techniques, metrics, and challenges. *Big Data and Cognitive Computing*, 9(12), Artículo 320. https://doi.org/10.3390/bdcc9120320

Chavan, A., Magazine, R., Kushwaha, S., Debbah, M., & Gupta, D. K. (2024). Faster and lighter llms: A survey on current challenges and way forward. *Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI-24)*, 8345–8354. https://doi.org/10.24963/ijcai.2024/883

Dahl, M., Magesh, V., Suzgun, M., & Ho, D. E. (2024). Large legal fictions: Profiling legal hallucinations in large language models. *Journal of Legal Analysis*, 16(1), 64–93. https://doi.org/10.1093/jla/laae003

Farahani, M., & Johansson, R. (2024). Deciphering the interplay of parametric and non-parametric memory in retrieval-augmented language models. *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, 16966–16977. https://doi.org/10.18653/v1/2024.emnlp-main.943

Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y. Q., Sun, J., Wang, M., & Wang, H. (2023). Retrieval-augmented generation for large language models: A survey. *arXiv preprint arXiv:2312.10997*. https://doi.org/10.48550/arXiv.2312.10997

Gómez Padilla, J. C., & Pantaleón Sirlopú, A. G. (2024). *Entrevista diagnóstica aplicada al personal de operaciones de tecnologías de la información de la universidad privada bajo estudio* [Instrumento de recolección de datos preliminar no publicado]. Escuela Profesional de Ingeniería de Sistemas, Universidad Nacional Pedro Ruiz Gallo, Lambayeque, Perú. (Ver Anexo 3).

Green Software Foundation. (2024, 17 de octubre). *The EU AI Act: Insights from the Green AI Committee*. https://greensoftware.foundation/articles/the-eu-ai-act-insights-from-the-green-ai-committee/

Han, K., Xiao, A., Wu, E., Guo, J., Xu, C., & Wang, Y. (2021). Transformer in transformer. *Advances in Neural Information Processing Systems (NeurIPS 2021)*, 34, 15908–15919. https://doi.org/10.48550/arXiv.2103.00112

Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2021). LoRA: Low-rank adaptation of large language models. *arXiv preprint arXiv:2106.09685*. https://doi.org/10.48550/arXiv.2106.09685

Ibrahim, H., & Hamarash, I. I. (2025). Developing IT service management in higher education institutions: A case study of ITIL implementation in universities in the Kurdistan region of Iraq. *International Conference on Emerging Trends in Industry (ICETI 2024)*. https://doi.org/10.31972/iceti2024.008

Kumar, V., Pulivarthi, M., Kumar, V., Sen, J., Bhat, R. A., & Joshi, S. (2026). STAIR (Structure-Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation. *arXiv preprint arXiv:2609.03874*. https://doi.org/10.48550/arXiv.2609.03874

Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems (NeurIPS 2020)*, 33, 9459–9474. https://doi.org/10.48550/arXiv.2005.11401

Majri, M. (2026). Structure-guided retrieval with LLM-directed table-of-contents navigation and precomputed semantic contagion: A hybrid RAG architecture. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.7467558

Mialon, G., Dessì, R., Lomelí, M., Nalmpantis, C., Pasunuru, R., Răileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Çelikyılmaz, A., Grave, É., LeCun, Y., & Scialom, T. (2023). Augmented language models: A survey. *arXiv preprint arXiv:2302.07842*. https://doi.org/10.48550/arXiv.2302.07842

Noguchi, O., Munechika, M., & Kajihara, C. (2016). A study on user satisfaction with an entire operation including indefinite-length response time. *Total Quality Science*, 2(2), 70–79. https://doi.org/10.17929/tqs.2.70

Okonkwo, C. W., & Ade-Ibijola, A. (2021). Chatbots applications in education: A systematic review. *Computers and Education: Artificial Intelligence*, 2, Artículo 100033. https://doi.org/10.1016/j.caeai.2021.100033

Organización de las Naciones Unidas. (2015). *Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible* (Resolución A/RES/70/1). Naciones Unidas. https://undocs.org/es/A/RES/70/1

Organización de las Naciones Unidas. (2023). *Informe sobre los Objetivos de Desarrollo Sostenible 2023: Edición especial*. Naciones Unidas. https://unstats.un.org/sdgs/report/2023/

Palilingan, V. R., & Batmetan, J. R. (2018). Incident management in academic information system using ITIL framework. *IOP Conference Series: Materials Science and Engineering*, 306, Artículo 012110. https://doi.org/10.1088/1757-899x/306/1/012110

Rahmana, M. Y. (2025). Evaluasi penerapan IT service management (ITSM) dengan framework ITIL v3 di universitas XYZ. *Jurnal Informatika dan Teknik Elektro Terapan*, 13(3). https://doi.org/10.23960/jitet.v13i3.7196

Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O. (2020). Green AI. *Communications of the ACM*, 63(12), 54–63. https://doi.org/10.1145/3381831

Serrano, J., Faustino, J., Adriano, D., Pereira, R., & da Silva, M. M. (2021). An IT service management literature review: Challenges, benefits, opportunities and implementation practices. *Information*, 12(3), Artículo 111. https://doi.org/10.3390/info12030111

Unión Europea. (2024). Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial (Reglamento de Inteligencia Artificial). *Diario Oficial de la Unión Europea*, L 2024/1689. https://data.europa.eu/eli/reg/2024/1689/oj

Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30, 5998–6008.

Voita, E., Talbot, D., Moiseev, F., Sennrich, R., & Titov, I. (2019). Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned. *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 5797–5808. https://doi.org/10.18653/v1/p19-1580

Wang, X., Li, Q., & Jia, W. (2025). Cognitive edge computing: A comprehensive survey on optimizing large models and AI agents for pervasive deployment. *TechRxiv / Authorea Preprint*. https://doi.org/10.22541/au.176348756.61222219/v1

Zhao, P., Zhang, H., Yu, Q., Wang, Z., Geng, Y., Fu, F., Yang, L. Q., Zhang, W., Jiang, J., & Cui, B. (2024). Retrieval-augmented generation for AI-generated content: A survey. *arXiv preprint arXiv:2402.19473*. https://doi.org/10.48550/arXiv.2402.19473

Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., & Stoica, I. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *Advances in Neural Information Processing Systems (NeurIPS 2023)*, 36, 46595–46623. https://doi.org/10.48550/arXiv.2306.05685

Zhou, Z., Chen, X., Li, E., Zeng, L., Luo, K., & Zhang, J. (2019). Edge intelligence: Paving the last mile of artificial intelligence with edge computing. *Proceedings of the IEEE*, 107(8), 1738–1762. https://doi.org/10.1109/jproc.2019.2918951


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
