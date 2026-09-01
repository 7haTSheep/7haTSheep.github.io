(function(){
  // reveal on scroll
  var els = document.querySelectorAll('.rv');
  if(!('IntersectionObserver' in window)){
    els.forEach(function(e){ e.classList.add('in'); });
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(en){
        if(en.isIntersecting){ en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, {rootMargin:'0px 0px -8% 0px', threshold:0.08});
    els.forEach(function(e,i){ e.style.transitionDelay = Math.min(i%6,5)*70 + 'ms'; io.observe(e); });
  }
  // year
  document.querySelectorAll('[data-year]').forEach(function(e){ e.textContent = new Date().getFullYear(); });
  // ticker duplicate for seamless loop
  document.querySelectorAll('.ticker .row').forEach(function(r){ r.innerHTML = r.innerHTML + r.innerHTML; });
})();
