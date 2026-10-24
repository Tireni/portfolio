const toggle = document.querySelector('.menu-toggle');
const nav = document.querySelector('#navigation');
toggle?.addEventListener('click', () => {
  const expanded = toggle.getAttribute('aria-expanded') === 'true';
  toggle.setAttribute('aria-expanded', String(!expanded));
  nav.classList.toggle('open', !expanded);
});
nav?.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
  toggle.setAttribute('aria-expanded', 'false');
  nav.classList.remove('open');
}));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && nav?.classList.contains('open')) {
    toggle.setAttribute('aria-expanded', 'false');
    nav.classList.remove('open');
    toggle.focus();
  }
});

const contactDialog=document.querySelector('#contact-dialog');
let lastContactTrigger=null;
document.querySelectorAll('[data-contact-open]').forEach(button=>button.addEventListener('click',()=>{lastContactTrigger=button;contactDialog?.showModal();}));
document.querySelector('[data-contact-close]')?.addEventListener('click',()=>contactDialog?.close());
contactDialog?.addEventListener('click',event=>{if(event.target===contactDialog)contactDialog.close();});
contactDialog?.addEventListener('close',()=>lastContactTrigger?.focus());
