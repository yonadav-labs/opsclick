$(function() {
    $('.blog_link').unbind('click').bind('click', function (e) {
        $(this).toggleClass("active");
        var cur_class = $(this).attr('class');
        // console.log(cur_class);
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

function submit_opsuser(event, form, genre) {
    event.preventDefault();
    var fd = new FormData($(form)[0]);
    console.log(genre);
    $.ajax({
        url: "/webinar_sign_up/",
        type: "POST",
        data: fd,
        processData: false,
        contentType: false,
        success: function(result) {
            $('#div_signup_'+genre).html(result);
        },
        error: function(ret) {
            $('#div_error_signup_'+genre).html(ret.responseText);
        }
    });    
}