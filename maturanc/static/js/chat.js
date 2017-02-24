var posljiButton = $('#poslji_button')
var sporociloTextBox = $('#besedilo_text')
var sogovornik_slika_url = '';
function posljiSporocilo(){
    $.ajax({
        type: 'POST',
        url: 'https://maturanc.com/api/chat/sporocilo/poslji/',
        data: {
            posiljatelj: mojID,
            prejemnik: sogovornikID,
            besedilo: sporociloTextBox.val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(data){
            dobiNovaSporocila();
            $('#besedilo_text').val('');
            
        },
    });
}

function osveziVsaSporocila(){
    //https://maturanc.com/api/chat/vsasporocila/?oseba1=22&oseba2=1
    chatHTML="";
    $.ajax({
        type: 'GET',
        url: 'https://maturanc.com/api/chat/vsasporocila/',
        data: {
            seen: 'da',
            starejsa: '',
            samo_nova: '',
            timestamp: '',
            oseba1: mojID,
            oseba2: sogovornikID
        },
        success: function(data){
            jsonResult = JSON.parse(data);
            $.each(jsonResult, function(i, item) {
                var cas_hms=jsonResult[i].cas_posiljanja.split("T")[1].split(".")[0].split(":");
                var cas_clean = cas_hms[0] + ':' + cas_hms[1];
                if(jsonResult[i].posiljatelj==mojID){
                    chatHTML='<li class="collection-item" cas="'+jsonResult[i].cas_posiljanja+'"><div class="chatmessagejaz"><p>'+jsonResult[i].besedilo+'</p></div><p class="right cajtjaz">'+cas_clean+'</p></li>'+chatHTML;
                }
                else{
                    
                    chatHTML='<li class="collection-item avatar" cas="'+jsonResult[i].cas_posiljanja+'"><img src="'+sogovornik_slika_url+'" alt="" class="circle chatslika"><div class="chatmessage"><p>'+jsonResult[i].besedilo+'</p></div><p class="right cajt">'+cas_clean+'</p></li>'+chatHTML;
                }
            });
            $('#chat_list').html(chatHTML);
            var objDiv = document.getElementById("chat_list");
            objDiv.scrollTop = objDiv.scrollHeight;
            
            
        }
    });
}

function dobiNovaSporocila(){
    var zadnjeSporociloCas = $('#chat_list li').last().attr('cas');
    $.ajax({
        type: 'GET',
        url: 'https://maturanc.com/api/chat/vsasporocila/',
        data: {
            seen: 'da',
            starejsa: '',
            samo_nova: 'da',
            timestamp: zadnjeSporociloCas,
            oseba1: mojID,
            oseba2: sogovornikID
        },
        success: function(data){
            jsonResult = JSON.parse(data);
            $.each(jsonResult, function(i, item) {
                var cas_hms=jsonResult[i].cas_posiljanja.split("T")[1].split(".")[0].split(":");
                var cas_clean = cas_hms[0] + ':' + cas_hms[1];
                if(jsonResult[i].posiljatelj==mojID){
                    
                    $('#chat_list').append('<li class="collection-item" cas="'+jsonResult[i].cas_posiljanja+'"><div class="chatmessagejaz"><p>'+jsonResult[i].besedilo+'</p></div><p class="right cajtjaz">'+cas_clean+'</p></li>');
                }
                else{
                    $('#chat_list').append('<li class="collection-item avatar" cas="'+jsonResult[i].cas_posiljanja+'"><img src="'+sogovornik_slika_url+'" alt="" class="circle chatslika"><div class="chatmessage"><p>'+jsonResult[i].besedilo+'</p></div><p class="right cajt">'+cas_clean+'</p></li>');
                }
                
                var objDiv = document.getElementById("chat_list");
                objDiv.scrollTop = objDiv.scrollHeight;

                
            });
            
        }
    });
}
function dobiStarejsaSporocila(){
    var zadnjeSporociloCas = $('#chat_list li').first().attr('cas'); //prvo sporocilo na seznamu
    $.ajax({
        type: 'GET',
        url: 'https://maturanc.com/api/chat/vsasporocila/',
        data: {
            seen: '',
            starejsa: 'da',
            samo_nova: '',
            timestamp: zadnjeSporociloCas,
            oseba1: mojID,
            oseba2: sogovornikID
        },
        success: function(data){
            jsonResult = JSON.parse(data);
            $.each(jsonResult, function(i, item) {
                var cas_hms=jsonResult[i].cas_posiljanja.split("T")[1].split(".")[0].split(":");
                var cas_clean = cas_hms[0] + ':' + cas_hms[1];
                if(jsonResult[i].posiljatelj==mojID){
                    $('#chat_list').prepend('<li class="collection-item" cas="'+jsonResult[i].cas_posiljanja+'"><div class="chatmessagejaz"><p>'+jsonResult[i].besedilo+'</p></div><p class="right cajtjaz">'+cas_clean+'</p></li>');
                }
                else{
                    $('#chat_list').prepend('<li class="collection-item avatar" cas="'+jsonResult[i].cas_posiljanja+'"><img src="'+sogovornik_slika_url+'" alt="" class="circle chatslika"><div class="chatmessage"><p>'+jsonResult[i].besedilo+'</p></div><p class="right cajt">'+cas_clean+'</p></li>');
                }
            });
            
        }
    });
}

$(document).ready(function () {
    sogovornikID = $( "div.chip.hoverable" ).first().attr('userid');
    $('#ime_sogovornika').html($( "div.chip.hoverable" ).first().attr('ime'));
    $('#url_slika').val($( "div.chip.hoverable[userid='"+sogovornikID+"'] img" ).attr('src'));
    sogovornik_slika_url = $('#url_slika').val();
    osveziVsaSporocila();
    $('#poslji_button').click(function(){
        posljiSporocilo();
        
    });
    var interval_id = setInterval(function(){ dobiNovaSporocila(); }, 2000);
    $('#besedilo_text').keypress(function (e) {
    if (e.which == 13) {
        $('#poslji_button').trigger('click');
        return false;
    }
    });
    $( "div.chip.hoverable" ).click(function(e){
        if(sogovornikID == $(this).attr('userid')){
            return;
        }
        $('#ime_sogovornika').html($(this).attr('ime'))
        
        sogovornikID = $(this).attr('userid');
        $('#chat_list').html('');
        $('#url_slika').val($( "div.chip.hoverable[userid='"+sogovornikID+"'] img" ).attr('src'));
        sogovornik_slika_url = $('#url_slika').val();
        osveziVsaSporocila();
        if($(this).hasClass('red white-text')){
            $(this).removeClass('red white-text')
        }
        
    });
    
    $(window).focus(function() {
        if (!interval_id){
            dobiNovaSporocila();
            interval_id = setInterval(function(){ dobiNovaSporocila(); }, 2000);
        }
            
    });

    $(window).blur(function() {
        clearInterval(interval_id);
        interval_id = 0;
    });

    $('#chat_list').on('scroll', function() {
    var chatScrollTop = $(this).scrollTop();
    if(chatScrollTop == 0){
        dobiStarejsaSporocila();
        $(this).scrollTop(1)
    }
    
    });
    
});