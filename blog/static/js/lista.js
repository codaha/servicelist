
  /*$(function() {
    $( "#sortable" ).sortable();
    $( "#sortable" ).disableSelection();
  });
*/
$(document).ready(function() {

  $("#sortable").sortable();




$( "#zmien" ).click(function() {
 $.post("{% url 'blog.views.kolejnosc' %}", { lista: $('#sortable').sortable('serialize'),'csrfmiddlewaretoken': '{{ csrf_token }}' } );
});

});

/*skondensowane*/
/*$("#menu-pages").sortable({
    update: function(event, ui) {
        $.post("ajax.php", { pages: $('#menu-pages').sortable('serialize') } );
    }
});*/

/*proba z tokenem */
/*  var result_active = $('#active_sortable').sortable('serialize');
        $.ajax({
            type: "POST",
            data: result_active + '&csrfmiddlewaretoken={{ csrf_token }}&active=true',
            url: ""
        });

*/
