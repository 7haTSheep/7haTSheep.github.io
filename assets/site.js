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

// Guided website-fit questionnaire
(function(){
  var form=document.querySelector('.quiz-form');
  if(!form) return;
  var steps=[].slice.call(form.querySelectorAll('.quiz-step'));
  var count=form.querySelector('[data-quiz-count]');
  var bars=[].slice.call(form.querySelectorAll('.quiz-progress i'));
  var next=form.querySelector('[data-quiz-next]');
  var back=form.querySelector('[data-quiz-back]');
  var submit=form.querySelector('[data-quiz-submit]');
  var message=form.querySelector('[data-quiz-message]');
  var current=0;
  function show(index){
    current=index;
    steps.forEach(function(step,i){step.hidden=i!==current;});
    bars.forEach(function(bar,i){bar.classList.toggle('on',i<=current);});
    count.innerHTML=('0'+(current+1)).slice(-2)+' / 03 &mdash; WEBSITE FIT CHECK';
    back.hidden=current===0;
    next.hidden=current===steps.length-1;
    submit.hidden=current!==steps.length-1;
    message.textContent=current===steps.length-1?'Check your contact details, then send the completed brief.':'About two minutes. No obligation, no spam.';
    var first=steps[current].querySelector('input,select,textarea');
    if(first) first.focus({preventScroll:true});
  }
  function valid(){
    var controls=[].slice.call(steps[current].querySelectorAll('input,select,textarea'));
    var required=controls.filter(function(control){return control.required;});
    for(var i=0;i<required.length;i++){
      if(!required[i].checkValidity()){required[i].reportValidity();return false;}
    }
    return true;
  }
  next.addEventListener('click',function(){if(valid()) show(current+1);});
  back.addEventListener('click',function(){show(current-1);});
  show(0);
})();
