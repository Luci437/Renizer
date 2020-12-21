$(document).ready(function () {
    $('.signup-box').hide();
});

$('#gotosignup').on('click',function () {
    $('.signup-box').show();
    $('.login-box').hide();
});

$('#gotologin').on('click', function () {
    $('.signup-box').hide();
    $('.login-box').show();
});

$('#login-form').on('submit',function (e) {
    e.preventDefault();
    let usrname = $('#username').val();
    let pswd = $('#password').val();

    if(usrname === 'admin' && pswd === 'admin') {
        window.location.href = 'http://127.0.0.1:8000/admindash/';
    }

    $.ajax({
        url : "checklogin/",
        type : 'POST',
        data : {
          username : usrname,
          password : pswd
        },
        success: function (response) {
            console.log(response.response);
            if(response.response) {
                $('.login-error').css('opacity','1').css('color','#aaff73').html('Welcome to Renizer');
                setTimeout(function () {
                    window.location.href = 'http://127.0.0.1:8000/';
                },2000);

            }else {
                $('.login-error').css('opacity','1');
            }
        }
    });

});

$('#newusername').on('keyup',function () {
    let newusername = $('#newusername').val();

    $.ajax({
        url: 'checkusername/',
        type: 'POST',
        data: {
            username: newusername
        },
        success: function (response) {
            if(response.response) {
                $('.username-error').css('opacity','1').html('Sorry, that username is taken.');
                $('#signup-button').attr('disabled','disabled').css('opacity','0.2');
            }else {
                $('#signup-button').removeAttr('disabled').css('opacity','1');
                $('.username-error').css('opacity','0').html('take it');
            }
        }
    });
});

$('#signup-form').on('submit', function (e) {
    e.preventDefault();
    let name = $('#fullname').val();
    let username = $('#newusername').val();
    let password = $('#newpassword').val();

    $.ajax({
        url: 'signup/',
        type: 'POST',
        data: {
            fname: name,
            username: username,
            password: password
        },
        success: function (response) {
            $('.username-error').html(response.done).css('opacity','1').css('color','#aaff73');
            setTimeout(function () {
                window.location.href = '';
            },4000);
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