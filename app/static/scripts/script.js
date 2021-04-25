$(document).ready(function() {
    $('.message').click(function() {
        $(this).fadeOut(300, function() {
            $(this).remove()
        })
    })
})