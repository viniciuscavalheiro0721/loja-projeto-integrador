

    console.log("OLA MUNDO1");

    var elements = document.getElementsByClassName('Total-Price');
    var sum = 0;

    for (i=0;i< elements.length;i++) 
    {
        sum += parseFloat(elements[i].innerHTML.replace(/,/,'.'));
    };

    acres = parseFloat(parent.document.getElementById("acres").value)
    desc = parseFloat(parent.document.getElementById("desc").value)

    console.log(desc)
    res = (sum + acres) - desc
    parent.document.getElementById("sub-total").value = sum.toFixed(2)
    parent.document.getElementById("total").value = res.toFixed(2)
    console.log(sum)

    console.log("AAAAAAAAAa")
