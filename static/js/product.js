$('#sortoption').on('change',function() {
    let sort = $(this).val();
    let finalsort = '';
    if(sort === 'High to Low') {
        finalsort = '-product_price';
    }else if(sort === 'Low to High') {
        finalsort = 'product_price';
    }else if(sort === 'Gender(Male)') {
        finalsort = '-product_gender';
    }else if(sort === 'Gender(Female)') {
        finalsort = 'product_gender';
    }

    let category = $('#categoryoption').val();

    console.log(category);
    if(category === null)
        category = 'all';

    $.ajax({
        url: 'sortcategory/',
        type: 'post',
        data: {
            'sortby': finalsort,
            'category': category
        },
        success: function (data) {
            let totalitems = data['total_items'];
            let totalcat = data['category'].length;

            console.log(totalcat);

            $('#product-box').children().remove();

            for(let i=0;i<totalitems;i++) {
                let imgz = '/media/'+data['products'][i][4];
                let catid = data['products'][i][2];
                let catname = '';

                for(let j=0;j<totalcat;j++) {
                    if(catid === data['category'][j][0]) {
                        catname = data['category'][j][1];
                    }
                }

                $('#product-box').append('<div class="sub-box"><div class="img-box"><img class="product-img" src='+ imgz +'></div><span class="product-gender">'+ data["products"][i][5] +'</span><h1 class="product-name">'+ data['products'][i][1] +'</h1><h5 class="product-category">'+ catname +'</h5><h3 class="product-price">$'+ data['products'][i][3] +'</h3><button class="cart-button" value='+ data['products'][i][0] +'><i class="fas fa-shopping-cart"></i>Add to Cart</button></div>');
            }
        }
    });
});

$('#categoryoption').on('change',function () {
    let categoryname = $(this).val();
    let sort = $('#sortoption').val();

    let finalsort = '';
    if(sort === 'High to Low') {
        finalsort = '-product_price';
    }else if(sort === 'Low to High') {
        finalsort = 'product_price';
    }else if(sort === 'Gender(Male)') {
        finalsort = '-product_gender';
    }else if(sort === 'Gender(Female)') {
        finalsort = 'product_gender';
    }

    console.log(categoryname);

    if(categoryname === null)
        categoryname = '';


    $.ajax({
        url: 'bycategory/',
        type: 'post',
        data: {
            'category': categoryname,
            'sortby': finalsort
        },
        success: function (data) {
            let totalitems = data['total_items'];
            let totalcat = data['category'].length;

            console.log(totalcat);

            $('#product-box').children().remove();

            for(let i=0;i<totalitems;i++) {
                let imgz = '/media/'+data['products'][i][4];
                let catid = data['products'][i][2];
                let catname = '';

                for(let j=0;j<totalcat;j++) {
                    if(catid === data['category'][j][0]) {
                        catname = data['category'][j][1];
                    }
                }

                $('#product-box').append('<div class="sub-box"><div class="img-box"><img class="product-img" src='+ imgz +'></div><span class="product-gender">'+ data["products"][i][5] +'</span><h1 class="product-name">'+ data['products'][i][1] +'</h1><h5 class="product-category">'+ catname +'</h5><h3 class="product-price">$'+ data['products'][i][3] +'</h3><button class="cart-button" value='+ data['products'][i][0] +'><i class="fas fa-shopping-cart"></i>Add to Cart</button></div>');
            }
        }
    });
});

$('#search-input').on('keyup', function () {
    let search = $(this).val();

    $.ajax({
        url: 'searchproduct/',
        type: 'post',
        data: {
            'search': search
        },
        success: function (data) {
            let totalitems = data['total_items'];
            let totalcat = data['category'].length;

            console.log(totalcat);

            $('#product-box').children().remove();

            for(let i=0;i<totalitems;i++) {
                let imgz = '/media/'+data['products'][i][4];
                let catid = data['products'][i][2];
                let catname = '';

                for(let j=0;j<totalcat;j++) {
                    if(catid === data['category'][j][0]) {
                        catname = data['category'][j][1];
                    }
                }

                $('#product-box').append('<div class="sub-box"><div class="img-box"><img class="product-img" src='+ imgz +'></div><span class="product-gender">'+ data["products"][i][5] +'</span><h1 class="product-name">'+ data['products'][i][1] +'</h1><h5 class="product-category">'+ catname +'</h5><h3 class="product-price">$'+ data['products'][i][3] +'</h3><button class="cart-button" value='+ data['products'][i][0] +'><i class="fas fa-shopping-cart"></i>Add to Cart</button></div>');
            }
        }
    });
});

$(document).on('click','.cart-button', function () {
    let prdid = $(this).val();
    let status = $('#login-status').html();
    console.log(status);
    if(status === 'online') {
        $.ajax({
            url: 'tocart/',
            type: 'post',
            data: {
                'prd_id': prdid
            },
            success: function (data) {
                console.log(data['cartcount']);
                if(data['response']) {
                    alert('Already in your Cart.');
                }else {
                    alert('Item Added to Cart')
                }
                $('#cart-no').html(data['cartcount']);
            }
        });
    }else {
        window.location.href = 'http://127.0.0.1:8000/login';
    }
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