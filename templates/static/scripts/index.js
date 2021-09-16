let buttons = document.getElementById('buttons')
let pagamento = document.getElementById('test')
let title = document.getElementById('title')
let buttonClose = document.getElementById('buttonClose')

function creditCard() {
    console.log('CREDIT_CARD')

    buttons.style.display = 'none'
    title.style.display = 'none'

    pagamento.style.display = 'block'
}

function closeX() {

    if($('#test').hasClass('moved')) {
        $('#test').removeClass('moved');
    }else{
        $('#test').addClass('moved');
    }

    title.style.display = 'block'
    buttons.style.display = 'flex'
    pagamento.style.display = 'none'
}

window.move = function() {
    if($('#test').hasClass('moved')) {
        $('#test').removeClass('moved');
    }else{
        $('#test').addClass('moved');
    }
}