function addStar(postId, ball) {
    $.ajax({
        type: 'POST',
        url: '/add_star/' + postId + '/' + ball + '/',
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success: function(data) {
            // Обновляем интерфейс на основе данных из JSON ответа
            // Например, обновляем количество звезд и их цвет
            // В данном примере предполагается, что вы используете эти данные для обновления элементов на странице
            console.log('Успех:', data);
            // Пример обновления элемента с id="rating" с помощью jQuery
            $('#rating').html('Рейтинг: ' + data.ball + ' (' + data.rat1 + ')');
            // Пример обновления списка звезд с классом ".stars" с помощью jQuery
            $('.stars').html('');
            for (var i = 0; i < data.rating; i++) {
                $('.stars').append('<span class="fa fa-star checked"></span>');
            }
            for (var j = data.rating; j < 5; j++) {
                $('.stars').append('<span class="fa fa-star"></span>');
            }
        },
        error: function(xhr, textStatus, errorThrown) {
            console.error('Ошибка:', errorThrown);
        }
    });
}
