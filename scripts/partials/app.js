const T = window.__T;
const q = document.getElementById('q');
const langSel = document.getElementById('lang');
const sortSel = document.getElementById('sort');
const diffSel = document.getElementById('diff');
const actBtn = document.getElementById('act');
const resetBtn = document.getElementById('reset');
const cnt = document.getElementById('cnt');
const toolbar = document.querySelector('.toolbar');
const chips = [...document.querySelectorAll('.chip')];
const cards = [...document.querySelectorAll('.card')];
const groups = [...document.querySelectorAll('.group')];
const empty = document.getElementById('empty');
let curCat = 'all';

// 记住每张卡的原始文案，用于搜索时加高亮、清空时还原
const text = new Map();
cards.forEach(c => {
  const t = {
    p: c.querySelector('.pitch'),
    n: c.querySelector('.note'),
    r: c.querySelector('.repo .name'),
    f: c.querySelector('.fitv')
  };
  t.pText = t.p.textContent;
  t.nText = t.n.textContent;
  t.rText = t.r.textContent;
  t.fText = t.f.textContent;
  text.set(c, t);
});

const esc = s => s.replace(/[&<>]/g, m => ({'&': '&amp;', '<': '&lt;', '>': '&gt;'}[m]));

function highlight(el, raw, kws){
  if(!kws.length || !raw){ el.textContent = raw; return; }
  const pat = kws.map(k => k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|');
  const re = new RegExp(pat, 'gi');
  let out = '', last = 0, m;
  while((m = re.exec(raw)) !== null){
    out += esc(raw.slice(last, m.index)) + '<mark>' + esc(m[0]) + '</mark>';
    last = m.index + m[0].length;
    if(!m[0]) break;
  }
  el.innerHTML = out + esc(raw.slice(last));
}

// 只在「可见文字里没有命中」时才提示是哪个人工标签把这条捞出来的
function markTags(c, kws){
  const top = c.querySelector('.card-top');
  let badge = top.querySelector('.tag-hit');
  const t = text.get(c);
  const visible = (t.pText + t.nText + t.rText + t.fText).toLowerCase();
  const visibleHit = kws.length && kws.every(k => visible.includes(k));
  const tags = (c.dataset.topics || '').split(' ').filter(Boolean);
  const hit = kws.length ? tags.filter(t => kws.some(k => t.toLowerCase().includes(k))) : [];
  if(kws.length && !visibleHit && hit.length){
    if(!badge){ badge = document.createElement('span'); badge.className = 'tag-hit'; top.appendChild(badge); }
    badge.textContent = T.js.tag + hit.slice(0, 2).join(' / ');
  } else if(badge){
    badge.remove();
  }
}

// 大数字展示：中文按「万」，英文按 k / M
function fmtBig(n){
  if(T.numStyle === 'zh'){
    return n >= 10000 ? (n / 10000).toFixed(1).replace(/\.0$/, '') + '万' : n.toLocaleString('en-US');
  }
  if(n >= 1e6){ return (n / 1e6).toFixed(2).replace(/\.?0+$/, '') + 'M'; }
  if(n >= 1e3){ return (n / 1e3).toFixed(1).replace(/\.0$/, '') + 'k'; }
  return n.toLocaleString('en-US');
}

function isOn(){ return actBtn.getAttribute('aria-pressed') === 'true'; }

function apply(){
  const raw = q.value.trim();
  // 多关键词：空格切分，每个词都要命中（AND）
  const kws = raw.toLowerCase().split(/\s+/).filter(Boolean);
  const lg = langSel.value, df = diffSel.value, actOnly = isOn();
  let shown = 0;

  cards.forEach(c => {
    const t = text.get(c);
    let ok = (curCat === 'all' || c.dataset.cat === curCat)
          && (!lg || c.dataset.lang === lg)
          && (!df || c.dataset.diff === df)
          && (!actOnly || c.dataset.act === '1');
    if(ok && kws.length){
      const hay = c.dataset.name + ' ' + (c.dataset.topics || '');
      ok = kws.every(k => hay.includes(k));
    }
    c.style.display = ok ? '' : 'none';
    if(ok){
      shown++;
      highlight(t.p, t.pText, kws);
      highlight(t.n, t.nText, kws);
      highlight(t.r, t.rText, kws);
      highlight(t.f, t.fText, kws);
      markTags(c, kws);
    } else {
      t.p.textContent = t.pText;
      t.n.textContent = t.nText;
      t.r.textContent = t.rText;
      t.f.textContent = t.fText;
      markTags(c, []);
    }
  });

  // 组内排序 → 空组隐藏 → 更新组内计数
  groups.forEach(g => {
    const grid = g.querySelector('.grid');
    const list = [...grid.children];
    list.sort((a, b) => sortSel.value === 'upd'
      ? b.dataset.upd.localeCompare(a.dataset.upd)
      : (+b.dataset.stars) - (+a.dataset.stars));
    list.forEach(el => grid.appendChild(el));
    const shownCards = list.filter(el => el.style.display !== 'none');
    g.style.display = shownCards.length ? '' : 'none';
    g.querySelector('.gc-n').textContent = shownCards.length;
    // 星数跟着筛选重算，否则筛出 1 个项目还挂着整条赛道的星数，容易误读
    const sum = shownCards.reduce((n, el) => n + (+el.dataset.stars), 0);
    g.querySelector('.gc-s').textContent = fmtBig(sum);
  });

  empty.style.display = shown ? 'none' : 'block';
  cnt.innerHTML = shown === cards.length
    ? T.js.all.replace('{n}', `<b>${cards.length}</b>`).replace('{t}', groups.length)
    : T.js.some.replace('{n}', `<b>${shown}</b>`).replace('{total}', cards.length);

  // 只要任一控件离开默认状态（含只改排序），「重置」就该出现
  const dirty = curCat !== 'all' || !!raw || !!lg || !!df || actOnly || sortSel.value !== 'stars';
  resetBtn.classList.toggle('on', dirty);
  syncHash();
}

// 筛选状态写进地址栏，刷新和转发都能还原
let hashTimer;
function syncHash(){
  clearTimeout(hashTimer);
  hashTimer = setTimeout(() => {
    const p = new URLSearchParams();
    if(curCat !== 'all') p.set('cat', curCat);
    if(q.value.trim()) p.set('q', q.value.trim());
    if(langSel.value) p.set('lang', langSel.value);
    if(diffSel.value) p.set('diff', diffSel.value);
    if(isOn()) p.set('act', '1');
    if(sortSel.value !== 'stars') p.set('sort', sortSel.value);
    const h = p.toString();
    history.replaceState(null, '', h ? '#' + h : location.pathname + location.search);
  }, 250);
}

function readHash(){
  if(!location.hash) return;
  const p = new URLSearchParams(location.hash.slice(1));
  q.value = p.get('q') || '';
  langSel.value = p.get('lang') || '';
  // 老链接里写的是中文门槛（易/中/难），映射到现在的稳定值
  const d = p.get('diff');
  diffSel.value = {'易': 'easy', '中': 'medium', '难': 'hard'}[d] || d || '';
  sortSel.value = p.get('sort') || 'stars';
  actBtn.setAttribute('aria-pressed', p.get('act') === '1' ? 'true' : 'false');
  const cat = p.get('cat');
  if(cat && chips.some(c => c.dataset.cat === cat)){
    curCat = cat;
    chips.forEach(c => {
      const on = c.dataset.cat === cat;
      c.classList.toggle('on', on);
      c.setAttribute('aria-pressed', String(on));
    });
  }
}

function reset(){
  q.value = ''; langSel.value = ''; diffSel.value = ''; sortSel.value = 'stars';
  actBtn.setAttribute('aria-pressed', 'false');
  curCat = 'all';
  chips.forEach(c => {
    const on = c.dataset.cat === 'all';
    c.classList.toggle('on', on);
    c.setAttribute('aria-pressed', String(on));
  });
  apply();
}

chips.forEach(ch => ch.addEventListener('click', () => {
  chips.forEach(x => { x.classList.remove('on'); x.setAttribute('aria-pressed', 'false'); });
  ch.classList.add('on');
  ch.setAttribute('aria-pressed', 'true');
  curCat = ch.dataset.cat;
  apply();
}));

actBtn.addEventListener('click', () => {
  actBtn.setAttribute('aria-pressed', isOn() ? 'false' : 'true');
  apply();
});
resetBtn.addEventListener('click', reset);
document.getElementById('empty-reset').addEventListener('click', reset);
q.addEventListener('input', apply);
langSel.addEventListener('change', apply);
diffSel.addEventListener('change', apply);
sortSel.addEventListener('change', apply);

// 快捷键：/ 聚焦搜索，Esc 清空或退出搜索框
document.addEventListener('keydown', e => {
  const typing = /^(INPUT|SELECT|TEXTAREA)$/.test(document.activeElement.tagName);
  if(e.key === '/' && !typing){ e.preventDefault(); q.focus(); q.select(); }
  if(e.key === 'Escape'){
    if(q.value){ q.value = ''; apply(); }
    else if(typing){ document.activeElement.blur(); }
  }
});

// 切到另一种语言时把当前筛选一起带过去，别让用户重筛一遍
const langLink = document.getElementById('langLink');
if(langLink){
  langLink.addEventListener('click', () => {
    const base = langLink.dataset.base;
    langLink.href = base + (location.hash || '');
  });
}

// 吸顶工具栏加投影，让「已经离开顶部」这件事看得见
addEventListener('scroll', () => {
  toolbar.classList.toggle('scrolled', scrollY > 8);
}, {passive: true});

// 页脚二维码：点一下放大，方便手机对着屏幕扫；再点一下收回
const qr = document.getElementById('qr');
if(qr){
  qr.addEventListener('click', () => {
    qr.closest('.connect').classList.toggle('open');
  });
  qr.addEventListener('keydown', e => {
    if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); qr.click(); }
  });
}

readHash();
apply();
