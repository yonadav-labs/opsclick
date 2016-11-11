$(function() {
    $(".blog_link").click(function() {
        $(this).toggleClass("active");
        var cur_class = $(this).attr('class');
        $('.blog_link.active').removeClass('active');
        $(this).attr('class', cur_class);
        
        var url = $(this).attr('data-url');
        $("#blog_content").remove();
        $(this).after('<div id="blog_content"></div>');

        if ($(this).hasClass("active")) {
            $.ajax({
                url: url,
                type: 'GET',
                success: function(html) {
                    $("#blog_content").html(html);
                }
            });
        }
    });
});

$('#webinar_signup_form').submit(function(event) {
    event.preventDefault();
    $.ajax({
        method: 'POST',
        url: '/webinar_sign_up/',
        data: $(this).serialize(),
        success: function(result) {
            $('#div_webinar_signup').html(result);
        },
        error: function(ret) {
            $('#div_error_webinar_signup').html(ret.responseText);
        }
    });
});

$('#reference_signup_form').submit(function(event) {
    event.preventDefault();
    $.ajax({
        method: 'POST',
        url: '/webinar_sign_up/',
        data: $(this).serialize(),
        success: function(result) {
            $('#div_reference_signup').html(result);
        },
        error: function(ret) {
            $('#div_error_reference_signup').html(ret.responseText);
        }
    });
});