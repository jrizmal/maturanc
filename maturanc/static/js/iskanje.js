/// <reference path="jquery.d.ts" />

    dobiRezultate(-1, 0, 300);
    $(function () {
    var slider = document.getElementById('iskanjepovisini');

    var skipValues = [
    slider1Value = document.getElementById('slider1-span'),
    slider2Value = document.getElementById('slider2-span')
    ];
    function crossUpdate(value, slider) {

        slider.noUiSlider.set(value);
    }


    noUiSlider.create(slider, {
        start: [150, 190],
        connect: true,
        step: 5,
        range: {
            'min': 100,
            'max': 260,
        },
        format: wNumb({
            decimals: 0
        }),
        
    });

    slider.noUiSlider.on('set', function(){
        dobiRezultateVrednosti();
    });
    

    slider.noUiSlider.on('update', function (values, handle) {
        skipValues[handle].innerHTML = values[handle];
    });

    
});

function dobiRezultateVrednosti(){
    var slider = document.getElementById('iskanjepovisini');
    var visinaRange = slider.noUiSlider.get();

    var regija=$('#regija_search').val();
    var sola=$('#sola_search').val();

    dobiRezultate(0,visinaRange[0],visinaRange[1],regija,sola);
}

var $container = $('.searchresult');

$(document).on('click','#btnShraniSpremembe',function(event){
    spolIndex = $("#spolSelect").val();
    visinaRange = document.getElementById('iskanjepovisini').noUiSlider.get();
    dobiRezultate(spolIndex,visinaRange[0],visinaRange[1]);
});
var regijaPrev = "";
var solaPrev = "";

$('#regija_search').focusout(function(){
    regijaNow = $('#regija_search').val();
    if(regijaPrev != regijaNow){
        regijaPrev = regijaNow;
        dobiRezultateVrednosti();
    }
});

$('#sola_search').focusout(function(){
    solaNow = $('#sola_search').val();
    if(solaPrev != solaNow){
        solaPrev = solaNow;
        dobiRezultateVrednosti();
    }
});

function dobiRezultate(spol, visina_start, visina_end, regija, sola){
    var karticeHTML="";
    var jsonResult;
    var appendedData = "";

    if(spol!=null){
        $.ajax({
            type: 'GET',
            url: '/api/iskanje/',
            data: {
                spol: spol,
                visina1: visina_start,
                visina2: visina_end,
                regija: regija,
                sola: sola,
            },
            success: function (data) {

                Materialize.toast('<i class="fa fa-info-circle" aria-hidden="true"></i>&nbsp;Poizvedba spremenjena', 5000);
                
                $('.searchresult').html('');
                
                jsonResult = JSON.parse(data);

                var kartice = "";

                $.each(jsonResult, function(i, item) {
                    var new_block = generirajKartico(item);
                    kartice+= new_block; 
                });
                var $kartice = $(kartice);

                $container.append($kartice);
            
            },
        }); 
    }
    else{
    } 
}

