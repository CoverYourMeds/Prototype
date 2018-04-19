$('body').on('click', '[data-toggle=collapse-next]', function(e) {
    var $target = $(this).parents('.list-group').find('.collapse');
    $target.collapse('toggle');
});
