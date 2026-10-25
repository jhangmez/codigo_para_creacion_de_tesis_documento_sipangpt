"""
Script para aplicar las 10 Bases Teóricas aprobadas con evidencia científica
y actualizar las 33 referencias APA 7ma edición en orden alfabético con sangría francesa (1.27 cm).
Compatible de forma nativa con macOS y Windows.
"""

import sys
import unicodedata
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from platform_utils import (
    get_workspace_path,
    find_onedrive_path,
    create_backup,
    dual_save,
    DOCUMENT_DEFAULT_NAME,
    MARKDOWN_DEFAULT_NAME
)

try:
    import docx
    from docx.shared import Pt, Cm, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    print("Error: python-docx no está instalado. Ejecute: pip install -r requirements.txt")
    sys.exit(1)

# Textos aprobados mapeados a sus encabezados
sections_drafts = {
    "2.2.1. Bases teóricas de Operaciones de TI en Educación Superior": (
        "La Gestión de Servicios de Tecnologías de la Información (ITSM, por sus siglas en inglés *Information Technology Service Management*) "
        "constituye el marco estratégico y operativo que alinea la provisión de infraestructura tecnológica con los objetivos institucionales y académicos "
        "de las organizaciones de educación superior. En los entornos universitarios contemporáneos, la creciente dependencia de sistemas de información académica, "
        "plataformas de matrícula y aulas virtuales exige una gestión formal de las operaciones de TI orientada a garantizar la disponibilidad continua, la integridad "
        "operativa y la satisfacción de la comunidad universitaria. Como demuestran Palilingan y Batmetan (2018), la ausencia de procesos sistemáticos de gestión "
        "operativa en sistemas de información académica desencadena la acumulación de incidencias no resueltas que degradan la calidad del servicio educativo. "
        "Al adoptar las directrices operativas del marco ITIL (*Information Technology Infrastructure Library*), los autores evidenciaron que el 84,5% de las incidencias "
        "operativas en sistemas académicos pueden resolverse con rapidez y pertinencia mediante flujos estandarizados, mientras que el 15,5% restante se canaliza hacia "
        "niveles especializados de escalamiento para evitar fallos sistémicos mayores. En consecuencia, la fundamentación teórica de las operaciones de TI en la educación "
        "superior demanda transitar de esquemas reactivos de soporte hacia modelos gobernados por procesos rigurosos que optimicen la asignación de recursos y aseguren "
        "la continuidad del servicio frente a picos de demanda."
    ),

    "2.2.1.1. Gestión de servicios e incidencias de TI (ITSM / Help Desk)": (
        "La gestión de incidencias representa uno de los procesos nucleares dentro del ciclo de vida de las operaciones de servicios de TI, cuyo propósito primordial "
        "es restaurar la operatividad normal del servicio en el menor tiempo posible y minimizar el impacto adverso en las actividades institucionales. De acuerdo "
        "con Ibrahim y Hamarash (2025), el marco ITSM se define formalmente como un conjunto articulado de procesos, documentación técnica y mejores prácticas "
        "requeridas para gobernar los servicios de tecnologías de la información de manera eficaz y medible. En los centros de soporte universitario (*Service Desks* "
        "o mesas de ayuda), la implementación de este marco se estructura sobre las fases normativas de ITIL: registro inicial del incidente, categorización temática, "
        "priorización basada en urgencia e impacto, diagnóstico preliminar, resolución técnica y cierre documentado (Palilingan y Batmetan, 2018). Asimismo, evaluaciones "
        "de madurez en la adopción de ITIL v3 en instituciones de educación superior revelan que la falta de estandarización en la recepción de solicitudes genera demoras "
        "críticas y sobrecarga en el personal técnico (Rahmana, 2025). La literatura especializada coincide en que la formalización de mesas de ayuda mediante flujos "
        "estandarizados de gestión de incidencias no solo reduce la tasa de reincidencia de problemas operativos, sino que incrementa significativamente la transparencia "
        "y trazabilidad del soporte brindado a estudiantes y docentes."
    ),

    "2.2.1.2. Problemática de atención y demanda asistencial en la institución evaluada": (
        "Las mesas de ayuda y dependencias de soporte técnico en instituciones universitarias enfrentan cuellos de botella operativos agudos originados por la "
        "volumetría masiva de consultas durante hitos clave del calendario académico, tales como los periodos de matrícula, el registro de asignaturas, los vencimientos "
        "de pensiones y las evaluaciones finales. La experiencia del usuario (UX) se posiciona como el criterio central de evaluación de la eficacia de los servicios de soporte "
        "de TI, viéndose severamente menoscabada cuando los canales de atención tradicionales (ventanillas presenciales, teléfonos o correos electrónicos) colapsan ante "
        "solicitudes concurrentes (Babar et al., 2025). En su revisión sistemática sobre la colaboración entre humanos e inteligencia artificial en servicios de soporte de TI, "
        "Babar et al. (2025) señalan que la saturación de los canales asistenciales genera tiempos excesivos de primera respuesta, fatiga cognitiva en el personal técnico "
        "de soporte y demoras prolongadas en la resolución de incidencias. En este contexto, la problemática asistencial constatada en la universidad privada bajo estudio refleja "
        "este fenómeno estructural, donde el personal técnico debe destinar un porcentaje sustancial de su jornada laboral a absolver consultas repetitivas de primer nivel "
        "(*Tier-1*), restando capacidad operativa para atender incidentes críticos de infraestructura de red o fallos de servidores. Por ende, la literatura fundamenta que "
        "la automatización conversacional y la colaboración sinérgica entre modelos inteligentes y operadores humanos representa la solución idónea para descongestionar el "
        "flujo de tickets y optimizar la experiencia asistencial universitaria."
    ),

    "b. Métricas de Generación y Tasa de Alucinación": (
        "En los sistemas conversacionales y modelos de lenguaje de gran escala aplicados a dominios cerrados, la evaluación de la calidad generativa no puede limitarse "
        "a métricas léxicas tradicionales (como BLEU o ROUGE), resultando indispensable cuantificar rigurosamente la fidelidad fáctica y la tasa de alucinación "
        "(*hallucination rate*). La alucinación se define formalmente como la generación de información verosímil y gramaticalmente correcta pero fácticamente errónea, "
        "desactualizada o carente de sustento en las fuentes documentales de referencia. En un estudio sistemático sobre el comportamiento de modelos generativos "
        "avanzados en dominios reglamentarios, Dahl et al. (2024) demostraron que los LLMs sin anclaje documental presentan alucinaciones en al menos el 58% de las "
        "interacciones, exhiben dificultades severas para anticipar o predecir sus propios errores y tienden a aceptar de forma acrítica premisas incorrectas formuladas "
        "por los usuarios. Para abordar esta vulnerabilidad en entornos normativos y de misión crítica, Asgari et al. (2025) formalizaron un marco integral de auditoría "
        "y evaluación de seguridad fáctica para modelos de lenguaje, el cual mide la tasa de alucinación mediante la clasificación y ponderación de inconsistencias "
        "intrínsecas (contradicciones directas con el texto base) e inconsistencias extrínsecas (inserción de hechos o directivas no respaldadas por la fuente oficial). "
        "La aplicación de estas métricas en sistemas de soporte universitario resulta imperativa, dado que la emisión de respuestas alucinadas respecto a normativas de matrícula, "
        "montos de trámites o plazos reglamentarios acarrea perjuicios administrativos directos para el estudiante y compromete la confiabilidad institucional del asistente virtual."
    ),

    "2.2.2.3. Arquitectura Transformer y Mecanismo de Autoatención": (
        "La arquitectura Transformer, introducida por Vaswani et al. (2017), revolucionó el campo del Procesamiento de Lenguaje Natural al prescindir totalmente de "
        "estructuras recurrentes y convolucionales, fundamentando su capacidad de representación exclusivamente en mecanismos de autoatención (*self-attention*). "
        "El componente central de esta formulación es la atención por producto escalar escalado (*Scaled Dot-Product Attention*), la cual calcula la compatibilidad entre una "
        "consulta (*Query*, Q), un conjunto de claves (*Key*, K) y valores (*Value*, V) escalados mediante la raíz cuadrada de su dimensión para prevenir la saturación "
        "del gradiente. La extensión a autoatención multicabezal (*Multi-Head Attention*) proyecta linealmente las consultas, claves y valores en múltiples subespacios de "
        "representación independientes, permitiendo que el modelo atienda conjuntamente a información contextual proveniente de distintas posiciones y relaciones sintáctico-semánticas. "
        "En un análisis empírico riguroso sobre el funcionamiento interno de la autoatención multicabezal, Voita et al. (2019) demostraron que los diferentes cabezales "
        "de atención se especializan funcionalmente en tareas lingüísticas concretas (tales como dependencias sintácticas directas o seguimiento de palabras adyacentes), "
        "mientras que una proporción sustancial de cabezales redundantes puede ser podada sin degradar el rendimiento del modelo (por ejemplo, podando 38 de 48 cabezales "
        "en el codificador con una pérdida marginal de solo 0,15 puntos BLEU). Complementariamente, investigaciones arquitectónicas avanzadas como Transformer in Transformer "
        "(Han et al., 2021) evidencian que el principio de autoatención anidada y multicabezal puede extenderse a representaciones atómicas jerárquicas con alta eficiencia "
        "computacional, validando la solidez matemática y la versatilidad de la autoatención para capturar dependencias de largo alcance en corpus documentales extensos."
    ),

    "2.2.2.5. Ajuste Fino Eficiente (PEFT) mediante LoRA y Cuantización GGUF": (
        "El despliegue práctico de modelos de lenguaje de gran escala en infraestructura computacional local y de consumo enfrenta severas restricciones de memoria "
        "de acceso aleatorio (RAM/VRAM) y capacidad de procesamiento. Para viabilizar la adaptación de dominio sin incurrir en los exorbitantes costos computacionales "
        "del reentrenamiento completo (*full fine-tuning*), surgieron las técnicas de Ajuste Fino Eficiente en Parámetros (PEFT, por sus siglas en inglés *Parameter-Efficient Fine-Tuning*), "
        "entre las cuales destaca la Adaptación de Bajo Rango (LoRA, *Low-Rank Adaptation*) formulada por Hu et al. (2021). LoRA congela los pesos preentrenados originales "
        "del modelo e introduce matrices de descomposición de bajo rango en las proyecciones lineales de las capas de atención, reduciendo los parámetros entrenables en más "
        "del 99% sin menoscabar la calidad representacional del modelo adaptado. En un exhaustivo estado del arte sobre modelos ligeros y eficientes, Chavan et al. (2024) "
        "destacan que la combinación de PEFT con cuantización post-entrenamiento a 4 bits (QLoRA) y formatos de compresión binaria como GGUF (*GPT-Generated Unified Format*) "
        "optimiza drásticamente la latencia y la huella de memoria durante la inferencia en entornos de computación en el borde (*edge computing*). Asimismo, Wang et al. (2025) "
        "fundamentan que el co-diseño coordinado entre algoritmos de bajo rango, entornos de ejecución optimizados y arquitecturas de hardware con memoria unificada permite "
        "ejecutar agentes cognitivos inteligentes de forma autosuficiente, confiable y con preservación estricta de la privacidad de los datos, demostrando la viabilidad "
        "técnica de alojar asistentes institucionales avanzados directamente en hardware local sin depender de clústeres de servidores externos."
    ),

    "2.2.2.6. Generación Aumentada por Recuperación (RAG)": (
        "La Generación Aumentada por Recuperación (RAG, por sus siglas en inglés *Retrieval-Augmented Generation*) constituye uno de los paradigmas más sólidos y extendidos "
        "para mitigar las alucinaciones y resolver el desfase temporal de los modelos de lenguaje de gran escala, combinando la memoria paramétrica del modelo generador "
        "con repositorios de conocimiento externo no paramétricos. De acuerdo con las revisiones integrales de Gao et al. (2023) y Zhao et al. (2024), el ecosistema RAG "
        "ha evolucionado desde formulaciones iniciales ingenuas (*Naive RAG*) (basadas en indexación plana y búsqueda semántica directa) hacia arquitecturas avanzadas y "
        "modulares (*Advanced & Modular RAG*) que incorporan preprocesamiento jerárquico, técnicas de filtrado dinámico, enrutamiento semántico y reordenamiento (*reranking*) "
        "de pasajes documentales. A nivel teórico, Mialon et al. (2023) catalogan a los sistemas aumentados como modelos dotados de habilidades de razonamiento y uso de "
        "herramientas externas para descomponer tareas complejas en subprocesos verificables. Asimismo, en una revisión sistemática de literatura, Brown et al. (2025) "
        "evidencian que los enfoques RAG estructurados y conscientes del contexto superan ampliamente a las arquitecturas generativas aisladas al anclar las respuestas "
        "en evidencias documentales explícitas. En este sentido, Farahani y Johansson (2024) descifran la interacción entre la memoria paramétrica del modelo y la memoria "
        "no paramétrica recuperada, demostrando experimentalmente que el suministro oportuno de fragmentos relevantes inhibe la generación de información ficticia y prioriza "
        "la verdad factual del contexto provisto. En consecuencia, la arquitectura RAG se consolida como el pilar fundamental para asistentes universitarios de soporte de TI, "
        "garantizando que cada directiva o respuesta técnica derive exclusivamente de los reglamentos institucionales oficiales."
    ),

    "2.2.2.7. Arquitectura STAIR (Structure-Aware Information Retriever)": (
        "A pesar de las ventajas intrínsecas de RAG, los sistemas convencionales suelen fallar ante textos institucionales extensos debido a dos deficiencias estructurales: "
        "el problema de la aguja en el pajar (*needle in a haystack*), donde la fragmentación arbitraria en trozos planos (*flat chunking*) despoja a las oraciones del contexto "
        "circundante necesario para su correcta interpretación y la pérdida de la visión global del documento, que impide sintetizar respuestas multietapa (Majri, 2026). "
        "Para superar estas limitaciones, surge la recuperación guiada por estructura jerárquica, materializada en arquitecturas que aprovechan la tabla de contenidos (ToC) "
        "del documento como un mapa semántico de navegación previa a la recuperación detallada (Majri, 2026; Kumar et al., 2026). En este paradigma se fundamenta STAIR "
        "(*STructure-Aware Information Retriever*), desarrollado por Kumar et al. (2026), el cual indexa y recupera secciones documentales completas mediante un esquema "
        "de enrutamiento en dos etapas guiado por el árbol ToC. Bajo esta arquitectura, el modelo recibe la consulta articulada con la estructura del índice institucional "
        "(q + ToC_D) y ejecuta una poda de ramas irrelevantes en memoria antes de descender hacia los nodos hoja pertinentes. Como demuestran empíricamente Kumar et al. (2026), "
        "la navegación estructurada eleva el Recall@1 al 82,6% y reduce la tasa de alucinación a valores inferiores al 0,05%, superando ampliamente a los índices densos "
        "convencionales (DPR) y a los motores léxicos basados en BM25. En la presente tesis, la arquitectura adoptada (denominada Sipán-STAIR) adapta este principio al "
        "ecosistema documental de soporte de TI de la institución bajo estudio, garantizando que el asistente conversacional localice con precisión milimétrica los "
        "reglamentos y guías oficiales sin extraviarse en pasajes inconexos."
    ),

    "2.2.2.8. Metodología Reference-Guided LLM-as-a-Judge": (
        "La evaluación de la calidad de respuesta en asistentes conversacionales orientados a tareas institucionales representa un desafío metodológico complejo, puesto "
        "que los benchmarks tradicionales sustentados en preguntas cerradas de opción múltiple (tales como MMLU o HELM) resultan incapaces de medir la coherencia contextual, "
        "el tono asistencial y la alineación con las preferencias humanas en diálogos abiertos. Frente a esta limitación, Zheng et al. (2023) introdujeron y validaron "
        "el paradigma *LLM-as-a-Judge*, una metodología sistemática que emplea modelos de lenguaje de última generación como árbitros automatizados para evaluar la precisión "
        "y exhaustividad de las respuestas generadas por otros modelos. Entre las modalidades formuladas por Zheng et al. (2023), la evaluación guiada por referencias "
        "(*Reference-Guided Grading*) destaca como el enfoque de mayor rigor para dominios cerrados, proveyendo al modelo evaluador una respuesta canónica certificada "
        "(*ground truth*) elaborada por expertos, acompañada de rúbricas multidimensionales para juzgar corrección fáctica, claridad y ausencia de omisiones. Esta modalidad "
        "mitiga de forma contundente los sesgos habituales del arbitraje automático (tales como el sesgo de verbosidad excesiva y el sesgo posicional de orden de presentación), "
        "alcanzando una concordancia del 85% frente a juicios emitidos por evaluadores humanos de nivel experto. De este modo, el paradigma *Reference-Guided LLM-as-a-Judge* "
        "se fundamenta como un estándar robusto, reproducible y escalable para auditar cuantitativamente la efectividad de asistentes de TI universitarios, permitiendo certificar "
        "la fidelidad fáctica del chatbot frente al banco institucional de preguntas y respuestas oficiales."
    ),

    "2.2.3. Bases teóricas de Hardware y Entorno de Inferencia": (
        "La proliferación de modelos de inteligencia artificial y su creciente demanda de recursos de cómputo han impulsado una transformación de los paradigmas de despliegue, "
        "evolucionando desde la dependencia exclusiva de macrocentros de datos en la nube hacia esquemas de Inteligencia en el Borde (*Edge Intelligence*). De acuerdo con "
        "la formulación teórica de Zhou et al. (2019), la inteligencia en el borde fusiona las capacidades del aprendizaje automático con la computación cercana al usuario final, "
        "resolviendo los desafíos críticos de latencia en la transmisión de datos, congestión de ancho de banda en la red institucional, costos recurrentes de licenciamiento "
        "y la vulnerabilidad en la privacidad de la información. En los entornos organizacionales y universitarios contemporáneos, la adopción de esquemas de inferencia y "
        "procesamiento local en el borde (*Edge Inference*) asegura que las consultas institucionales, historiales de estudiantes y credenciales de acceso se procesen de "
        "manera autónoma sin salir de la infraestructura física de la entidad (Zhou et al., 2019). Este marco arquitectónico respalda la soberanía tecnológica y la disponibilidad "
        "operativa continua (24/7), garantizando que el asistente de soporte de TI continúe operando con baja latencia incluso ante caídas de la conexión externa a internet "
        "o políticas restrictivas de protección de datos personales."
    )
}

