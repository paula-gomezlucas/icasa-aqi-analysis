document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("inicio").addEventListener("click", onSubmitLoginForm);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("registro").addEventListener("click", onSubmitSignupForm);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("btn-alta").addEventListener("click", onAlta);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("btn-baja").addEventListener("click", onBaja);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("query").addEventListener("click", onQuery);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("cargarDatos").addEventListener("click", obtenerDatos);
});

async function onSubmitLoginForm() {
    const email = document.getElementById("inputEmail").value
    const passw = document.getElementById("exampleInputPassword").value

    const object = {email:email,password:passw};
    const response = await fetch('http://localhost:8000/login', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:8000'
      },
      body: JSON.stringify(object)
    });
  
    const responseText = await response.json();

    if(responseText.status) {
        if(responseText.rol){
            location.replace("vistaAdmin.html")
        }
        else{
            location.replace("vistaGen.html")
        }
    }
    else  {
        alert("Error de autenticación")
    }
}

async function onSubmitSignupForm() {
    const name = document.getElementById("inputName").value
    const email = document.getElementById("inputEmail").value
    const passw1 = document.getElementById("inputPassword1").value
    const passw2 = document.getElementById("inputPassword2").value
    
    if(passw1 != passw2) {
        alert("Las contraseñas son distintas.");
    } 
    
    else {
        const object = {email:email,password:passw1, nombre:name};
        const response = await fetch('http://localhost:8000/signup', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
                'Origin': 'http://localhost:8000'
            },
            body: JSON.stringify(object)
        });
  
        const responseText = await response.json();

        if(responseText.registrado) {
        }
        else{
            alert("Este usuario ya existe")
        }
        location.replace("index.html")
    }
}

function onAlta() {
    const email = document.getElementById("inputEmail").value
    const alta = true

    const object = {email:email,upd:alta};
    const response = fetch('http://localhost:8000/actualizacion', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:8000'
      },
      body: JSON.stringify(object)
    });

    alert("Cambio realizado")
    location.replace("vistaAdmin.html")

}

function onBaja() {
    const email = document.getElementById("inputEmail").value
    const alta = false

    const object = {email:email,upd:alta};
    const response = fetch('http://localhost:8000/actualizacion', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:8000'
      },
      body: JSON.stringify(object)
    });

    alert("Cambio realizado")
    location.replace("vistaAdmin.html")
}
  
async function onQuery() {
    const email = document.getElementById("consulta").value

    const object = {email:email};
    const response = await fetch('http://localhost:8000/consulta', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:8000'
      },
      body: JSON.stringify(object)
    });

    const responseText = await response.json();

    if(responseText.nombre == ""){
        alert("El usuario no existe")
    } else {    
        alert("Email: " + email + "\nNombre: " + responseText.nombre)
    }

    location.replace("vistaAdmin.html");
}

async function obtenerDatos() {
    let tab = await chrome.tabs.query({ active: true, currentWindow: true })

    function getTitle() { 
        viviendas = document.querySelectorAll('[href*="/inmueble/"]');
        url = document.URL
        titulosViviendas = [{titulo: url, ica: 0}]
        for (let i = 0; i < viviendas.length; i++) {
            object = {titulo: viviendas[i].innerText, ica: 0} // definimos este formato para que sea mas facil en la api ya recibirlo y trabajarlo
            titulosViviendas.push(object)
        }        
        return (titulosViviendas)
    }

    let results;

    await chrome.scripting.executeScript({
        target: { tabId: tab[0].id },
        func: getTitle,
    }).then(injectionResults => {
        results = injectionResults[0].result
    });

    const response = await fetch('http://localhost:8000/icas', {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Origin': 'http://localhost:8000'
        },
        body: JSON.stringify(results)
    });

    const responseText = await response.json();

    for(var i = 0; i < responseText.length; i++){
        var container = document.createElement('div');
        container.style.display = 'flex';
        container.style.textAlign = 'center';
        var textDiv = document.createElement('div');
        var icaDiv = document.createElement('div');
        textDiv.id = i + "viviendas";
        textDiv.innerHTML = responseText[i].titulo;
        container.appendChild(textDiv);
        icaDiv.id = i + "icas";
        icaDiv.innerHTML = responseText[i].ica;

        if (parseInt(responseText[i].ica) < 0) {
            icaDiv.style.color = 'gray'
        }
        else if (parseInt(responseText[i].ica) < 51) {
            icaDiv.style.color = 'green'
        }
        else if (parseInt(responseText[i].ica) < 101){
            icaDiv.style.color = 'yellow'
        }
        else if (parseInt(responseText[i].ica) < 151){
            icaDiv.style.color = 'orange'
        }
        else {
            icaDiv.style.color = 'red'
        }

        icaDiv.style.fontWeight = 'bold';

        container.appendChild(icaDiv)
        document.getElementById("viviendas").appendChild(container);
        var division = document.createElement('hr');
        document.getElementById("viviendas").appendChild(division);

    }    
}

