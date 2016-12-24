/// <reference path="jquery.d.ts" />
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
                $('#loginError').css('display','none');
                location.reload();
            }
            else{
                $('#loginError').css('display','block');
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
    })
});