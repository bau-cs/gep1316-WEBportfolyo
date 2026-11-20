'use strict';

// Ortak arayuz davranislari: tema, mobil menu, proje filtreleme ve form dogrulama.
const root = document.documentElement;

// 1) Tema degistirme: tercih yalnizca bu tarayicida saklanir.
function setupThemeToggle() {
  let savedTheme = null;
  try { savedTheme = localStorage.getItem('hcs-theme'); } catch (error) { /* Depolama kapaliysa varsayilan tema kullanilir. */ }
  if (savedTheme === 'dark' || savedTheme === 'light') root.dataset.theme = savedTheme;

  document.querySelectorAll('.theme-toggle').forEach((button) => {
    const updateButton = () => {
      const isDark = root.dataset.theme === 'dark';
      button.setAttribute('aria-pressed', String(isDark));
      button.setAttribute('aria-label', isDark ? 'Aydinlik temaya gec' : 'Koyu temaya gec');
      const label = button.querySelector('.theme-label');
      if (label) label.textContent = isDark ? 'Aydinlik mod' : 'Koyu mod';
    };
    updateButton();
    button.addEventListener('click', () => {
      const nextTheme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      root.dataset.theme = nextTheme;
      try { localStorage.setItem('hcs-theme', nextTheme); } catch (error) { /* Tema yine de etkin olur. */ }
      updateButton();
    });
  });
}

// 2) Mobil gezinme: acik/kapali durumu erisilebilir niteliklerle duyurulur.
function setupMobileMenu() {
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('.primary-nav');
  if (!toggle || !nav) return;
  const closeMenu = () => {
    nav.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Menüyü aç');
  };
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
    toggle.setAttribute('aria-label', isOpen ? 'Menüyü kapat' : 'Menüyü aç');
  });
  nav.querySelectorAll('a').forEach((link) => link.addEventListener('click', closeMenu));
  document.addEventListener('keydown', (event) => { if (event.key === 'Escape') closeMenu(); });
  window.addEventListener('resize', () => { if (window.innerWidth > 680) closeMenu(); });
}

// 3) Proje filtreleme ve arama birlikte calisir.
function setupProjectFilters() {
  const grid = document.querySelector('#projects-grid');
  if (!grid) return;
  const cards = Array.from(grid.querySelectorAll('.project-card'));
  const filterButtons = Array.from(document.querySelectorAll('[data-filter]'));
  const searchInput = document.querySelector('#project-search');
  const results = document.querySelector('#project-results');
  const emptyState = document.querySelector('#empty-projects');
  const resetButton = document.querySelector('.reset-filters');
  let activeFilter = 'all';

  const applyFilters = () => {
    const term = (searchInput?.value || '').trim().toLocaleLowerCase('tr-TR');
    let visible = 0;
    cards.forEach((card) => {
      const categories = (card.dataset.categories || '').split(/\s+/);
      const searchable = (card.dataset.search || card.textContent).toLocaleLowerCase('tr-TR');
      const categoryMatch = activeFilter === 'all' || categories.includes(activeFilter);
      const textMatch = !term || searchable.includes(term);
      const show = categoryMatch && textMatch;
      card.hidden = !show;
      if (show) visible += 1;
    });
    if (results) results.textContent = `${visible} proje listeleniyor`;
    if (emptyState) emptyState.hidden = visible !== 0;
  };

  filterButtons.forEach((button) => button.addEventListener('click', () => {
    activeFilter = button.dataset.filter || 'all';
    filterButtons.forEach((item) => {
      const selected = item === button;
      item.classList.toggle('is-selected', selected);
      item.setAttribute('aria-pressed', String(selected));
    });
    applyFilters();
  }));
  searchInput?.addEventListener('input', applyFilters);
  const reset = () => {
    activeFilter = 'all';
    if (searchInput) searchInput.value = '';
    filterButtons.forEach((button) => {
      const selected = button.dataset.filter === 'all';
      button.classList.toggle('is-selected', selected);
      button.setAttribute('aria-pressed', String(selected));
    });
    applyFilters();
  };
  resetButton?.addEventListener('click', reset);
  applyFilters();

  // GitHub Pages adresi biliniyorsa depo linkleri otomatik olarak portfolyo deposuna yonelir.
  const host = window.location.hostname;
  if (host.endsWith('github.io')) {
    const owner = host.split('.')[0];
    const segments = window.location.pathname.split('/').filter(Boolean);
    const repo = segments.length ? segments[0] : `${owner}.github.io`;
    document.querySelectorAll('[data-repo-path]').forEach((link) => {
      const path = link.dataset.repoPath;
      if (path) link.href = `https://github.com/${owner}/${repo}/tree/main/${path}`;
    });
  }
}