# 33 referencias completas en formato APA 7ma edición
raw_references = [
    "Adamopoulou, E., & Moussiades, L. (2020). Chatbots: History, technology, and applications. *Machine Learning with Applications*, 2, Artículo 100006. https://doi.org/10.1016/j.mlwa.2020.100006",
    "Asgari, E., Montaña-Brown, N., Dubois, M., Khalil, S., Balloch, J., Yeung, J. A., & Pimenta, D. (2025). A framework to assess clinical safety and hallucination rates of llms for medical text summarisation. *npj Digital Medicine*, 8(1), Artículo 274. https://doi.org/10.1038/s41746-025-01670-7",
    "Babar, Z., Paul, R., Rahman, M. A., & Barua, T. (2025). A systematic review of human-ai collaboration in IT support services: Enhancing user experience and workflow automation. *Journal of Artificial Intelligence and Cloud Computing*, 4(1), 1–12. https://doi.org/10.63125/grqtf978",
    "Banu, A. (2023). The impact of technology integration in educational management and administration. *International Journal for Multidisciplinary Research (IJFMR)*, 5(6), 1–8. https://doi.org/10.36948/ijfmr.2023.v05i06.10858",
    "Brown, A., Roman, M., & Devereux, B. (2025). A systematic literature review of retrieval-augmented generation: Techniques, metrics, and challenges. *Big Data and Cognitive Computing*, 9(12), Artículo 320. https://doi.org/10.3390/bdcc9120320",
    "Chavan, A., Magazine, R., Kushwaha, S., Debbah, M., & Gupta, D. K. (2024). Faster and lighter llms: A survey on current challenges and way forward. *Proceedings of the Thirty-Third International Joint Conference on Artificial Intelligence (IJCAI-24)*, 8345–8354. https://doi.org/10.24963/ijcai.2024/883",
    "Dahl, M., Magesh, V., Suzgun, M., & Ho, D. E. (2024). Large legal fictions: Profiling legal hallucinations in large language models. *Journal of Legal Analysis*, 16(1), 64–93. https://doi.org/10.1093/jla/laae003",
    "Farahani, M., & Johansson, R. (2024). Deciphering the interplay of parametric and non-parametric memory in retrieval-augmented language models. *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*, 16966–16977. https://doi.org/10.18653/v1/2024.emnlp-main.943",
    "Gao, Y., Xiong, Y., Gao, X., Jia, K., Pan, J., Bi, Y., Dai, Y. Q., Sun, J., Wang, M., & Wang, H. (2023). Retrieval-augmented generation for large language models: A survey. *arXiv preprint arXiv:2312.10997*. https://doi.org/10.48550/arXiv.2312.10997",
    "Gómez Padilla, J. C., & Pantaleón Sirlopú, A. G. (2024). *Entrevista diagnóstica aplicada al personal de operaciones de tecnologías de la información de la universidad privada bajo estudio* [Instrumento de recolección de datos preliminar no publicado]. Escuela Profesional de Ingeniería de Sistemas, Universidad Nacional Pedro Ruiz Gallo, Lambayeque, Perú. (Ver Anexo 3).",
    "Green Software Foundation. (2024, 17 de octubre). *The EU AI Act: Insights from the Green AI Committee*. https://greensoftware.foundation/articles/the-eu-ai-act-insights-from-the-green-ai-committee/",
    "Han, K., Xiao, A., Wu, E., Guo, J., Xu, C., & Wang, Y. (2021). Transformer in transformer. *Advances in Neural Information Processing Systems (NeurIPS 2021)*, 34, 15908–15919. https://doi.org/10.48550/arXiv.2103.00112",
    "Hu, E. J., Shen, Y., Wallis, P., Allen-Zhu, Z., Li, Y., Wang, S., Wang, L., & Chen, W. (2021). LoRA: Low-rank adaptation of large language models. *arXiv preprint arXiv:2106.09685*. https://doi.org/10.48550/arXiv.2106.09685",
    "Ibrahim, H., & Hamarash, I. I. (2025). Developing IT service management in higher education institutions: A case study of ITIL implementation in universities in the Kurdistan region of Iraq. *International Conference on Emerging Trends in Industry (ICETI 2024)*. https://doi.org/10.31972/iceti2024.008",
    "Kumar, V., Pulivarthi, M., Kumar, V., Sen, J., Bhat, R. A., & Joshi, S. (2026). STAIR (Structure-Aware Information Retriever): A novel dataset and LLM based retriever for document structure augmentation. *arXiv preprint arXiv:2609.03874*. https://doi.org/10.48550/arXiv.2609.03874",
    "Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., Küttler, H., Lewis, M., Yih, W., Rocktäschel, T., Riedel, S., & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive NLP tasks. *Advances in Neural Information Processing Systems (NeurIPS 2020)*, 33, 9459–9474. https://doi.org/10.48550/arXiv.2005.11401",
    "Majri, M. (2026). Structure-guided retrieval with LLM-directed table-of-contents navigation and precomputed semantic contagion: A hybrid RAG architecture. *SSRN Electronic Journal*. https://doi.org/10.2139/ssrn.7467558",
    "Mialon, G., Dessì, R., Lomelí, M., Nalmpantis, C., Pasunuru, R., Răileanu, R., Rozière, B., Schick, T., Dwivedi-Yu, J., Çelikyılmaz, A., Grave, É., LeCun, Y., & Scialom, T. (2023). Augmented language models: A survey. *arXiv preprint arXiv:2302.07842*. https://doi.org/10.48550/arXiv.2302.07842",
    "Noguchi, O., Munechika, M., & Kajihara, C. (2016). A study on user satisfaction with an entire operation including indefinite-length response time. *Total Quality Science*, 2(2), 70–79. https://doi.org/10.17929/tqs.2.70",
    "Okonkwo, C. W., & Ade-Ibijola, A. (2021). Chatbots applications in education: A systematic review. *Computers and Education: Artificial Intelligence*, 2, Artículo 100033. https://doi.org/10.1016/j.caeai.2021.100033",
    "Organización de las Naciones Unidas. (2015). *Transformar nuestro mundo: la Agenda 2030 para el Desarrollo Sostenible* (Resolución A/RES/70/1). Naciones Unidas. https://undocs.org/es/A/RES/70/1",
    "Organización de las Naciones Unidas. (2023). *Informe sobre los Objetivos de Desarrollo Sostenible 2023: Edición especial*. Naciones Unidas. https://unstats.un.org/sdgs/report/2023/",
    "Palilingan, V. R., & Batmetan, J. R. (2018). Incident management in academic information system using ITIL framework. *IOP Conference Series: Materials Science and Engineering*, 306, Artículo 012110. https://doi.org/10.1088/1757-899x/306/1/012110",
    "Rahmana, M. Y. (2025). Evaluasi penerapan IT service management (ITSM) dengan framework ITIL v3 di universitas XYZ. *Jurnal Informatika dan Teknik Elektro Terapan*, 13(3). https://doi.org/10.23960/jitet.v13i3.7196",
    "Schwartz, R., Dodge, J., Smith, N. A., & Etzioni, O. (2020). Green AI. *Communications of the ACM*, 63(12), 54–63. https://doi.org/10.1145/3381831",
    "Serrano, J., Faustino, J., Adriano, D., Pereira, R., & da Silva, M. M. (2021). An IT service management literature review: Challenges, benefits, opportunities and implementation practices. *Information*, 12(3), Artículo 111. https://doi.org/10.3390/info12030111",
    "Unión Europea. (2024). Reglamento (UE) 2024/1689 del Parlamento Europeo y del Consejo, de 13 de junio de 2024, por el que se establecen normas armonizadas en materia de inteligencia artificial (Reglamento de Inteligencia Artificial). *Diario Oficial de la Unión Europea*, L 2024/1689. https://data.europa.eu/eli/reg/2024/1689/oj",
    "Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., Kaiser, Ł., & Polosukhin, I. (2017). Attention is all you need. *Advances in Neural Information Processing Systems (NeurIPS 2017)*, 30, 5998–6008.",
    "Voita, E., Talbot, D., Moiseev, F., Sennrich, R., & Titov, I. (2019). Analyzing multi-head self-attention: Specialized heads do the heavy lifting, the rest can be pruned. *Proceedings of the 57th Annual Meeting of the Association for Computational Linguistics*, 5797–5808. https://doi.org/10.18653/v1/p19-1580",
    "Wang, X., Li, Q., & Jia, W. (2025). Cognitive edge computing: A comprehensive survey on optimizing large models and AI agents for pervasive deployment. *TechRxiv / Authorea Preprint*. https://doi.org/10.22541/au.176348756.61222219/v1",
    "Zhao, P., Zhang, H., Yu, Q., Wang, Z., Geng, Y., Fu, F., Yang, L. Q., Zhang, W., Jiang, J., & Cui, B. (2024). Retrieval-augmented generation for AI-generated content: A survey. *arXiv preprint arXiv:2402.19473*. https://doi.org/10.48550/arXiv.2402.19473",
    "Zheng, L., Chiang, W.-L., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E. P., Zhang, H., Gonzalez, J. E., & Stoica, I. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. *Advances in Neural Information Processing Systems (NeurIPS 2023)*, 36, 46595–46623. https://doi.org/10.48550/arXiv.2306.05685",
    "Zhou, Z., Chen, X., Li, E., Zeng, L., Luo, K., & Zhang, J. (2019). Edge intelligence: Paving the last mile of artificial intelligence with edge computing. *Proceedings of the IEEE*, 107(8), 1738–1762. https://doi.org/10.1109/jproc.2019.2918951"
]

