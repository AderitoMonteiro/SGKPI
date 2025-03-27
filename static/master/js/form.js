
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


function editar_OE_model() {
    const descricao = document.getElementById('descricao_editar').value;
    const id = document.getElementById('id_editar').value;
    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'editar/editar_OE/',
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

function editar_OE(button){

   document.getElementById("descricao_editar").value = button.getAttribute("data-descricao");
   document.getElementById("id_editar").value = button.getAttribute("data-id");

 }