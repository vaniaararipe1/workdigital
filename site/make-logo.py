import re
s=open('/home/user/workdigital/home-final/img/logo-work-digital.svg').read()
s=s.replace('.b{fill:#fff;}','.p{fill:#6025E1;}.d{fill:#262626;}')
def recolor(m):
    tag=m.group(0); x=float(re.search(r' d="M\s*([\d.]+)',tag).group(1))
    return tag.replace('class="b"','class="p"' if x<1600 else 'class="d"')
s=re.sub(r'<path class="b"[^>]*>',recolor,s)
assert 'class="b"' not in s
open('site-build/img/logo-work-digital-positivo.svg','w').write(s)
print(s.count('class="p"'), s.count('class="d"'), len(s))
