
function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute("content");
}

function registrar_OE() {
    const descricao = document.getElementById('descricao').value;
    // Dados para enviar
    const data = {
        "descricao": descricao,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_OE/',
        type: 'POST',
        data: data,
        success: function(data) {
            alert(data.message);
        },
        error: function(xhr, status, error) {
            alert('Erro: ' + xhr.responseJSON.message);
        }
    });
}