$(document).ready(function(){
    $(document).bind('keydown', function(e) { 
        if (e.which == 27) {
            $('details').not($('.upload-details')).removeAttr("open"); 
        }
    }); 
});

function sendError(isUserFault, text){
    var title;
    if (isUserFault)
        title = 'סליחה';
    else
        title = 'מצטערים';

    Swal.fire({
        type: 'error',
        title: title,
        text: text,
        confirmButtonText: 'הבנתי',
        showCloseButton: true
    })
}

function sendSecsuss(text){
    var titles = ['מעולה!', 'מצויין!']
    var title = titles[Math.floor(Math.random()*titles.length)];

    Swal.fire({
        type: 'success',
        title: title,
        text: text,
        confirmButtonText: 'הבנתי',
        showCloseButton: true
    })
}