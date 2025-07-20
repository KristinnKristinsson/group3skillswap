function userChoice(choice) {


  // const reqForm   = document.getElementById("requestForm");
  // const offReqDiv = document.getElementById("OffReq");
  // console.log('choice=', choice, 'reqForm?', !!reqForm, 'offReqDiv?', !!offReqDiv);



  // console.log('Hi1', choice)
  if (choice=='offer'){
    document.getElementById("offerForm").style.display = "block";
    document.getElementById("OffReq").style.display = "none";

  }
  else if(choice=='request'){
    // console.log('Hi3', choice)
    document.getElementById("OffReq").style.display = "none";
    document.getElementById("requestForm").style.display = "block";
  }
  else{
    print ("Something went wrong, please try again.")
  }
} 

// function myFunction(){
//   console.log('Im working')

// }

document.addEventListener('DOMContentLoaded', function () {
  const toggle = document.getElementById('menuToggle');
  const menu   = document.getElementById('menu');
  if (!toggle || !menu) return;

  toggle.addEventListener('click', function () {
    menu.classList.toggle('show');
    // accessibility
    const expanded = menu.classList.contains('show');
    toggle.setAttribute('aria-expanded', expanded ? 'true' : 'false');
  });
});

function messageTimeout(){
  //self.time=5000;
  document.querySelectorAll('.messages .alert').forEach(function(el){
    el.style.transition = "opacity 1s";
    el.style.opacity = 0;
    setTimeout(() => el.remove(), 1000);  // remove after fade out
});
}
  // window.location.href = "{% url 'skills:skillboard' %}";

