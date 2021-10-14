$(function () {
    $.ajax({
        type: 'GET',
        url: 'https://api.giphy.com/v1/gifs/trending?api_key=x91jNWIe6d8y2vIH4zrWtQ2dOqgpcsQD&limit=25&rating=g',
        crossDomain: true,
        headers: {
            "accept": "application/json"
        },
        success: function(data) {
            /*console.log('success', data);*/
            $.each(data.data, function(indx, gif) {
                $('div#row1').append('<div class="col"><img src="' + gif.images.fixed_width.url + '"</div>');
            });
        }
    });
    var search = $("search_bar").value;
    console.log("search: ", search)
});