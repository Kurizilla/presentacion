# v7: ~600->~500 y dos láminas nuevas (objetos de aprendizaje) tras La orquestación
import re
P='/workspace/del_grafo_al_aula_v7/index.html'
h=open(P,encoding='utf-8').read()
def rep(a,b,n=1):
    global h; assert h.count(a)==n,(a,h.count(a)); h=h.replace(a,b)
# 1) ~600 -> ~500
rep('~600<sup','~500<sup',3)
rep('6 de 50 cuadros ≈ 600 nodos','5 de 50 cuadros ≈ 500 nodos')
rep("'Se priorizan ~600 nodos'","'Se priorizan ~500 nodos'")
i=h.index('class="fb-dots d1"'); j=h.index('</div>',i); seg=h[i:j]
k=seg.rindex('<i class="p0"></i>'); seg=seg[:k]+'<i></i>'+seg[k+len('<i class="p0"></i>'):]; h=h[:i]+seg+h[j:]
rep('<i class="kg-bar gb2" style="width:42px;background:#155DFC">','<i class="kg-bar gb2" style="width:34px;background:#155DFC">')

# 2) láminas nuevas
FT='<div class="a ft" style="left:96px;top:1012px;white-space:nowrap;">Proyecto de Modernización Educativa</div><svg class="a esc" style="left:1780px;top:998px;width:44px;height:44px;color:#162456" viewBox="0 0 31.4636 32" aria-hidden="true"><use href="#escudo" fill="currentColor"></use></svg>'
INFO='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#155DFC" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 11v6M12 7.5v.5"/></svg>'
def head(sid,title,eyb,ttl,baj,act):
    dots=''.join(f'<span class="nb{"" if k in act else " of"}">{k}</span>' for k in range(1,6))
    return (f'<section class="sl" id="{sid}" data-title="{title}" aria-roledescription="lámina" aria-label="{title}">'
      f'<div class="a eyb" style="left:96px;top:58px;white-space:nowrap;--d:0">{eyb}</div>'
      f'<div class="a ttl" style="left:96px;top:90px;white-space:nowrap;--d:0" role="heading" aria-level="1">{ttl}</div>'
      f'<div class="a baj" style="left:96px;top:166px;width:1240px;--d:0">{baj}</div>'+FT+
      f'<div class="a ob-blk" style="right:96px;top:150px;--d:1" aria-label="Bloques de la clase">{dots}</div>')
def card(x,w,c,kick,code,title,desc,steps,chips,extra=''):
    st=''.join(f'<li><span class="nb" style="background:{c}">{n}</span><div><div class="h5">{t}</div><div class="xs">{d}</div></div></li>' for n,(t,d) in enumerate(steps,1))
    ch=''.join(f'<span class="ch">{t}</span>' for t in chips)
    return (f'<div class="a cd ob-c" style="left:{x}px;top:250px;width:{w}px;height:660px;--c:{c}"><span class="lab" style="color:{c}">{kick}</span>'
            f'<div class="xs b7" style="color:{c};margin-top:10px">{code}</div><div class="h3">{title}</div><div class="sm">{desc}</div>{extra}<ul class="ob-l">{st}</ul><div class="ob-ch">{ch}</div></div>')
def foot(t): return ('<div class="a" style="left:96px;top:934px;width:1728px;height:1.5px;background:#E4E7EC;--d:7"></div>'
                     f'<div class="a sm ob-ft" style="left:96px;top:950px;width:1728px;--d:8">{INFO}<span>{t}</span></div>')
