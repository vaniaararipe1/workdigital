
(() => {
  const title = document.getElementById('wd-statement-2-title');
  if (!title || title.dataset.wdInitialized) return;
  title.dataset.wdInitialized = 'true';
  const text = title.getAttribute('aria-label');
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  const measure = document.createElement('canvas').getContext('2d');
  const clamp = value => Math.max(0, Math.min(1, value));
  const mix = (a, b, p) => `rgb(${a.map((v,i) => Math.round(v+(b[i]-v)*p)).join(',')})`;
  let frame = 0;

  function splitLines() {
    if (!measure || !title.clientWidth) return;
    const css = getComputedStyle(title);
    measure.font = `${css.fontWeight} ${css.fontSize} ${css.fontFamily}`;
    const spacing = parseFloat(css.letterSpacing) || 0;
    const widthOf = s => measure.measureText(s).width + spacing * Math.max(0,s.length-1);
    const words = text.split(/\s+/), lines = [];
    let line = '';
    words.forEach(word => {
      const next = line ? `${line} ${word}` : word;
      if (line && widthOf(next) > title.clientWidth) { lines.push(line); line = word; }
      else line = next;
    });
    if (line) lines.push(line);
    // Mesmo número de linhas, com comprimentos equilibrados.
    const target = widthOf(text)/lines.length, memo = new Map();
    function balance(start, count) {
      if (!count) return start === words.length ? {cost:0,lines:[]} : null;
      const key = `${start}:${count}`;
      if (memo.has(key)) return memo.get(key);
      let best = null;
      for (let end=start+1; end<=words.length-count+1; end++) {
        const part = words.slice(start,end).join(' '), width = widthOf(part);
        if (width > title.clientWidth) break;
        const next = balance(end,count-1);
        if (!next) continue;
        const cost = (width-target)**2 + next.cost;
        if (!best || cost < best.cost) best = {cost,lines:[part,...next.lines]};
      }
      memo.set(key,best);
      return best;
    }
    const balanced = balance(0,lines.length);
    const fragment = document.createDocumentFragment();
    (balanced?.lines || lines).forEach((part,i,array) => {
      const span = document.createElement('span');
      span.className = 'wd-statement-2-line';
      span.setAttribute('aria-hidden','true');
      span.textContent = part + (i < array.length-1 ? ' ' : '');
      fragment.append(span);
    });
    title.replaceChildren(fragment);
    update();
  }

  function update() {
    frame = 0;
    const rect = title.getBoundingClientRect(), lines = [...title.children];
    // Igual à frase anterior: scrub top 60% → bottom 60%, stagger 0.3.
    const progress = reduced.matches ? 1 : clamp((innerHeight*.6-rect.top)/Math.max(1,rect.height));
    const duration = 1 + .3 * Math.max(0,lines.length-1);
    lines.forEach((line,i) => {
      const p = clamp(progress*duration-i*.3);
      line.style.setProperty('--wd-from',mix([96,37,225],[239,231,255],p));
      line.style.setProperty('--wd-to',mix([203,182,255],[245,195,216],p));
    });
  }
  function request() { if (!frame) frame = requestAnimationFrame(update); }
  addEventListener('scroll',request,{passive:true});
  addEventListener('resize',splitLines,{passive:true});
  reduced.addEventListener('change',request);
  document.fonts.ready.then(splitLines);
  splitLines();
})();
