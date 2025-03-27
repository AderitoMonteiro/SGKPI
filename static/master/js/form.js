
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

function delete_OE_model() {

    const id = document.getElementById('id_delete').value;
    // Dados para enviar
    const data = {
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'delete/delete_OE/',
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

 function delete_OE(button){

    document.getElementById("id_delete").value = button.getAttribute("data-id");
 
  }



document.getElementById("id_deleteCk").addEventListener("click", function() {

    let checkboxes = document.querySelectorAll(".user-checkbox:checked");
    if (checkboxes.length === 0) {
        alert("Selecione pelo menos um objetivo estrategico para eliminar.");
        return;
    }else{

        let userIds = Array.from(checkboxes).map(checkbox => checkbox.value).join(",");
        const data = {
            "id": userIds,
            "X-CSRFToken": getCSRFToken()
        };
         // Configuração da requisição
            $.ajax({
                url: 'delect_checkbox/delect_checkbox_OE/',
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

});
