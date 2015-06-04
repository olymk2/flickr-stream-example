$(document).ready(function(){
    $(function() {
        $(document).endlessScroll({
            bottomPixels: 0,
            fireOnce: false,
            fireDelay: 100,
            ceaseFireOnEmpty: false,
            callback: function(fireSequence, pageSequence, scrollDirection) {
                if(scrollDirection=='prev'){
                    return false;
                }

                url_tags = '';
                if($('input').val()){
                    url_tags = '?tags=' + $('input').val();
                }
                $.ajax({
                    type: "GET",
                    url: '/photos/' + url_tags ,
                    dataType: 'html',
                    timeout: 3600,
                    success: function(data) {
                        $('#flickr-contain').append(data);
                    },
                    error: function(jqXHR, textStatus, errorThrown){
                        $('#flickr-contain').html('<p>Failed to fetch Flickr Stream</p>');
                    }
                });
                return true;
            }
        });
    });
});