def sort_key(s: str) -> str:
    """Normaliza acentos para ordenar alfabéticamente (ej. Gómez antes de Green)."""
    return unicodedata.normalize("NFKD", s.lower()).encode("ASCII", "ignore").decode("utf-8")

sorted_references = sorted(raw_references, key=sort_key)

def apply_to_docx(docx_file: Path) -> None:
    print(f"\n[APLICAR TEORÍA] Modificando {docx_file}...")
    doc = docx.Document(str(docx_file))

    # 1. Actualizar las 10 secciones
    replaced_count = 0
    for anchor, new_text in sections_drafts.items():
        for i, p in enumerate(doc.paragraphs):
            if p.text.strip() == anchor:
                target_p = doc.paragraphs[i + 1]
                target_p.text = ""
                target_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
                target_p.paragraph_format.line_spacing = 1.5
                target_p.paragraph_format.space_after = Pt(6)

                parts = new_text.split("*")
                for p_idx, part in enumerate(parts):
                    if not part:
                        continue
                    r = target_p.add_run(part)
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(12)
                    r.font.color.rgb = RGBColor(0, 0, 0)
                    if p_idx % 2 == 1:
                        r.italic = True

                replaced_count += 1
                break

    print(f"  Secciones académicas actualizadas: {replaced_count}/{len(sections_drafts)}")

    # 2. Actualizar Sección 8 (Referencias) con Sangría Francesa
    p_ref_heading = None
    ref_paras = []
    in_ref = False
    for p in doc.paragraphs:
        t = p.text.strip()
        if t == "8. REFERENCIAS":
            p_ref_heading = p
            in_ref = True
            continue
        if in_ref:
            if t.startswith("9. ANEXOS"):
                break
            if t:
                ref_paras.append(p)

    print(f"  Eliminando {len(ref_paras)} párrafos anteriores de referencias...")
    for p in ref_paras:
        p._p.getparent().remove(p._p)

    print(f"  Inyectando {len(sorted_references)} referencias APA 7ma edición ordenadas...")
    curr_ref = p_ref_heading
    for ref_text in sorted_references:
        new_p = doc.add_paragraph()
        new_p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        new_p.paragraph_format.line_spacing = 1.5
        new_p.paragraph_format.space_after = Pt(6)
        new_p.paragraph_format.left_indent = Cm(1.27)
        new_p.paragraph_format.first_line_indent = Cm(-1.27)

        parts = ref_text.split("*")
        for p_idx, part in enumerate(parts):
            if not part:
                continue
            r = new_p.add_run(part)
            r.font.name = "Times New Roman"
            r.font.size = Pt(12)
            r.font.color.rgb = RGBColor(0, 0, 0)
            if p_idx % 2 == 1:
                r.italic = True

        curr_ref._p.addnext(new_p._p)
        curr_ref = new_p

    # Guardado dual
    dual_save(doc, docx_file.name)

