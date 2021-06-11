$( document ).ready(function() {

    console.log("OLA MUNDO");

            var baseUrl   = 'http://127.0.0.1:8000/artifacts';
            var filter     = $('#filter');
            var searchBtn = $('#search-btn');
          
          
            

        
            $(searchBtn).on('click', function() {
                 searchForm.submit();
               
            });
        
            $(filter).change(function() {
                var filter = $(this).val();
                window.location.href = baseUrl + '?filter=' + filter;
            
            });

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
        
        });