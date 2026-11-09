# Aprender a su ritmo

Presentación HTML autónoma para Gerardo Kuri. Siete pantallas: portada + seis secciones. Estilo Editorial azul: #2B50C8, #1B2647, #4A5470, #6B7590, #C9D3F2, #EEF2FC; Poppins y Lato locales.

## Abrir

Abrir `index.html` directamente, incluso sin conexión, o servir esta carpeta:

    python3 -m http.server 8000 --directory /workspace/grafo_site

Abrir http://localhost:8000. No hay dependencias de CDN, analítica ni solicitudes externas; no requiere instalación ni compilación. JavaScript propio en assets/deck.js; no se necesita GSAP.

## Presentar

- Flechas izquierda/derecha y espacio: atrás/siguiente (espacio activa el control si tiene foco).
- Tocar/clic en fondo: mitad izquierda atrás, mitad derecha siguiente.
- Botones inferiores y puntos: navegación directa.
- Deslizar horizontalmente: atrás/siguiente.
- F, botón ⛶ o doble clic en el fondo: pantalla completa, cuando el navegador lo permita.
- Las interacciones dentro de cada pantalla no avanzan la presentación.
- Los ejemplos mantienen su estado al regresar a una pantalla. Recargar reinicia todo.
- Escala proporcional desde una escena 1920 × 1080; no se recorta en ventanas de otra relación de aspecto.

## Alcance factual

Únicas fuentes de contenido: archivos de investigación proporcionados `SYNTHESIS.md` y `essentials.json` (8 nov. 2026, America/El_Salvador). No se consultó ni modificó la plataforma.

- R1 del piloto tiene 137 metas y prerrequisitos; sigue siendo borrador. La cadena de multiplicación dibujada es una simplificación pedagógica, no una extracción literal de sus aristas.
- Existe la meta «Escribe multiplicaciones como suma, identificando la cantidad que se repite y la cantidad de veces que se repite».
- Reglas configuradas observadas: umbral de aprobación 80%; evaluación con un día de demora; repasos a 1, 3, 7, 14, 30 y 60 días; alerta docente tras dos chequeos fallidos. El umbral separado de chequeos es 90%, omitido de la pantalla por sencillez. Configuración no equivale a validación end-to-end.
- Existen cuatro artefactos por paquete: lección, práctica, evaluación y repaso. Los cinco momentos son la ruta pedagógica propuesta, no cinco archivos distintos. Acompañamiento del tutor de IA en la ruta completa: por validar.
- Ana y todos los estados, ejercicios y recorridos dibujados son ilustrativos. No hay datos personales ni resultados reales de alumnos.
- Diagnóstico con alumnos, estado de conocimiento en vivo y remediación automática no fueron verificados. La adaptación es una simulación conceptual.
- El ejemplo G06-I32 y sus cuatro artefactos existen. v2 está sin publicar; el borrador pequeño enlaza v1. No se afirma que todo el grafo esté completo ni publicado.
- Publicación y validación de la ruta completa permanecen pendientes. Sandbox no es producto publicado.

Fuentes locales originales (referencia de auditoría, no necesarias para ejecutar):
`/workspace/graph_adaptability_research/SYNTHESIS.md`
`/workspace/graph_adaptability_research/essentials.json`

Fuentes tipográficas incluidas bajo SIL Open Font License; ver assets/fonts/OFL-*.txt.
