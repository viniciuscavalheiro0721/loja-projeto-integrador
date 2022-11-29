

$( "#codigo" ).change(function() {
    $( "#pdv" ).submit();
 
  });


  $( "#desc" ).change(function() {
    aplicaExtras()
    $( "#pdv" ).submit();
  });

  $( "#acres" ).change(function() {
    aplicaExtras()
    $( "#pdv" ).submit();
  });

  $( "#pgto" ).change(function() {
    aplicaExtras()
    $( "#pdv" ).submit();
  });

  $( "#valor-pg" ).change(function() {
    pg = parseFloat(document.getElementById("valor-pg").value)
    tot = parseFloat(document.getElementById("total").value)

    document.getElementById("desc").value = y.toFixed(2)
    document.getElementById("troc").value = (pg - tot).toFixed(2)
  });


  function aplicaExtras(){
    
    x = parseFloat(document.getElementById("desc").value)
    y = parseFloat(document.getElementById("acres").value)
    z = parseFloat(document.getElementById("sub-total").value) 

    sum = z + y - x;
    document.getElementById("total").value = sum.toFixed(2)


  }