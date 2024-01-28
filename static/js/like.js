$(document).ready(function() {
    $('#likeButton').on('click', function(e) {
        e.preventDefault();

        var post_id = $(this).data('post-id');
        $.ajax({
            url: '/like/' + post_id + '/',
            method: 'GET',
            success: function(data) {
                $('#likesCount').text(data.likes_count);

                // Проверяем переменную liked и обновляем изображение лайка соответственно
                if (data.liked) {
                    $('#likeImage').attr('src', '{% static "img/heart.png" %}');
                } else {
                    $('#likeImage').attr('src', '{% static "img/love.png" %}');
                }
            }
        });
    });
});