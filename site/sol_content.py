# Conteúdo das soluções (texto enviado pela Vânia). Primeiro bloco: título + 1º parágrafo; os seguintes, só parágrafo.
import json, re
CONTENT = {
 'sites': ['Criamos sites de alta performance',
   'Você já sabe que precisa estar na internet. Na web é possível atrair, converter, fidelizar e fortalecer a sua marca. Para isso, ter um bom site é fundamental.',
   'Nós criamos sites de alta performance, mas você sabe o que isso quer dizer? Quer dizer que utilizamos as melhores ferramentas e práticas para que o seu investimento nos meios digitais traga resultados efetivos ao seu negócio.',
   'Desenvolvemos seu site para que ele seja um aliado estratégico de seus objetivos, aproveitando todo o potencial da internet.'],
 'blogs': ['Criação de blogs e portais de conteúdo',
   'O blog é uma ferramenta poderosa para consolidar sua presença online, atrair visitantes, criar autoridade e desenvolver relacionamentos. Nele você pode compartilhar conteúdos relevantes à sua audiência, gerando valor e transformação antes mesmo de vender seus produtos ou serviços!',
   'Na nova era digital, ser capaz de contar histórias e dividir informações e conhecimentos é essencial para dar alma à sua marca. O blog é ideal para isso. Se ele não faz parte de sua estratégia de marketing digital, é hora de repensar. Realizamos a criação de blogs utilizando práticas e ferramentas que permitem explorar todo o potencial dessa solução.'],
 'landing': ['Criação de landing pages que VENDEM!',
   'Então você fez um anúncio online. Investiu tempo e dinheiro para que sua campanha fosse um sucesso. Logo começou a notar que o número de visitantes aumentou, e muito!',
   'Mas, mesmo aumentando o número de visitas, seus resultados permaneceram iguais. Onde está o problema? As chances de que seja em sua landing page são grandes. Landing pages são páginas criadas com um único objetivo: converter os visitantes em clientes ou leads. Ou seja, trazer resultados para o seu negócio.',
   'Na Work Digital, a criação de landing pages une as melhores práticas de user experience e marketing digital para atingir seus objetivos.'],
}
def apply(t):
    for sid, (title, *paras) in CONTENT.items():
        blocks = [[title, paras[0]]] + [['', p] for p in paras[1:]]
        js = json.dumps(blocks, ensure_ascii=False)
        pat = r"(\{ id:'" + sid + r"',[^\n]*?blocks:)\[\n.*?\] \]\}"
        t, n = re.subn(pat, lambda m: m.group(1) + js + '}', t, count=1, flags=re.S)
        assert n == 1, sid
    a = "${s.blocks.map(([h,p])=>`<h3>${h}</h3><p>${p}</p>`).join('')}"
    assert t.count(a) == 1
    t = t.replace(a, "${s.blocks.map(([h,p])=>(h?`<h3>${h}</h3>`:'')+`<p>${p}</p>`).join('')}")
    return t