$(document).on('change',"#spolSelect", function() { 
     dobiRezultateVrednosti();
     
});
function generirajKartico(data){
    var karticaHTML = '<div class="col s12 m6 l4"><div class="card hoverable" ><div class="card-image waves-effect waves-block waves-light">';
    karticaHTML += '<img class="responsive-img karticaprofil activator" src="'+data.profilnaslika.slika_url+'" /></div>';
    karticaHTML += '<div class="card-content"><span class="card-title activator grey-text text-darken-4">'+data.first_name+' '+data.last_name+'<i class="material-icons right">more_vert</i></span></div>';
    karticaHTML += '<div class="card-reveal"><span class="card-title grey-text text-darken-4">'+data.first_name+' '+data.last_name+'<i class="material-icons right">close</i></span><div class="divider" style="width: 100%"></div><table class="centered bordered"><tbody>';
    
    if(data.profil.sola != "" && data.profil.sola !=null){
        karticaHTML+='<tr><td>'+data.profil.sola+'</td></tr>';
    }
    if(data.profil.visina != null){
        karticaHTML+='<tr><td>'+data.profil.visina+' cm'+'</td></tr>';
    }
    if(data.profil.starost != null){
        karticaHTML+='<tr><td>'+data.profil.starost_leta+' let'+'</td></tr>';
    }
    if(data.profil.spol != null){
        if(data.profil.spol == true){
            karticaHTML+='<tr><td>Moški</td></tr>';
        }
        else{
            karticaHTML+='<tr><td>Ženska</td></tr>';
        }
    }
    
    karticaHTML+='<tr><td><a href="../uporabnik/'+data.pk+'/" class="waves-effect waves-light btn">Pojdi na profil</a></td></tr>';

    karticaHTML+='</tbody></table></div></div></div>';

    return karticaHTML;
}
var sole = ["Biotehniški center Naklo",
    "Biotehniški center Naklo, Srednja šola",
    "Ekonomska gimnazija in srednja šola Radovljica",
    "Gimnazija Franceta Prešerna",
    "Gimnazija Jesenice",
    "Gimnazija Kranj",
    "Gimnazija Škofja Loka",
    "Srednja gostinska in turistična šola Radovljica",
    "Srednja šola Jesenice",
    "Šolski center Kranj",
    "Šolski center Kranj, Srednja ekonomska, storitvena in gradbena šola",
    "Šolski center Kranj, Srednja tehniška šola",
    "Šolski center Kranj, Strokovna gimnazija",
    "Šolski center Škofja Loka",
    "Šolski center Škofja Loka, Srednja šola za lesarstvo",
    "Šolski center Škofja Loka, Srednja šola za strojništvo",
    "Gimnazija Jurija Vege Idrija",
    "Gimnazija Nova Gorica",
    "Gimnazija Tolmin",
    "Srednja šola Veno Pilon Ajdovščina",
    "Škofijska gimnazija Vipava",
    "Šolski center Nova Gorica",
    "Šolski center Nova Gorica, Biotehniška šola",
    "Šolski center Nova Gorica, Elektrotehniška in računalniška šola",
    "Šolski center Nova Gorica, Gimnazija in zdravstvena šola",
    "Šolski center Nova Gorica, Srednja ekonomska in trgovska šola",
    "Šolski center Nova Gorica, Strojna, prometna in lesarska šola",
    "Ekonomska šola Novo mesto, Srednja šola in gimnazija",
    "Gimnazija in srednja šola Kočevje",
    "Gimnazija Novo mesto",
    "Grm Novo mesto - center biotehnike in turizma",
    "Grm Novo mesto - center biotehnike in turizma, Kmetijska šola Grm in biotehniška gimnazija",
    "Grm Novo mesto - center biotehnike in turizma, Srednja šola za gostinstvo in turizem",
    "Srednja šola Črnomelj",
    "Šolski center Novo mesto, Srednja elektro šola in tehniška gimnazija",
    "Šolski center Novo mesto, Srednja gradbena, lesarska in vzgojiteljska šola",
    "Šolski center Novo mesto, Srednja strojna šola",
    "Šolski center Novo mesto, Srednja zdravstvena in kemijska šola",
    "Šolski center Ravne na Koroškem",
    "Šolski center Ravne na Koroškem, Gimnazija",
    "Šolski center Ravne na Koroškem, Srednja šola",
    "Šolski center Slovenj Gradec",
    "Šolski center Slovenj Gradec, Gimnazija",
    "Šolski center Slovenj Gradec, Srednja šola Slovenj Gradec in Muta",
    "Šolski center Slovenj Gradec, Srednja zdravstvena šola",
    "Gimnazija Antonio Sema Piran",
    "Gimnazija, elektro in pomorska šola Piran",
    "Gimnazija Gian Rinaldo Carli Koper",
    "Gimnazija Koper",
    "Srednja ekonomsko - poslovna šola Koper",
    "Srednja šola Izola",
    "Srednja šola Pietro Coppo Izola",
    "Srednja tehniška šola Koper",
    "Šolski center Srečka Kosovela Sežana",
    "Šolski center Srečka Kosovela Sežana, Gimnazija in ekonomska šola",
    "Biotehniški izobraževalni center Ljubljana",
    "Biotehniški izobraževalni center Ljubljana, Gimnazija in veterinarska šola",
    "Biotehniški izobraževalni center Ljubljana, Živilska šola",
    "Center za izobraževanje, rehabilitacijo in usposabljanje Kamnik, Srednja šola",
    "Ekonomska šola Ljubljana",
    "Elektrotehniško-računalniška strokovna šola in gimnazija Ljubljana",
    "Gimnazija Bežigrad",
    "Gimnazija Bežigrad, Gimnazija",
    "Gimnazija Bežigrad, Mednarodna šola",
    "Gimnazija in srednja šola Rudolfa Maistra Kamnik",
    "Gimnazija Jožeta Plečnika Ljubljana",
    "Gimnazija Ledina",
    "Gimnazija Moste",
    "Gimnazija Poljane",
    "Gimnazija Šentvid",
    "Gimnazija Šiška",
    "Gimnazija Vič",
    "Konservatorij za glasbo in balet Ljubljana",
    "Konservatorij za glasbo in balet Ljubljana, Srednja glasbena in baletna šola",
    "Srednja ekonomska šola Ljubljana",
    "Srednja frizerska šola Ljubljana",
    "Srednja gradbena, geodetska in okoljevarstvena šola Ljubljana",
    "Srednja medijska in grafična šola Ljubljana",
    "Srednja poklicna in strokovna šola Bežigrad-Ljubljana",
    "Srednja poklicna in strokovna šola Bežigrad-Ljubljana, Srednja poklicna in strokovna šola Bežigrad",
    "Srednja šola Domžale",
    "Srednja šola Domžale, Gimnazija",
    "Srednja šola Domžale, Poklicna in strokovna šola",
    "Srednja šola Josipa Jurčiča Ivančna Gorica",
    "Srednja šola tehniških strok Šiška",
    "Srednja šola za farmacijo, kozmetiko in zdravstvo",
    "Srednja šola za gostinstvo in turizem v Ljubljani",
    "Srednja šola za oblikovanje in fotografijo Ljubljana",
    "Srednja trgovska šola Ljubljana",
    "Srednja upravno administrativna šola Ljubljana",
    "Srednja vzgojiteljska šola in gimnazija Ljubljana",
    "Srednja zdravstvena šola Ljubljana",
    "Šolski center Ljubljana",
    "Šolski center Ljubljana, Gimnazija Antona Aškerca",
    "Šolski center Ljubljana, Srednja lesarska šola",
    "Šolski center Ljubljana, Srednja strojna in kemijska šola",
    "Šolski center za pošto, ekonomijo in telekomunikacije Ljubljana",
    "Šolski center za pošto, ekonomijo in telekomunikacije Ljubljana, Srednja tehniška in strokovna šola",
    "Zavod sv. Frančiška Saleškega Gimnazija Želimlje",
    "Zavod sv. Stanislava",
    "Zavod sv. Stanislava, Škofijska klasična gimnazija",
    "Biotehniška šola Maribor",
    "Gimnazija in srednja kemijska šola Ruše",
    "Gimnazija Ormož",
    "Gimnazija Ptuj",
    "II. gimnazija Maribor",
    "III. gimnazija Maribor",
    "Izobraževalni center Piramida Maribor",
    "Izobraževalni center Piramida Maribor, Srednja šola za prehrano in živilstvo",
    "Konservatorij za glasbo in balet Maribor",
    "Lesarska šola Maribor",
    "Lesarska šola Maribor, Srednja šola",
    "Prometna šola Maribor",
    "Prometna šola Maribor, Srednja prometna šola in dijaški dom",
    "Prva gimnazija Maribor",
    "Srednja ekonomska šola Maribor",
    "Srednja elektro-računalniška šola Maribor",
    "Srednja gradbena šola in gimnazija Maribor",
    "Srednja šola Slovenska Bistrica",
    "Srednja šola za gostinstvo in turizem Maribor",
    "Srednja šola za oblikovanje Maribor",
    "Srednja trgovska šola Maribor",
    "Srednja zdravstvena in kozmetična šola Maribor",
    "Šolski center Ptuj",
    "Šolski center Ptuj, Biotehniška šola",
    "Šolski center Ptuj, Ekonomska šola",
    "Šolski center Ptuj, Elektro in računalniška šola",
    "Šolski center Ptuj, Strojna šola",
    "Tehniški šolski center Maribor",
    "Tehniški šolski center Maribor, Srednja strojna šola",
    "Zavod Antona Martina Slomška",
    "Zavod Antona Martina Slomška, Škofijska gimnazija Antona Martina Slomška",
    "Biotehniška šola Rakičan",
    "Dvojezična srednja šola Lendava",
    "Ekonomska šola Murska Sobota",
    "Ekonomska šola Murska Sobota, Srednja šola in gimnazija",
    "Gimnazija Franca Miklošiča Ljutomer",
    "Gimnazija Murska Sobota",
    "Srednja poklicna in tehniška šola Murska Sobota",
    "Srednja šola za gostinstvo in turizem Radenci",
    "Srednja zdravstvena šola Murska Sobota",
    "Ekonomska in trgovska šola Brežice",
    "Ekonomska in trgovska šola Brežice, Poklicna in strokovna šola",
    "Gimnazija Brežice",
    "Šolski center Krško - Sevnica",
    "Šolski center Krško - Sevnica, Gimnazija Krško",
    "Šolski center Krško - Sevnica, Srednja poklicna in strokovna šola Krško",
    "Šolski center Krško - Sevnica, Srednja šola Sevnica",
    "Srednja gozdarska in lesarska šola Postojna",
    "Šolski center Postojna",
    "Šolski center Postojna, Gimnazija Ilirska Bistrica",
    "Šolski center Postojna, Srednja šola",
    "Ekonomska šola Celje",
    "Ekonomska šola Celje, Gimnazija in srednja šola",
    "Gimnazija Celje - Center",
    "I. gimnazija v Celju",
    "Srednja šola za gostinstvo in turizem Celje",
    "Srednja zdravstvena šola Celje",
    "Šola za hortikulturo in vizualne umetnosti Celje",
    "Šola za hortikulturo in vizualne umetnosti Celje, Srednja poklicna in strokovna šola",
    "Šolski center Celje",
    "Šolski center Celje, Gimnazija Lava",
    "Šolski center Celje, Srednja šola za gradbeništvo in varovanje okolja",
    "Šolski center Celje, Srednja šola za kemijo, elektrotehniko in računalništvo",
    "Šolski center Celje, Srednja šola za storitvene dejavnosti in logistiko",
    "Šolski center Celje, Srednja šola za strojništvo, mehatroniko in medije",
    "Šolski center Rogaška Slatina",
    "Šolski center Slovenske Konjice - Zreče",
    "Šolski center Slovenske Konjice - Zreče, Gimnazija Slovenske Konjice",
    "Šolski center Slovenske Konjice - Zreče, Srednja poklicna in strokovna šola Zreče",
    "Šolski center Šentjur",
    "Šolski center Šentjur, Srednja poklicna in strokovna šola",
    "Šolski center Velenje",
    "Šolski center Velenje, Elektro in računalniška šola",
    "Šolski center Velenje, Gimnazija",
    "Šolski center Velenje, Strojna šola",
    "Šolski center Velenje, Šola za rudarstvo in varstvo okolja",
    "Šolski center Velenje, Šola za storitvene dejavnosti",
    "Gimnazija in ekonomska srednja šola Trbovlje",
    "Gimnazija Litija",
    "Srednja šola Zagorje",
    "Srednja tehniška in poklicna šola Trbovlje"
];
$('#sola_search').autocompletejq({
    lookup: sole
});

var regije = ["Pomurska", "Podravska", "Koroška", "Savinjska", "Zasavska", "Spodnjeposavska", "Jugovzhodna Slovenija", "Osrednjeslovenska", "Gorenjska", "Notranjsko-kraška", "Goriška", "Obalno-kraška"];
$('#regija_search').autocompletejq({
    lookup: regije
});