tag=lambda t,c: f' <span class="ob-tg" style="--t:{c}">{t}</span>'
B='#155DFC'
W,G=328,22; X=[96+i*(W+G) for i in range(5)]
L1=[('Explorar','1.1','Simulación','Una misión con un personaje y un contexto real. El estudiante hace la acción que se quiere enseñar.',
     [('Orientar','La misión y la representación.'),('Predecir','«¿Qué crees que pasará?»'),('Actuar','Una acción a la vez, y luego «Listo».'),('Conectar con la notación','La regla con sus números y una pregunta de comprensión.')],['2 a 3 pasos','Predicción','«Listo»'],''),
    ('Observar','1.2 · I do','Ejemplo resuelto','El tutor resuelve un problema en pantallas por pasos, pensando en voz alta.',
     [('Una pantalla por paso','Una animación muestra solo lo que cambia.'),('Narración','Qué quiero hacer, en qué me fijo y qué decido.'),('Paso clave marcado','El mismo que en la regla.'),('Pregunta final','Sobre la decisión clave, no sobre el cálculo.')],['Pantallas por pasos','Narración'],''),
    ('Hacer juntos','1.3 · We do','Ejemplo resuelto con problema emparejado','El tutor muestra un paso y el estudiante lo repite en su propio problema.',
     [('Números que no se copian','Obligan a pensar cada paso.'),('Decisión clave','El estudiante la toma al menos una vez.'),('Tras 3 intentos','Se muestra el paso y el ejemplo sigue.')],['Tutor y estudiante','3 intentos'],
     '<div class="ob-pair"><div><div class="h5">Tutor</div><div class="xs">Hace el paso</div></div><div><div class="h5">Estudiante</div><div class="xs">Lo repite con otros números</div></div></div>'),
    ('Completar','1.4 · You do','Ejemplo semi-resuelto','Los primeros pasos vienen resueltos. El estudiante hace los dos últimos.',
     [('Resuelto'+tag('','#009966').replace(' <span','<span hidden'),'Pasos iniciales, presentados con animación.'),('Te toca','Penúltimo paso: escribe el resultado parcial.'),('Te toca','Último paso: escribe la respuesta.'),('Retroalimentación','Un mensaje para cada error previsto.')],['Últimos 2 pasos','Te toca'],''),
    ('Aplicar','1.5 · Método de George Polya','Problema en contexto','El tutor resuelve un problema real y luego el estudiante resuelve uno emparejado.',
     [('Comprendo el problema','Datos, incógnita y estimación.'),('Hago un plan'+tag('Paso clave',B),'Qué operación hacer y por qué.'),('Ejecuto el plan','Los cálculos, en el orden del plan.'),('Reviso mi respuesta','Comparo el resultado con la estimación.')],['4 pasos de Polya','Problema emparejado'],'')]
s1=head('S06','Lección','Estructura de la clase · 1 de 2','<b>Lección</b>','De lo concreto a la notación, y de observar a resolver: el apoyo se retira paso a paso. Nada avanza solo.',{1})
s1+='<div data-g="BLOQUE · lección" style="display:contents;--d:2">'+''.join(card(X[i],W,B,*c) for i,c in enumerate(L1))+'</div>'
s1+=foot('El estudiante decide cuándo avanzar. Cada paso se verifica, y tras 3 intentos fallidos el sistema muestra el paso y la lección continúa.')+'</section>'
# chips de estado en la tarjeta 1.4 (Resuelto / Te toca)
s1=s1.replace('<div class="h5">Resuelto<span hidden class="ob-tg" style="--t:#009966"></span></div>','<div class="h5"><span class="ob-tg" style="--t:#009966">Resuelto</span></div>')
s1=s1.replace('<div class="h5">Te toca</div>','<div class="h5"><span class="ob-tg" style="--t:#BB4D00">Te toca</span></div>')
W2,G2=414,24; X2=[96+i*(W2+G2) for i in range(4)]
L2=[('#009966','Practicar con apoyo','Bloque 2','Práctica guiada','Ejercicios parecidos al ejemplo modelado, con pistas y retroalimentación inmediata.',
     [('Inicio','El estudiante ve el nombre de la habilidad.'),('Ejercicios 1 a 6','Van de lo más guiado a lo más autónomo.'),('Pistas en 4 niveles','La regla, el ejemplo, el paso y el planteamiento.')],['6 ejercicios','Con pistas','Tutor de IA']),
    ('#7008E7','Practicar solo','Bloque 3','Práctica independiente','Ejercicios sin ayuda, con más variación y más autonomía.',
     [('Inicio','«Esta vez resuelves solo».'),('Ejercicios 7 a 12','La dificultad sube con un solo cambio a la vez.'),('Retroalimentación','Llega después de responder y orienta sin dar la respuesta.')],['6 ejercicios','Sin pistas','Un intento']),
    ('#BB4D00','Demostrar dominio','Bloque 4 · Prueba de dominio','Assessment','Decide si el estudiante avanza o necesita más práctica. Su función es medir, no enseñar.',
     [('Inicio','Una explicación breve, sin el nombre de la habilidad.'),('10 ejercicios','Son nuevos, se presentan uno a la vez y tienen un intento cada uno.'),('Cierre','Sin resultados ni respuestas.')],['10 ejercicios','Sin ayuda','Dominio: [__ / 10]']),
    ('#C10007','Recordar','Bloque 5 · Repaso espaciado','Spaced repetition','Dos preguntas sobre una habilidad ya dominada, para frenar el olvido.',
     [('Ítem A','Sin ayuda y sin retroalimentación todavía.'),('Ítem B','La misma habilidad con otra superficie.'),('Cierre','Muestra las respuestas y la solución de lo fallado.')],['+1 día','+3','+14','+30','+60'])]
