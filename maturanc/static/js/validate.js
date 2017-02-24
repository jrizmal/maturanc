$(function(){

    $.validator.addMethod('dolgoGeslo',function(value,element){
        return value.length >= 8;
    }, 'Geslo mora biti dolgo vsaj 8 znakov.');

    $('#form-registracija').validate({
        rules: {
            email: {
                required: true,
                email: true,
                remote: 'api/prijava/obstaja/',
            },
            geslo: {
                required: true,
                dolgoGeslo: true,
            },
            ime: {
                required: true,
            },
            priimek: {
                required: true,
            }

        },
        messages:{
            email:{
                required: 'Vnesite e-mail naslov.',
                email: 'Vnesite veljaven e-mail naslov.',
                remote: $.validator.format("Uporabnik z e-mail naslovom {0} že obstaja."),
            },
            geslo:{
                required: 'Vnesite geslo.',
            },
            ime:{
                required: 'Vnesite svoje ime.',
            },
            priimek:{
                required: 'Vnesite svoj priimek.',
            },
        },
        errorElement : 'div',
        errorPlacement: function(error, element) {
            var placement = $(element).data('error');
            if (placement) {
                $(placement).append(error)
            } else {
                error.insertAfter(element);
            }
        },
    });
});