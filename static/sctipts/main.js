$(function () {
    $.ajax({
        type: 'GET',
        url: 'https://api.giphy.com/v1/gifs/trending?api_key=x91jNWIe6d8y2vIH4zrWtQ2dOqgpcsQD&limit=50&rating=g&offset=0',
        /*url: ' https://api.giphy.com/v1/gifs/random?api_key=x91jNWIe6d8y2vIH4zrWtQ2dOqgpcsQD&limit=25&rating=g',*/
        crossDomain: true,
        headers: {
            "accept": "application/json"
        },
        success: function display(data) {
            /*console.log('success', data);*/
            $.each(data.data, function(indx, gif) {
                $('div#row1').append('<div class="col"><img src="' + gif.images.fixed_height.url + '"</div>');
                /*console.log('idx', gif)*/
            });
            $('div.col').append('<img class="like" src="../static/Images/heart.png" alt="You can like me"/>');
            $('img.like').click(function() {
                alert('I see you liked me! RIGHT CLICK to save me ;)');
            });
            $('button.more').click(function(){
                var reads = 100;
                var count = data.pagination.total_count;
                var offst = data.pagination.offset;
                while (reads < 200){
                    offst = (offst + 1);
                    var ofst = offst.toString();
                    console.log("offst is", offst)
                    console.log("String ofst is", ofst)
                    $.ajax({
                        type: 'GET',
                        url: 'https://api.giphy.com/v1/gifs/trending?api_key=x91jNWIe6d8y2vIH4zrWtQ2dOqgpcsQD&limit=50&rating=g&offset=' + ofst,
                        crossDomain: true,
                        headers: {"accept": "application/json"},
                        success: function(data){
                            $.each(data.data, function(i, g){
                                $('div#row1').append('<div class="col"><img src="' + g.images.fixed_height.url + '"</div>');
                            });
                        }
                    });
                    reads += 50;
                    url = 'https://api.giphy.com/v1/gifs/trending?api_key=x91jNWIe6d8y2vIH4zrWtQ2dOqgpcsQD&limit=50&rating=g&offset=' + ofst
                    console.log("url: ", url)
                    console.log("reads so far are:", reads, "we are in the while loop.Total count is:", count)
                }
                console.log("outside the while loop now")
                
            });
            
        }
    });
    
/*Implement here search button: doesn't work here actually*/

});
