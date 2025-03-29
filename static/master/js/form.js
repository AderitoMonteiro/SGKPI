
function getCSRFToken() {
    return document.querySelector('meta[name="csrf-token"]').getAttribute("content");
}

// start OE
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
        alert("Selecione pelo menos um para eliminar.");
        return;
    }else{

        let userIds = Array.from(checkboxes).map(checkbox => checkbox.value).join(",");
        let id_url = document.getElementById('id_url').value;
        let url;

            switch (id_url) {
                case 'RAS':
                    url='delect_checkbox/delect_checkbox_RA/'
                    break;
                case 'OE':
                        url='delect_checkbox/delect_checkbox_OE/'
                    break;
                case 'ME':
                        url='delect_checkbox/delect_checkbox_ME/'
                    break;
                case 'KPI':
                        url='delect_checkbox/delect_checkbox_KPI/'
                break;
                case 'OA':
                        url='delect_checkbox/delect_checkbox_OA/'
                break;
                case 'AAN':
                    url='delect_checkbox/delect_checkbox_AAN/'
                break;
                case 'AC':
                    url='delect_checkbox/delect_checkbox_AC/'
                break;
                default:
                    console.log("erro");
             }

        const data = {
            "id": userIds,
            "X-CSRFToken": getCSRFToken()
        };
         // Configuração da requisição
            $.ajax({
                url:url,
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

// END OE
// START RAS
function registrar_RAS() {
    const descricao = document.getElementById('descricao').value;
    let select = document.getElementById("meta-select");
    let textoSelecionado =select.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_tabela_meta": textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_RAS/',
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

function editar_RAS_model() {
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
        url: 'editar/editar_RAS/',
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

function delete_RAS_model() {

    const id = document.getElementById('id_delete').value;
    // Dados para enviar
    const data = {
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'delete/delete_RAS/',
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

// start Me

function registrar_ME() {
    const descricao = document.getElementById('descricao').value;
    let select = document.getElementById("meta-kpi-select");
    let textoSelecionado = select.value;
    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_kpi":textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_ME/',
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

function delete_ME_model() {

    const id = document.getElementById('id_delete').value;
    // Dados para enviar
    const data = {
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'delete/delete_ME/',
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


function editar_ME_model() {
    const descricao = document.getElementById('descricao_editar').value;
    const id = document.getElementById('id_editar').value;
    let select = document.getElementById("meta-kpi-edit-select");
    let textoSelecionado = select.value;
    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id": id,
        "id_kpi":textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'editar/editar_ME/',
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
// start kpi

function registrar_KPI() {
    const descricao = document.getElementById('descricao').value;
    let select = document.getElementById("oe-select");
    let textoSelecionado =select.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_objeto_estrategico": textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_KPI/',
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

function registrar_RAS() {
    const descricao = document.getElementById('descricao').value;
    let select = document.getElementById("meta-select");
    let textoSelecionado =select.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_tabela_meta": textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_RAS/',
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


function editar_KPI_model() {
    const descricao = document.getElementById('descricao_editar').value;
    const id = document.getElementById('id_editar').value;
    let select = document.getElementById("oe-select");
    let textoSelecionado =select.value;    

    
    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id": id,
        "id_objeto_estrategico":textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'editar/editar_KPI/',
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

function delete_KPI_model() {

    const id = document.getElementById('id_delete').value;
    // Dados para enviar
    const data = {
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'delete/delete_KPI/',
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

function registrar_OA() {
    const descricao = document.getElementById('descricao').value;
    let select = document.getElementById("kpi-select");
    let textoSelecionado =select.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_kpi": textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_OA/',
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

function editar_OA_model() {
    const descricao = document.getElementById('descricao_editar').value;
    const id = document.getElementById('id_editar').value;
    let select = document.getElementById("kpi-editar");
    let textoSelecionado =select.value;    

    
    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id": id,
        "id_kpi":textoSelecionado,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'editar/editar_OA/',
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

function delete_OA_model() {

    const id = document.getElementById('id_delete').value;
    // Dados para enviar
    const data = {
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'delete/delete_OA/',
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

function registrar_AAN() {

    const descricao = document.getElementById('descricao').value;
    let select = document.getElementById("aan-oa-select");
    let data_inicio = document.getElementById("data_inicio").value;
    let data_fim = document.getElementById("data_fim").value;
    let textoSelecionado =select.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_objetivo_anual": textoSelecionado,
        "data_inicio":data_inicio,
        "data_fim":data_fim,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_AAN/',
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

function editar_AAN_model() {
    
    const descricao = document.getElementById('descricao_editar').value;
    const id = document.getElementById('id_editar').value;
    let select = document.getElementById("aan-oa-edit-select");
    let data_inicio = document.getElementById("data_inicio_edit").value;
    let data_fim = document.getElementById("data_fim_edit").value;
    let textoSelecionado =select.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_objetivo_anual": textoSelecionado,
        "data_inicio":data_inicio,
        "data_fim":data_fim,
        "id":id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'editar/editar_AAN/',
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

function delete_AAN_model() {

    const id = document.getElementById('id_delete').value;
    // Dados para enviar
    const data = {
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'delete/delete_AAN/',
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


function registrar_AC() {

    const descricao = document.getElementById('descricao').value;
    const obs = document.getElementById('w3review').value;
    let select_aan = document.getElementById("ac-aa-select");
    let select_p = document.getElementById("ac-p-select");
    let data_inicio = document.getElementById("data_inicio").value;
    let data_fim = document.getElementById("data_fim").value;

    let textoSelecionado_aan =select_aan.value;
    let textoSelecionado_p =select_p.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_atividade_anual": textoSelecionado_aan,
        "id_processo": textoSelecionado_p,
        "data_inicio":data_inicio,
        "data_fim":data_fim,
        "X-CSRFToken": getCSRFToken(),
        "obs":obs
    };

    // Configuração da requisição
    $.ajax({
        url: 'add/add_AC/',
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

function editar_AC_model() {
    
    const descricao = document.getElementById('descricao_editar').value;
    let select_aan = document.getElementById("ac-aa-select_edit");
    const obs = document.getElementById('w3review-edit').value;
    let select_p = document.getElementById("ac-p-select_edit");
    let data_inicio = document.getElementById("data_inicio_edit").value;
    let data_fim = document.getElementById("data_fim_edit").value;
    const id = document.getElementById('id_editar').value;
    let textoSelecionado_aan =select_aan.value;
    let textoSelecionado_p =select_p.value;

    // Dados para enviar
    const data = {
        "descricao": descricao,
        "id_atividade_anual": textoSelecionado_aan,
        "id_processo": textoSelecionado_p,
        "data_inicio":data_inicio,
        "data_fim":data_fim,
        "id":id,
        "obs":obs,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'editar/editar_AC/',
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


function delete_AC_model() {

    const id = document.getElementById('id_delete').value;
    // Dados para enviar
    const data = {
        "id": id,
        "X-CSRFToken": getCSRFToken()
    };

    // Configuração da requisição
    $.ajax({
        url: 'delete/delete_AC/',
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