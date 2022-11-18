let buttons = document.getElementById('buttons')
let pagamentoCreditCard = document.getElementById('test')
let pagamentoPix = document.getElementById('test2')
let title = document.getElementById('title')
let buttonClose = document.getElementById('buttonClose')
let input = document.getElementById('inputCard')
let qrcode = document.getElementById('qrcode')

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

function finishCard() {
    let amount = document.querySelector('input[name="payment-group"]:checked')
    let cardNumber = document.querySelector('#inputCard')
    let cvv = document.querySelector('#cvv')
    let validMonth = document.querySelector('#inputMonth')
    let validYear = document.querySelector('#inputYear')
    let titularName = document.querySelector('#titularName')
    let cpf = document.querySelector('#cpf')
    if (amount.value != '' && cardNumber.value != '' && cvv.value != '' && validMonth.value != '' && validYear.value != '' && titularName.value != '' && cpf.value != '') {
        if($('#test').hasClass('moved')) {
            $('#test').removeClass('moved');
        }else{
            $('#test').addClass('moved');
        }    
        title.style.display = 'block'
        buttons.style.display = 'flex'
        pagamentoCreditCard.style.display = 'none'
        amount.checked = false
        cardNumber.value = ''
        cvv.value = ''
        validMonth.value = ''
        validYear.value = ''
        titularName.value = ''
        cpf.value = ''
    } else {
        alert("Preencha todos os campos!")
    }
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

function finishPix() {
    let amount = document.querySelector('input[name="payment-group"]:checked')
    let anotherAmount = document.querySelector('#anotherAmount')
    if (amount.value != '' || anotherAmount.value != ''){
        if($('#test2').hasClass('moved')) {
            $('#test2').removeClass('moved');
        }else{
            $('#test2').addClass('moved');
        }
        amount.checked = false
        anotherAmount.value = ''
        title.style.display = 'block'
        buttons.style.display = 'flex'
        pagamentoPix.style.display = 'none'
    } else {
        alert("Preencha todos os campos!")
    }
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



