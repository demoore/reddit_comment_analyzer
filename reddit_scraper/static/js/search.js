/**
 * Created by dylan on 2014-05-24.
 */

$.expr[":"].iContains = $.expr.createPseudo(function(arg) {
    return function( elem ) {
        return $(elem).text().toUpperCase().indexOf(arg.toUpperCase()) >= 0;
    };
});

$('#text-field').on('input propertychange paste', function(){
    $text = $('#text-field').val();
    $(".md").parentsUntil('div.panel-group').parent().removeClass("on");
    $(".md:not(:iContains('" + $text + "'))").parentsUntil('div.panel-group').parent().addClass("on");

    $(".subreddit-entry").each(function(){
        if($(this).children('.panel-group:visible').length === 0){
            $(this).children('.subreddit-name').addClass("on");
        } else {
            $(this).children('.subreddit-name').removeClass("on");
        }
    });
});