def apply_to_markdown(md_file: Path) -> None:
    print(f"\n[APLICAR TEORÍA] Modificando Markdown {md_file}...")
    with open(md_file, "r", encoding="utf-8") as f:
        content = f.read()

    for anchor, new_text in sections_drafts.items():
        escaped_anchor = re.escape(anchor)
        pattern = rf"(#+\s+{escaped_anchor}\s*\n\n)\[Redacción correspondiente a [^\]]+\]"
        content = re.sub(pattern, rf"\g<1>{new_text}", content)

    ref_pattern = r"(# 8\. REFERENCIAS\s*\n\n)(.*?)(?=\n---\s*\n\n# 9\. ANEXOS)"
    new_refs_block = "\n\n".join(sorted_references) + "\n\n"
    content = re.sub(ref_pattern, rf"\g<1>{new_refs_block}", content, flags=re.DOTALL)

    with open(md_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  Markdown sincronizado exitosamente: {md_file}")

def main():
    ws_docx = get_workspace_path(DOCUMENT_DEFAULT_NAME)
    md_file = get_workspace_path(MARKDOWN_DEFAULT_NAME)

    create_backup(ws_docx)
    apply_to_docx(ws_docx)
    apply_to_markdown(md_file)

if __name__ == "__main__":
    main()
