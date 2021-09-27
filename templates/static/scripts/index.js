let buttons = document.getElementById('buttons')
let pagamentoCreditCard = document.getElementById('test')
let pagamentoPix = document.getElementById('test2')
let title = document.getElementById('title')
let buttonClose = document.getElementById('buttonClose')
let input = document.getElementById('inputCard')

function creditCard() {
    buttons.style.display = 'none'
    title.style.display = 'none'
    pagamentoCreditCard.style.display = 'block'
}

function closeX() {

    if($('#test').hasClass('moved')) {
        $('#test').removeClass('moved');
    }else{
        $('#test').addClass('moved');
    }

    title.style.display = 'block'
    buttons.style.display = 'flex'
    pagamentoCreditCard.style.display = 'none'
}

function pix() {
    buttons.style.display = 'none'
    title.style.display = 'none'

    pagamentoPix.style.display = 'block'
}

function closeX2() {

    if($('#test2').hasClass('moved')) {
        $('#test2').removeClass('moved');
    }else{
        $('#test2').addClass('moved');
    }

    title.style.display = 'block'
    buttons.style.display = 'flex'
    pagamentoPix.style.display = 'none'
}

window.move2 = function() {
    if($('#test2').hasClass('moved')) {
        $('#test2').removeClass('moved');
    }else{
        $('#test2').addClass('moved');
    }
}

window.move = function() {
    if($('#test').hasClass('moved')) {
        $('#test').removeClass('moved');
    }else{
        $('#test').addClass('moved');
    }
}