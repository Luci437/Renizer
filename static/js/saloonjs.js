$(document).ready(function () {
    let todays = new Date().toISOString().substr(0, 10);
    $('#todaysdate').val(todays).attr('min',todays);
});

function sundaycheck() {
    var dt = new Date($('#todaysdate').val());
    var dayz = dt.getDay();

    if(dayz === 0) {
        $('#appo-error').html("Sunday we don't work sir.").css('opacity','1');
        $('.appo-button').attr('disabled','disabled').css('opacity','0.2');
    }else {
        $('#appo-error').html("Thats fine..").css('opacity','0');
        $('.appo-button').removeAttr('disabled').css('opacity','1');
        checkBookingAvailable();
    }
}

$('#booking-form').on('submit',function (e) {
    e.preventDefault();
    let name = $('#name').val();
    let mobile = $('#mobile').val();
    let booking_date = $('#todaysdate').val();

    $.ajax({
        url: 'booking/',
        type: 'post',
        data: {
            'name': name,
            'mobile': mobile,
            'booking_date': booking_date
        },
        success: function (response) {
            $('#appo-error').html(response['response']).css('opacity','1').css('color','#30da70');
            $('#name').val('');
            $('#mobile').val('');
        }
    });

});

function checkBookingAvailable() {
    let booking_date = $('#todaysdate').val();
    $.ajax({
        url: 'checkbookingdate/',
        type: 'post',
        data: {
            'bkdate': booking_date
        },
        success: function (data) {
            console.log(data['is_available']);
            if(data['is_available']) {
                $('#appo-error').html('Come fast and grab your seat.').css('opacity','1');
                $('.appo-button').removeAttr('disabled').css('opacity','1');
            }else {
                $('.appo-button').attr('disabled','disabled').css('opacity','0.2');
                $('#appo-error').html('Sorry to say, Appointment is full.').css('opacity','1');
            }
        }
    });
}


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