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
        $('#background').html(
            $('html').html().replace(/</g,'&lt').replace(/>/g,'&gt')
        );
    }
}

