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
