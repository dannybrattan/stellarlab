
(() => {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.nav');
  const drop = document.querySelector('.dropdown');
  const dropButton = document.querySelector('.dropdown-toggle');
  if (toggle && nav) toggle.addEventListener('click', () => {
    const open = nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded', String(open));
  });
  if (dropButton && drop) dropButton.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = drop.classList.toggle('open');
    dropButton.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('click', (e) => {
    if (drop && !drop.contains(e.target)) {
      drop.classList.remove('open');
      if (dropButton) dropButton.setAttribute('aria-expanded','false');
    }
  });

  const q = document.querySelector('#pub-search');
  const y = document.querySelector('#pub-year');
  const pubs = [...document.querySelectorAll('.pub[data-year]')];
  const count = document.querySelector('#pub-count');
  function filterPubs(){
    if (!pubs.length) return;
    const needle = (q?.value || '').toLowerCase().trim();
    const year = y?.value || 'all';
    let shown = 0;
    pubs.forEach(p => {
      const okText = !needle || p.textContent.toLowerCase().includes(needle);
      const okYear = year === 'all' || p.dataset.year === year;
      p.classList.toggle('hidden', !(okText && okYear));
      if(okText && okYear) shown++;
    });
    if(count) count.textContent = `${shown} publication${shown===1?'':'s'}`;
  }
  q?.addEventListener('input', filterPubs);
  y?.addEventListener('change', filterPubs);
  filterPubs();
})();
