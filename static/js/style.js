$(document).ready(
    function(){
        styleSlider();
    }
);

$('#gender-male').on('click',function (e) {
    e.preventDefault();
    $('#male-symbol').addClass('clickedGender');
    $('#female-symbol').removeClass('clickedGender');
    $.ajax({
        url: 'menstyle/',
        dataType : 'json',
        success: function (data) {
            let totalitems = data['totalitems'];

            console.log(totalitems);

            $('#result').children().remove();
            for(let i=0;i<totalitems;i++) {
                let el = "/media/" + data["styles"][i][3];
                $('#result').append('<div class="style-box"><img src='+ el +' class="hairstyle-img"><span class="stylecover"></span><h1 class="style-name">'+ data['styles'][i][1] +'</h1><h6 class="style-category-name">'+ data['styles'][i][2] +'</h6></div>');
            }

        }
    });
});

$('#gender-female').on('click',function (e) {
    e.preventDefault();
    $('#female-symbol').addClass('clickedGender');
    $('#male-symbol').removeClass('clickedGender');
    $.ajax({
        url: 'femalestyle/',
        dataType : 'json',
        success: function (data) {
            let totalitems = data['totalitems'];

            console.log(totalitems);
            $('#result').children().fadeOut();
            $('#result').children().remove();
            for(let i=0;i<totalitems;i++) {
                let el = "/media/" + data["styles"][i][3];
                $('#result').append('<div class="style-box"><img src='+ el +' class="hairstyle-img"><span class="stylecover"></span><h1 class="style-name">'+ data['styles'][i][1] +'</h1><h6 class="style-category-name">'+ data['styles'][i][2] +'</h6></div>');
            }

        }
    });
});

$('#gender-female').on('click', function () {

    let el1 = document.getElementsByClassName('style-category-name');
    let el2 = document.getElementsByClassName('style-box');

    for(let i=0;i<el1.length;i++) {
        if(el1[i].innerHTML === 'male') {
            el2[i].style.display = 'none';
        }
    }

});

function styleSlider() {
    let el1 = document.getElementsByClassName('style-slide-img');
    let totalimg = el1.length;
    let currentimg = 0;

    el1[totalimg - 1].style.opacity = '1';

    setInterval(function () {
        for(let i=0; i<totalimg; i++){
            if(currentimg === i) {
                el1[currentimg].style.opacity = '1';
            }else {
                el1[i].style.opacity = '0';
            }
        }
        currentimg++;
        if(currentimg === totalimg)
            currentimg = 0;
    },10000);
}


$('#search-style').on('keyup',function (e) {
    let stylename = $(this).val();

    $.ajax({
        url: 'searchstyle/',
        type: 'post',
        data: {
            'stylename': stylename
        },
        success: function(data) {
            if(data['styles'] === 'none') {
                $('#result').children().remove();
                $('#no-result').css('visibility','visible');
            }else {
            $('#no-result').css('visibility','hidden');
            let totalitems = data['totalitems'];
            console.log(totalitems);
            $('#result').children().remove();
            for(let i=0;i<totalitems;i++) {
                let el = "/media/" + data["styles"][i][3];
                $('#result').append('<div class="style-box"><img src='+ el +' class="hairstyle-img"><span class="stylecover"></span><h1 class="style-name">'+ data['styles'][i][1] +'</h1><h6 class="style-category-name">'+ data['styles'][i][2] +'</h6></div>');
            }
            }
            }
    });
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});