/// <reference path="jquery.d.ts" />

$( document ).ready(function() {
    $(document).on('click','#prijavabtn',function(event){
        var passwordBox = $('#password');
        var usernameBox = $('#email');
        $.ajax({
            type: 'GET',
            url: '/api/prijava/',
            data: {
                uIme: usernameBox.val(),
                uGeslo: passwordBox.val()
            },
            success: function (data) {
                if(data=='prijava uspesna'){
                    location.reload();
                }
                else{
                    Materialize.toast('<i class="fa fa-exclamation-circle" aria-hidden="true"></i>&nbsp;E-mail in geslo se ne ujemata', 5000);
                }
            },
        })
    });

    $(document).on('click','#odjavaButton',function(event){
        $.ajax({
            type: 'GET',
            url: '/api/odjava/',
            success: function (data) {
                location.reload();
            },
        });
        
    });
    $('#email').keypress(function (e) {
    if (e.which == 13) {
        $('#prijavabtn').trigger('click');
        return false;
    }
    });
    $('#password').keypress(function (e) {
    if (e.which == 13) {
        $('#prijavabtn').trigger('click');
        return false;
    }
    });
});