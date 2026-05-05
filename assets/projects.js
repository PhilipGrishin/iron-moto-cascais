/**
 * Iron Custom Motors — Project page enhancements
 *
 * Effects:
 *  - Hero parallax bg
 *  - Hero text reveal on load
 *  - Story reveal on scroll
 *  - Gallery: 3D tilt, mouse-light, stagger reveal, click-to-lightbox
 *  - Lightbox: prev/next, ESC, arrows, swipe (mobile)
 *  - KPI counter (animates "99.764 mph" 0 → final)
 *  - Magnetic CTA buttons
 *  - Respects prefers-reduced-motion
 */
(function(){
  'use strict';

  const reduced = window.matchMedia('(prefers-reduced-motion:reduce)').matches;

  function ready(fn){
    if(document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  /* === HERO PARALLAX BG === */
  function initHeroParallax(){
    if(reduced) return;
    // Disable parallax on mobile — small viewport doesn't benefit from the effect
    // and iOS Safari rubber-band bounce makes JS-driven transforms jump.
    if(window.matchMedia('(max-width: 900px)').matches) return;
    if(window.matchMedia('(pointer: coarse)').matches) return;

    const bg = document.querySelector('.subpage .bg');
    if(!bg) return;

    let ticking = false;
    let lastY = -1;
    function update(){
      const y = Math.max(0, window.scrollY); // clamp negatives (overscroll)
      if(y === lastY){ ticking = false; return; }
      lastY = y;
      const offset = Math.min(y * 0.4, 220);
      const scale = 1.05 + Math.min(y / 4000, 0.06);
      bg.style.transform = `translate3d(0, ${offset}px, 0) scale(${scale})`;
      ticking = false;
    }
    window.addEventListener('scroll', () => {
      if(!ticking){
        ticking = true;
        requestAnimationFrame(update);
      }
    }, { passive: true });
    // Set initial transform synchronously so first scroll doesn't snap
    update();
    // Re-sync after layout/load (fonts, images may shift scrollY)
    window.addEventListener('load', () => { lastY = -1; update(); });
  }

  /* === HERO TEXT REVEAL === */
  function initHeroReveal(){
    const els = [
      '.subpage .proj-badge',
      '.subpage h1',
      '.subpage .tagline',
      '.subpage .proj-meta'
    ].map(s => document.querySelector(s)).filter(Boolean);
    // Stagger by adding .visible
    els.forEach((el, i) => {
      setTimeout(() => el.classList.add('visible'), 80 + i * 60);
    });
  }

  /* === STORY REVEAL ON SCROLL === */
  function initStoryReveal(){
    const story = document.querySelector('.proj-story');
    if(!story) return;
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if(e.isIntersecting){
          story.classList.add('visible');
          io.disconnect();
        }
      });
    }, { rootMargin: '0px 0px -80px 0px' });
    io.observe(story);
  }

  /* === GALLERY: 3D TILT + MOUSE LIGHT === */
  function initGalleryTilt(){
    if(reduced) return;
    const tiles = document.querySelectorAll('.proj-gallery .gtile');
    tiles.forEach(tile => {
      let raf = null;
      tile.addEventListener('mousemove', (e) => {
        const rect = tile.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width;
        const y = (e.clientY - rect.top) / rect.height;
        // Tilt: max 6deg
        const rx = (0.5 - y) * 6;
        const ry = (x - 0.5) * 6;
        tile.style.setProperty('--mx', `${x * 100}%`);
        tile.style.setProperty('--my', `${y * 100}%`);
        if(raf) cancelAnimationFrame(raf);
        raf = requestAnimationFrame(() => {
          tile.style.transform = `perspective(900px) rotateX(${rx}deg) rotateY(${ry}deg) translateZ(0)`;
        });
      });
      tile.addEventListener('mouseleave', () => {
        if(raf) cancelAnimationFrame(raf);
        tile.style.transform = '';
      });
    });
  }

  /* === GALLERY: STAGGER REVEAL ON SCROLL === */
  function initGalleryReveal(){
    const gallery = document.querySelector('.proj-gallery');
    if(!gallery) return;
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if(e.isIntersecting){
          gallery.classList.add('in');
          io.disconnect();
        }
      });
    }, { rootMargin: '0px 0px -80px 0px' });
    io.observe(gallery);
  }

  /* === LIGHTBOX === */
  function buildLightbox(){
    const lb = document.createElement('div');
    lb.className = 'lb';
    lb.setAttribute('role', 'dialog');
    lb.setAttribute('aria-modal', 'true');
    lb.setAttribute('aria-label', 'Image viewer');
    lb.innerHTML = `
      <div class="lb-stage">
        <button class="lb-close" aria-label="Close"><svg viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18"/></svg></button>
        <button class="lb-prev" aria-label="Previous"><svg viewBox="0 0 24 24"><path d="M15 18l-6-6 6-6"/></svg></button>
        <button class="lb-next" aria-label="Next"><svg viewBox="0 0 24 24"><path d="M9 6l6 6-6 6"/></svg></button>
        <div class="lb-counter"></div>
        <img class="lb-img" alt="" />
        <div class="lb-caption"></div>
      </div>`;
    document.body.appendChild(lb);
    return lb;
  }

  function initLightbox(){
    const tiles = Array.from(document.querySelectorAll('.proj-gallery .gtile'));
    if(!tiles.length) return;

    // Inject zoom icons + click handlers
    tiles.forEach((tile, idx) => {
      // Add zoom icon if not present
      if(!tile.querySelector('.zoom-ic')){
        const ic = document.createElement('div');
        ic.className = 'zoom-ic';
        ic.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3M11 8v6M8 11h6"/></svg>';
        tile.appendChild(ic);
      }
      tile.style.cursor = 'pointer';
      tile.dataset.lbIndex = idx;
      // Click handler (delegated to tile, ignores zoom icon)
      tile.addEventListener('click', () => openLightbox(idx));
      // Keyboard accessible
      tile.setAttribute('tabindex', '0');
      tile.setAttribute('role', 'button');
      tile.setAttribute('aria-label', `Open image ${idx+1} of ${tiles.length}`);
      tile.addEventListener('keydown', (e) => {
        if(e.key === 'Enter' || e.key === ' '){ e.preventDefault(); openLightbox(idx); }
      });
    });

    const lb = buildLightbox();
    const lbImg = lb.querySelector('.lb-img');
    const lbCounter = lb.querySelector('.lb-counter');
    const lbCaption = lb.querySelector('.lb-caption');
    let current = 0;

    function getFullSrc(tile){
      const img = tile.querySelector('img');
      if(!img) return '';
      // Use srcset 832w version (the largest we have)
      const srcset = img.getAttribute('srcset') || '';
      const m = srcset.match(/(\S+)\s+832w/);
      if(m) return m[1];
      return img.src;
    }
    function getCaption(tile){
      const img = tile.querySelector('img');
      return (img && img.alt) || '';
    }

    function show(idx){
      current = ((idx % tiles.length) + tiles.length) % tiles.length;
      const tile = tiles[current];
      const src = getFullSrc(tile);
      // Preload before showing
      const tmp = new Image();
      tmp.onload = () => {
        lbImg.src = src;
        lbImg.alt = getCaption(tile);
        lbCaption.textContent = getCaption(tile);
        lbCounter.textContent = `${current+1} / ${tiles.length}`;
      };
      tmp.src = src;
    }

    function openLightbox(idx){
      show(idx);
      lb.classList.add('open');
      document.body.style.overflow = 'hidden';
      document.addEventListener('keydown', onKey);
    }
    function closeLightbox(){
      lb.classList.remove('open');
      document.body.style.overflow = '';
      document.removeEventListener('keydown', onKey);
    }
    function onKey(e){
      if(e.key === 'Escape') closeLightbox();
      else if(e.key === 'ArrowLeft') show(current - 1);
      else if(e.key === 'ArrowRight') show(current + 1);
    }

    lb.querySelector('.lb-close').addEventListener('click', closeLightbox);
    lb.querySelector('.lb-prev').addEventListener('click', () => show(current - 1));
    lb.querySelector('.lb-next').addEventListener('click', () => show(current + 1));
    // Click on backdrop closes
    lb.addEventListener('click', (e) => {
      if(e.target === lb || e.target.classList.contains('lb-stage')) closeLightbox();
    });

    // Touch swipe
    let touchX = 0;
    lb.addEventListener('touchstart', (e) => { touchX = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', (e) => {
      const dx = (e.changedTouches[0].clientX - touchX);
      if(Math.abs(dx) > 50) show(current + (dx < 0 ? 1 : -1));
    }, { passive: true });
  }

  /* === KPI COUNTER === */
  function initCounter(){
    const els = document.querySelectorAll('.proj-meta .val.kpi[data-count]');
    if(!els.length) return;
    const io = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if(!e.isIntersecting) return;
        const el = e.target;
        const target = parseFloat(el.dataset.count);
        const decimals = parseInt(el.dataset.decimals || '0', 10);
        const suffix = el.dataset.suffix || '';
        const dur = parseInt(el.dataset.dur || '1400', 10);
        const start = performance.now();
        function frame(now){
          const t = Math.min((now - start) / dur, 1);
          // easeOutCubic
          const eased = 1 - Math.pow(1 - t, 3);
          const val = (target * eased).toFixed(decimals);
          el.textContent = val + (suffix ? ' ' + suffix : '');
          if(t < 1) requestAnimationFrame(frame);
        }
        requestAnimationFrame(frame);
        io.unobserve(el);
      });
    }, { threshold: 0.4 });
    els.forEach(el => io.observe(el));
  }

  /* === MAGNETIC BUTTONS === */
  function initMagneticButtons(){
    if(reduced) return;
    const btns = document.querySelectorAll('.cta-back .btn');
    btns.forEach(btn => {
      btn.addEventListener('mousemove', (e) => {
        const r = btn.getBoundingClientRect();
        const x = e.clientX - r.left - r.width/2;
        const y = e.clientY - r.top - r.height/2;
        btn.style.transform = `translate(${x*0.18}px, ${y*0.22}px)`;
      });
      btn.addEventListener('mouseleave', () => {
        btn.style.transform = '';
      });
    });
  }

  /* === SCROLL HINT (under hero) === */
  function injectScrollHint(){
    const hero = document.querySelector('.subpage .container');
    if(!hero) return;
    const hint = document.createElement('div');
    hint.className = 'scroll-hint';
    hint.innerHTML = '<span data-i18n="proj.scrollHint">Scroll to explore</span><svg width="14" height="20" viewBox="0 0 14 20" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="1" y="1" width="12" height="18" rx="6"/><line x1="7" y1="5" x2="7" y2="9"/></svg>';
    hero.parentElement.appendChild(hint);
  }

  /* === BOOT === */
  ready(() => {
    initHeroParallax();
    initHeroReveal();
    initStoryReveal();
    initGalleryReveal();
    initGalleryTilt();
    initLightbox();
    initCounter();
    initMagneticButtons();
    injectScrollHint();
  });
})();
