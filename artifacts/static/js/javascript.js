console.log("OLA MUNDO");


function convertToSlug(Text)
        {
            return Text
                .toLowerCase()
                .replace(/ /g,'-')
                .replace(/[^\w-]+/g,'')
                ;
        }
        
        
document.getElementById("id_name").onchange = function(){

    document.getElementById("id_slug").value = convertToSlug(document.getElementById("id_name").value);
    document.getElementById("id_slug").readOnly = true;
        };