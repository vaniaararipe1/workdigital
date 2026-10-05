# Efeitos de hover: alguns Chrome (Windows) respondem "false" para (hover: hover) e (pointer: fine)
# mesmo com mouse. Por isso os efeitos ficam desligados só em aparelhos de toque (pointer: coarse).
import glob, os, re
TOUCH_OFF = 'not all and (pointer: coarse)'
def fix_text(t):
    t = re.sub(r'\(hover: ?hover\) and \(pointer: ?fine\)', TOUCH_OFF, t)
    t = re.sub(r'@media ?\(hover: ?hover\)', '@media ' + TOUCH_OFF, t)
    t = t.replace('matchMedia("(any-hover: hover)").matches || matchMedia("(any-pointer: fine)").matches', '!matchMedia("(pointer: coarse)").matches')
    return t
def run(out):
    for p in glob.glob(os.path.join(out, '*.html')):
        t = open(p).read(); n = fix_text(t)
        if n != t: open(p, 'w').write(n)
if __name__ == '__main__':
    run(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'site-build'))
