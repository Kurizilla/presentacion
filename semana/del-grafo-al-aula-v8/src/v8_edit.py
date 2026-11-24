# v8: lámina "Equipo de asesores" tras Práctica y evaluación
import re
P='/workspace/del_grafo_al_aula_v8/index.html'
h=open(P,encoding='utf-8').read()
def rep(a,b,n=1):
    global h; assert h.count(a)==n,(a,h.count(a)); h=h.replace(a,b)
FT='<div class="a ft" style="left:96px;top:1012px;white-space:nowrap;">Proyecto de Modernización Educativa</div><svg class="a esc" style="left:1780px;top:998px;width:44px;height:44px;color:#162456" viewBox="0 0 31.4636 32" aria-hidden="true"><use href="#escudo" fill="currentColor"></use></svg>'
INFO='<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#155DFC" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="M12 11v6M12 7.5v.5"/></svg>'
G=[('#009966','Cómo se aprende','Learning Scientists','Evidencia sobre cómo se aprende mejor.',
    [('ZG','Zach Groshell','','Estados Unidos','PhD en Diseño Instruccional (Capella University). Chief Learning Scientist en Alpha Schools y fundador de Education Rickshaw. Autor de «Just Tell Them» y conferencista en enseñanza explícita.'),
     ('NS','Nidhi Sachdeva','','Canadá','PhD en Currículo y Pedagogía (University of Toronto). Especialista en microaprendizaje y ciencia cognitiva, con más de 20 años como educadora e investigadora. Dirige la newsletter «Science of Learning».')],
    ['Enseñanza explícita','Ciencia cognitiva']),
   ('#7008E7','Cómo se construye','EdTech e IA','Tecnología al servicio del aprendizaje.',
    [('NS','Nani Skinner','','Estados Unidos · Ingeniera de IA','Product Engineer en Austin, Texas, y egresada de Gauntlet AI, con experiencia previa en educación. Construye productos de IA para docentes, como un sistema agéntico de acompañamiento docente.'),
     ('PS','Patrick Skinner','Nuevo','Ingeniero de software','Ingeniero de software autodidacta, antes paracaidista y médico de combate del Ejército de EE. UU. Construye productos educativos en Alpha School y Superbuilders.')],
    ['Productos con IA','Ingeniería de software']),
   ('#BB4D00','Qué se enseña','Expertos de dominio matemático','Contenido y didáctica de la matemática por ciclo.',
    [('MG','Marvin Guifarro','','Honduras · Matemática, primaria','25 años en educación matemática y evaluación (AIR, RTI, EDC) en Honduras y El Salvador. Máster en Matemática Educativa y especialista en psicometría. Ha sido docente desde primer grado hasta bachillerato.'),
     ('CT','Carlos Torres','','Perú · Matemática, secundaria','Doctorando en Didáctica de la Matemática (Universidad de Barcelona). Especialista en evaluación a gran escala en el Ministerio de Educación de Perú. Consultor de Khan Academy y ponente en ICME y PME.')],
    ['Primaria','Secundaria','Evaluación'])]
W,GP=560,24; X=[96+i*(W+GP) for i in range(3)]
s=('<section class="sl" id="S08" data-title="Equipo de asesores" aria-roledescription="lámina" aria-label="Equipo de asesores">'
   '<div class="a eyb" style="left:96px;top:58px;white-space:nowrap;--d:0">Modernización educativa · Equipo</div>'
   '<div class="a ttl" style="left:96px;top:90px;white-space:nowrap;--d:0" role="heading" aria-level="1">Equipo de <b>asesores</b></div>'
   '<div class="a baj" style="left:96px;top:166px;width:1728px;--d:0">Tres perfiles complementarios: cómo se aprende, cómo se construye la tecnología y qué matemática se enseña.</div>'+FT)
s+='<div data-g="BLOQUE · equipo" style="display:contents;--d:2">'
for x,(c,kick,t,d,ppl,chips) in zip(X,G):
    pp=''.join(f'<div class="eq-p"><div class="eq-h"><span class="eq-av" style="background:{c}">{ini}</span><div><div class="h4">{n}'
               +(f' <span class="ob-tg" style="--t:{c}">{tg}</span>' if tg else '')+f'</div><div class="xs">{loc}</div></div></div><div class="sm">{bio}</div></div>' for ini,n,tg,loc,bio in ppl)
    ch=''.join(f'<span class="ch">{k}</span>' for k in chips)
    s+=(f'<div class="a cd ob-c" style="left:{x}px;top:250px;width:{W}px;height:660px;--c:{c}"><span class="lab" style="color:{c}">{kick}</span>'
        f'<div class="h3" style="margin-top:12px">{t}</div><div class="sm">{d}</div><div class="eq-ps">{pp}</div><div class="ob-ch">{ch}</div></div>')
s+='</div>'
s+=('<div class="a" style="left:96px;top:934px;width:1728px;height:1.5px;background:#E4E7EC;--d:7"></div>'
    f'<div class="a sm ob-ft" style="left:96px;top:950px;width:1728px;--d:8">{INFO}<span>Cada clase combina los tres perfiles: la ciencia del aprendizaje define la estructura, EdTech e IA la construye y los expertos de dominio aseguran la matemática.</span></div></section>')
CSS='''
/* equipo de asesores (v8) */
.eq-ps{display:flex;flex-direction:column;gap:14px;margin-top:20px}
.eq-p{background:#F9FAFB;border:1.5px solid #E4E7EC;border-radius:12px;padding:16px 18px}
.eq-h{display:flex;align-items:center;gap:14px}.eq-h .h4{display:flex;align-items:center;gap:8px}
.eq-av{flex:none;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:16px}
.eq-p>.sm{margin-top:10px}
'''
rep('\n</style>\n</head>',CSS+'\n</style>\n</head>')
rep('<section class="sl" id="S08" data-title="El tutor de IA"','<section class="sl" id="S09" data-title="El tutor de IA"')
rep("['S08'].forEach","['S09'].forEach")
rep('<section class="sl navy" id="S09" data-title="Cierre"','<section class="sl navy" id="S10" data-title="Cierre"')
i=h.index('<section class="sl" id="S09" data-title="El tutor de IA"'); h=h[:i]+s+'\n'+h[i:]
rep('cnt-n">1</b> / 9<','cnt-n">1</b> / 10<')
open(P,'w',encoding='utf-8').write(h)
print(re.findall(r'<section class="sl[^"]*" id="([^"]+)" data-title="([^"]+)"',h))
low=h.lower(); print({w:low.count(w) for w in ['nimbo','grok','gerardo','maestro decide']})