// 4) Iletisim formu: istemci tarafinda dogrular, hicbir yere gondermez.
function setupContactForm() {
  const form = document.querySelector('#contact-form');
  if (!form) return;
  const fields = [
    { id: 'full-name', error: 'name-error', message: 'Ad soyad en az 2 karakter olmalidir.' },
    { id: 'email-address', error: 'email-error', message: 'Gecerli bir e-posta adresi girin.' },
    { id: 'topic', error: 'topic-error', message: 'Lutfen bir konu secin.' },
    { id: 'message', error: 'message-error', message: 'Mesaj en az 10 karakter olmalidir.' }
  ];
  const feedback = document.querySelector('#form-feedback');
  const message = document.querySelector('#message');
  const counter = document.querySelector('#message-count');

  const getError = (field) => {
    const element = document.getElementById(field.id);
    const value = (element?.value || '').trim();
    if (!element) return '';
    if (!value) return field.id === 'topic' ? 'Lutfen bir konu secin.' : 'Bu alan zorunludur.';
    if (field.id === 'full-name' && value.length < 2) return field.message;
    if (field.id === 'email-address' && !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(value)) return field.message;
    if (field.id === 'message' && value.length < 10) return field.message;
    return '';
  };
  const validateField = (field) => {
    const element = document.getElementById(field.id);
    const errorElement = document.getElementById(field.error);
    const error = getError(field);
    if (element) element.setAttribute('aria-invalid', String(Boolean(error)));
    if (errorElement) errorElement.textContent = error;
    return !error;
  };

  fields.forEach((field) => {
    const element = document.getElementById(field.id);
    element?.addEventListener('blur', () => validateField(field));
    element?.addEventListener('input', () => {
      if (element.getAttribute('aria-invalid') === 'true') validateField(field);
      if (feedback) feedback.hidden = true;
    });
    element?.addEventListener('change', () => {
      if (element.getAttribute('aria-invalid') === 'true') validateField(field);
    });
  });
  message?.addEventListener('input', () => {
    if (counter) counter.textContent = `${message.value.length} / 1200`;
  });

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const valid = fields.map(validateField).every(Boolean);
    if (!valid) {
      if (feedback) {
        feedback.hidden = false;
        feedback.classList.add('is-error');
        feedback.textContent = 'Lutfen isaretli alanlari duzeltin. Bu demo formu mesaj gondermez.';
      }
      const firstInvalid = form.querySelector('[aria-invalid="true"]');
      firstInvalid?.focus();
      return;
    }
    if (feedback) {
      feedback.hidden = false;
      feedback.classList.remove('is-error');
      feedback.textContent = 'Form dogrulamasi basarili. Bu egitim demosunda mesaj kaydedilmedi veya gonderilmedi.';
    }
    form.reset();
    fields.forEach((field) => {
      document.getElementById(field.id)?.removeAttribute('aria-invalid');
      const errorElement = document.getElementById(field.error);
      if (errorElement) errorElement.textContent = '';
    });
    if (counter) counter.textContent = '0 / 1200';
  });
}

function setupCurrentYear() {
  document.querySelectorAll('[data-current-year]').forEach((element) => {
    element.textContent = String(new Date().getFullYear());
  });
}

document.addEventListener('DOMContentLoaded', () => {
  setupThemeToggle();
  setupMobileMenu();
  setupProjectFilters();
  setupContactForm();
  setupCurrentYear();
});
