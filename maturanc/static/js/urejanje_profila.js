$("#form_podatki").submit(function(e) {
    
    var url = "shrani/"; // the script where you handle the form input.

    $.ajax({
           type: "POST",
           url: "shrani/",
           data: $("#form_podatki").serialize(), // serializes the form's elements.
           success: function(data)
           {
               Materialize.toast('<i class="fa fa-check" aria-hidden="true"></i>&nbsp;Spremembe shranjene',5000);

           }
    });
    e.preventDefault();
});
$("#form_omrezja").submit(function(e) {
    
    var url = "shrani/omrezja/"; // the script where you handle the form input.

    $.ajax({
           type: "POST",
           url: "shrani/omrezja/",
           data: $("#form_omrezja").serialize(), // serializes the form's elements.
           success: function(data)
           {
               Materialize.toast('<i class="fa fa-check" aria-hidden="true"></i>&nbsp;Spremembe shranjene',5000);

           }
    });
    e.preventDefault();
});