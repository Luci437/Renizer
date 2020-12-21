$('#cart-button').on('click', function () {
    $('#main-loader').animate({
        width: "30%"
    });
    $('.billing-box').animate({
        opacity: "1"
    });
    $('#loader').html('30% completed');
});

$('#billing-button').on('click', function () {
    $('#main-loader').animate({
        width: "65%"
    });
    $('.card-box').animate({
        opacity: "1"
    });
    $('#loader').html('65% completed');
});

$('#paymoney-button').on('click', function () {
    $('.thankyou-box').css('transform','rotateY(0deg)');
    $('.card').css('transform','rotateY(180deg)');
    setTimeout(function () {
        $('#main-loader').animate({
            width: "100%"
        });
        $('#loader').html('100% completed');
    },5000);
    setTimeout(function () {
        window.location.href = 'http://127.0.0.1:8000/';
    },6000);
});

$(document).on('click','.cart-remove', function () {
    let prdid = $(this).val();

    console.log(prdid);

    $.ajax({
        url: 'removecart/',
        type: 'post',
        data: {
            'prdid': prdid
        },
        success: function (data) {
            let cartitems = data['carts'].length;
            let prditems = data['product'].length;
            let prdname = '';
            let prdprice = '';
            let prdimg = '';

            if(cartitems === 0)
                window.location.href = 'http://127.0.0.1:8000/';

            $('#all-cart-items').children().remove();
            $('.totalpay').html('$'+data['totalpay']);
            $('.finalpay').val(data['totalpay']);

            for(let i=0;i<cartitems;i++) {
                let prdid = data['carts'][i][2];
                console.log(prdid);

                for(let j=0;j<prditems;j++) {
                    if(prdid === data['product'][j][0]) {
                        prdname = data['product'][j][1];
                        prdprice = data['product'][j][3];
                        prdimg = '/media/'+data['product'][j][4];
                    }
                }
                $('#all-cart-items').append('<div class="cart"><table width="100%" cellspacing="10" align="left"><tr><td rowspan="2" width="80px"><div class="cart-img-box"><img class="cart-img" src='+ prdimg +'></div></td><td><h1 class="cart-name">'+ prdname +'</h1></td></tr><tr><td style="display: flex;position: relative;"><h3 class="cart-price">$'+ prdprice +'</h3><button class="cart-remove" value='+ data['carts'][i][2] +'><i class="fas fa-trash"></i></button></td></tr></table></div>');
            }

        }
    });
});

$('#formpay').on('submit',function (e) {
    e.preventDefault();
    let address = $('#address').val();
    let state = $('#state').val();
    let city = $('#city').val();
    let pincode = $('#pincode').val();
    let phone = $('#phone').val();

    let cardnumber = $('#cardnumber').val();
    let cardname = $('#cardname').val();
    let cvv = $('#cardcvv').val();
    let exp = $('#cardexp').val();

    let totalpay = $('#totalpay').val();

    $.ajax({
        url: 'paybill/',
        type: 'post',
        data: {
            'address':address,
            'state':state,
            'city':city,
            'pincode':pincode,
            'phone':phone,
            'cardname':cardname,
            'cardnumber':cardnumber,
            'cardexp':exp,
            'cvv':cvv,
            'totalpay':totalpay
        },
        success: function () {
            console.log('Something happened.');
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