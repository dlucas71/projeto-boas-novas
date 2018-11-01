$(document).ready(function() {
            $('#list').click(function(event){event.preventDefault();$('#list_artigos .item').addClass('list-group-item');});
            $('#grid').click(function(event){event.preventDefault();$('#list_artigos .item').removeClass('list-group-item');$('#products .item').addClass('grid-group-item');});
        });
