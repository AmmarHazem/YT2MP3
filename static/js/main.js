$(document).ready(function() {

    $('.convert').on('submit', function(e){
        $(this).find('.btn-primary').addClass('disabled').html('<i class="fas fa-sync fa-spin"></i> Working')
    });
});