s2=head('S07','Práctica y evaluación','Estructura de la clase · 2 de 2','Práctica y <b>evaluación</b>','Después de la lección: practicar con apoyo, practicar solo, demostrar dominio y recordar con el tiempo.',{2,3,4,5})
s2+='<div data-g="BLOQUE · práctica" style="display:contents;--d:2">'+''.join(card(X2[i],W2,c[0],*c[1:]) for i,c in enumerate(L2))+'</div>'
s2+=foot('Las prácticas guiada e independiente forman una sola serie de 12 ejercicios por lección. La meta es que el estudiante resuelva bien cerca de 8 de cada 10.')+'</section>'
CSS='''
/* objetos de aprendizaje (v7) */
.ob-blk{display:flex;gap:8px}.ob-blk .nb{width:36px;height:36px;font-size:16px}
.ob-c{display:flex;flex-direction:column;padding:22px 22px 20px;border-top:4px solid var(--c)}
.ob-c .lab{font-size:13px;letter-spacing:1.8px;line-height:16px}
.ob-c .h3{margin-top:4px}.ob-c>.sm{margin-top:10px}
.ob-l{list-style:none;margin:18px 0 0;padding:0;display:flex;flex-direction:column;gap:14px}
.ob-l li{display:flex;gap:12px;align-items:flex-start}.ob-l .nb{flex:none;width:26px;height:26px;font-size:13px;margin-top:-2px}
.ob-l .h5{display:flex;align-items:center;gap:8px;flex-wrap:wrap}.ob-l .xs{margin-top:2px}
.ob-tg{display:inline-flex;align-items:center;height:24px;padding:0 10px;border-radius:1000px;font-size:13px;font-weight:700;color:var(--t);background:color-mix(in srgb,var(--t) 12%,#fff)}
.ob-pair{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:14px}.ob-pair>div{background:#F9FAFB;border:1.5px solid #E4E7EC;border-radius:12px;padding:10px 12px}
.ob-ch{margin-top:auto;display:flex;flex-wrap:wrap;gap:8px}.ob-ch .ch{height:30px;font-size:14px;padding:0 12px;color:var(--c);background:color-mix(in srgb,var(--c) 10%,#fff)}
.ob-ft{display:flex;align-items:center;gap:10px}.ob-ft svg{flex:none}
'''
rep('\n</style>\n</head>',CSS+'\n</style>\n</head>')
# renumerar tutor S06->S08 y cierre S07->S09, insertar
rep('<section class="sl" id="S06" data-title="El tutor de IA"','<section class="sl" id="S08" data-title="El tutor de IA"')
rep("['S06'].forEach","['S08'].forEach")
rep('<section class="sl navy" id="S07" data-title="Cierre"','<section class="sl navy" id="S09" data-title="Cierre"')
i=h.index('<section class="sl" id="S08" data-title="El tutor de IA"'); h=h[:i]+s1+'\n'+s2+'\n'+h[i:]
rep('cnt-n">1</b> / 7<','cnt-n">1</b> / 9<')
rep('<span>Orquestación</span><span>Tutor de IA</span>','<span>Orquestación</span><span>Objetos</span><span>Tutor de IA</span>')
open(P,'w',encoding='utf-8').write(h)
print(re.findall(r'<section class="sl[^"]*" id="([^"]+)" data-title="([^"]+)"',h))
low=h.lower(); print({w:low.count(w) for w in ['nimbo','grok','gerardo','~600','maestro decide']})
