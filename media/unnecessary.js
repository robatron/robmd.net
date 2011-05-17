/* Unnecessary eye candy to spruce up RobMD.net 
 *
 * Dependancies: jQuery
 */

var unnecessary = {
    set_source_background: function(){
        /* Set the background to the source of the page.
         *
         * There must be a div with the id 'background' on the same level as
         * the element you want to sit on top of the background.
         */
        var page_source = $('html').html();
        var page_source_sanitized = page_source
                .replace(/</g,'&lt').replace(/>/g,'&gt').split('\n');
        var RAND_MIN = 0;
        var RAND_MAX_HORIZ = $(window).width();
        var RAND_MAX_VERT = $(window).height();
      
        function place_code_lines(){
            for(var i in page_source_sanitized){
                var rand_horiz = Math.round(
                        RAND_MIN+Math.random()*(RAND_MAX_HORIZ - RAND_MIN));
                var rand_vert = Math.round(RAND_MIN + 
                        Math.random()*(RAND_MAX_VERT - RAND_MIN));
                $('#background').append(
                    "<div class='background_code_line' style='top: "+
                            rand_vert+"px; left: "+rand_horiz+"px'>"+
                        page_source_sanitized[i]+
                    "</div>"
                );
            }
        }

        place_code_lines();
        place_code_lines()
        place_code_lines()

        /*
        $('#background').html(
            page_source_sanitized
        );
        */
    }
}

